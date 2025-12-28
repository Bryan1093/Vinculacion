"""
Verificar el orden de las parroquias en el archivo transpuesto
"""

import pandas as pd

archivo = 'resultados/Votos_Por_Candidato_Transpuesto.xlsx'
df = pd.read_excel(archivo)

print("\n" + "="*80)
print("VERIFICACIÓN DEL ORDEN EN EL ARCHIVO TRANSPUESTO")
print("="*80 + "\n")

# Orden esperado
orden_pastaza = ['3180', '3195', '3785', '3985', '4005', '4205', 
                 '4510', '5825', '2310', '3840', '5650', '6395']

# Obtener orden real
pastaza_real = df[df['Provincia'] == 'PASTAZA']['Codigo_Parroquia'].tolist()

print("PASTAZA:")
print("-" * 80)
print(f"Orden esperado: {orden_pastaza}")
print(f"Orden real:     {pastaza_real}")

if orden_pastaza == pastaza_real:
    print("\n✓ El orden de PASTAZA es CORRECTO")
else:
    print("\n✗ El orden de PASTAZA NO coincide")

print("\n" + "="*80)
print("PARROQUIAS DE PASTAZA EN EL ARCHIVO (en orden):")
print("="*80 + "\n")

pastaza_df = df[df['Provincia'] == 'PASTAZA']
for i, (_, row) in enumerate(pastaza_df.iterrows(), 1):
    print(f"{i:2}. {row['Codigo_Parroquia']}")

print("\n" + "="*80 + "\n")
