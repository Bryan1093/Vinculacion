import json

# Cargar el JSON
with open('JSON-Parroquias/presidentes_primera_vuelta.json', encoding='utf-8') as f:
    data = json.load(f)

print("=" * 70)
print("VERIFICACIÓN DE CÓDIGOS CON CEROS")
print("=" * 70)

# 1. Códigos que empiezan con 0
print("\n1. Códigos que EMPIEZAN con 0:")
print("-" * 70)
codigos_inicio_0 = [r for r in data if r['CODPAR'].startswith('0')]
print(f"Total: {len(codigos_inicio_0)}")
for r in codigos_inicio_0:
    print(f"  CODPAR: '{r['CODPAR']}' - {r['PARROQUIA']}")

# 2. Códigos que terminan en 0 (ejemplos)
print("\n2. Ejemplos de códigos que TERMINAN en 0:")
print("-" * 70)
codigos_fin_0 = [r for r in data if r['CODPAR'].endswith('0') and len(r['CODPAR']) >= 3]
print(f"Total: {len(codigos_fin_0)}")
for r in codigos_fin_0[:15]:
    print(f"  CODPAR: '{r['CODPAR']}' - {r['PARROQUIA']}")

# 3. Buscar específicamente algunos códigos mencionados
print("\n3. Búsqueda de códigos específicos:")
print("-" * 70)
codigos_buscar = ['0285', '285', '590', '59', '730', '73']
for cod in codigos_buscar:
    encontrado = [r for r in data if r['CODPAR'] == cod]
    if encontrado:
        print(f"  ✓ '{cod}' ENCONTRADO - {encontrado[0]['PARROQUIA']}")
    else:
        print(f"  ✗ '{cod}' NO encontrado")

print("\n" + "=" * 70)
print("RESUMEN")
print("=" * 70)
print(f"Total de registros en JSON: {len(data)}")
print(f"Códigos con cero inicial: {len(codigos_inicio_0)}")
print(f"Códigos que terminan en 0: {len(codigos_fin_0)}")
