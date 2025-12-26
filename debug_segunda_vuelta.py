import pandas as pd

df = pd.read_excel('Datos-Presidentes-Completos/Segunda Vuelta/1996 - Presidentes - segunda vuelta.xlsx')

print("Valores únicos en PROVINCI:")
print(df['PROVINCI'].unique())
print("\nTipo de dato:", df['PROVINCI'].dtype)

print("\nFiltrando por código 15 (NAPO):")
df_15 = df[df['PROVINCI'] == 15]
print(f"Registros encontrados: {len(df_15)}")

print("\nFiltrando por código '15' (string):")
df_15_str = df[df['PROVINCI'].astype(str) == '15']
print(f"Registros encontrados: {len(df_15_str)}")

print("\nPrimeras filas de NAPO:")
if len(df_15) > 0:
    print(df_15[['PROVINCI', 'CANTON', 'PSC6', 'PRE10']].head())

