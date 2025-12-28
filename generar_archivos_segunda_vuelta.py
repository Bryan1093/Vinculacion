"""
Generar archivos adicionales para segunda vuelta:
1. Votos válidos, blancos, nulos por parroquia
2. Votos por candidato en formato transpuesto
"""

import pandas as pd

print("\n" + "="*80)
print("GENERANDO ARCHIVOS ADICIONALES - SEGUNDA VUELTA")
print("="*80 + "\n")

# ========== 1. VOTOS VÁLIDOS, BLANCOS, NULOS ==========
print("1. Generando archivo de votos válidos, blancos, nulos...")

archivo_origen = 'resultados/Segunda_Vuelta_Votos_Por_Candidato.xlsx'
df_resumen = pd.read_excel(archivo_origen, sheet_name='Resumen_General')

archivo_votos = 'resultados/Segunda_Vuelta_Votos_Validos_Blancos_Nulos.xlsx'
df_resumen.to_excel(archivo_votos, index=False)

print(f"✓ Archivo guardado: {archivo_votos}")

# ========== 2. FORMATO TRANSPUESTO ==========
print("\n2. Generando archivo en formato transpuesto...")

df_detalle = pd.read_excel(archivo_origen, sheet_name='Detalle_Por_Candidato')

# Definir el orden correcto de las parroquias
orden_pastaza = ['3180', '3195', '3785', '3985', '4005', '4205', 
                 '4510', '5825', '2310', '3840', '5650', '6395']

orden_pichincha = ['30', '80', '195', '430', '440', '625', '725', '855', '865',
                   '1400', '1440', '1475', '2055', '2265', '2275', '2525', '2530',
                   '2540', '2560', '2690', '2825', '2855', '2895', '2925', '2980',
                   '2985', '3100', '3325', '3475', '3925', '4085', '4290', '4325',
                   '5015', '5110', '5220', '5235', '5260', '5325', '5410', '5435',
                   '5530', '5535', '5540', '5575', '5935', '5985']

orden_completo = orden_pastaza + orden_pichincha

# Crear tabla pivote: parroquias en filas, candidatos en columnas
df_pivot = df_detalle.pivot_table(
    index=['Provincia', 'Codigo_Parroquia', 'Parroquia'],
    columns='Candidato',
    values='Votos',
    aggfunc='sum',
    fill_value=0
).reset_index()

df_pivot.columns.name = None

# Convertir Codigo_Parroquia a string
df_pivot['Codigo_Parroquia'] = df_pivot['Codigo_Parroquia'].astype(str)

# Aplicar el orden correcto
df_pivot['Codigo_Parroquia'] = pd.Categorical(
    df_pivot['Codigo_Parroquia'],
    categories=orden_completo,
    ordered=True
)

# Ordenar
df_pivot = df_pivot.sort_values('Codigo_Parroquia').reset_index(drop=True)

# Convertir de vuelta a string
df_pivot['Codigo_Parroquia'] = df_pivot['Codigo_Parroquia'].astype(str)

# Guardar
archivo_transpuesto = 'resultados/Segunda_Vuelta_Votos_Transpuesto.xlsx'
df_pivot.to_excel(archivo_transpuesto, index=False)

print(f"✓ Archivo guardado: {archivo_transpuesto}")

# ========== RESUMEN ==========
print("\n" + "="*80)
print("RESUMEN DE ARCHIVOS GENERADOS:")
print("="*80)
print(f"\n1. {archivo_origen}")
print(f"   - Hoja 'Detalle_Por_Candidato': {len(df_detalle)} registros")
print(f"   - Hoja 'Resumen_General': {len(df_resumen)} registros")
print(f"   - Hoja 'Totales_Por_Candidato': 2 candidatos")

print(f"\n2. {archivo_votos}")
print(f"   - Votos válidos, blancos, nulos y totales por parroquia")
print(f"   - {len(df_resumen)} parroquias")

print(f"\n3. {archivo_transpuesto}")
print(f"   - Formato transpuesto: parroquias en filas, candidatos en columnas")
print(f"   - {len(df_pivot)} parroquias x 2 candidatos")

print("\n" + "="*80)
print("VISTA PREVIA - FORMATO TRANSPUESTO:")
print("="*80 + "\n")

print("PASTAZA:")
print("-" * 80)
pastaza = df_pivot[df_pivot['Provincia'] == 'PASTAZA']
print(pastaza.to_string(index=False))

print("\n\nPICHINCHA (primeras 5):")
print("-" * 80)
pichincha = df_pivot[df_pivot['Provincia'] == 'PICHINCHA'].head(5)
print(pichincha.to_string(index=False))

print(f"\n... y {len(df_pivot[df_pivot['Provincia'] == 'PICHINCHA']) - 5} parroquias más de Pichincha")

print("\n" + "="*80)
print("✓ TODOS LOS ARCHIVOS GENERADOS EXITOSAMENTE")
print("="*80 + "\n")
