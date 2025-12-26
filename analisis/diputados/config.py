"""
Configuración para análisis electoral de Diputados Nacionales 1996
"""

import os

# Nombre del archivo a analizar
NOMBRE_ARCHIVO = '1996 - Diputados - nacionales.xlsx'

# Rutas de archivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'Datos-Diputados-Completos')
RESULTS_DIR = os.path.join(BASE_DIR, 'resultados', 'diputados')
DATA_FILE = os.path.join(DATA_DIR, NOMBRE_ARCHIVO)

# Crear directorio de resultados si no existe
os.makedirs(RESULTS_DIR, exist_ok=True)

# Mapeo de partidos/listas a columnas de votos
# Basado en el análisis del archivo de diputados nacionales 1996
# Total: 14 partidos/listas
PARTIDOS = {
    'PCE': {
        'columnas': ['PCE1'],
        'nombre_completo': 'PARTIDO COMUNISTA ECUATORIANO'
    },
    'CFP': {
        'columnas': ['CFP4'],
        'nombre_completo': 'CONCENTRACIÓN DE FUERZAS POPULARES'
    },
    'DP': {
        'columnas': ['DP5'],
        'nombre_completo': 'DEMOCRACIA POPULAR'
    },
    'PSC': {
        'columnas': ['PSC6'],
        'nombre_completo': 'PARTIDO SOCIAL CRISTIANO'
    },
    'PRE': {
        'columnas': ['PRE10'],
        'nombre_completo': 'PARTIDO ROLDOSISTA ECUATORIANO'
    },
    'AN': {
        'columnas': ['AN11'],
        'nombre_completo': 'ALIANZA NACIONAL'
    },
    'ID': {
        'columnas': ['ID12'],
        'nombre_completo': 'IZQUIERDA DEMOCRÁTICA'
    },
    'APRE': {
        'columnas': ['APRE13'],
        'nombre_completo': 'ACCIÓN POPULAR REVOLUCIONARIA ECUATORIANA'
    },
    'MPD': {
        'columnas': ['MPD15'],
        'nombre_completo': 'MOVIMIENTO POPULAR DEMOCRÁTICO'
    },
    'UPL': {
        'columnas': ['UPL16'],
        'nombre_completo': 'UNIÓN POPULAR LATINOAMERICANA'
    },
    'PSE': {
        'columnas': ['PSE17'],
        'nombre_completo': 'PARTIDO SOCIALISTA ECUATORIANO'
    },
    'MUPP-NP': {
        'columnas': ['MUPP-NP-18'],
        'nombre_completo': 'MOVIMIENTO UNIDAD PLURINACIONAL PACHAKUTIK - NUEVO PAÍS'
    },
    'MITI': {
        'columnas': ['MITI20'],
        'nombre_completo': 'MOVIMIENTO INDEPENDIENTE TIERRA INDÍGENA'
    },
    'PLRE-FRA': {
        'columnas': ['PLRE - FRA'],
        'nombre_completo': 'PARTIDO LIBERAL RADICAL ECUATORIANO - FRENTE RADICAL ALFARISTA'
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

# Provincias a analizar (actualizar según necesidad)
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

# Nombres de columnas importantes
COL_PROVINCIA = 'PROVINCI'
COL_CANTON = 'CANTON'
COL_PARROQUIA = 'PARROQUIA'
COL_VOTOS_VALIDOS = 'VOTOSVAL'
COL_VOTOS_NULOS = 'VOTOSNUL'
COL_VOTOS_BLANCOS = 'VOTOSBLA'
COL_VOTOS_ESCRUTADOS = 'VOTOSESC'

