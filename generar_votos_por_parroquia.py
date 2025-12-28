"""
Crear archivo Excel solo con votos válidos, blancos, nulos y totales por parroquia
"""

import pandas as pd

print("\n" + "="*80)
print("GENERANDO ARCHIVO DE VOTOS POR PARROQUIA")
print("="*80 + "\n")

# Leer el archivo completo
archivo_origen = 'resultados/Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx'
df = pd.read_excel(archivo_origen, sheet_name='Resumen_General')

print(f"✓ Datos cargados: {len(df)} parroquias")

# El DataFrame ya tiene las columnas correctas
# Solo vamos a guardarlo en un archivo separado más simple

archivo_destino = 'resultados/Votos_Validos_Blancos_Nulos_Por_Parroquia.xlsx'

# Guardar
df.to_excel(archivo_destino, index=False)

print(f"✓ Archivo guardado: {archivo_destino}")

print("\n" + "="*80)
print("VISTA PREVIA DEL ARCHIVO:")
print("="*80 + "\n")

print("PASTAZA:")
print("-" * 80)
pastaza = df[df['Provincia'] == 'PASTAZA']
print(pastaza.to_string(index=False))

print("\n\nPICHINCHA (primeras 10):")
print("-" * 80)
pichincha = df[df['Provincia'] == 'PICHINCHA'].head(10)
print(pichincha.to_string(index=False))

print(f"\n... y {len(df[df['Provincia'] == 'PICHINCHA']) - 10} parroquias más de Pichincha")

print("\n" + "="*80)
print("✓ ARCHIVO GENERADO EXITOSAMENTE")
print("="*80 + "\n")
