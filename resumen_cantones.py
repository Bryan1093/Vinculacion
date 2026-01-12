import json

files = {
    'Presidentes 1ra Vuelta': 'JSON-Cantones/presidentes_primera_vuelta.json',
    'Presidentes 2da Vuelta': 'JSON-Cantones/presidentes_segunda_vuelta.json',
    'Diputados Nacionales': 'JSON-Cantones/diputados_nacionales.json'
}

print("\n" + "="*80)
print("RESUMEN DE ARCHIVOS JSON DE CANTONES")
print("="*80)

for nombre, archivo in files.items():
    with open(archivo, encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"\n{nombre}:")
    print(f"  - Total cantones: {len(data)}")
    
    # Verificar si hay "N/A" en códigos
    cantones_sin_codigo = [c for c in data if c.get('CODCAN') == 'N/A']
    if cantones_sin_codigo:
        print(f"  - ⚠️ Cantones sin código: {len(cantones_sin_codigo)}")
        for c in cantones_sin_codigo[:3]:
            print(f"      * {c['CANTON']} (Provincia: {c['PROVINCIA']})")
    else:
        print(f"  - ✅ Todos los cantones tienen código")
    
    # Mostrar primeros 3 cantones
    print(f"  - Primeros 3 cantones:")
    for c in data[:3]:
        print(f"      * {c['CANTON']} (Código: {c['CODCAN']}, Provincia: {c['PROVINCIA']})")

print("\n" + "="*80)
print("Verificación completada")
print("="*80 + "\n")
