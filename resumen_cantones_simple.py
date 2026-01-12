import json

files = {
    'Presidentes 1ra Vuelta': 'JSON-Cantones/presidentes_primera_vuelta.json',
    'Presidentes 2da Vuelta': 'JSON-Cantones/presidentes_segunda_vuelta.json',
    'Diputados Nacionales': 'JSON-Cantones/diputados_nacionales.json'
}

print("\nRESUMEN DE ARCHIVOS JSON DE CANTONES")
print("="*60)

for nombre, archivo in files.items():
    with open(archivo, encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"\n{nombre}: {len(data)} cantones")
    
    # Verificar si hay "N/A" en códigos
    cantones_sin_codigo = [c for c in data if c.get('CODCAN') == 'N/A']
    if cantones_sin_codigo:
        print(f"  ADVERTENCIA: {len(cantones_sin_codigo)} cantones sin codigo")
    else:
        print(f"  OK: Todos los cantones tienen codigo")
    
    # Mostrar primeros 3 cantones
    print(f"  Ejemplos:")
    for c in data[:3]:
        print(f"    - {c['CANTON']} (Cod: {c['CODCAN']}, Prov: {c['PROVINCIA']})")

print("\n" + "="*60)
