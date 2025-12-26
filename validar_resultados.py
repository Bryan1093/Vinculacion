"""
Script de validación manual para verificar la exactitud de los resultados
"""

import pandas as pd
from analisis_electoral_1996 import config

print("="*80)
print("VALIDACIÓN DE RESULTADOS ELECTORALES - NAPO Y PASTAZA")
print("="*80)

# Cargar datos originales
df_original = pd.read_excel(config.DATA_FILE)
df_original['PROVINCI'] = df_original['PROVINCI'].astype(str).str.strip()

# Cargar resultados calculados
df_resultados = pd.read_excel('resultados/Votos_Por_Candidato_Y_Provincia.xlsx')

print("\n📋 VERIFICACIÓN 1: Suma de votos por candidato vs Total de votos válidos")
print("-" * 80)

for provincia in ['NAPO', 'PASTAZA']:
    print(f"\n{provincia}:")
    
    # Total de votos válidos del dataset original
    votos_validos_original = df_original[df_original['PROVINCI'] == provincia]['VOTOSVAL'].sum()
    
    # Suma de votos de todos los candidatos (calculados)
    votos_candidatos_calculados = df_resultados[df_resultados['Provincia'] == provincia]['Total_Votos'].sum()
    
    print(f"  Votos válidos (dataset original): {int(votos_validos_original):,}")
    print(f"  Suma votos candidatos (calculado): {int(votos_candidatos_calculados):,}")
    
    diferencia = abs(votos_validos_original - votos_candidatos_calculados)
    
    if diferencia < 1:
        print(f"  ✅ ¡COINCIDEN PERFECTAMENTE! (diferencia: {diferencia})")
    else:
        print(f"  ⚠️ HAY DIFERENCIA: {diferencia} votos")

print("\n" + "="*80)
print("📋 VERIFICACIÓN 2: Votos por candidato individual")
print("-" * 80)

# Verificar cada candidato
for provincia in ['NAPO', 'PASTAZA']:
    print(f"\n{provincia}:")
    df_prov_original = df_original[df_original['PROVINCI'] == provincia]
    df_prov_resultados = df_resultados[df_resultados['Provincia'] == provincia]
    
    for candidato, info in config.CANDIDATOS.items():
        columnas = info['columnas']
        
        # Votos del dataset original
        votos_original = df_prov_original[columnas].sum().sum()
        
        # Votos calculados
        votos_calculado = df_prov_resultados[df_prov_resultados['Candidato'] == candidato]['Total_Votos'].values
        votos_calculado = int(votos_calculado[0]) if len(votos_calculado) > 0 else 0
        
        coincide = "✅" if abs(votos_original - votos_calculado) < 1 else "⚠️"
        print(f"  {coincide} {candidato:20s}: Original={int(votos_original):6,} | Calculado={votos_calculado:6,}")

print("\n" + "="*80)
print("📋 VERIFICACIÓN 3: Suma de porcentajes = 100%")
print("-" * 80)

for provincia in ['NAPO', 'PASTAZA']:
    df_prov = df_resultados[df_resultados['Provincia'] == provincia]
    suma_porcentajes = df_prov['Porcentaje (%)'].sum()
    
    print(f"\n{provincia}:")
    print(f"  Suma de porcentajes: {suma_porcentajes:.2f}%")
    
    if abs(suma_porcentajes - 100.0) < 0.1:
        print(f"  ✅ ¡CORRECTO! (≈ 100%)")
    else:
        print(f"  ⚠️ Diferencia: {abs(suma_porcentajes - 100.0):.2f}%")

print("\n" + "="*80)
print("📋 VERIFICACIÓN 4: Verificar ganador correcto")
print("-" * 80)

import json
with open('resultados/provincias_1996.json', encoding='utf-8') as f:
    json_data = json.load(f)

for prov_json in json_data:
    provincia = prov_json['PROVINCIA']
    ganador_json = prov_json['ganador']
    
    # Encontrar el candidato con más votos en el Excel
    df_prov = df_resultados[df_resultados['Provincia'] == provincia]
    candidato_mas_votos = df_prov.loc[df_prov['Total_Votos'].idxmax(), 'Candidato']
    
    # Obtener el partido del candidato
    partido_ganador = None
    for cand, info in config.CANDIDATOS.items():
        if cand == candidato_mas_votos:
            partido_ganador = info['partido']
            break
    
    print(f"\n{provincia}:")
    print(f"  Ganador declarado (JSON): {ganador_json}")
    print(f"  Candidato con más votos: {candidato_mas_votos} ({partido_ganador})")
    
    if ganador_json == partido_ganador:
        print(f"  ✅ ¡GANADOR CORRECTO!")
    else:
        print(f"  ⚠️ DISCREPANCIA EN GANADOR")

print("\n" + "="*80)
print("\n✅ VALIDACIÓN COMPLETA")
print("\nSi todos los checks muestran ✅, los resultados son 100% válidos y confiables.")
print("="*80 + "\n")
