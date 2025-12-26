"""
Configuración y constantes para el análisis electoral 1996
"""

import os

# Nombre del archivo a analizar (cambiar aquí para usar otro archivo)
NOMBRE_ARCHIVO = '1996 - Presidentes - primera vuelta.xlsx'

# Rutas de archivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'Datos-Presidentes-Completos', 'Primera Vuelta')
RESULTS_DIR = os.path.join(BASE_DIR, 'resultados')
DATA_FILE = os.path.join(DATA_DIR, NOMBRE_ARCHIVO)

# Crear directorio de resultados si no existe
os.makedirs(RESULTS_DIR, exist_ok=True)

# Mapeo de candidatos a columnas de votos
# Basado en el análisis del notebook original
CANDIDATOS = {
    'NOBOA RICARDO': {
        'columnas': ['PLRE - FRA'],
        'partido': 'PLRE-FRA',
        'nombre_completo': 'RICARDO NOBOA BEJARANO'
    },
    'PAZ RODRIGO': {
        'columnas': ['DP5'],
        'partido': 'DP',
        'nombre_completo': 'RODRIGO PAZ DELGADO'
    },
    'NEBOT JAIME': {
        'columnas': ['PSC6'],
        'partido': 'PSC',
        'nombre_completo': 'JAIME NEBOT SAADI'
    },
    'BUCARAM ABDALÁ': {
        'columnas': ['PRE10'],
        'partido': 'PRE',
        'nombre_completo': 'ABDALÁ BUCARAM ORTIZ'
    },
    'VARGAS FRANK': {
        'columnas': ['APRE13'],
        'partido': 'APRE',
        'nombre_completo': 'FRANK VARGAS PAZZOS'
    },
    'CASTELLÓ JUAN': {
        'columnas': ['MPD15'],
        'partido': 'MPD',
        'nombre_completo': 'JUAN JOSÉ CASTELLÓ MANZANO'
    },
    'EHLEARS FREDDY': {
        'columnas': ['MUPP-NP18'],
        'partido': 'MUPP-NP',
        'nombre_completo': 'FREDDY EHLERS ZURITA'
    },
    'GALLARDO JOSÉ': {
        'columnas': ['UCI19'],
        'partido': 'UCI',
        'nombre_completo': 'JOSÉ GALLARDO ZAVALA'
    },
    'VELÁZQUEZ JACINTO': {
        'columnas': ['MITI20'],
        'partido': 'MITI',
        'nombre_completo': 'JACINTO VELÁZQUEZ ROSALES'
    }
}

# Mapeo de nombres de provincias a códigos (para JSON)
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

# Mapeo de códigos de provincias a nombres (provincias a analizar)
PROVINCIAS_SELECCIONADAS = {
    'NAPO': '15',
    'PASTAZA': '16',
}

# Mapeo de cantones de Pichincha (código: nombre real)
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

# Parroquias de Pastaza
PARROQUIAS_PASTAZA = {
    '30': 'PARROQUIA 30',
    '80': 'PARROQUIA 80'
}

# Nombres de columnas importantes
COL_PROVINCIA = 'PROVINCI'
COL_CANTON = 'CANTON'
COL_PARROQUIA = 'PARROQUIA'
COL_VOTOS_VALIDOS = 'VOTOSVAL'
COL_VOTOS_NULOS = 'VOTOSNUL'
COL_VOTOS_BLANCOS = 'VOTOSBLA'
COL_VOTOS_ESCRUTADOS = 'VOTOSESC'
