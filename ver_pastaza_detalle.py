"""
Script para mostrar TODAS las parroquias de Pastaza en el Excel
"""

import pandas as pd

print("\n" + "="*80)
print("LISTADO COMPLETO DE PARROQUIAS DE PASTAZA EN EL EXCEL")
print("="*80 + "\n")

# Leer el archivo Excel
archivo = 'resultados/Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx'
df_resumen = pd.read_excel(archivo, sheet_name='Resumen_General')

# Filtrar solo Pastaza
pastaza_df = df_resumen[df_resumen['Provincia'] == 'PASTAZA']

print(f"Total de parroquias de PASTAZA en el Excel: {len(pastaza_df)}\n")

print("Listado completo:")
print("-" * 80)
for i, (_, row) in enumerate(pastaza_df.iterrows(), 1):
    print(f"{i:2}. Código: {row['Codigo_Parroquia']:>4} - Votos: {row['Total_Votos']:>7,}")

print("\n" + "="*80)
print("Códigos de parroquia de Pastaza encontrados:")
print("="*80)
codigos = pastaza_df['Codigo_Parroquia'].tolist()
print(codigos)

print("\n" + "="*80)
print("Códigos esperados:")
print("="*80)
esperados = ['3180', '3195', '3785', '3985', '4005', '4205', '4510', '5825', '2310', '3840', '5650', '6395']
print(esperados)

print("\n" + "="*80)
print("COMPARACIÓN:")
print("="*80)
print(f"Esperados: {len(esperados)} parroquias")
print(f"Encontrados: {len(codigos)} parroquias")

if set(codigos) == set(esperados):
    print("✓ Los códigos coinciden (mismo conjunto)")
else:
    print("✗ Los códigos NO coinciden")
    extra = set(codigos) - set(esperados)
    faltantes = set(esperados) - set(codigos)
    if extra:
        print(f"  Códigos EXTRA (no deberían estar): {extra}")
    if faltantes:
        print(f"  Códigos FALTANTES: {faltantes}")

print("\n" + "="*80 + "\n")
