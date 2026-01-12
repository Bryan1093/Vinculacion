import json
import os

files = {
    'Presidentes 1ra': 'JSON-Parroquias/presidentes_primera_vuelta.json',
    'Presidentes 2da': 'JSON-Parroquias/presidentes_segunda_vuelta.json',
    'Diputados': 'JSON-Parroquias/diputados_nacionales.json'
}

print("="*60)
print("REVISIÓN DE ARCHIVOS DE PARROQUIAS")
print("="*60)

for nombre, archivo in files.items():
    if not os.path.exists(archivo):
        print(f"❌ {nombre}: Archivo no encontrado")
        continue

    with open(archivo, encoding='utf-8') as f:
        data = json.load(f)
    
    # Buscar problemas: 'nan' en códigos o nombres, o claves 'nan'
    nans = []
    
    # 1. Verificar si es una lista (formato plano)
    if isinstance(data, list):
        for item in data:
            # Chequear campos clave
            if str(item.get('CODPRO')).lower() == 'nan' or \
               str(item.get('CODCAN')).lower() == 'nan' or \
               str(item.get('CODPAR')).lower() == 'nan' or \
               str(item.get('PROVINCIA')).lower() == 'nan':
                nans.append(item)
    
    # 2. Verificar si es un diccionario (formato anidado)
    elif isinstance(data, dict):
        # A veces el formato de parroquias es { "CODIGO": {datos}, ... }
        # Voy a asumir que podría ser así y chequear las claves
        for key, val in data.items():
            if str(key).lower() == 'nan':
                 nans.append({'key': key, 'val': val})

    print(f"\n{nombre}:")
    print(f"  - Total registros: {len(data)}")
    if nans:
        print(f"  - ⚠️ Registros con 'nan': {len(nans)}")
        # Mostrar el primero como ejemplo
        ejemplo = nans[0]
        print(f"    Ejemplo: {str(ejemplo)[:100]}...")
    else:
        print(f"  - ✅ No se encontraron 'nan'")

print("\n" + "="*60)
