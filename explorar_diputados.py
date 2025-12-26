import pandas as pd
import numpy as np

# Cargar archivo de diputados
df = pd.read_excel('Datos-Diputados-Completos/1996 - Diputados - nacionales.xlsx')

print("=" * 80)
print("ANÁLISIS COMPLETO - DIPUTADOS NACIONALES 1996")
print("=" * 80)
print()

# Mostrar todas las columnas
print("TODAS LAS COLUMNAS:")
print("-" * 80)
for i, col in enumerate(df.columns, 1):
    tipo = df[col].dtype
    print(f"{i:2d}. {col:30s} (tipo: {tipo})")

print()
print("=" * 80)
print("PRIMERAS 3 FILAS:")
print("=" * 80)
print(df.head(3).to_string())

print()
print("=" * 80)
print("COLUMNAS QUE PARECEN SER PARTIDOS/LISTAS:")
print("=" * 80)

# Identificar columnas de partidos (las que no son metadatos)
columnas_metadata = ['AÑO', 'DIGNIDAD', 'PROVINCI', 'CANTON', 'PARROQUIA', 
                     'VOTOSVAL', 'VOTOSNUL', 'VOTOSBLA', 'VOTOSESC', 
                     'ABSTENCI', 'ACTASVAL', 'ACTASESC']

columnas_partidos = [col for col in df.columns if col not in columnas_metadata]

for i, partido in enumerate(columnas_partidos, 1):
    # Convertir a numérico y calcular suma
    try:
        votos_numericos = pd.to_numeric(df[partido], errors='coerce')
        total_votos = votos_numericos.sum()
        if not np.isnan(total_votos):
            print(f"{i:2d}. {partido:30s} - Total votos: {total_votos:,.0f}")
        else:
            print(f"{i:2d}. {partido:30s} - (no numérico)")
    except:
        print(f"{i:2d}. {partido:30s} - (error al procesar)")
