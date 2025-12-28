"""
Script para mostrar resumen de los resultados del análisis
"""

import pandas as pd

print("\n" + "="*80)
print("RESUMEN DE RESULTADOS - ANÁLISIS DE PARROQUIAS")
print("="*80 + "\n")

# Leer el archivo Excel con los resultados
archivo = 'resultados/Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx'

# Leer las diferentes hojas
df_detalle = pd.read_excel(archivo, sheet_name='Detalle_Por_Candidato')
df_resumen = pd.read_excel(archivo, sheet_name='Resumen_General')
df_totales = pd.read_excel(archivo, sheet_name='Totales_Por_Candidato')

print("1. INFORMACIÓN GENERAL")
print("-" * 80)
print(f"Total de parroquias analizadas: {df_resumen.shape[0]}")
print(f"  - PASTAZA:   {len(df_resumen[df_resumen['Provincia'] == 'PASTAZA'])} parroquias")
print(f"  - PICHINCHA: {len(df_resumen[df_resumen['Provincia'] == 'PICHINCHA'])} parroquias")
print(f"\nTotal de registros detallados: {df_detalle.shape[0]}")

print("\n2. TOTALES GENERALES")
print("-" * 80)
total_validos = df_resumen['Votos_Validos'].sum()
total_blancos = df_resumen['Votos_Blancos'].sum()
total_nulos = df_resumen['Votos_Nulos'].sum()
total_general = df_resumen['Total_Votos'].sum()

print(f"Votos Válidos:  {total_validos:>12,}")
print(f"Votos Blancos:  {total_blancos:>12,}")
print(f"Votos Nulos:    {total_nulos:>12,}")
print(f"{'─'*40}")
print(f"TOTAL:          {total_general:>12,}")

print("\n3. TOTALES POR CANDIDATO/PARTIDO")
print("-" * 80)
print(f"{'Candidato':<25} {'Partido':<12} {'Votos':>12} {'Porcentaje':>12}")
print("-" * 80)

for _, row in df_totales.iterrows():
    porcentaje = (row['Votos'] / total_validos * 100) if total_validos > 0 else 0
    print(f"{row['Candidato']:<25} {row['Partido']:<12} {row['Votos']:>12,} {porcentaje:>11.2f}%")

print("\n4. PARROQUIAS DE PASTAZA ANALIZADAS")
print("-" * 80)
pastaza_parroquias = df_resumen[df_resumen['Provincia'] == 'PASTAZA'].sort_values('Codigo_Parroquia')
for i, (_, row) in enumerate(pastaza_parroquias.iterrows(), 1):
    print(f"{i:2}. Código {row['Codigo_Parroquia']:>4} - Votos totales: {row['Total_Votos']:>6,}")

print("\n5. PRIMERAS 10 PARROQUIAS DE PICHINCHA")
print("-" * 80)
pichincha_parroquias = df_resumen[df_resumen['Provincia'] == 'PICHINCHA'].sort_values('Codigo_Parroquia').head(10)
for i, (_, row) in enumerate(pichincha_parroquias.iterrows(), 1):
    print(f"{i:2}. Código {row['Codigo_Parroquia']:>5} - Votos totales: {row['Total_Votos']:>7,}")

print(f"\n... (y {len(df_resumen[df_resumen['Provincia'] == 'PICHINCHA']) - 10} parroquias más de Pichincha)")

print("\n6. TOP 5 CANDIDATOS EN PASTAZA")
print("-" * 80)
pastaza_detalle = df_detalle[df_detalle['Provincia'] == 'PASTAZA']
top_pastaza = pastaza_detalle.groupby(['Candidato', 'Partido'])['Votos'].sum().reset_index().sort_values('Votos', ascending=False).head(5)
total_pastaza_validos = df_resumen[df_resumen['Provincia'] == 'PASTAZA']['Votos_Validos'].sum()

for i, (_, row) in enumerate(top_pastaza.iterrows(), 1):
    porcentaje = (row['Votos'] / total_pastaza_validos * 100) if total_pastaza_validos > 0 else 0
    print(f"{i}. {row['Candidato']:<25} ({row['Partido']:<10}): {row['Votos']:>6,} votos ({porcentaje:>5.2f}%)")

print("\n7. TOP 5 CANDIDATOS EN PICHINCHA")
print("-" * 80)
pichincha_detalle = df_detalle[df_detalle['Provincia'] == 'PICHINCHA']
top_pichincha = pichincha_detalle.groupby(['Candidato', 'Partido'])['Votos'].sum().reset_index().sort_values('Votos', ascending=False).head(5)
total_pichincha_validos = df_resumen[df_resumen['Provincia'] == 'PICHINCHA']['Votos_Validos'].sum()

for i, (_, row) in enumerate(top_pichincha.iterrows(), 1):
    porcentaje = (row['Votos'] / total_pichincha_validos * 100) if total_pichincha_validos > 0 else 0
    print(f"{i}. {row['Candidato']:<25} ({row['Partido']:<10}): {row['Votos']:>7,} votos ({porcentaje:>5.2f}%)")

print("\n" + "="*80)
print("ARCHIVOS GENERADOS:")
print("="*80)
print(f"✓ {archivo}")
print(f"  - Hoja 'Detalle_Por_Candidato': {df_detalle.shape[0]} registros")
print(f"  - Hoja 'Resumen_General': {df_resumen.shape[0]} registros")
print(f"  - Hoja 'Totales_Por_Candidato': {df_totales.shape[0]} registros")
print(f"\n✓ resultados/parroquias_pastaza_pichincha_detallado_1996.json")
print("\n" + "="*80 + "\n")
