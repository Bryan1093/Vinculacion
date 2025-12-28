"""
Análisis DETALLADO de votos por parroquia y partido
DIPUTADOS NACIONALES 1996
12 Parroquias de PASTAZA y 47 Parroquias de PICHINCHA
"""

import pandas as pd
import json
import os

# Configuración
ARCHIVO_DATOS = 'Datos-Diputados-Completos/1996 - Diputados - nacionales.xlsx'
DIR_RESULTADOS = 'resultados'

# Asegurar que existe el directorio de resultados
os.makedirs(DIR_RESULTADOS, exist_ok=True)

# Partidos/Listas de Diputados Nacionales (14 partidos)
PARTIDOS = {
    'PCE': {
        'columnas': ['PCE1'],
        'nombre_completo': 'PARTIDO COMUNISTA ECUATORIANO'
    },
    'CFP': {
        'columnas': ['CFP4'],
        'nombre_completo': 'CONCENTRACIÓN DE FUERZAS POPULARES'
    },
    'DP': {
        'columnas': ['DP5'],
        'nombre_completo': 'DEMOCRACIA POPULAR'
    },
    'PSC': {
        'columnas': ['PSC6'],
        'nombre_completo': 'PARTIDO SOCIAL CRISTIANO'
    },
    'PRE': {
        'columnas': ['PRE10'],
        'nombre_completo': 'PARTIDO ROLDOSISTA ECUATORIANO'
    },
    'AN': {
        'columnas': ['AN11'],
        'nombre_completo': 'ALIANZA NACIONAL'
    },
    'ID': {
        'columnas': ['ID12'],
        'nombre_completo': 'IZQUIERDA DEMOCRÁTICA'
    },
    'APRE': {
        'columnas': ['APRE13'],
        'nombre_completo': 'ACCIÓN POPULAR REVOLUCIONARIA ECUATORIANA'
    },
    'MPD': {
        'columnas': ['MPD15'],
        'nombre_completo': 'MOVIMIENTO POPULAR DEMOCRÁTICO'
    },
    'UPL': {
        'columnas': ['UPL16'],
        'nombre_completo': 'UNIÓN POPULAR LATINOAMERICANA'
    },
    'PSE': {
        'columnas': ['PSE17'],
        'nombre_completo': 'PARTIDO SOCIALISTA ECUATORIANO'
    },
    'MUPP-NP': {
        'columnas': ['MUPP-NP-18'],
        'nombre_completo': 'MOVIMIENTO UNIDAD PLURINACIONAL PACHAKUTIK - NUEVO PAÍS'
    },
    'MITI': {
        'columnas': ['MITI20'],
        'nombre_completo': 'MOVIMIENTO INDEPENDIENTE TIERRA INDÍGENA'
    },
    'PLRE-FRA': {
        'columnas': ['PLRE - FRA'],
        'nombre_completo': 'PARTIDO LIBERAL RADICAL ECUATORIANO - FRENTE RADICAL ALFARISTA'
    }
}

# Nombres de columnas
COL_PROVINCIA = 'PROVINCI'
COL_PARROQUIA = 'PARROQUIA'
COL_VOTOS_VALIDOS = 'VOTOSVAL'
COL_VOTOS_NULOS = 'VOTOSNUL'
COL_VOTOS_BLANCOS = 'VOTOSBLA'


def cargar_y_limpiar_datos():
    """Carga y limpia los datos del archivo Excel"""
    print("Cargando datos de diputados nacionales...")
    df = pd.read_excel(ARCHIVO_DATOS)
    
    # Limpiar columnas
    df[COL_PROVINCIA] = df[COL_PROVINCIA].astype(str).str.strip()
    df[COL_PARROQUIA] = df[COL_PARROQUIA].astype(str).str.strip().str.replace('.0$', '', regex=True)
    
    print(f"✓ Datos cargados: {len(df)} registros")
    return df


