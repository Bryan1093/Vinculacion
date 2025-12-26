    import pandas as pd

# Cargar archivo de segunda vuelta
df = pd.read_excel('Datos-Presidentes-Completos/Segunda Vuelta/1996 - Presidentes - segunda vuelta.xlsx')

print("=" * 80)
print("ESTRUCTURA DEL ARCHIVO DE SEGUNDA VUELTA - PRESIDENTES")
print("=" * 80)
print()

print(f"Total de filas: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")
print()

print("COLUMNAS:")
print("-" * 80)
for i, col in enumerate(df.columns, 1):
    print(f"{i:2d}. {col}")

print()
print("=" * 80)
print("PRIMERAS 5 FILAS:")
print("=" * 80)
print(df.head())

print()
print("=" * 80)
print("IDENTIFICAR CANDIDATOS:")
print("=" * 80)

# Identificar columnas de candidatos (las que no son metadatos)
columnas_metadata = ['AÑO', 'DIGNIDAD', 'PROVINCI', 'CANTON', 'PARROQUIA', 
                     'VOTOSVAL', 'VOTOSNUL', 'VOTOSBLA', 'VOTOSESC', 
                     'ABSTENCI', 'ACTASVAL', 'ACTASESC']

columnas_candidatos = [col for col in df.columns if col not in columnas_metadata]

print("Columnas de candidatos encontradas:")
for i, candidato in enumerate(columnas_candidatos, 1):
    import numpy as np
    votos_numericos = pd.to_numeric(df[candidato], errors='coerce')
    total_votos = votos_numericos.sum()
    if not np.isnan(total_votos):
        print(f"{i:2d}. {candidato:30s} - Total votos: {total_votos:,.0f}")
