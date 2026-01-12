import pandas as pd

# Leer el archivo de nombres
df = pd.read_excel('parroquias-nombres.xlsx')
df.columns = ['PROVINCIA', 'CODIGOPROV', 'CANTON', 'CODIGOCANT', 'PARROQUIA', 'CODIGO']

print("Primeras 20 filas:")
print(df.head(20))

print(f"\nTotal cantones únicos: {df['CODIGOCANT'].nunique()}")

# Mostrar algunos ejemplos de cantones
print("\nEjemplos de cantones (primeros 10):")
cantones_unicos = df[['CODIGOPROV', 'PROVINCIA', 'CODIGOCANT', 'CANTON']].drop_duplicates().head(10)
print(cantones_unicos)

# Verificar estructura del código de cantón
print("\nEstructura de códigos de cantón:")
print(df[['CODIGOPROV', 'CODIGOCANT', 'PROVINCIA', 'CANTON']].drop_duplicates().head(15))
