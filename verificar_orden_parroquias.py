"""
Script para verificar el orden de las parroquias en los resultados
"""

import pandas as pd

print("\n" + "="*80)
print("VERIFICACIÓN DEL ORDEN DE PARROQUIAS")
print("="*80 + "\n")

# Leer el archivo Excel
archivo = 'resultados/Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx'
df_resumen = pd.read_excel(archivo, sheet_name='Resumen_General')

# Orden esperado de Pastaza
pastaza_esperado = ['3180', '3195', '3785', '3985', '4005', '4205', 
                    '4510', '5825', '2310', '3840', '5650', '6395']

# Orden esperado de Pichincha
pichincha_esperado = ['30', '80', '195', '430', '440', '625', '725', '855', '865',
                      '1400', '1440', '1475', '2055', '2265', '2275', '2525', '2530',
                      '2540', '2560', '2690', '2825', '2855', '2895', '2925', '2980',
                      '2985', '3100', '3325', '3475', '3925', '4085', '4290', '4325',
                      '5015', '5110', '5220', '5235', '5260', '5325', '5410', '5435',
                      '5530', '5535', '5540', '5575', '5935', '5985']

# Obtener orden real de Pastaza
pastaza_real = df_resumen[df_resumen['Provincia'] == 'PASTAZA']['Codigo_Parroquia'].tolist()

# Obtener orden real de Pichincha
pichincha_real = df_resumen[df_resumen['Provincia'] == 'PICHINCHA']['Codigo_Parroquia'].tolist()

print("PASTAZA:")
print("-" * 80)
print(f"Orden esperado: {len(pastaza_esperado)} parroquias")
print(f"Orden real:     {len(pastaza_real)} parroquias")

if pastaza_esperado == pastaza_real:
    print("✓ El orden de PASTAZA se mantuvo CORRECTAMENTE")
else:
    print("✗ El orden de PASTAZA NO coincide")
    print("\nEsperado:", pastaza_esperado)
    print("Real:    ", pastaza_real)

print("\n" + "="*80)
print("PICHINCHA:")
print("-" * 80)
print(f"Orden esperado: {len(pichincha_esperado)} parroquias")
print(f"Orden real:     {len(pichincha_real)} parroquias")

if pichincha_esperado == pichincha_real:
    print("✓ El orden de PICHINCHA se mantuvo CORRECTAMENTE")
else:
    print("✗ El orden de PICHINCHA NO coincide")
    print("\nPrimeras 10 esperadas:", pichincha_esperado[:10])
    print("Primeras 10 reales:   ", pichincha_real[:10])

print("\n" + "="*80)
print("RESUMEN DE PARROQUIAS EN EL EXCEL:")
print("="*80)

print("\nPASTAZA (en orden del Excel):")
for i, (_, row) in enumerate(df_resumen[df_resumen['Provincia'] == 'PASTAZA'].iterrows(), 1):
    print(f"{i:2}. {row['Codigo_Parroquia']:>4} - {row['Total_Votos']:>7,} votos totales")

print("\nPICHINCHA (primeras 10 en orden del Excel):")
for i, (_, row) in enumerate(df_resumen[df_resumen['Provincia'] == 'PICHINCHA'].head(10).iterrows(), 1):
    print(f"{i:2}. {row['Codigo_Parroquia']:>4} - {row['Total_Votos']:>7,} votos totales")

print(f"\n... y {len(pichincha_real) - 10} parroquias más de Pichincha")

print("\n" + "="*80 + "\n")
