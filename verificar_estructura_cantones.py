import pandas as pd

# Leer el archivo de presidentes primera vuelta
df = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')

print("Columnas del archivo:")
print(df.columns.tolist())

print("\nPrimeras 10 filas de CANTON y PROVINCI:")
print(df[['PROVINCI', 'CANTON']].head(20))

print("\nTipos de datos:")
print(df[['PROVINCI', 'CANTON']].dtypes)

print("\nCantones únicos (primeros 20):")
print(df['CANTON'].unique()[:20])
