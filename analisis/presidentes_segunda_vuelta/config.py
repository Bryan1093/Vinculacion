"""
Configuración para análisis electoral de Presidentes - Segunda Vuelta 1996
"""

import os

# Nombre del archivo a analizar
NOMBRE_ARCHIVO = '1996 - Presidentes - segunda vuelta.xlsx'

# Rutas de archivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'Datos-Presidentes-Completos', 'Segunda Vuelta')
RESULTS_DIR = os.path.join(BASE_DIR, 'PRESEDENTES', 'SEGUNDA_VUELTA')
DATA_FILE = os.path.join(DATA_DIR, NOMBRE_ARCHIVO)

# Crear directorio de resultados si no existe
os.makedirs(RESULTS_DIR, exist_ok=True)

# Mapeo de candidatos a columnas de votos (Segunda Vuelta - solo 2 candidatos)
CANDIDATOS = {
    'NEBOT JAIME': {
        'columnas': ['PSC6'],
        'partido': 'PSC',
        'nombre_completo': 'JAIME NEBOT SAADI'
    },
    'BUCARAM ABDALÁ': {
        'columnas': ['PRE10'],
        'partido': 'PRE',
        'nombre_completo': 'ABDALÁ BUCARAM ORTIZ'
    }
}

# Mapeo de nombres de provincias a códigos
CODIGOS_PROVINCIAS = {
    'AZUAY': '01',
    'BOLÍVAR': '02',
    'CAÑAR': '03',
    'CARCHI': '04',
    'COTOPAXI': '05',
    'CHIMBORAZO': '06',
    'EL ORO': '07',
    'ESMERALDAS': '08',
    'GUAYAS': '09',
    'IMBABURA': '10',
    'LOJA': '11',
    'LOS RÍOS': '12',
    'MANABÍ': '13',
    'MORONA SANTIAGO': '14',
    'NAPO': '15',
    'PASTAZA': '16',
    'PICHINCHA': '17',
    'TUNGURAHUA': '18',
    'ZAMORA CHINCHIPE': '19',
    'GALÁPAGOS': '20',
    'SUCUMBÍOS': '21',
    'ORELLANA': '22',
    'SANTO DOMINGO DE LOS TSÁCHILAS': '23',
    'SANTA ELENA': '24'
}

# Provincias a analizar (las mismas que primera vuelta)
PROVINCIAS_SELECCIONADAS = {
    'NAPO': '15',
    'PASTAZA': '16',
}

# Mapeo de cantones de Pichincha
CANTONES_PICHINCHA = {
    '60': 'QUITO',
    '65': 'CAYAMBE',
    '70': 'MEJIA',
    '75': 'PEDRO MONCAYO',
    '80': 'RUMIÑAHUI',
    '85': 'SANTO DOMINGO',
    '770': 'SAN MIGUEL DE LOS BANCOS',
    '895': 'PEDRO VICENTE MALDONADO'
}

# ========== CONFIGURACIÓN SIMPLE DE CANTONES ==========
# Solo cambia esta línea para analizar cantones de otra provincia:
PROVINCIA_PARA_CANTONES = 'PICHINCHA'  # Cambia a 'GUAYAS', 'AZUAY', etc.
# ======================================================

# Nombres de columnas importantes
COL_PROVINCIA = 'PROVINCI'
COL_CANTON = 'CANTON'
COL_PARROQUIA = 'PARROQUIA'
COL_VOTOS_VALIDOS = 'VOTOSVAL'
COL_VOTOS_NULOS = 'VOTOSNUL'
COL_VOTOS_BLANCOS = 'VOTOSBLA'
COL_VOTOS_ESCRUTADOS = 'VOTOSESC'