def obtener_parroquias_seleccionadas(df):
    """Obtiene las parroquias específicas de Pastaza y Pichincha en el orden proporcionado"""
    # Parroquias específicas de PASTAZA (en el orden proporcionado por el usuario)
    parroquias_pastaza = ['3180', '3195', '3785', '3985', '4005', '4205', 
                          '4510', '5825', '2310', '3840', '5650', '6395']
    
    # Parroquias específicas de PICHINCHA (en el orden proporcionado por el usuario)
    parroquias_pichincha = ['30', '80', '195', '430', '440', '625', '725', '855', '865',
                            '1400', '1440', '1475', '2055', '2265', '2275', '2525', '2530',
                            '2540', '2560', '2690', '2825', '2855', '2895', '2925', '2980',
                            '2985', '3100', '3325', '3475', '3925', '4085', '4290', '4325',
                            '5015', '5110', '5220', '5235', '5260', '5325', '5410', '5435',
                            '5530', '5535', '5540', '5575', '5935', '5985']
    
    return parroquias_pastaza, parroquias_pichincha


def analizar_parroquia_detallado(df_parroquia, codigo_parroquia, provincia):
    """Analiza una parroquia específica y retorna estadísticas detalladas por partido"""
    if df_parroquia.empty:
        return None
    
    # Calcular totales generales
    votos_validos = int(df_parroquia[COL_VOTOS_VALIDOS].sum())
    votos_blancos = int(df_parroquia[COL_VOTOS_BLANCOS].sum())
    votos_nulos = int(df_parroquia[COL_VOTOS_NULOS].sum())
    total_votos = votos_validos + votos_blancos + votos_nulos
    
    # Calcular votos por partido
    resultados_partidos = []
    votos_partidos_dict = {}
    
    for partido, info in PARTIDOS.items():
        votos_total = 0
        for columna in info['columnas']:
            if columna in df_parroquia.columns:
                votos = pd.to_numeric(df_parroquia[columna], errors='coerce').fillna(0).sum()
                votos_total += votos
        
        votos_total = int(votos_total)
        porcentaje = round((votos_total / votos_validos * 100) if votos_validos > 0 else 0, 2)
        
        resultados_partidos.append({
            'Provincia': provincia,
            'Codigo_Parroquia': codigo_parroquia,
            'Parroquia': f'PARROQUIA_{codigo_parroquia}',
            'Partido': partido,
            'Nombre_Completo': info['nombre_completo'],
            'Votos': votos_total,
            'Porcentaje': porcentaje
        })
        
        if votos_total > 0:
            votos_partidos_dict[partido] = {
                'votos': votos_total,
                'porcentaje': porcentaje
            }
    
    return {
        'provincia': provincia,
        'codigo_parroquia': codigo_parroquia,
        'votos_validos': votos_validos,
        'votos_blancos': votos_blancos,
        'votos_nulos': votos_nulos,
        'total_votos': total_votos,
        'partidos': resultados_partidos,
        'partidos_dict': votos_partidos_dict
    }


