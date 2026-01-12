import pandas as pd

# Cargar Excel electoral
df_excel = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')

print("Primera fila del Excel electoral:")
fila = df_excel.iloc[0]
print(f"  PROVINCI: {fila['PROVINCI']}")
print(f"  CANTON: {fila['CANTON']}")
print(f"  PARROQUIA: {fila['PARROQUIA']}")

# Cargar mapeo
df_mapeo = pd.read_excel('parroquias-nombres.xlsx')
df_mapeo.columns = ['PROVINCIA', 'COD_PROV', 'CANTON', 'COD_CANTON', 'PARROQUIA', 'COD_PARROQUIA']

print("\nBuscar canton con codigo 285:")
resultado = df_mapeo[df_mapeo['COD_CANTON'] == 285]
if len(resultado) > 0:
    print(resultado[['PROVINCIA', 'CANTON', 'COD_CANTON']].iloc[0])
else:
    print("No encontrado")

print("\nBuscar canton con codigo 260:")
resultado = df_mapeo[df_mapeo['COD_CANTON'] == 260]
if len(resultado) > 0:
    print(resultado[['PROVINCIA', 'CANTON', 'COD_CANTON']].iloc[0])
else:
    print("No encontrado")
