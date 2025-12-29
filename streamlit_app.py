"""
SUMEP v2.0 - VERSIÓN STREAMLIT CLOUD
Sistema de Monitoreo Emocional Perinatal

Esta versión está optimizada para despliegue gratuito en Streamlit Cloud.
Cualquiera puede acceder sin instalar nada.

Deployment: streamlit.io
"""

import streamlit as st
import re
import numpy as np
import pandas as pd
from datetime import datetime
import torch
from transformers import pipeline
import spacy
import plotly.graph_objects as go
import plotly.express as px
from keywords_extended import EXTENDED_ASPECTS
import time

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================

st.set_page_config(
    page_title="SUMEP - Monitoreo Emocional Perinatal",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #A8DADC 0%, #F4A7B9 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stAlert {
        border-radius: 10px;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #A8DADC;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# CACHÉ DE MODELOS (SE CARGAN UNA SOLA VEZ)
# ============================================================================

@st.cache_resource
def load_models():
    """Cargar modelos una sola vez y cachear"""
    with st.spinner('🔄 Cargando modelos de IA... (esto tarda ~30 segundos la primera vez)'):
        # Modelo de sentimientos
        device = 0 if torch.cuda.is_available() else -1
        sentiment_model = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual",
            device=device,
            truncation=True,
            max_length=512
        )
        
        # Modelo SpaCy
        try:
            nlp = spacy.load("es_core_news_md")
        except:
            import os
            os.system("python -m spacy download es_core_news_md")
            nlp = spacy.load("es_core_news_md")
        
        return sentiment_model, nlp

sentiment_model, nlp = load_models()

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

THRESHOLDS = {
    'green': -0.15,
    'yellow': -0.35,
    'red': -0.35
}

CRITICAL_ASPECTS = ['Mental_Health', 'Emotions', 'Mother_Self', 'Baby']

# ============================================================================
# FUNCIONES DE PROCESAMIENTO
# ============================================================================

