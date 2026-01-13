import pandas as pd

# Leer el Excel con CODIGO como string
df = pd.read_excel('parroquias-nombres.xlsx', dtype={'CODIGO': str})
df.columns = ['PROVINCIA', 'COD_PROV', 'CANTON', 'COD_CANTON', 'PARROQUIA', 'COD_PARROQUIA']

print("Primeros 20 códigos del Excel:")
print("=" * 60)
for i, row in df.head(20).iterrows():
    print(f"{i+1}. CODIGO: '{row['COD_PARROQUIA']}', PARROQUIA: {row['PARROQUIA']}")

print("\n\nCódigos que empiezan con 0:")
print("=" * 60)
codigos_con_cero = df[df['COD_PARROQUIA'].str.startswith('0', na=False)]
print(f"Total: {len(codigos_con_cero)}")
for i, row in codigos_con_cero.head(20).iterrows():
    print(f"CODIGO: '{row['COD_PARROQUIA']}', PARROQUIA: {row['PARROQUIA']}, PROVINCIA: {row['PROVINCIA']}")

print("\n\nCódigos que terminan en 0 (3 o 4 dígitos):")
print("=" * 60)
codigos_terminan_0 = df[df['COD_PARROQUIA'].str.match(r'^\d{2,3}0$', na=False)]
print(f"Total: {len(codigos_terminan_0)}")
for i, row in codigos_terminan_0.head(20).iterrows():
    print(f"CODIGO: '{row['COD_PARROQUIA']}', PARROQUIA: {row['PARROQUIA']}")
