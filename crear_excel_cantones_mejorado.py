"""
Script para crear Excel mejorado de cantones con votos válidos, blancos, nulos y totales
"""
import pandas as pd
import json
import os

# Cargar datos del JSON
json_file = 'resultados/diputados/cantones_diputados_1996.json'
with open(json_file, 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Preparar datos para el Excel
resultados = []

for codigo_canton, info_canton in datos.items():
    nombre_canton = info_canton['nombre']
    
    # Fila con totales generales
    resultados.append({
        'Canton': nombre_canton,
        'Partido': 'TOTALES GENERALES',
        'Votos_Partido': '',
        'Porcentaje (%)': '',
        'VOTOS VALIDOS': info_canton['votos_validos'],
        'VOTOS BLANCOS': info_canton['votos_blancos'],
        'VOTOS NULOS': info_canton['votos_nulos'],
        'TOTAL VOTOS': info_canton['total_votos']
    })
    
    # Filas con votos por partido
    for partido, info_partido in info_canton['partidos'].items():
        porcentaje = (info_partido['votos'] / info_canton['votos_validos'] * 100) if info_canton['votos_validos'] > 0 else 0
        resultados.append({
            'Canton': nombre_canton,
            'Partido': partido,
            'Votos_Partido': info_partido['votos'],
            'Porcentaje (%)': round(porcentaje, 2),
            'VOTOS VALIDOS': '',
            'VOTOS BLANCOS': '',
            'VOTOS NULOS': '',
            'TOTAL VOTOS': ''
        })
    
    # Fila separadora
    resultados.append({
        'Canton': '',
        'Partido': '',
        'Votos_Partido': '',
        'Porcentaje (%)': '',
        'VOTOS VALIDOS': '',
        'VOTOS BLANCOS': '',
        'VOTOS NULOS': '',
        'TOTAL VOTOS': ''
    })

# Crear DataFrame
df = pd.DataFrame(resultados)

# Guardar Excel
output_file = 'resultados/diputados/Resumen_Diputados_Cantones_Pichincha.xlsx'
df.to_excel(output_file, index=False)

print(f"✓ Archivo Excel mejorado guardado: {output_file}")
print(f"\nTotal de cantones analizados: {len(datos)}")
print(f"Cantones: {', '.join([info['nombre'] for info in datos.values()])}")
print("\nVista previa (primeras 20 filas):")
print(df.head(20).to_string(index=False))
