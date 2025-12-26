"""
Módulo para cargar datos electorales de presidentes - Segunda Vuelta
"""

import pandas as pd
from analisis.presidentes_segunda_vuelta import config

def cargar_datos():
    """
    Carga el archivo de datos electorales de segunda vuelta
    
    Returns:
        pandas.DataFrame: DataFrame con los datos electorales
    """
    try:
        print(f"📂 Cargando datos desde: {config.DATA_FILE}")
        df = pd.read_excel(config.DATA_FILE)
        print(f"✓ Datos cargados exitosamente: {len(df)} registros, {len(df.columns)} columnas")
        return df
    except FileNotFoundError:
        print(f"✗ Error: No se encontró el archivo {config.DATA_FILE}")
        print(f"   Asegúrate de que el archivo existe en la ubicación correcta.")
        return None
    except Exception as e:
        print(f"✗ Error al cargar datos: {e}")
        return None

def filtrar_por_provincias(df, provincias=None):
    """
    Filtra el DataFrame por provincias específicas
    
    Args:
        df: DataFrame con los datos
        provincias: Lista de nombres de provincias (ej: ['NAPO', 'PASTAZA'])
                   Si es None, usa PROVINCIAS_SELECCIONADAS del config
    
    Returns:
        pandas.DataFrame: DataFrame filtrado
    """
    if provincias is None:
        # En segunda vuelta, PROVINCI tiene nombres, no códigos
        provincias = list(config.PROVINCIAS_SELECCIONADAS.keys())
    
    df_filtrado = df[df[config.COL_PROVINCIA].isin(provincias)].copy()
    print(f"✓ Filtrado por provincias: {len(df_filtrado)} registros")
    return df_filtrado

