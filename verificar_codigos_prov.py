import json

data = json.load(open('JSON-Provincias/presidentes_primera_vuelta.json', encoding='utf-8'))

print('Todas las provincias:')
for i, p in enumerate(data):
    es_numero = p["CODPRO"].isdigit()
    estado = "✅" if es_numero else "❌"
    print(f'{i+1:2}. {estado} CODPRO: "{p["CODPRO"]:15}", PROVINCIA: "{p["PROVINCIA"]}"')

sin_codigo = [p for p in data if not p["CODPRO"].isdigit()]
print(f'\n❌ Provincias sin código numérico: {len(sin_codigo)}')