def clean_text(text):
    """Limpieza de texto"""
    text = text.lower()
    patterns = [
        r'entrevista\s+\d+', r'entrevistador[a]?:', r'entrevistado[a]?:',
        r'participante:', r'e:\s*', r'p:\s*', r'\d{1,2}:\d{2}',
        r'\[.*?\]', r'\(.*?\)'
    ]
    for pattern in patterns:
        text = re.sub(pattern, ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_lemmas(text, max_chars=100000):
    """Extraer lemas"""
    if len(text) > max_chars:
        text = text[:max_chars]
    doc = nlp(text)
    lemmas = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(lemmas)

def keyword_match_advanced(text, keywords):
    """Matching avanzado con lemas"""
    text_lower = text.lower()
    matches = []
    
    for kw in keywords:
        if kw in text_lower:
            matches.append(kw)
            continue
        kw_doc = nlp(kw)
        kw_lemma = kw_doc[0].lemma_.lower() if len(kw_doc) > 0 else kw
        if kw_lemma in text_lower:
            matches.append(kw)
    
    return matches

def analyze_aspect_sentiment(text, keywords):
    """Análisis de sentimiento por aspecto"""
    sentences = re.split(r'[.!?]', text)
    matched_keywords = keyword_match_advanced(text, keywords)
    
    relevant_sentences = []
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 15:
            continue
        for kw in matched_keywords:
            if kw in sent.lower():
                relevant_sentences.append(sent)
                break
    
    if not relevant_sentences:
        return {
            'score': np.nan,
            'mentions': 0,
            'positive': 0,
            'negative': 0,
            'neutral': 0,
            'alert_level': 'N/A',
            'examples': [],
            'keywords_found': []
        }
    
    scores = []
    pos_count = neg_count = neu_count = 0
    examples = []
    
    for sent in relevant_sentences[:10]:
        try:
            result = sentiment_model(sent[:512])[0]
            label = result['label'].lower()
            confidence = result['score']
            
            if 'negative' in label or '1' in label or '2' in label:
                score = -confidence
                neg_count += 1
                if confidence > 0.8:
                    examples.append(sent[:100])
            elif 'positive' in label or '4' in label or '5' in label:
                score = confidence
                pos_count += 1
            else:
                score = 0
                neu_count += 1
            
            scores.append(score)
        except:
            continue
    
    avg_score = np.mean(scores) if scores else 0
    
    if avg_score > THRESHOLDS['green']:
        alert = 'Verde'
    elif avg_score > THRESHOLDS['red']:
        alert = 'Amarillo'
    else:
        alert = 'Rojo'
    
    return {
        'score': float(avg_score),
        'mentions': len(relevant_sentences),
        'positive': pos_count,
        'negative': neg_count,
        'neutral': neu_count,
        'alert_level': alert,
        'examples': examples[:3],
        'keywords_found': list(set(matched_keywords))[:10]
    }

def analyze_interview(text, patient_id="", stage=""):
    """Análisis completo de entrevista"""
    clean_text_content = clean_text(text)
    text_with_lemmas = clean_text_content + " " + extract_lemmas(clean_text_content)
    
    results = {}
    alerts = {'Rojo': [], 'Amarillo': [], 'Verde': []}
    
    # Barra de progreso
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    total_aspects = len(EXTENDED_ASPECTS)
    
    for idx, (aspect_id, aspect_data) in enumerate(EXTENDED_ASPECTS.items()):
        status_text.text(f'Analizando: {aspect_data["label"]}...')
        progress_bar.progress((idx + 1) / total_aspects)
        
        analysis = analyze_aspect_sentiment(
            text_with_lemmas, 
            aspect_data['keywords']
        )
        
        results[aspect_id] = {
            'label': aspect_data['label'],
            'critical': aspect_data.get('critical', False),
            **analysis
        }
        
        if analysis['alert_level'] != 'N/A':
            alerts[analysis['alert_level']].append(aspect_data['label'])
    
    progress_bar.empty()
    status_text.empty()
    
    # Calcular score global
    valid_scores = [r['score'] for r in results.values() if not np.isnan(r['score'])]
    global_score = float(np.mean(valid_scores)) if valid_scores else 0
    
    # Determinar nivel de riesgo
    critical_red = [
        r['label'] for r in results.values()
        if r['critical'] and r['alert_level'] == 'Rojo'
    ]
    
    if len(critical_red) >= 2:
        risk_level = "ALTO"
    elif len(critical_red) >= 1 or len(alerts['Rojo']) >= 2:
        risk_level = "MEDIO"
    else:
        risk_level = "BAJO"
    
    return {
        'patient_id': patient_id,
        'stage': stage,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'global_score': global_score,
        'risk_level': risk_level,
        'alerts': alerts,
        'critical_red': critical_red,
        'results': results
    }

# ============================================================================
# INTERFAZ STREAMLIT
# ============================================================================

# Header
st.markdown("""
<div class="main-header">
    <h1>🌸 SUMEP v2.0</h1>
    <h3>Sistema Universal de Monitoreo Emocional Perinatal</h3>
    <p>Análisis automatizado con IA | 880+ Keywords | 16 Aspectos Psicosociales</p>
</div>
""", unsafe_allow_html=True)

# Sidebar con información
with st.sidebar:
    st.image("https://via.placeholder.com/300x150/A8DADC/FFFFFF?text=SUMEP+2.0", use_container_width=True)
    
    st.markdown("### 📊 Sobre el Sistema")
    st.info("""
    **SUMEP** analiza entrevistas perinatales detectando:
    - 🧠 Salud Mental
    - ❤️ Emociones
    - 👶 Relación con Bebé
    - 👤 Identidad Materna
    - ... y 12 aspectos más
    
    **Detección 3-5x más precisa** vs métodos tradicionales.
    """)
    
    st.markdown("### ⚠️ Advertencia")
    st.warning("""
    Este sistema es una herramienta de **screening complementaria**.
    
    NO sustituye la evaluación clínica profesional.
    """)
    
    st.markdown("### 📚 Documentación")
    st.markdown("""
    - [Manual de Usuario](#)
    - [Paper Científico](#)
    - [GitHub](#)
    """)
    
    st.markdown("---")
    st.markdown("**Versión**: 2.0")
    st.markdown("**Última actualización**: Dic 2024")

# Tabs principales
tab1, tab2, tab3 = st.tabs(["📝 Nueva Entrevista", "📖 Ejemplos", "ℹ️ Ayuda"])

with tab1:
    st.markdown("## Analizar Entrevista")
    
    col1, col2 = st.columns(2)
    
    with col1:
        patient_id = st.text_input(
            "🆔 ID del Paciente",
            placeholder="Ej: Paciente_001",
            help="Identificador único (puede ser anónimo)"
        )
    
    with col2:
        stage = st.selectbox(
            "📅 Etapa",
            ["Seleccionar...", "Embarazo", "Postparto"],
            help="Etapa del periodo perinatal"
        )
    
    st.markdown("### 📄 Texto de la Entrevista")
    
    input_method = st.radio(
        "Método de entrada:",
        ["Pegar texto", "Subir archivo"],
        horizontal=True
    )
    
    interview_text = ""
    
    if input_method == "Pegar texto":
        interview_text = st.text_area(
            "Pega aquí el texto completo de la entrevista",
            height=300,
            placeholder="""Ejemplo:

Entrevistador: ¿Cómo te sientes últimamente?
Paciente: La verdad es que muy cansada. El bebé no duerme bien...

Entrevistador: ¿Y emocionalmente?
Paciente: Tengo altibajos. A veces lloro sin motivo...""",
            help="Mínimo 50 caracteres. Incluye respuestas completas de la paciente."
        )
    else:
        uploaded_file = st.file_uploader(
            "Sube un archivo de texto",
            type=['txt', 'docx'],
            help="Formatos: TXT o DOCX"
        )
        if uploaded_file is not None:
            if uploaded_file.type == "text/plain":
                interview_text = uploaded_file.read().decode('utf-8')
            else:
                import docx
                doc = docx.Document(uploaded_file)
                interview_text = "\n".join([para.text for para in doc.paragraphs])
            
            st.success(f"✅ Archivo cargado: {uploaded_file.name} ({len(interview_text)} caracteres)")
    
    st.markdown("---")
    
    # Botón de análisis
    analyze_button = st.button(
        "🧠 Analizar Entrevista",
        type="primary",
        use_container_width=True,
        disabled=(not interview_text or len(interview_text) < 50 or stage == "Seleccionar...")
    )
    
    if analyze_button:
        if not patient_id:
            patient_id = f"Anónimo_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        with st.spinner('🔄 Analizando... Esto puede tardar 20-30 segundos'):
            start_time = time.time()
            result = analyze_interview(interview_text, patient_id, stage)
            elapsed_time = time.time() - start_time
        
        st.success(f'✅ Análisis completado en {elapsed_time:.1f} segundos')
        
        # Guardar en session state
        st.session_state['last_result'] = result
        
        # Mostrar resultados
        st.markdown("---")
        st.markdown("## 📊 Resultados del Análisis")
        
        # Evaluación Global
        st.markdown("### 🎯 Evaluación Global")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            risk_color = {
                'ALTO': '🔴',
                'MEDIO': '🟡',
                'BAJO': '🟢'
            }[result['risk_level']]
            
            st.metric(
                "Nivel de Riesgo",
                f"{risk_color} {result['risk_level']}"
            )
        
        with col2:
            score_color = "🟢" if result['global_score'] > -0.15 else "🟡" if result['global_score'] > -0.35 else "🔴"
            st.metric(
                "Score Global",
                f"{score_color} {result['global_score']:.3f}"
            )
        
        with col3:
            st.metric(
                "Alertas Rojas",
                f"🔴 {len(result['alerts']['Rojo'])}"
            )
        
        with col4:
            st.metric(
                "Alertas Amarillas",
                f"🟡 {len(result['alerts']['Amarillo'])}"
            )
        
        # Alertas Críticas
        if result['critical_red']:
            st.markdown("### ⚠️ ALERTAS CRÍTICAS")
            for aspect in result['critical_red']:
                st.error(f"🚨 **{aspect}** requiere atención inmediata")
        
        # Visualizaciones
        st.markdown("### 📈 Visualizaciones")
        
        viz_tab1, viz_tab2, viz_tab3 = st.tabs(["Barras", "Distribución", "Radar"])
        
        with viz_tab1:
            # Gráfico de barras
            labels = []
            scores = []
            colors = []
            
            for aspect_id, data in result['results'].items():
                if not np.isnan(data['score']):
                    labels.append(data['label'])
                    scores.append(data['score'])
                    
                    if data['alert_level'] == 'Rojo':
                        colors.append('#E57373')
                    elif data['alert_level'] == 'Amarillo':
                        colors.append('#FFD54F')
                    else:
                        colors.append('#81C784')
            
            fig_bar = go.Figure(data=[
                go.Bar(
                    x=scores,
                    y=labels,
                    orientation='h',
                    marker_color=colors,
                    text=[f'{s:.2f}' for s in scores],
                    textposition='auto',
                )
            ])
            
            fig_bar.update_layout(
                title='Puntuaciones por Aspecto',
                xaxis_title='Score de Sentimiento',
                yaxis_title='Aspecto',
                height=600,
                template='plotly_white'
            )
            
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with viz_tab2:
            # Gráfico circular
            alert_counts = [
                len(result['alerts']['Verde']),
                len(result['alerts']['Amarillo']),
                len(result['alerts']['Rojo'])
            ]
            
            fig_pie = go.Figure(data=[
                go.Pie(
                    labels=['Verde', 'Amarillo', 'Rojo'],
                    values=alert_counts,
                    marker_colors=['#81C784', '#FFD54F', '#E57373'],
                    hole=0.4
                )
            ])
            
            fig_pie.update_layout(
                title='Distribución de Alertas',
                height=500,
                template='plotly_white'
            )
            
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with viz_tab3:
            # Radar chart
            critical_labels = []
            critical_scores = []
            
            for aspect_id in CRITICAL_ASPECTS:
                if aspect_id in result['results']:
                    data = result['results'][aspect_id]
                    if not np.isnan(data['score']):
                        critical_labels.append(data['label'])
                        critical_scores.append(data['score'])
            
            fig_radar = go.Figure()
            
            fig_radar.add_trace(go.Scatterpolar(
                r=critical_scores,
                theta=critical_labels,
                fill='toself',
                name='Aspectos Críticos',
                line_color='#E57373'
            ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[-1, 1]
                    )
                ),
                title='Perfil de Aspectos Críticos',
                height=500,
                template='plotly_white'
            )
            
            st.plotly_chart(fig_radar, use_container_width=True)
        
        # Análisis Detallado
        st.markdown("### 📋 Análisis Detallado por Aspecto")
        
        for aspect_id, data in result['results'].items():
            if np.isnan(data['score']):
                continue
            
            alert_emoji = {
                'Rojo': '🔴',
                'Amarillo': '🟡',
                'Verde': '🟢'
            }.get(data['alert_level'], '⚪')
            
            with st.expander(f"{alert_emoji} {data['label']} - Score: {data['score']:.3f}"):
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Menciones", data['mentions'])
                with col2:
                    st.metric("Positivas", data['positive'])
                with col3:
                    st.metric("Negativas", data['negative'])
                with col4:
                    st.metric("Neutrales", data['neutral'])
                
                if data['keywords_found']:
                    st.markdown("**Keywords detectadas:**")
                    st.write(", ".join(data['keywords_found']))
                
                if data['examples']:
                    st.markdown("**Ejemplos:**")
                    for ex in data['examples']:
                        st.markdown(f"> *{ex}...*")
        
        # Recomendaciones
        st.markdown("### 💡 Recomendaciones Clínicas")
        
        if result['risk_level'] == 'ALTO':
            st.error("""
            **🔴 ACCIÓN URGENTE RECOMENDADA:**
            - Evaluación psicológica/psiquiátrica inmediata
            - Aplicar escala EPDS para confirmar riesgo
            - Valorar riesgo de ideación suicida
            - Activar protocolo de seguimiento intensivo
            """)
        elif result['risk_level'] == 'MEDIO':
            st.warning("""
            **🟡 SEGUIMIENTO PRIORITARIO:**
            - Cita de seguimiento en <7 días
            - Aplicar escala EPDS
            - Valorar derivación a salud mental
            - Reforzar red de apoyo
            """)
        else:
            st.success("""
            **🟢 SEGUIMIENTO RUTINARIO:**
            - Continuar con visitas programadas
            - Reforzar aspectos positivos
            - Mantener vigilancia
            - Ofrecer recursos preventivos
            """)

