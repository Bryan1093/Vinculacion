"""
Leer DIRECTAMENTE del Excel recién generado
"""

import pandas as pd

archivo = 'resultados/Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx'

print("\n" + "="*80)
print("LEYENDO DIRECTAMENTE DEL EXCEL GENERADO")
print("="*80 + "\n")

# Leer hoja de resumen
df = pd.read_excel(archivo, sheet_name='Resumen_General')

# Filtrar Pastaza
pastaza = df[df['Provincia'] == 'PASTAZA']

print(f"Total de parroquias de PASTAZA en el Excel: {len(pastaza)}\n")

print("Códigos de parroquia encontrados:")
print("-" * 80)
codigos_encontrados = pastaza['Codigo_Parroquia'].tolist()
print(codigos_encontrados)

print("\n" + "="*80)
print("DETALLE DE CADA PARROQUIA:")
print("="*80 + "\n")

for idx, row in pastaza.iterrows():
    print(f"Código: {row['Codigo_Parroquia']:>4} - Votos totales: {row['Total_Votos']:>7,}")

print("\n" + "="*80)
