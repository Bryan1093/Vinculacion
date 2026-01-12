import pandas as pd

# Leer datos originales
df_pres = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')

print("=== DATOS DE PRESIDENTES ===")
print("\nPrimeras 20 filas de CANTON:")
print(df_pres[['PROVINCI', 'CANTON']].head(20))

print("\nTipo de datos de CANTON:")
print(df_pres['CANTON'].dtype)

print("\nCantones únicos (primeros 30):")
cantones_unicos = df_pres['CANTON'].unique()[:30]
for c in cantones_unicos:
    print(f"  - {c} (tipo: {type(c)})")

# Leer archivo de nombres
df_nombres = pd.read_excel('parroquias-nombres.xlsx')
df_nombres.columns = ['PROVINCIA', 'CODIGOPROV', 'CANTON', 'CODIGOCANT', 'PARROQUIA', 'CODIGO']

print("\n\n=== ARCHIVO DE NOMBRES ===")
print("\nPrimeras 20 filas:")
print(df_nombres[['PROVINCIA', 'CANTON', 'CODIGOCANT']].head(20))

print("\nCantones únicos (primeros 10):")
print(df_nombres[['CANTON', 'CODIGOCANT']].drop_duplicates().head(10))
