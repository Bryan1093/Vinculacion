import json
import pandas as pd

# 1. Verificar qué códigos hay en el Excel de nombres
print("=" * 70)
print("CÓDIGOS EN EL EXCEL DE NOMBRES (parroquias-nombres.xlsx)")
print("=" * 70)
df_nombres = pd.read_excel('parroquias-nombres.xlsx', dtype={'CODIGO': str})
df_nombres.columns = ['PROVINCIA', 'COD_PROV', 'CANTON', 'COD_CANTON', 'PARROQUIA', 'COD_PARROQUIA']

# Buscar códigos con cero inicial
codigos_cero_inicial = df_nombres[df_nombres['COD_PARROQUIA'].str.startswith('0', na=False)]
print(f"\nCódigos que empiezan con 0: {len(codigos_cero_inicial)}")
for _, row in codigos_cero_inicial.head(10).iterrows():
    print(f"  '{row['COD_PARROQUIA']}' - {row['PARROQUIA']} ({row['PROVINCIA']})")

# 2. Verificar qué códigos hay en los datos electorales
print("\n" + "=" * 70)
print("CÓDIGOS EN LOS DATOS ELECTORALES (Presidentes 1V)")
print("=" * 70)
df_elecciones = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx', 
                               dtype={'PARROQUIA': str, 'CANTON': str})
print(f"\nPrimeros 10 códigos de PARROQUIA en el archivo electoral:")
print(df_elecciones['PARROQUIA'].head(10).tolist())

# Buscar si existe 0285 en los datos electorales
parroquias_con_cero = df_elecciones[df_elecciones['PARROQUIA'].str.startswith('0', na=False)]
print(f"\nCódigos de PARROQUIA que empiezan con 0: {len(parroquias_con_cero)}")
if len(parroquias_con_cero) > 0:
    print(parroquias_con_cero['PARROQUIA'].unique()[:20])
else:
    print("  ¡No hay códigos con cero inicial en los datos electorales!")

# Buscar específicamente 0285 y 285
print(f"\n¿Existe '0285' en datos electorales? {('0285' in df_elecciones['PARROQUIA'].values)}")
print(f"¿Existe '285' en datos electorales? {('285' in df_elecciones['PARROQUIA'].values)}")

# 3. Verificar el JSON generado
print("\n" + "=" * 70)
print("CÓDIGOS EN EL JSON GENERADO")
print("=" * 70)
with open('JSON-Parroquias/presidentes_primera_vuelta.json', encoding='utf-8') as f:
    data = json.load(f)

# Buscar códigos con cero inicial
codigos_json_cero = [r for r in data if r['CODPAR'].startswith('0')]
print(f"\nCódigos que empiezan con 0 en JSON: {len(codigos_json_cero)}")
for r in codigos_json_cero[:10]:
    print(f"  '{r['CODPAR']}' - {r['PARROQUIA']}")

# Buscar específicamente 0285 y 285
codigo_0285 = [r for r in data if r['CODPAR'] == '0285']
codigo_285 = [r for r in data if r['CODPAR'] == '285']
print(f"\n¿Existe '0285' en JSON? {len(codigo_0285) > 0}")
print(f"¿Existe '285' en JSON? {len(codigo_285) > 0}")
if len(codigo_285) > 0:
    print(f"  Registro con '285': {codigo_285[0]}")
