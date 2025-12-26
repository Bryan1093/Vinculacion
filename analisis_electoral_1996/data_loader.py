"""
Módulo para cargar y preparar datos electorales
"""

import pandas as pd
from . import config


def cargar_datos():
    """
    Carga el archivo Excel de datos electorales y realiza limpieza básica.
    
    Returns:
        pd.DataFrame: DataFrame con los datos electorales limpios
    """
    try:
        df = pd.read_excel(config.DATA_FILE)
        
        # Limpiar columnas de códigos geográficos
        df[config.COL_PROVINCIA] = df[config.COL_PROVINCIA].astype(str).str.strip()
        df[config.COL_CANTON] = df[config.COL_CANTON].astype(str).str.strip().str.replace('.0$', '', regex=True)
        df[config.COL_PARROQUIA] = df[config.COL_PARROQUIA].astype(str).str.strip().str.replace('.0$', '', regex=True)
        
        print(f"✓ Datos cargados exitosamente: {df.shape[0]} registros, {df.shape[1]} columnas")
        return df
        
    except FileNotFoundError:
        print(f"✗ Error: No se encontró el archivo {config.DATA_FILE}")
        raise
    except Exception as e:
        print(f"✗ Error al cargar datos: {str(e)}")
        raise


def filtrar_por_provincias(df, provincias):
    """
    Filtra el DataFrame por una lista de provincias.
    
    Args:
        df (pd.DataFrame): DataFrame original
        provincias (list): Lista de nombres de provincias
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    df_filtrado = df[df[config.COL_PROVINCIA].isin(provincias)].copy()
    print(f"✓ Filtrado por provincias: {len(df_filtrado)} registros")
    return df_filtrado


def filtrar_por_canton(df, provincia, cantones_dict):
    """
    Filtra el DataFrame por provincia y cantones específicos.
    
    Args:
        df (pd.DataFrame): DataFrame original
        provincia (str): Nombre de la provincia
        cantones_dict (dict): Diccionario de códigos de cantones
        
    Returns:
        pd.DataFrame: DataFrame filtrado con columna Canton_Nombre
    """
    # Filtrar por provincia
    df_filtrado = df[df[config.COL_PROVINCIA] == provincia].copy()
    
    # Filtrar por cantones
    codigos_cantones = list(cantones_dict.keys())
    df_filtrado = df_filtrado[df_filtrado[config.COL_CANTON].isin(codigos_cantones)].copy()
    
    # Agregar nombres de cantones
    df_filtrado['Canton_Nombre'] = df_filtrado[config.COL_CANTON].map(cantones_dict)
    
    print(f"✓ Filtrado por cantones de {provincia}: {len(df_filtrado)} registros")
    return df_filtrado


def filtrar_por_parroquia(df, provincia, parroquias_dict):
    """
    Filtra el DataFrame por provincia y parroquias específicas.
    
    Args:
        df (pd.DataFrame): DataFrame original
        provincia (str): Nombre de la provincia
        parroquias_dict (dict): Diccionario de códigos de parroquias
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    # Filtrar por provincia
    df_filtrado = df[df[config.COL_PROVINCIA] == provincia].copy()
    
    # Filtrar por parroquias
    codigos_parroquias = list(parroquias_dict.keys())
    df_filtrado = df_filtrado[df_filtrado[config.COL_PARROQUIA].isin(codigos_parroquias)].copy()
    
    print(f"✓ Filtrado por parroquias de {provincia}: {len(df_filtrado)} registros")
    return df_filtrado
