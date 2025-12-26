"""
Utilidades compartidas para análisis electoral
"""

import pandas as pd
import os
from . import config


def calcular_porcentajes(df, group_column):
    """
    Calcula porcentajes de votos por grupo.
    
    Args:
        df (pd.DataFrame): DataFrame con columnas [group_column, 'Candidato', 'Total_Votos']
        group_column (str): Nombre de la columna de agrupación
        
    Returns:
        pd.DataFrame: DataFrame con columna 'Porcentaje (%)' agregada
    """
    def _calcular(group):
        total = group['Total_Votos'].sum()
        group['Porcentaje (%)'] = (group['Total_Votos'] / total * 100).round(2)
        return group
    
    # Suprimir FutureWarning de pandas
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)
        return df.groupby(group_column, group_keys=False).apply(_calcular).reset_index(drop=True)


def validar_votos(df_resultados, df_original, group_column, nombre_nivel):
    """
    Valida que los votos calculados coincidan con los votos originales.
    
    Args:
        df_resultados (pd.DataFrame): DataFrame con resultados calculados
        df_original (pd.DataFrame): DataFrame original
        group_column (str): Columna de agrupación
        nombre_nivel (str): Nombre del nivel geográfico (para mensajes)
        
    Returns:
        bool: True si todos coinciden, False si hay diferencias
    """
    print(f"\n{'='*60}")
    print(f"VALIDACIÓN DE VOTOS - {nombre_nivel.upper()}")
    print(f"{'='*60}")
    
    # Obtener valores únicos del grupo
    grupos = df_resultados[group_column].unique()
    
    todo_correcto = True
    for grupo in grupos:
        # Total calculado
        total_calculado = df_resultados[df_resultados[group_column] == grupo]['Total_Votos'].sum()
        
        # Total real del dataset
        total_real = df_original[df_original[group_column] == grupo][config.COL_VOTOS_VALIDOS].sum()
        
        coincide = abs(total_calculado - total_real) < 1
        simbolo = "✅" if coincide else "⚠️"
        
        print(f"\n{nombre_nivel}: {grupo}")
        print(f"  Total calculado: {int(total_calculado):,}")
        print(f"  Total real:      {int(total_real):,}")
        print(f"  {simbolo} {'¡Coinciden!' if coincide else '¡NO COINCIDEN!'}")
        
        if not coincide:
            todo_correcto = False
    
    print(f"\n{'='*60}\n")
    return todo_correcto


def exportar_excel(df, filename, output_dir=None):
    """
    Exporta DataFrame a archivo Excel.
    
    Args:
        df (pd.DataFrame): DataFrame a exportar
        filename (str): Nombre del archivo (sin extensión)
        output_dir (str, optional): Directorio de salida. Por defecto usa config.RESULTS_DIR
    """
    if output_dir is None:
        output_dir = config.RESULTS_DIR
    
    filepath = os.path.join(output_dir, f"{filename}.xlsx")
    df.to_excel(filepath, index=False)
    print(f"✓ Archivo Excel guardado: {filepath}")


def mostrar_resultados(df, titulo, max_rows=None):
    """
    Muestra resultados en consola de forma formateada.
    
    Args:
        df (pd.DataFrame): DataFrame a mostrar
        titulo (str): Título de la tabla
        max_rows (int, optional): Número máximo de filas a mostrar
    """
    print(f"\n{'='*80}")
    print(f"{titulo.upper()}")
    print(f"{'='*80}\n")
    
    if max_rows:
        print(df.head(max_rows).to_string(index=False))
        if len(df) > max_rows:
            print(f"\n... y {len(df) - max_rows} filas más")
    else:
        print(df.to_string(index=False))
    
    print(f"\n{'='*80}\n")


def obtener_ganador(resultados_dict):
    """
    Determina el ganador basado en el mayor número de votos.
    
    Args:
        resultados_dict (dict): Diccionario con resultados por partido
        
    Returns:
        str: Siglas del partido ganador
    """
    max_votos = 0
    ganador = None
    
    for partido, datos in resultados_dict.items():
        if datos['votos'] > max_votos:
            max_votos = datos['votos']
            ganador = partido
    
    return ganador
