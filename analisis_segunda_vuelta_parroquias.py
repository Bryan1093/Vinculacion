"""
Análisis DETALLADO de votos por parroquia y candidato
SEGUNDA VUELTA PRESIDENCIAL 1996
12 Parroquias de PASTAZA y 47 Parroquias de PICHINCHA
"""

import pandas as pd
import json
import os

# Configuración
ARCHIVO_DATOS = 'Datos-Presidentes-Completos/Segunda Vuelta/1996 - Presidentes - segunda vuelta.xlsx'
DIR_RESULTADOS = 'resultados'

# Asegurar que existe el directorio de resultados
os.makedirs(DIR_RESULTADOS, exist_ok=True)

# Candidatos de la SEGUNDA VUELTA (solo 2 candidatos)
CANDIDATOS = {
    'BUCARAM ABDALÁ': {
        'columnas': ['PRE10'],
        'partido': 'PRE',
        'nombre_completo': 'ABDALÁ BUCARAM ORTIZ'
    },
    'NEBOT JAIME': {
        'columnas': ['PSC6'],
        'partido': 'PSC',
        'nombre_completo': 'JAIME NEBOT SAADI'
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
    print("Cargando datos de segunda vuelta...")
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
    """Analiza una parroquia específica y retorna estadísticas detalladas por candidato"""
    if df_parroquia.empty:
        return None
    
    # Calcular totales generales
    votos_validos = int(df_parroquia[COL_VOTOS_VALIDOS].sum())
    votos_blancos = int(df_parroquia[COL_VOTOS_BLANCOS].sum())
    votos_nulos = int(df_parroquia[COL_VOTOS_NULOS].sum())
    total_votos = votos_validos + votos_blancos + votos_nulos
    
    # Calcular votos por candidato
    resultados_candidatos = []
    votos_candidatos_dict = {}
    
    for candidato, info in CANDIDATOS.items():
        votos_total = 0
        for columna in info['columnas']:
            if columna in df_parroquia.columns:
                votos = pd.to_numeric(df_parroquia[columna], errors='coerce').fillna(0).sum()
                votos_total += votos
        
        votos_total = int(votos_total)
        porcentaje = round((votos_total / votos_validos * 100) if votos_validos > 0 else 0, 2)
        
        resultados_candidatos.append({
            'Provincia': provincia,
            'Codigo_Parroquia': codigo_parroquia,
            'Parroquia': f'PARROQUIA_{codigo_parroquia}',
            'Candidato': candidato,
            'Partido': info['partido'],
            'Nombre_Completo': info['nombre_completo'],
            'Votos': votos_total,
            'Porcentaje': porcentaje
        })
        
        if votos_total > 0:
            votos_candidatos_dict[candidato] = {
                'partido': info['partido'],
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
        'candidatos': resultados_candidatos,
        'candidatos_dict': votos_candidatos_dict
    }


def main():
    """Función principal"""
    print("\n" + "="*80)
    print("ANÁLISIS DETALLADO - SEGUNDA VUELTA PRESIDENCIAL 1996")
    print("12 Parroquias de PASTAZA y 47 Parroquias de PICHINCHA (orden específico)")
    print("="*80 + "\n")
    
    # Cargar datos
    df = cargar_y_limpiar_datos()
    
    # Obtener parroquias seleccionadas
    parroquias_pastaza, parroquias_pichincha = obtener_parroquias_seleccionadas(df)
    
    print(f"\n✓ Parroquias de Pastaza seleccionadas: {len(parroquias_pastaza)}")
    print(f"✓ Parroquias de Pichincha seleccionadas: {len(parroquias_pichincha)}")
    
    # Preparar estructuras para resultados
    resultados_por_candidato = []  # Para Excel detallado
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
                'candidatos': resultado['candidatos_dict']
            }
            
            # Guardar detalle por candidato
            resultados_por_candidato.extend(resultado['candidatos'])
            
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
            
            # Mostrar en consola
            print(f"{i}. Parroquia {parroquia_cod}:")
            print(f"   Votos Válidos: {resultado['votos_validos']:,}")
            print(f"   Votos por candidato:")
            for cand in sorted(resultado['candidatos'], key=lambda x: x['Votos'], reverse=True):
                if cand['Votos'] > 0:
                    print(f"      {cand['Candidato']:20} ({cand['Partido']:10}): {cand['Votos']:>6,} votos ({cand['Porcentaje']:>5.2f}%)")
            print()
    
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
                'candidatos': resultado['candidatos_dict']
            }
            
            # Guardar detalle por candidato
            resultados_por_candidato.extend(resultado['candidatos'])
            
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
            
            # Mostrar en consola (solo primeras 5 para no saturar)
            if i <= 5:
                print(f"{i}. Parroquia {parroquia_cod}:")
                print(f"   Votos Válidos: {resultado['votos_validos']:,}")
                print(f"   Votos por candidato:")
                for cand in sorted(resultado['candidatos'], key=lambda x: x['Votos'], reverse=True):
                    if cand['Votos'] > 0:
                        print(f"      {cand['Candidato']:20} ({cand['Partido']:10}): {cand['Votos']:>6,} votos ({cand['Porcentaje']:>5.2f}%)")
                print()
    
    print(f"   ... (mostrando solo las primeras 5 de {len(parroquias_pichincha)} parroquias de Pichincha)")
    
    # ========== GUARDAR RESULTADOS ==========
    df_detallado = pd.DataFrame(resultados_por_candidato)
    df_resumen = pd.DataFrame(resultados_resumen)
    
    # Archivos de salida
    archivo_excel_detallado = os.path.join(DIR_RESULTADOS, 'Segunda_Vuelta_Votos_Por_Candidato.xlsx')
    archivo_json = os.path.join(DIR_RESULTADOS, 'segunda_vuelta_parroquias_1996.json')
    
    # Guardar Excel con múltiples hojas
    with pd.ExcelWriter(archivo_excel_detallado, engine='openpyxl') as writer:
        df_detallado.to_excel(writer, sheet_name='Detalle_Por_Candidato', index=False)
        df_resumen.to_excel(writer, sheet_name='Resumen_General', index=False)
        
        # Crear hoja de totales por candidato
        df_totales_candidato = df_detallado.groupby(['Candidato', 'Partido']).agg({
            'Votos': 'sum'
        }).reset_index().sort_values('Votos', ascending=False)
        df_totales_candidato.to_excel(writer, sheet_name='Totales_Por_Candidato', index=False)
    
    print(f"\n✓ Archivo Excel detallado guardado: {archivo_excel_detallado}")
    print(f"  - Hoja 'Detalle_Por_Candidato': Votos de cada candidato en cada parroquia")
    print(f"  - Hoja 'Resumen_General': Totales por parroquia")
    print(f"  - Hoja 'Totales_Por_Candidato': Suma total de votos por candidato")
    
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(resultados_json, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Archivo JSON guardado: {archivo_json}")
    
    # ========== RESUMEN FINAL ==========
    print("\n" + "="*80)
    print("RESUMEN GENERAL - SEGUNDA VUELTA")
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
    
    print(f"\nTOTALES POR CANDIDATO (en las {len(resultados_resumen)} parroquias):")
    print(f"{'─'*80}")
    for _, row in df_totales_candidato.iterrows():
        porcentaje = (row['Votos'] / total_votos_validos * 100) if total_votos_validos > 0 else 0
        print(f"  {row['Candidato']:20} ({row['Partido']:10}): {row['Votos']:>10,} votos ({porcentaje:>5.2f}%)")
    
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