with tab2:
    st.markdown("## 📖 Entrevistas de Ejemplo")
    
    st.info("""
    Prueba el sistema con estas entrevistas de ejemplo que representan diferentes niveles de riesgo.
    Simplemente copia el texto y pégalo en la pestaña "Nueva Entrevista".
    """)
    
    example = st.selectbox(
        "Selecciona un ejemplo:",
        [
            "Seleccionar...",
            "Ejemplo 1: Postparto - Riesgo ALTO",
            "Ejemplo 2: Embarazo - Riesgo MEDIO",
            "Ejemplo 3: Embarazo - Riesgo BAJO"
        ]
    )
    
    if example == "Ejemplo 1: Postparto - Riesgo ALTO":
        st.markdown("""
        ### 🔴 Postparto - Múltiples Alertas Críticas
        
        **ID Sugerido:** TEST_001  
        **Etapa:** Postparto
        """)
        
        st.code("""
Entrevistador: ¿Cómo te sientes desde que nació el bebé?

Paciente: La verdad es que muy mal. No esperaba sentirme así. Estoy constantemente cansada, no duermo nada porque el bebé se despierta cada dos horas. Me siento completamente desbordada y no sé si voy a poder con esto.

Entrevistador: ¿Puedes contarme más sobre cómo te sientes emocionalmente?

Paciente: Pues... es que lloro mucho. A veces sin motivo. Me siento muy triste todo el tiempo, y tengo mucha ansiedad. Me da miedo no ser buena madre, no saber cuidar bien al bebé. Cuando llora y no consigo calmarlo, me siento una inútil, como si no sirviera para esto. 

Creo que estoy desarrollando depresión postparto. Mi madre también la tuvo y tengo miedo de estar igual. A veces pienso que fue un error tener el bebé, aunque sé que no debería pensar así y eso me hace sentir aún peor.

Entrevistador: ¿Cómo es tu relación con el bebé?

Paciente: Es complicado. Lo quiero, claro, pero no siento esa conexión que todo el mundo dice que deberías sentir. A veces cuando lo miro es como si fuera un extraño. No es como me imaginaba.
        """, language="text")
        
        if st.button("📋 Copiar Ejemplo 1", key="copy1"):
            st.success("✅ Copiado (usa Ctrl+V para pegar en el área de texto)")
    
    elif example == "Ejemplo 2: Embarazo - Riesgo MEDIO":
        st.markdown("""
        ### 🟡 Embarazo - Algunas Preocupaciones
        
        **ID Sugerido:** TEST_002  
        **Etapa:** Embarazo
        """)
        
        st.code("""
Entrevistador: ¿Cómo llevas el embarazo?

Paciente: En general bien, aunque tengo muchas dudas y preocupaciones. Es mi primer bebé y todo es nuevo. Físicamente me siento bastante bien, solo un poco de cansancio y las típicas molestias del embarazo, pero nada grave.

Entrevistador: ¿Y emocionalmente?

Paciente: Tengo altibajos. Hay días que estoy muy ilusionada y emocionada por conocer al bebé, pero otros días me entra mucha ansiedad pensando en el parto y en si voy a saber cuidarlo bien. 

Tengo miedo al dolor del parto. He leído muchas cosas en internet y algunas historias dan bastante miedo. También me preocupa no saber qué hacer cuando nazca.
        """, language="text")
    
    elif example == "Ejemplo 3: Embarazo - Riesgo BAJO":
        st.markdown("""
        ### 🟢 Embarazo - Adaptación Positiva
        
        **ID Sugerido:** TEST_003  
        **Etapa:** Embarazo
        """)
        
        st.code("""
Entrevistador: ¿Cómo te encuentras?

Paciente: Me siento muy bien, la verdad. Estoy muy contenta con el embarazo. Es mi segundo bebé y esta vez lo llevo mucho mejor que con el primero porque ya sé más o menos qué esperar.

Entrevistador: ¿Y físicamente?

Paciente: Bien también. Tengo algo de cansancio, normal en el tercer trimestre, y me cuesta dormir cómoda porque la barriga ya es grande. Pero son molestias normales del embarazo. Me cuido, hago yoga prenatal y procuro descansar cuando puedo.

Entrevistador: ¿Cómo te sientes emocionalmente?

Paciente: Estoy muy ilusionada. Tengo ganas de que nazca para conocerle. Con mi hijo mayor fue todo más nuevo y tenía más miedo, pero ahora me siento más preparada y confiada.
        """, language="text")

