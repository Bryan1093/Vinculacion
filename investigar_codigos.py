import pandas as pd

# Cargar Excel
df_excel = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')
df_excel['PARROQUIA'] = df_excel['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)

# Cargar mapeo
df_mapeo = pd.read_excel('parroquias-nombres.xlsx')

print("Parroquia 285 en Excel:")
fila = df_excel[df_excel['PARROQUIA'] == '285'].iloc[0]
print(f"  PROVINCI: {fila['PROVINCI']}")
print(f"  CANTON: {fila['CANTON']}")
print(f"  PARROQUIA: {fila['PARROQUIA']}")

print("\nTotal codigos en Excel:", len(df_excel['PARROQUIA'].unique()))
print("Total codigos en mapeo:", len(df_mapeo))

print("\nCodigos que coinciden:")
codigos_excel = set(df_excel['PARROQUIA'].unique())
codigos_mapeo = set(df_mapeo['CODIGO'].astype(str))
coincidencias = codigos_excel.intersection(codigos_mapeo)
print(f"  {len(coincidencias)} de {len(codigos_excel)} coinciden")
