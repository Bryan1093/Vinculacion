"""
Análisis de votos por provincia para diputados nacionales
"""

import pandas as pd
import json
import os
from analisis.diputados import config
from analisis.diputados.data_loader import cargar_datos, filtrar_por_provincias

def analizar_provincias():
    """Analiza los votos por provincia para diputados nacionales"""
    
    print("=" * 80)
    print("ANÁLISIS POR PROVINCIAS - DIPUTADOS NACIONALES 1996")
    print("=" * 80)
    print()
    
    # Cargar datos
    df = cargar_datos()
    if df is None:
        return
    
    # Filtrar por provincias seleccionadas
    df_filtrado = filtrar_por_provincias(df)
    
    # Preparar resultados
    resultados = []
    resultados_json = {}
    
    # Analizar cada provincia
    for nombre_prov, codigo_prov in config.PROVINCIAS_SELECCIONADAS.items():
        # Filtrar por nombre de provincia (no por código)
        df_prov = df_filtrado[df_filtrado[config.COL_PROVINCIA] == nombre_prov]
        
        if df_prov.empty:
            continue
        
        # Calcular votos por partido
        votos_provincia = {}
        
        for partido, info in config.PARTIDOS.items():
            votos_total = 0
            for columna in info['columnas']:
                if columna in df_prov.columns:
                    votos = pd.to_numeric(df_prov[columna], errors='coerce').fillna(0).sum()
                    votos_total += votos
            
            if votos_total > 0:
                votos_provincia[partido] = {
                    'votos': int(votos_total),
                    'nombre_completo': info['nombre_completo']
                }
        
        # Calcular totales
        total_votos_validos = df_prov[config.COL_VOTOS_VALIDOS].sum()
        total_votos_blancos = df_prov[config.COL_VOTOS_BLANCOS].sum()
        total_votos_nulos = df_prov[config.COL_VOTOS_NULOS].sum()
        total_votos = total_votos_validos + total_votos_blancos + total_votos_nulos
        
        # Guardar en JSON
        resultados_json[codigo_prov] = {
            'nombre': nombre_prov,
            'votos_validos': int(total_votos_validos),
            'votos_blancos': int(total_votos_blancos),
            'votos_nulos': int(total_votos_nulos),
            'total_votos': int(total_votos),
            'partidos': votos_provincia
        }
        
        # Preparar para Excel - Votos por partido
        for partido, datos in votos_provincia.items():
            porcentaje = (datos['votos'] / total_votos_validos * 100) if total_votos_validos > 0 else 0
            resultados.append({
                'Provincia': nombre_prov,
                'Partido': partido,
                'Total_Votos': datos['votos'],
                'Porcentaje (%)': round(porcentaje, 2)
            })
        
        # Agregar filas de totales para esta provincia
        resultados.append({
            'Provincia': nombre_prov,
            'Partido': '--- TOTALES ---',
            'Total_Votos': '',
            'Porcentaje (%)': ''
        })
        resultados.append({
            'Provincia': nombre_prov,
            'Partido': 'Votos Válidos',
            'Total_Votos': int(total_votos_validos),
            'Porcentaje (%)': round((total_votos_validos / total_votos * 100) if total_votos > 0 else 0, 2)
        })
        resultados.append({
            'Provincia': nombre_prov,
            'Partido': 'Votos Blancos',
            'Total_Votos': int(total_votos_blancos),
            'Porcentaje (%)': round((total_votos_blancos / total_votos * 100) if total_votos > 0 else 0, 2)
        })
        resultados.append({
            'Provincia': nombre_prov,
            'Partido': 'Votos Nulos',
            'Total_Votos': int(total_votos_nulos),
            'Porcentaje (%)': round((total_votos_nulos / total_votos * 100) if total_votos > 0 else 0, 2)
        })
        resultados.append({
            'Provincia': nombre_prov,
            'Partido': 'TOTAL VOTOS',
            'Total_Votos': int(total_votos),
            'Porcentaje (%)': 100.0
        })
        resultados.append({
            'Provincia': '',
            'Partido': '',
            'Total_Votos': '',
            'Porcentaje (%)': ''
        })
    
    # Crear DataFrame de resultados
    df_resultados = pd.DataFrame(resultados)
    
    # Mostrar resultados en consola
    print()
    print("=" * 80)
    print("VOTOS Y PORCENTAJE POR PARTIDO Y PROVINCIA")
    print("=" * 80)
    print()
    print(df_resultados.to_string(index=False))
    print()
    
    # Guardar resultados
    archivo_excel = os.path.join(config.RESULTS_DIR, 'Votos_Por_Partido_Y_Provincia.xlsx')
    archivo_json = os.path.join(config.RESULTS_DIR, 'provincias_diputados_1996.json')
    
    df_resultados.to_excel(archivo_excel, index=False)
    print(f"✓ Archivo Excel guardado: {archivo_excel}")
    
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(resultados_json, f, ensure_ascii=False, indent=2)
    print(f"✓ Archivo JSON guardado: {archivo_json}")
    
    print("✓ Análisis de provincias completado")
    print()

if __name__ == "__main__":
    analizar_provincias()
