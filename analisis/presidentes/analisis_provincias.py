"""
Análisis electoral a nivel de provincias
"""

import pandas as pd
import json
import os
from analisis.presidentes import config
from analisis.presidentes.data_loader import cargar_datos, filtrar_por_provincias


def analizar_provincias():
    """
    Realiza el análisis electoral a nivel de provincias.
    """
    print("\n" + "="*80)
    print("ANÁLISIS POR PROVINCIAS - PRIMERA VUELTA 1996")
    print("="*80 + "\n")
    
    # Cargar datos
    df = cargar_datos()
    
    # Filtrar por las provincias seleccionadas
    provincias = list(config.PROVINCIAS_SELECCIONADAS.keys())
    df_filtrado = filtrar_por_provincias(df, provincias)
    
    # Renombrar columna para claridad
    df_filtrado = df_filtrado.copy()
    df_filtrado['Provincia'] = df_filtrado[config.COL_PROVINCIA]
    
    # Calcular votos por provincia y candidato
    resultados = []
    
    for candidato, info in config.CANDIDATOS.items():
        columnas = info['columnas']
        
        # Agrupar por provincia y sumar votos
        df_votos = df_filtrado.groupby('Provincia')[columnas].sum(numeric_only=True).sum(axis=1).reset_index()
        df_votos['Candidato'] = candidato
        df_votos.rename(columns={0: 'Total_Votos'}, inplace=True)
        resultados.append(df_votos)
    
    # Combinar todos los resultados
    df_resultados = pd.concat(resultados, ignore_index=True)
    
    # Reordenar columnas
    df_resultados = df_resultados[['Provincia', 'Candidato', 'Total_Votos']]
    
    # Calcular porcentajes
    total_por_provincia = df_resultados.groupby('Provincia')['Total_Votos'].transform('sum')
    df_resultados['Porcentaje (%)'] = (df_resultados['Total_Votos'] / total_por_provincia * 100).round(2)
    
    # Mostrar resultados
    print("\n" + "="*80)
    print("VOTOS Y PORCENTAJE POR CANDIDATO Y PROVINCIA")
    print("="*80 + "\n")
    print(df_resultados.to_string(index=False))
    print()
    
    # Exportar a Excel
    archivo_excel = os.path.join(config.RESULTS_DIR, 'Votos_Por_Candidato_Y_Provincia.xlsx')
    df_resultados.to_excel(archivo_excel, index=False)
    print(f"✓ Archivo Excel guardado: {archivo_excel}")
    
    # Exportar a JSON
    json_data = {}
    for provincia in provincias:
        codigo_prov = config.PROVINCIAS_SELECCIONADAS[provincia]
        df_prov = df_resultados[df_resultados['Provincia'] == provincia]
        
        json_data[codigo_prov] = {
            'nombre': provincia,
            'candidatos': {}
        }
        
        for _, row in df_prov.iterrows():
            json_data[codigo_prov]['candidatos'][row['Candidato']] = {
                'votos': int(row['Total_Votos']),
                'porcentaje': float(row['Porcentaje (%)'])
            }
    
    archivo_json = os.path.join(config.RESULTS_DIR, 'provincias_1996.json')
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print(f"✓ Archivo JSON guardado: {archivo_json}")
    
    print("\n✓ Análisis de provincias completado\n")
    
    return df_resultados, df_filtrado
