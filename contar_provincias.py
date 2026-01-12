import json

# Leer el JSON
with open('JSON-Provincias/presidentes_primera_vuelta.json', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total de provincias: {len(data)}')
print('\nProvincias encontradas:')

# Ordenar por CODPRO
provincias_ordenadas = sorted(data, key=lambda x: int(x['CODPRO']) if x['CODPRO'].isdigit() else 999)

for i, p in enumerate(provincias_ordenadas, 1):
    print(f'{i}. CODPRO: {p["CODPRO"]}, PROVINCIA: {p["PROVINCIA"]}')