def main():
    """Función principal"""
    print("\n" + "="*80)
    print("ANÁLISIS DETALLADO - DIPUTADOS NACIONALES 1996")
    print("12 Parroquias de PASTAZA y 47 Parroquias de PICHINCHA (orden específico)")
    print("="*80 + "\n")
    
    # Cargar datos
    df = cargar_y_limpiar_datos()
    
    # Obtener parroquias seleccionadas
    parroquias_pastaza, parroquias_pichincha = obtener_parroquias_seleccionadas(df)
    
    print(f"\n✓ Parroquias de Pastaza seleccionadas: {len(parroquias_pastaza)}")
    print(f"✓ Parroquias de Pichincha seleccionadas: {len(parroquias_pichincha)}")
    print(f"✓ Total de partidos/listas: {len(PARTIDOS)}")
    
    # Preparar estructuras para resultados
    resultados_por_partido = []  # Para Excel detallado
    resultados_resumen = []  # Para Excel resumen
    resultados_json = {
        'PASTAZA': {},
        'PICHINCHA': {}
    }
    
    # ========== ANÁLISIS DE PASTAZA ==========
    print("\n" + "="*80)
    print("PASTAZA - 12 PARROQUIAS ESPECÍFICAS")
    print("="*80 + "\n")
    
    df_pastaza = df[df[COL_PROVINCIA] == 'PASTAZA'].copy()
    
    for i, parroquia_cod in enumerate(parroquias_pastaza, 1):
        df_parroquia = df_pastaza[df_pastaza[COL_PARROQUIA] == parroquia_cod]
        
        resultado = analizar_parroquia_detallado(df_parroquia, parroquia_cod, 'PASTAZA')
        if resultado:
            # Guardar en JSON
            resultados_json['PASTAZA'][parroquia_cod] = {
                'nombre': f'PARROQUIA_{parroquia_cod}',
                'votos_validos': resultado['votos_validos'],
                'votos_blancos': resultado['votos_blancos'],
                'votos_nulos': resultado['votos_nulos'],
                'total_votos': resultado['total_votos'],
                'partidos': resultado['partidos_dict']
            }
            
            # Guardar detalle por partido
            resultados_por_partido.extend(resultado['partidos'])
            
            # Guardar resumen
            resultados_resumen.append({
                'Provincia': 'PASTAZA',
                'Codigo_Parroquia': parroquia_cod,
                'Parroquia': f'PARROQUIA_{parroquia_cod}',
                'Votos_Validos': resultado['votos_validos'],
                'Votos_Blancos': resultado['votos_blancos'],
                'Votos_Nulos': resultado['votos_nulos'],
                'Total_Votos': resultado['total_votos']
            })
            
            # Mostrar en consola (solo primeras 3 parroquias)
            if i <= 3:
                print(f"{i}. Parroquia {parroquia_cod}:")
                print(f"   Votos Válidos: {resultado['votos_validos']:,}")
                print(f"   Top 5 partidos:")
                for cand in sorted(resultado['partidos'], key=lambda x: x['Votos'], reverse=True)[:5]:
                    if cand['Votos'] > 0:
                        print(f"      {cand['Partido']:12}: {cand['Votos']:>6,} votos ({cand['Porcentaje']:>5.2f}%)")
                print()
    
    print(f"   ... (mostrando solo las primeras 3 de {len(parroquias_pastaza)} parroquias de Pastaza)")
    
    # ========== ANÁLISIS DE PICHINCHA ==========
    print("\n" + "="*80)
    print("PICHINCHA - 47 PARROQUIAS ESPECÍFICAS")
    print("="*80 + "\n")
    
    df_pichincha = df[df[COL_PROVINCIA] == 'PICHINCHA'].copy()
    
    for i, parroquia_cod in enumerate(parroquias_pichincha, 1):
        df_parroquia = df_pichincha[df_pichincha[COL_PARROQUIA] == parroquia_cod]
        
        resultado = analizar_parroquia_detallado(df_parroquia, parroquia_cod, 'PICHINCHA')
        if resultado:
            # Guardar en JSON
            resultados_json['PICHINCHA'][parroquia_cod] = {
                'nombre': f'PARROQUIA_{parroquia_cod}',
                'votos_validos': resultado['votos_validos'],
                'votos_blancos': resultado['votos_blancos'],
                'votos_nulos': resultado['votos_nulos'],
                'total_votos': resultado['total_votos'],
                'partidos': resultado['partidos_dict']
            }
            
            # Guardar detalle por partido
            resultados_por_partido.extend(resultado['partidos'])
            
            # Guardar resumen
            resultados_resumen.append({
                'Provincia': 'PICHINCHA',
                'Codigo_Parroquia': parroquia_cod,
                'Parroquia': f'PARROQUIA_{parroquia_cod}',
                'Votos_Validos': resultado['votos_validos'],
                'Votos_Blancos': resultado['votos_blancos'],
                'Votos_Nulos': resultado['votos_nulos'],
                'Total_Votos': resultado['total_votos']
            })
            
            # Mostrar en consola (solo primeras 3 para no saturar)
            if i <= 3:
                print(f"{i}. Parroquia {parroquia_cod}:")
                print(f"   Votos Válidos: {resultado['votos_validos']:,}")
                print(f"   Top 5 partidos:")
                for cand in sorted(resultado['partidos'], key=lambda x: x['Votos'], reverse=True)[:5]:
                    if cand['Votos'] > 0:
                        print(f"      {cand['Partido']:12}: {cand['Votos']:>6,} votos ({cand['Porcentaje']:>5.2f}%)")
                print()
    
    print(f"   ... (mostrando solo las primeras 3 de {len(parroquias_pichincha)} parroquias de Pichincha)")
    
    # ========== GUARDAR RESULTADOS ==========
    df_detallado = pd.DataFrame(resultados_por_partido)
    df_resumen = pd.DataFrame(resultados_resumen)
    
    # Archivos de salida
    archivo_excel_detallado = os.path.join(DIR_RESULTADOS, 'Diputados_Votos_Por_Partido.xlsx')
    archivo_json = os.path.join(DIR_RESULTADOS, 'diputados_parroquias_1996.json')
    
    # Guardar Excel con múltiples hojas
    with pd.ExcelWriter(archivo_excel_detallado, engine='openpyxl') as writer:
        df_detallado.to_excel(writer, sheet_name='Detalle_Por_Partido', index=False)
        df_resumen.to_excel(writer, sheet_name='Resumen_General', index=False)
        
        # Crear hoja de totales por partido
        df_totales_partido = df_detallado.groupby('Partido').agg({
            'Votos': 'sum'
        }).reset_index().sort_values('Votos', ascending=False)
        df_totales_partido.to_excel(writer, sheet_name='Totales_Por_Partido', index=False)
    
    print(f"\n✓ Archivo Excel detallado guardado: {archivo_excel_detallado}")
    print(f"  - Hoja 'Detalle_Por_Partido': Votos de cada partido en cada parroquia")
    print(f"  - Hoja 'Resumen_General': Totales por parroquia")
    print(f"  - Hoja 'Totales_Por_Partido': Suma total de votos por partido")
    
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(resultados_json, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Archivo JSON guardado: {archivo_json}")
    
    # ========== RESUMEN FINAL ==========
    print("\n" + "="*80)
    print("RESUMEN GENERAL - DIPUTADOS NACIONALES")
    print("="*80)
    
    total_pastaza = len([r for r in resultados_resumen if r['Provincia'] == 'PASTAZA'])
    total_pichincha = len([r for r in resultados_resumen if r['Provincia'] == 'PICHINCHA'])
    
    print(f"\nTotal de parroquias analizadas: {len(resultados_resumen)}")
    print(f"  - Pastaza:   {total_pastaza} parroquias")
    print(f"  - Pichincha: {total_pichincha} parroquias")
    
    total_votos_validos = df_resumen['Votos_Validos'].sum()
    total_votos_blancos = df_resumen['Votos_Blancos'].sum()
    total_votos_nulos = df_resumen['Votos_Nulos'].sum()
    total_general = df_resumen['Total_Votos'].sum()
    
    print(f"\nTOTAL GENERAL DE VOTOS:")
    print(f"  Votos Válidos:  {total_votos_validos:>12,}")
    print(f"  Votos Blancos:  {total_votos_blancos:>12,}")
    print(f"  Votos Nulos:    {total_votos_nulos:>12,}")
    print(f"  {'─'*30}")
    print(f"  TOTAL:          {total_general:>12,}")
    
    print(f"\nTOP 10 PARTIDOS (en las {len(resultados_resumen)} parroquias):")
    print(f"{'─'*80}")
    for _, row in df_totales_partido.head(10).iterrows():
        porcentaje = (row['Votos'] / total_votos_validos * 100) if total_votos_validos > 0 else 0
        print(f"  {row['Partido']:12}: {row['Votos']:>10,} votos ({porcentaje:>5.2f}%)")
    
    print("\n" + "="*80)
    print("✓ ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("="*80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n✗ Error durante el análisis: {str(e)}")
        import traceback
        traceback.print_exc()
