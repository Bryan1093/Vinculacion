import json

# Cargar el JSON
with open('JSON-Parroquias/presidentes_primera_vuelta.json', encoding='utf-8') as f:
    data = json.load(f)

print("Primeros 10 registros:")
print("=" * 60)
for i, r in enumerate(data[:10]):
    print(f"{i+1}. CODPAR: {r['CODPAR']}, PARROQUIA: {r['PARROQUIA']}")

print("\n\nBuscando códigos con CEROS INICIALES (empiezan con 0):")
print("=" * 60)
count = 0
for r in data:
    if r['CODPAR'].startswith('0'):
        print(f"CODPAR: {r['CODPAR']}, PARROQUIA: {r['PARROQUIA']}")
        count += 1
        if count >= 10:
            break

print(f"\nTotal de códigos con cero inicial: {sum(1 for r in data if r['CODPAR'].startswith('0'))}")

print("\n\nBuscando códigos que terminan en 0 (como 590):")
print("=" * 60)
count = 0
for r in data:
    if r['CODPAR'].endswith('0') and len(r['CODPAR']) >= 3:
        print(f"CODPAR: {r['CODPAR']}, PARROQUIA: {r['PARROQUIA']}")
        count += 1
        if count >= 10:
            break

print(f"\nTotal de códigos que terminan en 0: {sum(1 for r in data if r['CODPAR'].endswith('0'))}")
