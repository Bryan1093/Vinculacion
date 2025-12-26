"""
Análisis de votos por cantón para diputados nacionales
"""

import pandas as pd
import json
import os
from analisis.diputados import config
from analisis.diputados.data_loader import cargar_datos

def analizar_cantones():
    """Analiza los votos por cantón (enfocado en Pichincha)"""
    
    print("=" * 80)
    print("ANÁLISIS POR CANTONES - PICHINCHA - DIPUTADOS NACIONALES 1996")
    print("=" * 80)
    print()
    
    # Cargar datos
    df = cargar_datos()
    if df is None:
        return
    
    # Filtrar solo Pichincha (por nombre, no por código)
    df_pichincha = df[df[config.COL_PROVINCIA] == 'PICHINCHA'].copy()
    print(f"✓ Filtrado Pichincha: {len(df_pichincha)} registros")
    print()
    
    # Preparar resultados
    resultados = []
    resultados_json = {}
    
    # Analizar cada cantón
    cantones_unicos = df_pichincha[config.COL_CANTON].unique()
    
    for canton_cod in cantones_unicos:
        df_canton = df_pichincha[df_pichincha[config.COL_CANTON] == canton_cod]
        
        if df_canton.empty:
            continue
        
        # Obtener nombre del cantón
        nombre_canton = config.CANTONES_PICHINCHA.get(str(int(canton_cod)), f"CANTON_{int(canton_cod)}")
        
        # Calcular votos por partido
        votos_canton = {}
        
        for partido, info in config.PARTIDOS.items():
            votos_total = 0
            for columna in info['columnas']:
                if columna in df_canton.columns:
                    votos = pd.to_numeric(df_canton[columna], errors='coerce').fillna(0).sum()
                    votos_total += votos
            
            if votos_total > 0:
                votos_canton[partido] = {
                    'votos': int(votos_total),
                    'nombre_completo': info['nombre_completo']
                }
        
        # Calcular totales
        total_votos_validos = df_canton[config.COL_VOTOS_VALIDOS].sum()
        total_votos_blancos = df_canton[config.COL_VOTOS_BLANCOS].sum()
        total_votos_nulos = df_canton[config.COL_VOTOS_NULOS].sum()
        total_votos = total_votos_validos + total_votos_blancos + total_votos_nulos
        
        # Guardar en JSON
        resultados_json[str(int(canton_cod))] = {
            'nombre': nombre_canton,
            'votos_validos': int(total_votos_validos),
            'votos_blancos': int(total_votos_blancos),
            'votos_nulos': int(total_votos_nulos),
            'total_votos': int(total_votos),
            'partidos': votos_canton
        }
        
        # Preparar para Excel
        for partido, datos in votos_canton.items():
            porcentaje = (datos['votos'] / total_votos_validos * 100) if total_votos_validos > 0 else 0
            resultados.append({
                'Provincia': 'PICHINCHA',
                'Canton': nombre_canton,
                'Partido': partido,
                'Total_Votos': datos['votos'],
                'Porcentaje (%)': round(porcentaje, 2)
            })
    
    # Crear DataFrame de resultados
    df_resultados = pd.DataFrame(resultados)
    
    # Mostrar resultados en consola
    print()
    print("=" * 80)
    print("VOTOS Y PORCENTAJE POR PARTIDO Y CANTÓN")
    print("=" * 80)
    print()
    if not df_resultados.empty:
        print(df_resultados.to_string(index=False))
    else:
        print("No se encontraron datos para cantones de Pichincha")
    print()
    
    # Guardar resultados
    archivo_excel = os.path.join(config.RESULTS_DIR, 'Votos_Por_Partido_Y_Canton.xlsx')
    archivo_json = os.path.join(config.RESULTS_DIR, 'cantones_diputados_1996.json')
    
    df_resultados.to_excel(archivo_excel, index=False)
    print(f"✓ Archivo Excel guardado: {archivo_excel}")
    
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(resultados_json, f, ensure_ascii=False, indent=2)
    print(f"✓ Archivo JSON guardado: {archivo_json}")
    
    print("✓ Análisis de cantones completado")
    print()

if __name__ == "__main__":
    analizar_cantones()
