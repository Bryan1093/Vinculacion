import json

archivos = [
    'JSON-Cantones/presidentes_primera_vuelta.json',
    'JSON-Cantones/presidentes_segunda_vuelta.json',
    'JSON-Cantones/diputados_nacionales.json'
]

for archivo in archivos:
    print(f"\n{'='*80}")
    print(f"Archivo: {archivo}")
    print('='*80)
    
    with open(archivo, encoding='utf-8') as f:
        data = json.load(f)
    
    print(f'Total de cantones: {len(data)}')
    
    # Verificar si hay algún registro con "nan"
    cantones_nan = [c for c in data if c.get('CODCAN') == 'nan' or c.get('CANTON') == 'nan']
    
    if cantones_nan:
        print(f'⚠️ ADVERTENCIA: Se encontraron {len(cantones_nan)} registros con "nan"')
    else:
        print('✅ No se encontraron registros con "nan"')
    
    # Mostrar primeros 5 cantones como ejemplo
    print('\nPrimeros 5 cantones:')
    for i, c in enumerate(data[:5], 1):
        print(f'  {i}. CODPRO: {c["CODPRO"]:2s} - {c["PROVINCIA"]:20s} | CODCAN: {c["CODCAN"]:3s} - {c["CANTON"]}')
    
    # Contar cantones por provincia
    provincias = {}
    for c in data:
        prov = c['PROVINCIA']
        if prov not in provincias:
            provincias[prov] = 0
        provincias[prov] += 1
    
    print(f'\nCantones por provincia (total: {len(provincias)} provincias):')
    for prov, count in sorted(provincias.items())[:5]:
        print(f'  - {prov}: {count} cantones')

print(f"\n{'='*80}")
print("Verificación completada")
print('='*80)