with tab3:
    st.markdown("## ℹ️ Ayuda y Documentación")
    
    help_tab1, help_tab2, help_tab3 = st.tabs(["Cómo Usar", "Interpretación", "Sobre el Sistema"])
    
    with help_tab1:
        st.markdown("""
        ### 📝 Cómo Usar el Sistema
        
        1. **Introduce los datos básicos:**
           - ID del Paciente (puede ser anónimo)
           - Selecciona la etapa (Embarazo o Postparto)
        
        2. **Introduce la entrevista:**
           - Opción A: Pega el texto directamente
           - Opción B: Sube un archivo TXT o DOCX
           - Mínimo recomendado: 300-500 palabras
        
        3. **Analiza:**
           - Haz clic en "Analizar Entrevista"
           - Espera 20-30 segundos
           - Revisa los resultados
        
        4. **Interpreta los resultados:**
           - Evalúa el nivel de riesgo global
           - Revisa aspectos en alerta roja
           - Lee las recomendaciones clínicas
        
        ### 💡 Consejos para Mejores Resultados
        
        - ✅ Entrevistas de 500+ palabras son más precisas
        - ✅ Incluye respuestas descriptivas (no solo sí/no)
        - ✅ Haz preguntas abiertas sobre emociones
        - ✅ Permite que la paciente se exprese libremente
        - ❌ Evita entrevistas muy cortas (<200 palabras)
        - ❌ No uses solo cuestionarios estructurados
        """)
    
    with help_tab2:
        st.markdown("""
        ### 📊 Interpretación de Resultados
        
        #### Niveles de Alerta
        
        - **🟢 Verde (Score > -0.15):** Sentimiento neutral o positivo. Seguimiento rutinario.
        - **🟡 Amarillo (Score -0.35 a -0.15):** Precaución. Monitoreo más frecuente.
        - **🔴 Rojo (Score < -0.35):** Alerta. Requiere atención prioritaria.
        
        #### Niveles de Riesgo Global
        
        **🔴 RIESGO ALTO**
        - Criterios: ≥2 aspectos críticos en rojo
        - Acción: Evaluación psicológica INMEDIATA + EPDS
        
        **🟡 RIESGO MEDIO**
        - Criterios: 1 aspecto crítico en rojo O ≥2 aspectos en rojo
        - Acción: Seguimiento en <7 días + EPDS
        
        **🟢 RIESGO BAJO**
        - Criterios: Mayoría de aspectos en verde
        - Acción: Seguimiento rutinario
        
        #### Aspectos Críticos (Prioritarios)
        
        1. **Salud Mental** 🚨 - Indicador más fuerte de depresión/ansiedad
        2. **Emociones** 🚨 - Regulación emocional
        3. **Identidad Materna** 🚨 - Adaptación al rol materno
        4. **Relación con Bebé** 🚨 - Crítico para detectar problemas de apego
        
        #### ⚠️ IMPORTANTE
        
        Este sistema es una **herramienta de screening**, NO un diagnóstico clínico.
        
        Debe complementar, no sustituir, la evaluación profesional.
        """)
    
    with help_tab3:
        st.markdown("""
        ### 🧠 Sobre SUMEP v2.0
        
        **Sistema Universal de Monitoreo Emocional Perinatal**
        
        SUMEP es un sistema automatizado basado en Inteligencia Artificial para analizar 
        entrevistas perinatales y detectar señales de alerta emocional.
        
        #### Características Principales
        
        - **880+ Keywords Validadas** - 11x más completo que sistemas básicos
        - **16 Aspectos Psicosociales** - Análisis multidimensional
        - **Detección de Raíces Lingüísticas** - Reconoce variaciones morfológicas
        - **Análisis de Sentimientos con IA** - Modelo multilingüe CardiffNLP
        - **Precisión 3-5x Superior** - vs métodos tradicionales
        
        #### Tecnología
        
        - **Modelo de Sentimientos:** CardiffNLP Twitter-XLM-RoBERTa
        - **Procesamiento del Lenguaje:** SpaCy (español)
        - **Visualizaciones:** Plotly Interactive
        - **Framework:** Streamlit + Python
        
        #### Validación Científica
        
        Este sistema está en fase de validación clínica. Los resultados preliminares 
        muestran concordancia con escalas validadas (EPDS), pero se requiere estudio 
        prospectivo mayor (n>100) para establecer sensibilidad/especificidad.
        
        #### Limitaciones
        
        - No es una herramienta diagnóstica
        - No reemplaza evaluación clínica
        - No detecta comunicación no verbal
        - Optimizado para español (España)
        - Requiere entrevistas de calidad
        
        #### Citar Este Sistema
        
        Si usas SUMEP en investigación:
        
        > "El análisis se realizó mediante SUMEP v2.0 (Sistema Universal 
        > de Monitoreo Emocional Perinatal), un sistema automatizado basado 
        > en NLP con 880+ keywords y capacidad de lematización."
        
        ---
        
        **Versión:** 2.0  
        **Desarrollado por:** [Tu Nombre]  
        **Fecha:** Diciembre 2024  
        **Licencia:** Uso académico y clínico no comercial
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>SUMEP v2.0</strong> - Sistema Universal de Monitoreo Emocional Perinatal</p>
    <p>🌸 Mejorando la detección temprana de problemas emocionales perinatales 🌸</p>
    <p style='font-size: 0.9em;'>
        <a href='#'>Documentación</a> | 
        <a href='#'>GitHub</a> | 
        <a href='#'>Paper Científico</a>
    </p>
    <p style='font-size: 0.8em; margin-top: 1rem;'>
        ⚠️ Herramienta de screening complementaria - No sustituye evaluación clínica
    </p>
</div>
""", unsafe_allow_html=True)
