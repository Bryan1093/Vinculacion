"""
Verificar cuáles de las 12 parroquias de Pastaza tienen datos
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
print("VERIFICACIÓN DE PARROQUIAS DE PASTAZA EN LOS DATOS")
print("="*80)

# Filtrar Pastaza
df_pastaza = df[df['PROVINCI'] == 'PASTAZA'].copy()

print(f"\nParroquias que DEBERÍAN estar (12 total):")
print("-" * 80)

con_datos = []
sin_datos = []

for i, parroquia in enumerate(parroquias_pastaza_correctas, 1):
    df_temp = df_pastaza[df_pastaza['PARROQUIA'] == parroquia]
    if len(df_temp) > 0:
        votos_total = df_temp['VOTOSVAL'].sum() + df_temp['VOTOSBLA'].sum() + df_temp['VOTOSNUL'].sum()
        print(f"{i:2}. {parroquia:>4} - ✓ TIENE DATOS ({len(df_temp)} registros, {int(votos_total):,} votos totales)")
        con_datos.append(parroquia)
    else:
        print(f"{i:2}. {parroquia:>4} - ✗ NO TIENE DATOS")
        sin_datos.append(parroquia)

print("\n" + "="*80)
print("RESUMEN:")
print("="*80)
print(f"Parroquias CON datos: {len(con_datos)}")
print(f"Parroquias SIN datos: {len(sin_datos)}")

if sin_datos:
    print(f"\nParroquias sin datos: {sin_datos}")
    print("\nEstas parroquias NO aparecerán en el Excel porque no tienen registros.")

print("\n" + "="*80)
