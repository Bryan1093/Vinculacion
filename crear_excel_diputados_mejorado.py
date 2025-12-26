"""
Script para crear Excel mejorado con votos válidos, blancos, nulos y totales
"""
import pandas as pd
import json
import os

# Cargar datos del JSON
json_file = 'resultados/diputados/provincias_diputados_1996.json'
with open(json_file, 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Preparar datos para el Excel
resultados = []

for codigo_prov, info_prov in datos.items():
    nombre_prov = info_prov['nombre']
    
    # Fila con totales generales
    resultados.append({
        'Provincia': nombre_prov,
        'Partido': 'TOTALES GENERALES',
        'Total_Votos': '',
        'Porcentaje (%)': '',
        'Votos_Validos': info_prov['votos_validos'],
        'Votos_Blancos': info_prov['votos_blancos'],
        'Votos_Nulos': info_prov['votos_nulos'],
        'Total_Votos_Provincia': info_prov['total_votos']
    })
    
    # Filas con votos por partido
    for partido, info_partido in info_prov['partidos'].items():
        porcentaje = (info_partido['votos'] / info_prov['votos_validos'] * 100) if info_prov['votos_validos'] > 0 else 0
        resultados.append({
            'Provincia': nombre_prov,
            'Partido': partido,
            'Total_Votos': info_partido['votos'],
            'Porcentaje (%)': round(porcentaje, 2),
            'Votos_Validos': '',
            'Votos_Blancos': '',
            'Votos_Nulos': '',
            'Total_Votos_Provincia': ''
        })
    
    # Fila separadora
    resultados.append({
        'Provincia': '',
        'Partido': '',
        'Total_Votos': '',
        'Porcentaje (%)': '',
        'Votos_Validos': '',
        'Votos_Blancos': '',
        'Votos_Nulos': '',
        'Total_Votos_Provincia': ''
    })

# Crear DataFrame
df = pd.DataFrame(resultados)

# Renombrar columnas para mejor presentación
df.columns = ['Provincia', 'Partido', 'Votos_Partido', 'Porcentaje (%)', 
              'VOTOS VALIDOS', 'VOTOS BLANCOS', 'VOTOS NULOS', 'TOTAL VOTOS']

# Guardar Excel
output_file = 'resultados/diputados/Resumen_Diputados_Napo_Pastaza.xlsx'
df.to_excel(output_file, index=False)

print(f"✓ Archivo Excel mejorado guardado: {output_file}")
print("\nVista previa:")
print(df.to_string(index=False))
