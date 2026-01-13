import json
import sys

# Redirigir output a archivo
output_file = open('resultado_verificacion_parroquias.txt', 'w', encoding='utf-8')
sys.stdout = output_file

# 1. Leer los códigos del archivo parroquias.txt
print("=" * 80)
print("VERIFICACIÓN DE CÓDIGOS DE PARROQUIAS")
print("=" * 80)

with open('parroquias.txt', 'r', encoding='utf-8') as f:
    codigos_txt = [line.strip() for line in f if line.strip()]

print(f"\nTotal de códigos en parroquias.txt: {len(codigos_txt)}")
print(f"Primeros 10 códigos: {codigos_txt[:10]}")
print(f"Últimos 10 códigos: {codigos_txt[-10:]}")

# 2. Leer los códigos de cada JSON
archivos_json = [
    'JSON-Parroquias/presidentes_primera_vuelta.json',
    'JSON-Parroquias/presidentes_segunda_vuelta.json',
    'JSON-Parroquias/diputados_nacionales.json'
]

resultados = {}

for archivo in archivos_json:
    nombre = archivo.split('/')[-1].replace('.json', '')
    
    with open(archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extraer todos los CODPAR únicos
    codigos_json = set(r['CODPAR'] for r in data)
    
    # Verificar qué códigos del txt están en el JSON
    codigos_encontrados = [cod for cod in codigos_txt if cod in codigos_json]
    codigos_faltantes = [cod for cod in codigos_txt if cod not in codigos_json]
    
    resultados[nombre] = {
        'total_json': len(codigos_json),
        'encontrados': len(codigos_encontrados),
        'faltantes': len(codigos_faltantes),
        'lista_faltantes': codigos_faltantes
    }
    
    print(f"\n{'-' * 80}")
    print(f"Archivo: {nombre}")
    print(f"{'-' * 80}")
    print(f"  Total de códigos únicos en JSON: {len(codigos_json)}")
    print(f"  Códigos del txt encontrados: {len(codigos_encontrados)} / {len(codigos_txt)}")
    print(f"  Códigos del txt NO encontrados: {len(codigos_faltantes)}")
    
    if codigos_faltantes:
        print(f"\n  ⚠️  CÓDIGOS FALTANTES:")
        for cod in codigos_faltantes:
            print(f"    - {cod}")

# 3. Resumen general
print(f"\n{'=' * 80}")
print("RESUMEN GENERAL")
print(f"{'=' * 80}")

# Verificar si todos los archivos tienen los mismos códigos faltantes
todos_faltantes = set(resultados['presidentes_primera_vuelta']['lista_faltantes'])
for nombre, res in resultados.items():
    if nombre != 'presidentes_primera_vuelta':
        todos_faltantes = todos_faltantes.intersection(set(res['lista_faltantes']))

print(f"\nCódigos del txt que faltan en TODOS los JSONs: {len(todos_faltantes)}")
if todos_faltantes:
    print("\nEstos códigos no están en ningún archivo JSON:")
    for cod in sorted(todos_faltantes):
        print(f"  - {cod}")

# 4. Verificar si hay códigos en los JSONs que NO están en el txt
print(f"\n{'=' * 80}")
print("CÓDIGOS EN JSON QUE NO ESTÁN EN parroquias.txt")
print(f"{'=' * 80}")

for archivo in archivos_json:
    nombre = archivo.split('/')[-1].replace('.json', '')
    
    with open(archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    codigos_json = set(r['CODPAR'] for r in data)
    codigos_extra = [cod for cod in codigos_json if cod not in codigos_txt]
    
    print(f"\n{nombre}:")
    print(f"  Códigos en JSON pero NO en txt: {len(codigos_extra)}")
    if codigos_extra:
        print(f"  Lista completa:")
        for cod in sorted(codigos_extra):
            # Buscar el nombre de la parroquia
            parroquia = next((r['PARROQUIA'] for r in data if r['CODPAR'] == cod), 'N/A')
            print(f"    - {cod}: {parroquia}")

print(f"\n{'=' * 80}")
print("✓ VERIFICACIÓN COMPLETADA")
print(f"{'=' * 80}")

output_file.close()

# Mostrar resumen en consola
sys.stdout = sys.__stdout__
print("✓ Verificación completada. Resultados guardados en: resultado_verificacion_parroquias.txt")
print(f"\nResumen rápido:")
print(f"  - Códigos en parroquias.txt: {len(codigos_txt)}")
for nombre, res in resultados.items():
    print(f"  - {nombre}: {res['encontrados']}/{len(codigos_txt)} encontrados, {res['faltantes']} faltantes")
