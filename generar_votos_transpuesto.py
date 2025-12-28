"""
Crear archivo Excel con votos por candidato en formato transpuesto
Parroquias en filas, candidatos en columnas
"""

import pandas as pd

print("\n" + "="*80)
print("GENERANDO ARCHIVO CON VOTOS POR CANDIDATO (FORMATO TRANSPUESTO)")
print("="*80 + "\n")

# Leer el archivo con el detalle por candidato
archivo_origen = 'resultados/Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx'
df_detalle = pd.read_excel(archivo_origen, sheet_name='Detalle_Por_Candidato')

print(f"✓ Datos cargados: {len(df_detalle)} registros")

# Definir el orden correcto de las parroquias
orden_pastaza = ['3180', '3195', '3785', '3985', '4005', '4205', 
                 '4510', '5825', '2310', '3840', '5650', '6395']

orden_pichincha = ['30', '80', '195', '430', '440', '625', '725', '855', '865',
                   '1400', '1440', '1475', '2055', '2265', '2275', '2525', '2530',
                   '2540', '2560', '2690', '2825', '2855', '2895', '2925', '2980',
                   '2985', '3100', '3325', '3475', '3925', '4085', '4290', '4325',
                   '5015', '5110', '5220', '5235', '5260', '5325', '5410', '5435',
                   '5530', '5535', '5540', '5575', '5935', '5985']

# Combinar el orden completo
orden_completo = orden_pastaza + orden_pichincha

print(f"✓ Orden de parroquias definido: {len(orden_completo)} parroquias")

# Crear tabla pivote: parroquias en filas, candidatos en columnas
df_pivot = df_detalle.pivot_table(
    index=['Provincia', 'Codigo_Parroquia', 'Parroquia'],
    columns='Candidato',
    values='Votos',
    aggfunc='sum',
    fill_value=0
).reset_index()

# Renombrar las columnas para que sean más claras
df_pivot.columns.name = None

# Convertir Codigo_Parroquia a string para asegurar compatibilidad
df_pivot['Codigo_Parroquia'] = df_pivot['Codigo_Parroquia'].astype(str)

# Aplicar el orden correcto usando Categorical
df_pivot['Codigo_Parroquia'] = pd.Categorical(
    df_pivot['Codigo_Parroquia'],
    categories=orden_completo,
    ordered=True
)

# Ordenar según el orden especificado
df_pivot = df_pivot.sort_values('Codigo_Parroquia').reset_index(drop=True)

# Convertir de vuelta a string normal para el Excel
df_pivot['Codigo_Parroquia'] = df_pivot['Codigo_Parroquia'].astype(str)

print(f"✓ Tabla transpuesta creada y ordenada: {len(df_pivot)} parroquias x {len(df_detalle['Candidato'].unique())} candidatos")

# Guardar en Excel
archivo_destino = 'resultados/Votos_Por_Candidato_Transpuesto.xlsx'
df_pivot.to_excel(archivo_destino, index=False)

print(f"✓ Archivo guardado: {archivo_destino}")

print("\n" + "="*80)
print("VISTA PREVIA - PASTAZA:")
print("="*80 + "\n")

pastaza = df_pivot[df_pivot['Provincia'] == 'PASTAZA']
print(pastaza.to_string(index=False))

print("\n" + "="*80)
print("VISTA PREVIA - PICHINCHA (primeras 5):")
print("="*80 + "\n")

pichincha = df_pivot[df_pivot['Provincia'] == 'PICHINCHA'].head(5)
print(pichincha.to_string(index=False))

print(f"\n... y {len(df_pivot[df_pivot['Provincia'] == 'PICHINCHA']) - 5} parroquias más de Pichincha")

print("\n" + "="*80)
print("ESTRUCTURA DEL ARCHIVO:")
print("="*80)
print("\nColumnas:")
print("  - Provincia")
print("  - Codigo_Parroquia")
print("  - Parroquia")
for candidato in sorted(df_detalle['Candidato'].unique()):
    print(f"  - {candidato}")

print("\n" + "="*80)
print("✓ ARCHIVO GENERADO EXITOSAMENTE")
print("="*80 + "\n")
