"""
Análisis electoral a nivel de provincias
"""

import pandas as pd
from . import config
from .data_loader import cargar_datos, filtrar_por_provincias
from .utils import calcular_porcentajes, validar_votos, exportar_excel, mostrar_resultados
from .json_exporter import generar_json_provincia, exportar_json


def analizar_provincias():
    """
    Realiza el análisis electoral a nivel de provincias.
    Replica la funcionalidad de las celdas 4-6 del notebook original.
    
    Returns:
        tuple: (df_resultados, df_original_filtrado)
    """
    print("\n" + "="*80)
    print("ANÁLISIS POR PROVINCIAS - PRIMERA VUELTA 1996")
    print("="*80 + "\n")
    
    # Cargar datos
    df = cargar_datos()
    
    # Filtrar por las 3 provincias seleccionadas
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
    df_resultados = calcular_porcentajes(df_resultados, 'Provincia')
    
    # Mostrar resultados
    mostrar_resultados(df_resultados, "Votos y Porcentaje por Candidato y Provincia")
    
    # Validar cálculos
    validar_votos(df_resultados, df_filtrado, 'Provincia', 'Provincia')
    
    # Exportar a Excel
    exportar_excel(df_resultados, 'Votos_Por_Candidato_Y_Provincia')
    
    # Exportar a JSON
    json_data = []
    for provincia in provincias:
        json_prov = generar_json_provincia(df_filtrado, df_resultados, provincia)
        json_data.append(json_prov)
    
    exportar_json(json_data, 'provincias_1996')
    
    print("\n✓ Análisis de provincias completado\n")
    
    return df_resultados, df_filtrado
