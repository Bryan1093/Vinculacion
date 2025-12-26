import pandas as pd

# Cargar el archivo Excel
ruta = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
df = pd.read_excel(ruta)

print(f'Filas: {df.shape[0]}, Columnas: {df.shape[1]}')
print(f'\nColumnas:\n{list(df.columns)}')
print(f'\nPrimeras 5 filas:\n{df.head()}')
print(f'\nProvincias únicas (primeras 10):')
print(df["PROVINCI"].unique()[:10])
print(f'\nTipos de datos:\n{df.dtypes}')
