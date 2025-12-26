"""
Análisis de votos por cantón para presidentes - Segunda Vuelta
"""

import pandas as pd
import json
import os
from analisis.presidentes_segunda_vuelta import config
from analisis.presidentes_segunda_vuelta.data_loader import cargar_datos

def analizar_cantones():
    """Analiza los votos por cantón de la provincia configurada"""
    
    print("=" * 80)
    print(f"ANÁLISIS POR CANTONES - {config.PROVINCIA_PARA_CANTONES} - PRESIDENTES SEGUNDA VUELTA 1996")
    print("=" * 80)
    print()
    
    # Cargar datos
    df = cargar_datos()
    if df is None:
        return
    
    # Filtrar por la provincia configurada (en segunda vuelta usa nombre, no código)
    df_provincia = df[df[config.COL_PROVINCIA] == config.PROVINCIA_PARA_CANTONES].copy()
    print(f"✓ Filtrado {config.PROVINCIA_PARA_CANTONES}: {len(df_provincia)} registros")
    print()
    
    # Preparar resultados
    resultados = []
    resultados_json = {}
    
    # Analizar cada cantón
    cantones_unicos = df_provincia[config.COL_CANTON].unique()
    
    for canton_cod in cantones_unicos:
        df_canton = df_provincia[df_provincia[config.COL_CANTON] == canton_cod]
        
        if df_canton.empty:
            continue
        
        # Obtener nombre del cantón
        nombre_canton = config.CANTONES_PICHINCHA.get(str(int(canton_cod)), f"CANTON_{int(canton_cod)}")
        
        # Calcular votos por candidato
        votos_canton = {}
        
        for candidato, info in config.CANDIDATOS.items():
            votos_total = 0
            for columna in info['columnas']:
                if columna in df_canton.columns:
                    votos = pd.to_numeric(df_canton[columna], errors='coerce').fillna(0).sum()
                    votos_total += votos
            
            if votos_total > 0:
                votos_canton[candidato] = {
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
            'candidatos': votos_canton
        }
        
        # Preparar para Excel
        for candidato, datos in votos_canton.items():
            porcentaje = (datos['votos'] / total_votos_validos * 100) if total_votos_validos > 0 else 0
            resultados.append({
                'Provincia': config.PROVINCIA_PARA_CANTONES,
                'Canton': nombre_canton,
                'Candidato': candidato,
                'Total_Votos': datos['votos'],
                'Porcentaje (%)': round(porcentaje, 2)
            })
    
    # Crear DataFrame de resultados
    df_resultados = pd.DataFrame(resultados)
    
    # Mostrar totales por cantón primero
    print()
    print("=" * 80)
    print("TOTALES DE VOTOS POR CANTÓN")
    print("=" * 80)
    print()
    
    totales_cantones = []
    for canton_cod in sorted(resultados_json.keys()):
        datos = resultados_json[canton_cod]
        totales_cantones.append({
            'Canton': datos['nombre'],
            'Votos_Validos': datos['votos_validos'],
            'Votos_Blancos': datos['votos_blancos'],
            'Votos_Nulos': datos['votos_nulos'],
            'Total_Votos': datos['total_votos']
        })
    
    df_totales = pd.DataFrame(totales_cantones)
    print(df_totales.to_string(index=False))
    print()
    
    # Mostrar resultados por candidato
    print()
    print("=" * 80)
    print("VOTOS Y PORCENTAJE POR CANDIDATO Y CANTÓN")
    print("=" * 80)
    print()
    if not df_resultados.empty:
        print(df_resultados.to_string(index=False))
    else:
        print(f"No se encontraron datos para cantones de {config.PROVINCIA_PARA_CANTONES}")
    print()
    
    # Guardar resultados
    archivo_excel = os.path.join(config.RESULTS_DIR, 'Votos_Por_Candidato_Y_Canton_2daVuelta.xlsx')
    archivo_totales_excel = os.path.join(config.RESULTS_DIR, 'Totales_Por_Canton_2daVuelta.xlsx')
    archivo_json = os.path.join(config.RESULTS_DIR, 'cantones_segunda_vuelta_1996.json')
    
    df_resultados.to_excel(archivo_excel, index=False)
    print(f"✓ Archivo Excel guardado: {archivo_excel}")
    
    if not df_totales.empty:
        df_totales.to_excel(archivo_totales_excel, index=False)
        print(f"✓ Archivo Excel de totales guardado: {archivo_totales_excel}")
    else:
        print(f"⚠ No se generaron totales por cantón")
    
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(resultados_json, f, ensure_ascii=False, indent=2)
    print(f"✓ Archivo JSON guardado: {archivo_json}")
    
    print("✓ Análisis de cantones completado")
    print()

if __name__ == "__main__":
    analizar_cantones()
