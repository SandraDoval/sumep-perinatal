"""
DICCIONARIO EXTENDIDO DE KEYWORDS - ANÁLISIS EMOCIONAL PERINATAL
Versión 2.0 - Con raíces y variaciones completas

Cada aspecto incluye:
- Keywords principales
- Variaciones morfológicas
- Expresiones coloquiales
- Raíces lemmatizadas
"""

# ============================================================================
# ASPECTOS EXTENDIDOS CON RAÍCES Y VARIACIONES
# ============================================================================

EXTENDED_ASPECTS = {
    
    # ========================================================================
    # 1. SALUD MENTAL (CRÍTICO)
    # ========================================================================
    "Mental_Health": {
        "keywords": [
            # Depresión - todas las formas
            "depresión", "depresivo", "depresiva", "deprimida", "deprimido", 
            "deprimir", "depre", "bajón", "bajona",
            
            # Ansiedad - todas las formas
            "ansiedad", "ansiosa", "ansioso", "angustia", "angustiada", "angustiado",
            "angustiar", "ansiada", "pánico", "ataques de pánico", "crisis de ansiedad",
            
            # Estado mental general
            "salud mental", "problema mental", "trastorno mental", "enfermedad mental",
            "psicológico", "psicológica", "psíquico", "psíquica",
            
            # Tratamiento
            "terapia", "psicólogo", "psicóloga", "psiquiatra", "terapeuta",
            "medicación", "antidepresivo", "antidepresivos", "pastillas",
            "fármaco", "tratamiento psicológico",
            
            # Sensaciones negativas intensas
            "desbordada", "desbordado", "desbordar", "sobrepasada", "sobrepasado",
            "no puedo más", "no aguanto", "no doy más", "saturada", "saturado",
            "agobiada", "agobio", "ahogada", "asfixiada",
            
            # Desesperanza
            "desesperada", "desesperado", "desesperación", "sin esperanza",
            "no veo salida", "túnel sin luz", "oscuridad", "vacío", "vacía",
            
            # Pensamientos oscuros
            "suicidar", "suicidio", "morir", "muerte", "acabar con todo",
            "desaparecer", "no estar", "ojalá no hubiera",
            
            # Estado emocional negativo
            "triste todo el tiempo", "siempre triste", "constantemente mal",
            "cada día peor", "empeorando", "no mejoro",
            
            # Pérdida de interés (anhedonia)
            "no disfruto", "no me gusta nada", "sin ganas", "sin ilusión",
            "todo me da igual", "nada me importa", "no me apetece nada",
            
            # Culpa y autocrítica
            "culpa", "culpable", "mi culpa", "mala persona",
            "merezco", "castigo", "fracaso como persona",
            
            # Diagnósticos
            "depresión postparto", "depresión perinatal", "baby blues",
            "trastorno de ansiedad", "trastorno adaptativo", "crisis emocional",
            
            # Expresiones coloquiales
            "estar mal", "pasarlo mal", "muy mal psicológicamente",
            "cabeza no para", "mente no descansa", "rumiación",
            "darle vueltas", "pensamientos negativos", "ideas negativas"
        ],
        "label": "Salud Mental",
        "critical": True
    },
    
    # ========================================================================
    # 2. EMOCIONES (CRÍTICO)
    # ========================================================================
    "Emotions": {
        "keywords": [
            # Miedo
            "miedo", "miedos", "temer", "temor", "terror", "pavor",
            "asustada", "asustado", "asustar", "espanto", "horror",
            "fobia", "fóbica",
            
            # Tristeza
            "triste", "tristeza", "llorar", "lloro", "llanto", "llorando",
            "lágrimas", "entristecer", "melancolía", "melancólica",
            "pena", "apena", "apenada",
            
            # Preocupación
            "preocupación", "preocupada", "preocupado", "preocupar",
            "inquieta", "inquieto", "inquietud", "intranquila", "intranquilo",
            
            # Nerviosismo
            "nervios", "nerviosa", "nervioso", "nerviosismo", "inquieta",
            "tensa", "tenso", "tensión", "estrés", "estresada", "estresado",
            
            # Ansiedad emocional
            "ansiosa", "ansioso", "angustia", "angustiada", "angustiado",
            
            # Pánico
            "pánico", "ataque de pánico", "crisis", "colapso emocional",
            
            # Alegría y felicidad (positivo)
            "alegría", "alegre", "contenta", "contento", "feliz", "felicidad",
            "ilusión", "ilusionada", "emoción positiva", "emocionada",
            
            # Amor
            "amor", "amar", "querer", "cariño", "ternura", "enamorada",
            
            # Emociones mixtas
            "ambivalencia", "ambivalente", "contradicción", "contradictoria",
            "no sé qué siento", "mezcla de sentimientos", "emociones encontradas",
            
            # Intensidad emocional
            "emocionalmente", "sentimiento", "sentimientos", "sentir",
            "siento", "me siento", "sensación", "emoción", "emociones",
            
            # Irritabilidad
            "irritable", "irritación", "irritada", "enfadada", "enfado",
            "rabia", "ira", "furia", "mal humor", "humor cambiante",
            
            # Culpa emocional
            "culpa", "culpabilidad", "avergonzada", "vergüenza",
            
            # Frustración
            "frustración", "frustrada", "frustrado", "impotencia", "impotente",
            
            # Expresiones de cambio emocional
            "cambios de humor", "altibajos", "inestable emocionalmente",
            "lábil", "montaña rusa emocional"
        ],
        "label": "Emociones",
        "critical": True
    },
    
    # ========================================================================
    # 3. IDENTIDAD MATERNA (CRÍTICO)
    # ========================================================================
    "Mother_Self": {
        "keywords": [
            # Identidad como madre
            "madre", "mamá", "mami", "madre soy", "mamá soy",
            "ser madre", "como madre", "mi maternidad", "maternidad",
            
            # Auto-referencia
            "yo como madre", "yo de madre", "mi papel de madre",
            "mi rol", "mi función", "mi responsabilidad",
            
            # Sentimientos sobre sí misma como madre
            "me siento", "me veo", "me percibo", "siento que soy",
            
            # Dudas sobre capacidad materna
            "no sé si sirvo", "no valgo", "no estoy preparada",
            "no sé ser madre", "no sé cómo", "no puedo",
            
            # Autocrítica materna severa
            "mala madre", "madre horrible", "madre terrible", "pésima madre",
            "no merezco ser madre", "no debería ser madre",
            
            # Insuficiencia
            "insuficiente", "no doy la talla", "no llego", "no lo hago bien",
            "lo hago todo mal", "no sé hacerlo",
            
            # Fracaso
            "fracaso", "fracaso como madre", "he fallado", "fallo",
            "decepción", "decepciono", "frustrante",
            
            # Incompetencia
            "incompetente", "incapaz", "no soy capaz", "no puedo",
            "torpe", "inútil", "no sirvo",
            
            # Comparación negativa
            "otras madres", "comparándome", "peor madre que",
            "no soy como otras", "todas lo hacen mejor",
            
            # Expectativas vs realidad
            "esperaba ser diferente", "pensé que sería", "no es como imaginaba",
            "idealicé", "no es lo que pensaba",
            
            # Ambivalencia sobre maternidad
            "arrepiento", "arrepentimiento", "no debí", "error",
            "no quería", "no estaba preparada",
            
            # Identidad perdida
            "ya no soy yo", "he perdido mi identidad", "quién soy",
            "no me reconozco", "extraña para mí misma",
            
            # Transformación
            "he cambiado", "ya no soy la misma", "otra persona",
            "transformación", "cambio radical"
        ],
        "label": "Identidad Materna",
        "critical": True
    },
    
    # ========================================================================
    # 4. RELACIÓN CON BEBÉ (CRÍTICO)
    # ========================================================================
    "Baby": {
        "keywords": [
            # Nombres del bebé
            "bebé", "bebe", "bebés", "niño", "niña", "hijo", "hija",
            "recién nacido", "recién nacida", "neonato", "criatura",
            "pequeño", "pequeña", "chiquitín", "chiquitina",
            
            # Vínculo
            "vínculo", "apego", "unión", "conexión", "lazo",
            "conexión con", "vinculada", "vinculado",
            
            # Sentimientos hacia bebé
            "amor hacia", "quiero a", "adoro a", "amo a",
            "cariño hacia", "ternura hacia",
            
            # Problemas de vínculo
            "no siento", "no conecto", "no me une", "distante",
            "lejos", "ajena", "ajeno", "extraño",
            "no lo siento mío", "no es mío", "como si no fuera mío",
            
            # Rechazo (clave para detección)
            "rechazo", "rechazar", "no quiero", "no lo aguanto",
            "me molesta", "me irrita", "me enfada",
            
            # Ambivalencia
            "sentimientos contradictorios", "a veces sí a veces no",
            "no sé qué siento", "confusa con",
            
            # Idealización vs realidad
            "no es como esperaba", "pensé que sería diferente",
            "imaginaba otra cosa", "no es lo que creía",
            
            # Interacciones
            "coger en brazos", "abrazar", "besar", "acariciar",
            "mirar", "observar", "jugar con",
            
            # Llanto del bebé (reacción materna)
            "cuando llora", "su llanto", "llorar", "llanto me",
            "no sé calmarlo", "no para de llorar", "llora mucho",
            
            # Cuidados
            "cuidar", "cuidado", "atender", "atención",
            "ocuparme", "responsable de",
            
            # Preocupación por bebé
            "me preocupa", "temor por", "miedo a que",
            "si le pasa algo", "peligro",
            
            # Disfrute
            "disfruto", "disfrutar", "gozar", "placer",
            "feliz con", "me hace feliz",
            
            # Falta de disfrute
            "no disfruto", "no me gusta", "no es placentero",
            "pesado", "carga", "obligación",
            
            # Comportamiento bebé
            "tranquilo", "inquieto", "dormilón", "llorón",
            "fácil", "difícil", "demandante", "exigente",
            
            # Expresiones coloquiales sobre bebé
            "se porta", "cómo es", "su carácter", "su forma de ser"
        ],
        "label": "Relación con Bebé",
        "critical": True
    },
    
    # ========================================================================
    # 5. PAREJA
    # ========================================================================
    "Partner": {
        "keywords": [
            # Referencia a pareja
            "pareja", "mi pareja", "compañero", "compañera",
            "esposo", "esposa", "marido", "mujer",
            "padre del bebé", "madre del bebé",
            "novio", "novia",
            
            # Relación
            "relación de pareja", "nuestra relación", "lo nuestro",
            "entre nosotros", "con él", "con ella",
            
            # Apoyo de pareja
            "me apoya", "me ayuda", "está conmigo", "me acompaña",
            "cuenta con él", "cuenta con ella", "puedo contar",
            
            # Falta de apoyo
            "no me apoya", "no me ayuda", "no está", "ausente",
            "solo", "sola", "no cuento con", "no me escucha",
            
            # Participación en cuidados
            "participa", "colabora", "se implica", "se involucra",
            "cuida", "atiende", "cambia pañales", "da biberón",
            
            # Falta de participación
            "no participa", "no colabora", "no ayuda", "no hace nada",
            "todo yo", "yo sola", "carga sola",
            
            # Comunicación
            "hablamos", "nos comunicamos", "expresamos", "compartimos",
            "le cuento", "me escucha", "escuchamos",
            
            # Problemas de comunicación
            "no hablamos", "no me entiende", "no entiendo",
            "discutimos", "peleamos", "conflictos", "peleas",
            
            # Comprensión
            "me comprende", "me entiende", "entiende por lo que paso",
            "empatiza", "se pone en mi lugar",
            
            # Falta de comprensión
            "no me comprende", "no me entiende", "no se da cuenta",
            "minimiza", "no le importa",
            
            # Conflictos
            "problemas con", "crisis", "tensión", "distancia",
            "alejamiento", "frialdad", "mal ambiente",
            
            # Expresiones sobre pareja
            "cómo es", "su actitud", "su comportamiento",
            "lo que hace", "lo que dice",
            
            # Trabajo de pareja
            "trabaja mucho", "llega tarde", "no está en casa",
            "horarios", "ocupado", "ocupada",
            
            # Intimidad
            "intimidad", "sexo", "relaciones", "sexualidad",
            "deseo", "atracción", "cercanía física",
            
            # Cambios en relación
            "ha cambiado", "ya no es igual", "diferente",
            "desde el bebé", "desde el embarazo"
        ],
        "label": "Relación de Pareja",
        "critical": False
    },
    
    # ========================================================================
    # 6. SUEÑO Y DESCANSO
    # ========================================================================
    "Sleep_Rest": {
        "keywords": [
            # Sueño
            "dormir", "duermo", "sueño", "descanso", "descansar",
            "dormir bien", "dormir mal", "no duermo", "sin dormir",
            
            # Insomnio
            "insomnio", "no puedo dormir", "me cuesta dormir",
            "me desvelo", "no me quedo dormida", "despertarme",
            
            # Calidad del sueño
            "bien descansada", "mal descansada", "sueño profundo",
            "sueño ligero", "interrupciones", "fragmentado",
            
            # Noche
            "noche", "noches", "nocturna", "nocturno", "de noche",
            "por la noche", "durante la noche", "madrugada",
            
            # Despertares
            "me despierto", "despertares", "interrupciones nocturnas",
            "cada hora", "varias veces", "constantemente",
            
            # Cansancio relacionado
            "cansancio", "cansada", "agotamiento", "agotada",
            "exhausta", "extenuada", "sin fuerzas",
            
            # Necesidad de descanso
            "necesito dormir", "necesito descansar", "ansío dormir",
            "deseo descansar", "muero por dormir",
            
            # Falta de descanso
            "no descanso", "sin descanso", "no puedo descansar",
            "nunca descanso", "imposible descansar",
            
            # Siestas
            "siesta", "dormir de día", "cabezada", "descansar de día",
            
            # Expresiones coloquiales
            "ojos se cierran", "zombi", "sonámbula", "autómata",
            "no funciono", "funcionar sin dormir",
            
            # Bebé y sueño
            "bebé no duerme", "bebé no me deja", "despierta mucho",
            "llora por la noche", "demanda nocturna",
            
            # Consecuencias
            "ojeras", "aspecto", "demacrada", "sin energía",
            "irritable por sueño", "mal humor por no dormir"
        ],
        "label": "Sueño y Descanso",
        "critical": False
    },
    
    # ========================================================================
    # 7. LACTANCIA
    # ========================================================================
    "Breastfeeding": {
        "keywords": [
            # Lactancia materna
            "lactancia", "lactar", "lactancia materna", "amamantar",
            "dar el pecho", "pecho", "teta", "dar teta",
            
            # Leche
            "leche materna", "mi leche", "producción de leche",
            "subida de leche", "bajada de leche",
            
            # Acción de amamantar
            "amamanto", "le doy pecho", "le pongo al pecho",
            "se agarra", "succiona", "mama",
            
            # Problemas lactancia
            "grietas", "dolor al dar", "me duele", "sangra",
            "mastitis", "obstrucción", "conducto obstruido",
            
            # Producción
            "poca leche", "mucha leche", "no tengo suficiente",
            "hipogalactia", "hipergalactia",
            
            # Agarre
            "mal agarre", "buen agarre", "no se agarra bien",
            "posición", "postura al dar",
            
            # Dificultades
            "cuesta mucho", "difícil", "complicado", "sufrimiento",
            "no lo consigo", "no puedo",
            
            # Lactancia mixta
            "mixta", "complemento", "suplemento", "biberón también",
            
            # Biberón
            "biberón", "leche de fórmula", "fórmula", "artificial",
            "dar biberón", "leche artificial",
            
            # Decisiones sobre lactancia
            "dejar la lactancia", "abandonar", "desistir",
            "lactancia prolongada", "hasta cuándo",
            
            # Frecuencia
            "cada cuánto", "demanda", "libre demanda", "horarios",
            "tomas", "muchas tomas", "pocas tomas",
            
            # Duración
            "cuánto tiempo", "minutos", "media hora", "tiempo al pecho",
            
            # Sentimientos sobre lactancia
            "disfruto", "sufro", "me gusta", "no me gusta",
            "placentero", "doloroso", "incómodo",
            
            # Presión social
            "obligada", "presión", "debería", "esperan que",
            "juzgan", "critican",
            
            # Apoyo profesional
            "matrona lactancia", "asesora de lactancia", "consultora",
            "grupo de lactancia"
        ],
        "label": "Lactancia",
        "critical": False
    },
    
    # ========================================================================
    # 8. SALUD FÍSICA
    # ========================================================================
    "Physical": {
        "keywords": [
            # Dolor
            "dolor", "duele", "doloroso", "dolorosa", "molestia",
            "molestias", "sufrimiento físico",
            
            # Recuperación postparto
            "recuperación", "recuperándome", "curación", "sanar",
            "cicatrizar", "cicatrización",
            
            # Heridas específicas
            "herida", "episiotomía", "desgarro", "puntos",
            "sutura", "cesárea", "cicatriz",
            
            # Sangrado
            "sangrado", "sangrar", "sangre", "hemorragia",
            "loquios", "menstruación", "regla",
            
            # Molestias generales
            "molestia", "malestar", "incomodidad", "fastidio",
            
            # Cansancio físico
            "cansancio físico", "agotamiento corporal", "físicamente agotada",
            "sin fuerzas", "debilidad", "débil",
            
            # Cambios corporales
            "mi cuerpo", "cambios físicos", "físicamente diferente",
            "corporalmente", "aspecto físico",
            
            # Problemas específicos
            "estreñimiento", "hemorroides", "incontinencia",
            "pérdidas de orina", "suelo pélvico",
            
            # Pechos
            "pechos duelen", "mastitis", "ingurgitación", "hinchazón",
            
            # Espalda
            "dolor de espalda", "lumbar", "cervical", "contracturas",
            
            # Periné
            "periné", "zona perineal", "entre las piernas",
            
            # Estado general
            "me encuentro", "físicamente", "estado físico",
            "salud física", "corporalmente",
            
            # Energía
            "energía", "vitalidad", "vigor", "fuerza",
            "sin energía", "falta de energía",
            
            # Medicación
            "analgésico", "ibuprofeno", "paracetamol", "medicación para dolor",
            
            # Expresiones sobre recuperación
            "todavía me duele", "aún molesta", "no termino de curar",
            "tarda en sanar"
        ],
        "label": "Salud Física",
        "critical": False
    },
    
    # ========================================================================
    # 9. EXPERIENCIA DE PARTO
    # ========================================================================
    "Birth": {
        "keywords": [
            # Parto
            "parto", "dar a luz", "alumbramiento", "nacimiento",
            "nacer", "nació", "nacimiento del bebé",
            
            # Tipos de parto
            "parto natural", "parto vaginal", "cesárea", "cesárea de urgencia",
            "cesárea programada", "inducción", "parto inducido",
            
            # Hospital
            "hospital", "clínica", "centro médico", "paritorio",
            "sala de partos", "dilatación", "sala de dilatación",
            
            # Fases del parto
            "dilatación", "dilatar", "expulsivo", "coronación",
            "salida", "nacimiento", "alumbramiento de placenta",
            
            # Dolor del parto
            "contracciones", "dolor de parto", "sufrir", "doloroso",
            "dolor intenso", "agónico",
            
            # Anestesia
            "epidural", "anestesia", "sin epidural", "con epidural",
            "pinchazo", "anestesiar",
            
            # Episiotomía y desgarros
            "episiotomía", "corte", "desgarro", "rasgadura",
            
            # Instrumentalización
            "fórceps", "ventosa", "instrumental", "ayuda instrumental",
            
            # Duración
            "horas de parto", "largo", "corto", "rápido", "duró",
            
            # Experiencia emocional
            "experiencia del parto", "cómo fue", "vivencia",
            "traumático", "traumática", "bonito", "horrible",
            
            # Complicaciones
            "complicación", "urgencia", "emergencia", "riesgo",
            "peligro", "sufrimiento fetal",
            
            # Personas presentes
            "acompañada", "sola", "pareja presente", "matrona",
            "médico", "equipo médico",
            
            # Satisfacción
            "contenta con", "decepcionada", "no fue como esperaba",
            "fue como quería", "respetado", "plan de parto",
            
            # Secuelas emocionales
            "recuerdo", "flashbacks", "pesadillas", "vuelvo a vivir",
            "no puedo olvidar", "me persigue"
        ],
        "label": "Experiencia de Parto",
        "critical": False
    },
    
    # ========================================================================
    # 10. PROFESIONALES SANITARIOS
    # ========================================================================
    "Healthcare": {
        "keywords": [
            # Matrona
            "matrona", "matronas", "comadrona", "comadronas",
            
            # Médicos
            "médico", "médica", "doctor", "doctora",
            "ginecólogo", "ginecóloga", "obstetra",
            "pediatra", "neonatólogo", "neonatóloga",
            
            # Enfermería
            "enfermera", "enfermero", "enfermería",
            "auxiliar", "TCAE",
            
            # Salud mental
            "psicólogo", "psicóloga", "psiquiatra",
            "terapeuta", "psicoterapeuta",
            
            # Personal sanitario general
            "personal sanitario", "equipo médico", "equipo sanitario",
            "profesional", "profesionales", "sanitario", "sanitaria",
            
            # Instituciones
            "hospital", "centro de salud", "consultorio",
            "ambulatorio", "clínica",
            
            # Atención recibida
            "atención", "atender", "atendida", "cuidado",
            "cuidar", "tratar", "tratamiento",
            
            # Calidad de atención
            "bien atendida", "mal atendida", "trato bueno", "trato malo",
            "amable", "brusco", "brusca", "empática", "empático",
            
            # Comunicación
            "me explican", "me informan", "me escuchan",
            "no me escuchan", "no me explican", "no me informan",
            
            # Confianza
            "confío", "confianza", "segura con", "insegura con",
            
            # Seguimiento
            "seguimiento", "control", "visita", "revisión",
            "cita", "consulta",
            
            # Apoyo profesional
            "me apoyan", "me ayudan", "me orientan", "me guían",
            
            # Problemas con profesionales
            "desatención", "abandono", "mal trato", "violencia obstétrica",
            "no me hacen caso", "infravaloran", "minimizan",
            
            # Derivaciones
            "derivan", "referir", "enviar a", "remitir a"
        ],
        "label": "Profesionales Sanitarios",
        "critical": False
    },
    
    # ========================================================================
    # 11. APOYO SOCIAL
    # ========================================================================
    "Social_Support": {
        "keywords": [
            # Familia
            "familia", "familiar", "familiares", "mi familia",
            "parientes", "consanguíneos",
            
            # Padres
            "padres", "mi padre", "mi madre", "papá", "mamá",
            "suegro", "suegra", "suegros",
            
            # Hermanos
            "hermano", "hermana", "hermanos", "hermanas",
            
            # Amigas/os
            "amiga", "amigo", "amigas", "amigos", "mis amigas",
            "círculo de amistades", "grupo de amigas",
            
            # Apoyo
            "apoyo", "me apoyan", "apoyar", "ayuda", "me ayudan",
            "ayudar", "socorro", "auxilio", "respaldo",
            
            # Acompañamiento
            "acompañamiento", "acompañar", "acompañada", "compañía",
            "estar ahí", "presente", "disponible",
            
            # Grupos de apoyo
            "grupo", "grupo de apoyo", "grupo de madres",
            "asociación", "comunidad", "red de apoyo",
            
            # Soledad vs compañía
            "sola", "soledad", "aislada", "aislamiento",
            "acompañada", "rodeada", "arropada",
            
            # Red social
            "red social", "red de apoyo", "círculo",
            "entorno", "alrededor", "gente cerca",
            
            # Falta de apoyo
            "no tengo apoyo", "sin apoyo", "nadie me ayuda",
            "nadie", "abandono", "desamparo",
            
            # Vecinos/comunidad
            "vecina", "vecino", "vecindario", "barrio",
            "comunidad", "entorno cercano",
            
            # Ayuda práctica
            "ayuda práctica", "tareas", "recados", "hacer compra",
            "limpiar", "cocinar", "cuidar al bebé",
            
            # Apoyo emocional
            "apoyo emocional", "escuchar", "desahogarme",
            "hablar", "compartir", "expresar",
            
            # Comprensión social
            "me entienden", "me comprenden", "empatizan",
            "se ponen en mi lugar",
            
            # Falta de comprensión
            "no me entienden", "no comprenden", "juzgan",
            "critican", "opinan", "se meten"
        ],
        "label": "Apoyo Social",
        "critical": False
    },
    
    # ========================================================================
    # 12. RELACIÓN CON PROPIA MADRE
    # ========================================================================
    "Own_Mother": {
        "keywords": [
            # Referencias directas
            "mi madre", "mi mamá", "mi propia madre",
            "mi ma", "mami",
            
            # Relación
            "relación con mi madre", "vínculo con mi madre",
            "cómo es mi madre", "mi madre es",
            
            # Interacciones actuales
            "mi madre me", "mi mamá me", "hablar con mi madre",
            "llamar a mi madre", "ver a mi madre",
            
            # Apoyo maternal
            "mi madre me apoya", "mi madre me ayuda",
            "cuenta mi madre", "mi madre está",
            
            # Conflictos
            "problemas con mi madre", "discuto con mi madre",
            "tensión con mi madre", "no me llevo",
            
            # Ausencia
            "mi madre no", "sin mi madre", "no tengo a mi madre",
            "mi madre murió", "mi madre falleció",
            
            # Influencia
            "como mi madre", "igual que mi madre",
            "parecida a mi madre", "diferente a mi madre",
            
            # Aprendizaje
            "mi madre me enseñó", "aprendí de mi madre",
            "mi madre decía", "consejos de mi madre",
            
            # Estilo de crianza materno
            "cómo me crió", "cómo fue mi crianza",
            "mi infancia con mi madre", "mi madre como madre",
            
            # Repetición de patrones
            "repito", "hago lo mismo", "como ella",
            "no quiero ser como", "quiero ser diferente",
            
            # Expectativas
            "mi madre espera", "mi madre quiere",
            "presión de mi madre", "exigencias",
            
            # Comparaciones
            "mi madre lo hacía", "mi madre era",
            "comparar con", "diferente a",
            
            # Apoyo en crianza
            "mi madre cuida", "mi madre me aconseja",
            "mi madre opina", "consejos",
            
            # Intrusión
            "mi madre se mete", "mi madre interfiere",
            "mi madre controla", "entrometida"
        ],
        "label": "Relación con Propia Madre",
        "critical": False
    },
    
    # ========================================================================
    # 13. IMAGEN CORPORAL
    # ========================================================================
    "Body_Image": {
        "keywords": [
            # Cuerpo
            "mi cuerpo", "cuerpo", "corporalmente", "físicamente",
            "mi físico", "aspecto corporal",
            
            # Peso
            "peso", "kilos", "pesar", "pesarme", "báscula",
            "subir de peso", "bajar de peso", "engordar", "adelgazar",
            
            # Imagen
            "imagen", "imagen corporal", "cómo me veo",
            "mi aspecto", "apariencia", "mi apariencia",
            
            # Descriptores negativos
            "gorda", "gordo", "obesa", "sobrepeso", "kilos de más",
            "michelines", "grasa", "barriga", "tripa",
            
            # Descriptores positivos/neutros
            "delgada", "delgado", "flaca", "peso normal",
            
            # Cambios corporales
            "cambios físicos", "cambios corporales", "cambió mi cuerpo",
            "cuerpo diferente", "ya no es igual",
            
            # Verme
            "verme", "mirarme", "cuando me miro", "espejo",
            "en el espejo", "mi reflejo",
            
            # Aceptación
            "acepto", "me acepto", "aceptar mi cuerpo",
            "conforme con", "a gusto con",
            
            # Rechazo
            "no me gusta", "odio mi cuerpo", "rechazo",
            "asco", "disgusto", "me da pena",
            
            # Estética
            "estrías", "celulitis", "flacidez", "piel",
            "cicatriz", "marcas", "manchas",
            
            # Pechos
            "mis pechos", "senos", "busto", "pecho caído",
            "tamaño", "forma",
            
            # Abdomen
            "barriga", "tripa", "abdomen", "vientre",
            "flacidez abdominal", "diástasis",
            
            # Ropa
            "ropa", "no me queda", "talla", "tallaje",
            "no me entra", "vestirio", "no encuentro qué ponerme",
            
            # Comparación con antes
            "antes del embarazo", "cuerpo anterior",
            "recuperar", "volver a ser", "como antes",
            
            # Presión social/estética
            "debería", "expectativas", "presión por",
            "otros cuerpos", "modelos", "famosas",
            
            # Autocrítica
            "me critico", "soy muy crítica", "exigente",
            "perfeccionista", "nunca conforme"
        ],
        "label": "Imagen Corporal",
        "critical": False
    },
    
    # ========================================================================
    # 14. TRABAJO Y CARRERA
    # ========================================================================
    "Work_Career": {
        "keywords": [
            # Trabajo general
            "trabajo", "trabajar", "empleo", "ocupación",
            "mi trabajo", "mi empleo",
            
            # Carrera
            "carrera", "carrera profesional", "trayectoria",
            "desarrollo profesional", "ascenso",
            
            # Lugar de trabajo
            "oficina", "empresa", "lugar de trabajo",
            "puesto", "mi puesto",
            
            # Jefes y compañeros
            "jefe", "jefa", "superior", "compañeros de trabajo",
            "equipo", "colegas",
            
            # Laboral
            "laboral", "profesional", "ambiente laboral",
            "situación laboral",
            
            # Baja maternal
            "baja maternal", "permiso maternal", "maternidad",
            "excedencia", "permiso parental",
            
            # Reincorporación
            "volver al trabajo", "reincorporarme", "vuelta",
            "cuando vuelva", "reintegrarme",
            
            # Preocupaciones laborales
            "miedo a perder", "despido", "incertidumbre",
            "contrato", "estabilidad laboral",
            
            # Conciliación
            "conciliar", "conciliación", "compatibilizar",
            "equilibrio", "balance trabajo-familia",
            
            # Dificultades conciliación
            "no puedo", "imposible", "difícil conciliar",
            "no llego", "no da tiempo",
            
            # Guardería
            "guardería", "escuela infantil", "cuidadora",
            "niñera", "dejar al bebé",
            
            # Culpa laboral
            "culpa por trabajar", "mala madre por trabajar",
            "debería estar con", "le quito tiempo",
            
            # Ambición vs maternidad
            "ambición", "aspiraciones", "metas profesionales",
            "sacrificar carrera", "renunciar a",
            
            # Horarios
            "horario", "jornada", "turnos", "horario laboral",
            "flexibilidad", "inflexible",
            
            # Rendimiento
            "rendimiento", "productividad", "eficiencia",
            "concentración", "no rindo igual",
            
            # Identidad profesional
            "identidad profesional", "quién soy profesionalmente",
            "me define", "soy más que madre"
        ],
        "label": "Trabajo y Carrera",
        "critical": False
    },
    
    # ========================================================================
    # 15. PREOCUPACIONES ECONÓMICAS
    # ========================================================================
    "Financial": {
        "keywords": [
            # Dinero
            "dinero", "plata", "dineros", "euros",
            "económico", "económica", "economía", "finanzas",
            
            # Gastos
            "gastos", "gastar", "gasto", "coste", "cuesta",
            "precio", "precios", "caro", "cara", "costoso",
            
            # Pagar
            "pagar", "pago", "pagos", "abonar", "desembolso",
            
            # Permitirse
            "permitir", "puedo permitirme", "no puedo permitir",
            "alcanza", "no alcanza", "llega", "no llega",
            
            # Situación económica
            "situación económica", "economía familiar",
            "situación financiera", "bolsillo",
            
            # Problemas económicos
            "apuros", "dificultades económicas", "estrecheces",
            "escasez", "falta dinero", "no tenemos",
            
            # Necesidades del bebé
            "pañales", "leche artificial", "ropa del bebé",
            "cosas del bebé", "cuna", "carrito", "sillita",
            
            # Presupuesto
            "presupuesto", "ajustar", "recortar", "economizar",
            "ahorrar", "ahorro",
            
            # Ingresos
            "ingreso", "ingresos", "sueldo", "salario",
            "nómina", "ganar", "gano",
            
            # Ayudas
            "ayuda", "subsidio", "prestación", "beca",
            "ayudas económicas",
            
            # Deudas
            "deuda", "deudas", "deber", "préstamo",
            "crédito", "hipoteca",
            
            # Preocupación
            "preocupa el dinero", "angustia económica",
            "estrés financiero", "agobio económico",
            
            # Dependencia económica
            "dependo de", "mantiene", "sostén",
            "independencia económica",
            
            # Consumo
            "comprar", "compra", "adquirir", "necesitar comprar"
        ],
        "label": "Preocupaciones Económicas",
        "critical": False
    },
    
    # ========================================================================
    # 16. EXPECTATIVAS FUTURAS
    # ========================================================================
    "Future_Expectations": {
        "keywords": [
            # Futuro general
            "futuro", "futura", "porvenir", "mañana",
            "más adelante", "próximo", "próxima", "próximamente",
            
            # Esperar
            "espero", "esperar", "esperanza", "espero que",
            "ojalá", "deseo que", "confío en que",
            
            # Imaginar
            "imagino", "imaginar", "me imagino", "visualizo",
            "fantaseo", "sueño con",
            
            # Cuando crezca
            "cuando crezca", "cuando sea mayor", "cuando tenga",
            "más grande", "de mayor", "en el futuro",
            
            # Planes
            "planes", "planear", "planificar", "proyecto",
            "proyectos", "intenciones", "propósito",
            
            # Objetivos
            "objetivo", "objetivos", "meta", "metas",
            "aspiración", "aspiraciones",
            
            # Esperanzas
            "espero", "anhelo", "deseo", "quiero que",
            "me gustaría que", "quisiera que",
            
            # Miedos futuros
            "miedo a", "temor a", "preocupa el futuro",
            "inquieta el futuro", "incertidumbre",
            
            # Crecimiento del bebé
            "cuando sea mayor", "su desarrollo", "crecimiento",
            "evolución", "etapas", "fases",
            
            # Familia futura
            "más hijos", "hermano", "hermana", "ampliar familia",
            "tener más", "otro bebé",
            
            # No querer más hijos
            "no más hijos", "suficiente", "basta", "uno solo",
            
            # Educación del hijo
            "colegio", "educación", "escuela", "formación",
            "crianza futura",
            
            # Vida personal futura
            "recuperar mi vida", "volver a", "retomar",
            "cuando pase esto", "normalidad",
            
            # Optimismo
            "mejor", "mejorará", "pasará", "superaremos",
            "saldremos adelante", "confío",
            
            # Pesimismo
            "no mejorará", "peor", "empeorará",
            "no veo salida", "sin futuro", "negro",
            
            # Tiempo
            "dentro de", "en unos meses", "en un año",
            "pronto", "algún día"
        ],
        "label": "Expectativas Futuras",
        "critical": False
    }
}
