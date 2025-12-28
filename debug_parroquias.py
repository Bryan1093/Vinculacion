"""
Script de depuración para ver qué está pasando
"""

import pandas as pd

# Cargar datos
df = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')

# Limpiar columnas
df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
df['PARROQUIA'] = df['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)

# Parroquias que DEBERÍAN usarse
parroquias_pastaza_correctas = ['3180', '3195', '3785', '3985', '4005', '4205', 
                                '4510', '5825', '2310', '3840', '5650', '6395']

print("="*80)
print("DEPURACIÓN - PARROQUIAS DE PASTAZA")
print("="*80)

# Filtrar Pastaza
df_pastaza = df[df['PROVINCI'] == 'PASTAZA'].copy()
print(f"\nTotal de registros de PASTAZA en el archivo: {len(df_pastaza)}")

# Ver todas las parroquias únicas de Pastaza
todas_parroquias = df_pastaza['PARROQUIA'].unique()
print(f"\nTotal de parroquias únicas en PASTAZA: {len(todas_parroquias)}")
print(f"Parroquias: {sorted(todas_parroquias)}")

print("\n" + "="*80)
print("VERIFICANDO CADA PARROQUIA QUE DEBERÍA ESTAR:")
print("="*80)

for parroquia in parroquias_pastaza_correctas:
    df_temp = df_pastaza[df_pastaza['PARROQUIA'] == parroquia]
    print(f"Parroquia {parroquia}: {len(df_temp)} registros")
    if len(df_temp) > 0:
        print(f"  ✓ Existe en los datos")
    else:
        print(f"  ✗ NO EXISTE en los datos")

print("\n" + "="*80)
print("FILTRANDO CON isin():")
print("="*80)

df_filtrado = df_pastaza[df_pastaza['PARROQUIA'].isin(parroquias_pastaza_correctas)]
print(f"Registros después del filtro: {len(df_filtrado)}")
print(f"Parroquias únicas después del filtro: {df_filtrado['PARROQUIA'].unique()}")

print("\n" + "="*80)
