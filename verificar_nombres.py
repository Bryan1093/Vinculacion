import json

# Cargar y verificar
with open('JSON-Parroquias/presidentes_primera_vuelta.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Primeros 5 registros:")
for i in range(5):
    print(f"\n{i+1}. CODPAR={data[i]['CODPAR']}, PARROQUIA={data[i]['PARROQUIA']}, ganador={data[i]['ganador']}")

print(f"\n\nTotal parroquias: {len(data)}")

# Contar cuantas tienen nombre real vs PARROQUIA_XXX
con_nombre = sum(1 for p in data if not p['PARROQUIA'].startswith('PARROQUIA_'))
sin_nombre = len(data) - con_nombre

print(f"Con nombre real: {con_nombre}")
print(f"Sin nombre (PARROQUIA_XXX): {sin_nombre}")
