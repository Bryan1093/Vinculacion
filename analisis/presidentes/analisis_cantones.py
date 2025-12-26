"""
Análisis electoral a nivel de cantones
"""

import pandas as pd
from . import config
from .data_loader import cargar_datos, filtrar_por_canton
from .utils import calcular_porcentajes, validar_votos, exportar_excel, mostrar_resultados
from .json_exporter import generar_json_canton, exportar_json


def analizar_cantones():
    """
    Realiza el análisis electoral a nivel de cantones de Guayas.
    Replica la funcionalidad de la sección de cantones del notebook original.
    
    Returns:
        tuple: (df_resultados, df_original_filtrado)
    """
    print("\n" + "="*80)
    print("ANÁLISIS POR CANTONES - PICHINCHA - PRIMERA VUELTA 1996")
    print("="*80 + "\n")
    
    # Cargar datos
    df = cargar_datos()
    
    # Filtrar por provincia Pichincha y cantones seleccionados
    df_filtrado = filtrar_por_canton(df, 'PICHINCHA', config.CANTONES_PICHINCHA)
    
    # Calcular votos por cantón y candidato
    resultados = []
    
    for candidato, info in config.CANDIDATOS.items():
        columnas = info['columnas']
        
        # Agrupar por cantón y sumar votos
        df_votos = df_filtrado.groupby('Canton_Nombre')[columnas].sum(numeric_only=True).sum(axis=1).reset_index()
        df_votos['Candidato'] = candidato
        df_votos.rename(columns={0: 'Total_Votos'}, inplace=True)
        resultados.append(df_votos)
    
    # Combinar todos los resultados
    df_resultados = pd.concat(resultados, ignore_index=True)
    
    # Reordenar columnas
    df_resultados = df_resultados[['Canton_Nombre', 'Candidato', 'Total_Votos']]
    
    # Calcular porcentajes
    df_resultados = calcular_porcentajes(df_resultados, 'Canton_Nombre')
    
    # Aplicar orden personalizado de cantones
    orden_cantones = [
        'QUITO',
        'CAYAMBE',
        'MEJIA',
        'PEDRO MONCAYO',
        'RUMIÑAHUI',
        'SANTO DOMINGO',
        'SAN MIGUEL DE LOS BANCOS',
        'PEDRO VICENTE MALDONADO'
    ]
    
    # Ordenar el DataFrame: primero por Candidato, luego por Canton en orden personalizado
    df_resultados['Canton_Nombre'] = pd.Categorical(
        df_resultados['Canton_Nombre'],
        categories=orden_cantones,
        ordered=True
    )
    df_resultados = df_resultados.sort_values(['Candidato', 'Canton_Nombre']).reset_index(drop=True)
    
    # Calcular totales por cantón (votos válidos, blancos, nulos, total)
    # Definir orden personalizado de cantones
    orden_cantones = [
        'QUITO',
        'CAYAMBE',
        'MEJIA',
        'PEDRO MONCAYO',
        'RUMIÑAHUI',
        'SANTO DOMINGO',
        'SAN MIGUEL DE LOS BANCOS',
        'PEDRO VICENTE MALDONADO'
    ]
    
    totales_canton = []
    for canton in orden_cantones:
        df_cant = df_filtrado[df_filtrado['Canton_Nombre'] == canton]
        if len(df_cant) > 0:  # Solo agregar si el cantón existe en los datos
            totales_canton.append({
                'Canton': canton,
                'Votos_Validos': int(df_cant[config.COL_VOTOS_VALIDOS].sum()),
                'Votos_Blancos': int(df_cant[config.COL_VOTOS_BLANCOS].sum()),
                'Votos_Nulos': int(df_cant[config.COL_VOTOS_NULOS].sum()),
                'Total_Votos': int(df_cant[config.COL_VOTOS_VALIDOS].sum() + 
                                  df_cant[config.COL_VOTOS_BLANCOS].sum() + 
                                  df_cant[config.COL_VOTOS_NULOS].sum())
            })
    
    df_totales = pd.DataFrame(totales_canton)
    
    # Mostrar totales por cantón
    print("\n" + "="*80)
    print("TOTALES DE VOTOS POR CANTÓN")
    print("="*80 + "\n")
    print(df_totales.to_string(index=False))
    print("\n" + "="*80 + "\n")
    
    # Mostrar resultados por candidato (primeras 20 filas)
    mostrar_resultados(df_resultados, "Votos y Porcentaje por Candidato y Cantón", max_rows=20)
    
    # Validar cálculos
    validar_votos(df_resultados, df_filtrado, 'Canton_Nombre', 'Cantón')
    
    # Exportar resultados por candidato a Excel
    exportar_excel(df_resultados, 'Votos_Por_Candidato_Y_Canton')
    
    # Exportar totales por cantón a Excel
    exportar_excel(df_totales, 'Totales_Por_Canton')
    
    # Exportar a JSON
    json_data = []
    cantones = df_resultados['Canton_Nombre'].unique()
    for canton in cantones:
        json_canton = generar_json_canton(df_filtrado, df_resultados, canton)
        json_data.append(json_canton)
    
    exportar_json(json_data, 'cantones_1996')
    
    print("\n✓ Análisis de cantones completado\n")
    
    return df_resultados, df_filtrado
