import json

archivos = [
    'JSON-Provincias/presidentes_primera_vuelta.json',
    'JSON-Provincias/presidentes_segunda_vuelta.json',
    'JSON-Provincias/diputados_nacionales.json'
]

for archivo in archivos:
    print(f"\n{'='*80}")
    print(f"Archivo: {archivo}")
    print('='*80)
    
    with open(archivo, encoding='utf-8') as f:
        data = json.load(f)
    
    print(f'Total de provincias: {len(data)}')
    
    # Verificar si hay algún registro con "nan"
    provincias_nan = [p for p in data if p['CODPRO'] == 'nan' or p['PROVINCIA'] == 'nan']
    
    if provincias_nan:
        print(f'⚠️ ADVERTENCIA: Se encontraron {len(provincias_nan)} registros con "nan"')
        for p in provincias_nan:
            print(f'   - CODPRO: {p["CODPRO"]}, PROVINCIA: {p["PROVINCIA"]}')
    else:
        print('✅ No se encontraron registros con "nan"')
    
    # Mostrar lista de provincias
    print('\nProvincias:')
    provincias_ordenadas = sorted(data, key=lambda x: int(x['CODPRO']) if x['CODPRO'].isdigit() else 999)
    
    for i, p in enumerate(provincias_ordenadas, 1):
        print(f'  {i:2d}. CODPRO: {p["CODPRO"]:2s} - {p["PROVINCIA"]}')

print(f"\n{'='*80}")
print("Verificación completada")
print('='*80)
