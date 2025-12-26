"""
Análisis de votos por provincia para presidentes - Segunda Vuelta
"""

import pandas as pd
import json
import os
from analisis.presidentes_segunda_vuelta import config
from analisis.presidentes_segunda_vuelta.data_loader import cargar_datos, filtrar_por_provincias

def analizar_provincias():
    """Analiza los votos por provincia para segunda vuelta presidencial"""
    
    print("=" * 80)
    print("ANÁLISIS POR PROVINCIAS - PRESIDENTES SEGUNDA VUELTA 1996")
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
        # En segunda vuelta, PROVINCI tiene nombres, no códigos
        df_prov = df_filtrado[df_filtrado[config.COL_PROVINCIA] == nombre_prov]
        
        if df_prov.empty:
            continue
        
        # Calcular votos por candidato
        votos_provincia = {}
        
        for candidato, info in config.CANDIDATOS.items():
            votos_total = 0
            for columna in info['columnas']:
                if columna in df_prov.columns:
                    votos = pd.to_numeric(df_prov[columna], errors='coerce').fillna(0).sum()
                    votos_total += votos
            
            if votos_total > 0:
                votos_provincia[candidato] = {
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
            'candidatos': votos_provincia
        }
        
        # Preparar para Excel
        for candidato, datos in votos_provincia.items():
            porcentaje = (datos['votos'] / total_votos_validos * 100) if total_votos_validos > 0 else 0
            resultados.append({
                'Provincia': nombre_prov,
                'Candidato': candidato,
                'Total_Votos': datos['votos'],
                'Porcentaje (%)': round(porcentaje, 2)
            })
    
    # Crear DataFrame de resultados
    df_resultados = pd.DataFrame(resultados)
    
    # Mostrar totales por provincia primero
    print()
    print("=" * 80)
    print("TOTALES DE VOTOS POR PROVINCIA")
    print("=" * 80)
    print()
    
    totales_provincias = []
    for nombre_prov, codigo_prov in config.PROVINCIAS_SELECCIONADAS.items():
        if codigo_prov in resultados_json:
            datos = resultados_json[codigo_prov]
            totales_provincias.append({
                'Provincia': nombre_prov,
                'Votos_Validos': datos['votos_validos'],
                'Votos_Blancos': datos['votos_blancos'],
                'Votos_Nulos': datos['votos_nulos'],
                'Total_Votos': datos['total_votos']
            })
    
    df_totales = pd.DataFrame(totales_provincias)
    print(df_totales.to_string(index=False))
    print()
    
    # Mostrar resultados por candidato
    print()
    print("=" * 80)
    print("VOTOS Y PORCENTAJE POR CANDIDATO Y PROVINCIA")
    print("=" * 80)
    print()
    print(df_resultados.to_string(index=False))
    print()
    
    # Guardar resultados
    archivo_excel = os.path.join(config.RESULTS_DIR, 'Votos_Por_Candidato_Y_Provincia_2daVuelta.xlsx')
    archivo_totales_excel = os.path.join(config.RESULTS_DIR, 'Totales_Por_Provincia_2daVuelta.xlsx')
    archivo_json = os.path.join(config.RESULTS_DIR, 'provincias_segunda_vuelta_1996.json')
    
    df_resultados.to_excel(archivo_excel, index=False)
    print(f"✓ Archivo Excel guardado: {archivo_excel}")
    
    if not df_totales.empty:
        df_totales.to_excel(archivo_totales_excel, index=False)
        print(f"✓ Archivo Excel de totales guardado: {archivo_totales_excel}")
    else:
        print(f"⚠ No se generaron totales por provincia")
    
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(resultados_json, f, ensure_ascii=False, indent=2)
    print(f"✓ Archivo JSON guardado: {archivo_json}")
    
    print("✓ Análisis de provincias completado")
    print()

if __name__ == "__main__":
    analizar_provincias()
