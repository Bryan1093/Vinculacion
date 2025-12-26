"""
Análisis electoral a nivel de parroquias
"""

import pandas as pd
from . import config
from .data_loader import cargar_datos, filtrar_por_parroquia
from .utils import calcular_porcentajes, validar_votos, exportar_excel, mostrar_resultados
from .json_exporter import generar_json_parroquia, exportar_json


def analizar_parroquias():
    """
    Realiza el análisis electoral a nivel de parroquias de Pastaza.
    Replica la funcionalidad de la sección de parroquias del notebook original.
    
    Returns:
        tuple: (df_resultados, df_original_filtrado)
    """
    print("\n" + "="*80)
    print("ANÁLISIS POR PARROQUIAS - PASTAZA - PRIMERA VUELTA 1996")
    print("="*80 + "\n")
    
    # Cargar datos
    df = cargar_datos()
    
    # Filtrar por provincia Pastaza y parroquias seleccionadas
    df_filtrado = filtrar_por_parroquia(df, 'PASTAZA', config.PARROQUIAS_PASTAZA)
    
    # Calcular votos por parroquia y candidato
    resultados = []
    
    for candidato, info in config.CANDIDATOS.items():
        columnas = info['columnas']
        
        # Agrupar por parroquia y sumar votos
        df_votos = df_filtrado.groupby(config.COL_PARROQUIA)[columnas].sum(numeric_only=True).sum(axis=1).reset_index()
        df_votos['Candidato'] = candidato
        df_votos.rename(columns={0: 'Total_Votos'}, inplace=True)
        resultados.append(df_votos)
    
    # Combinar todos los resultados
    df_resultados = pd.concat(resultados, ignore_index=True)
    
    # Calcular porcentajes
    df_resultados = calcular_porcentajes(df_resultados, config.COL_PARROQUIA)
    
    # Ordenar por parroquia según el orden especificado
    parroquias_orden = list(config.PARROQUIAS_PASTAZA.keys())
    df_resultados[config.COL_PARROQUIA] = pd.Categorical(
        df_resultados[config.COL_PARROQUIA], 
        categories=parroquias_orden, 
        ordered=True
    )
    df_resultados = df_resultados.sort_values(config.COL_PARROQUIA).reset_index(drop=True)
    
    # Mostrar resultados
    mostrar_resultados(df_resultados, "Votos y Porcentaje por Candidato y Parroquia")
    
    # Validar cálculos
    validar_votos(df_resultados, df_filtrado, config.COL_PARROQUIA, 'Parroquia')
    
    # Exportar a Excel
    exportar_excel(df_resultados, 'Votos_Por_Candidato_Y_Parroquia')
    
    # Exportar a JSON
    json_data = []
    for parroquia_cod in parroquias_orden:
        json_parroquia = generar_json_parroquia(df_filtrado, df_resultados, parroquia_cod)
        json_data.append(json_parroquia)
    
    exportar_json(json_data, 'parroquias_1996')
    
    print("\n✓ Análisis de parroquias completado\n")
    
    return df_resultados, df_filtrado
