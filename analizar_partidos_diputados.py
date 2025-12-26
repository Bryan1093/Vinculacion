import pandas as pd

# Leer el archivo
df = pd.read_excel('Datos-Diputados-Completos/1996 - Diputados - nacionales.xlsx')

# Obtener todas las columnas
todas_columnas = df.columns.tolist()

# Columnas que NO son partidos
columnas_sistema = [
    'AÑO', 'DIGNIDAD', 'REGION', 'PROVINCI', 'CANTON', 'PARROQUIA', 
    'JUNTAS ', 'ELECTORES', 'VOTOSVAL', 'VOTOSNUL', 'VOTOSBLA', 
    'VOTOSESC', 'ABSTENCI', 'ACTASVAL'
]

# Filtrar solo columnas de partidos
partidos = [col for col in todas_columnas if col not in columnas_sistema]

print(f"=" * 80)
print(f"ANÁLISIS DE PARTIDOS POLÍTICOS - DIPUTADOS NACIONALES 1996")
print(f"=" * 80)
print(f"\nTotal de partidos/listas encontrados: {len(partidos)}")
print(f"\nListado completo de partidos:")
print("-" * 80)

for i, partido in enumerate(partidos, 1):
    print(f"{i:2d}. {partido}")

print(f"\n" + "=" * 80)
print(f"PARTIDOS CONFIGURADOS EN config.py")
print(f"=" * 80)

partidos_config = [
    'PCE1', 'CFP4', 'DP5', 'PSC6', 'PRE10', 'AN11', 'ID12', 
    'APRE13', 'MPD15', 'UPL16', 'PSE17', 'MUPP-NP-18', 'MITI20', 'PLRE - FRA'
]

print(f"\nTotal configurados: {len(partidos_config)}")
print(f"\nPartidos en config.py:")
print("-" * 80)
for i, partido in enumerate(partidos_config, 1):
    print(f"{i:2d}. {partido}")

print(f"\n" + "=" * 80)
print(f"COMPARACIÓN")
print(f"=" * 80)

# Partidos en Excel pero NO en config
faltantes = [p for p in partidos if p not in partidos_config]
if faltantes:
    print(f"\n⚠️  PARTIDOS EN EXCEL QUE FALTAN EN CONFIG ({len(faltantes)}):")
    print("-" * 80)
    for i, partido in enumerate(faltantes, 1):
        print(f"{i:2d}. {partido}")
else:
    print("\n✅ Todos los partidos del Excel están en config.py")

# Partidos en config pero NO en Excel
sobrantes = [p for p in partidos_config if p not in partidos]
if sobrantes:
    print(f"\n⚠️  PARTIDOS EN CONFIG QUE NO EXISTEN EN EXCEL ({len(sobrantes)}):")
    print("-" * 80)
    for i, partido in enumerate(sobrantes, 1):
        print(f"{i:2d}. {partido}")
else:
    print("\n✅ Todos los partidos del config.py existen en el Excel")

print(f"\n" + "=" * 80)
