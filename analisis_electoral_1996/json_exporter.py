"""
Módulo de exportación a formato JSON
Genera archivos JSON con estructura estandarizada para datos electorales
"""

import json
import os
from . import config
from .utils import obtener_ganador


def generar_json_provincia(df_original, df_resultados, provincia):
    """
    Genera estructura JSON para una provincia.
    
    Args:
        df_original (pd.DataFrame): DataFrame original con todos los datos
        df_resultados (pd.DataFrame): DataFrame con resultados por candidato
        provincia (str): Nombre de la provincia
        
    Returns:
        dict: Estructura JSON para la provincia
    """
    # Filtrar datos de la provincia
    df_prov = df_original[df_original[config.COL_PROVINCIA] == provincia]
    df_res_prov = df_resultados[df_resultados['Provincia'] == provincia]
    
    # Obtener código de provincia
    codigo_prov = config.PROVINCIAS_SELECCIONADAS.get(provincia, "00")
    
    # Calcular totales
    votos_validos = int(df_prov[config.COL_VOTOS_VALIDOS].sum())
    votos_blancos = int(df_prov[config.COL_VOTOS_BLANCOS].sum())
    votos_nulos = int(df_prov[config.COL_VOTOS_NULOS].sum())
    votos_total = votos_validos + votos_blancos + votos_nulos
    
    # Verificar que hay datos
    if len(df_res_prov) == 0:
        return {
            "CODPRO": codigo_prov,
            "PROVINCIA": provincia,
            "votos_validos": votos_validos,
            "votos_blancos": votos_blancos,
            "votos_nulos": votos_nulos,
            "votos_total": votos_total,
            "ganador": None,
            "resultados": {}
        }
    
    # Encontrar al ganador (candidato con más votos)
    fila_ganador = df_res_prov.loc[df_res_prov['Total_Votos'].idxmax()]
    candidato_nombre = fila_ganador['Candidato']
    candidato_info = config.CANDIDATOS.get(candidato_nombre, {})
    partido_ganador = candidato_info.get('partido', 'DESCONOCIDO')
    
    # Construir resultados solo con el ganador
    resultados = {
        partido_ganador: {
            "candidato": candidato_info.get('nombre_completo', candidato_nombre),
            "votos": int(fila_ganador['Total_Votos']),
            "porcentaje": float(fila_ganador['Porcentaje (%)'])
        }
    }
    
    # Estructura JSON
    return {
        "CODPRO": codigo_prov,
        "PROVINCIA": provincia,
        "votos_validos": votos_validos,
        "votos_blancos": votos_blancos,
        "votos_nulos": votos_nulos,
        "votos_total": votos_total,
        "ganador": partido_ganador,
        "resultados": resultados
    }


def generar_json_canton(df_original, df_resultados, canton):
    """
    Genera estructura JSON para un cantón.
    
    Args:
        df_original (pd.DataFrame): DataFrame original con todos los datos
        df_resultados (pd.DataFrame): DataFrame con resultados por candidato
        canton (str): Nombre del cantón
        
    Returns:
        dict: Estructura JSON para el cantón
    """
    # Filtrar datos del cantón
    df_cant = df_original[df_original['Canton_Nombre'] == canton]
    df_res_cant = df_resultados[df_resultados['Canton_Nombre'] == canton]
    
    # Obtener código de cantón
    codigo_canton = None
    for cod, nombre in config.CANTONES_PICHINCHA.items():
        if nombre == canton:
            codigo_canton = cod
            break
    
    # Obtener código de provincia del primer registro del cantón
    codigo_provincia = None
    if len(df_cant) > 0:
        nombre_provincia = str(df_cant[config.COL_PROVINCIA].iloc[0])
        codigo_provincia = config.CODIGOS_PROVINCIAS.get(nombre_provincia, nombre_provincia)
    
    # Calcular totales
    votos_validos = int(df_cant[config.COL_VOTOS_VALIDOS].sum())
    votos_blancos = int(df_cant[config.COL_VOTOS_BLANCOS].sum())
    votos_nulos = int(df_cant[config.COL_VOTOS_NULOS].sum())
    votos_total = votos_validos + votos_blancos + votos_nulos
    
    # Verificar que hay datos
    if len(df_res_cant) == 0:
        return {
            "CODCAN": codigo_canton,
            "CODPRO": codigo_provincia,
            "CANTON": canton,
            "votos_validos": votos_validos,
            "votos_blancos": votos_blancos,
            "votos_nulos": votos_nulos,
            "votos_total": votos_total,
            "ganador": None,
            "resultados": {}
        }
    
    # Encontrar al ganador (candidato con más votos)
    fila_ganador = df_res_cant.loc[df_res_cant['Total_Votos'].idxmax()]
    candidato_nombre = fila_ganador['Candidato']
    candidato_info = config.CANDIDATOS.get(candidato_nombre, {})
    partido_ganador = candidato_info.get('partido', 'DESCONOCIDO')
    
    # Construir resultados solo con el ganador
    resultados = {
        partido_ganador: {
            "candidato": candidato_info.get('nombre_completo', candidato_nombre),
            "votos": int(fila_ganador['Total_Votos']),
            "porcentaje": float(fila_ganador['Porcentaje (%)'])
        }
    }
    
    # Estructura JSON
    return {
        "CODCAN": codigo_canton,
        "CODPRO": codigo_provincia,
        "CANTON": canton,
        "votos_validos": votos_validos,
        "votos_blancos": votos_blancos,
        "votos_nulos": votos_nulos,
        "votos_total": votos_total,
        "ganador": partido_ganador,
        "resultados": resultados
    }


def generar_json_parroquia(df_original, df_resultados, parroquia_cod):
    """
    Genera estructura JSON para una parroquia.
    
    Args:
        df_original (pd.DataFrame): DataFrame original con todos los datos
        df_resultados (pd.DataFrame): DataFrame con resultados por candidato
        parroquia_cod (str): Código de la parroquia
        
    Returns:
        dict: Estructura JSON para la parroquia
    """
    # Filtrar datos de la parroquia
    df_parr = df_original[df_original[config.COL_PARROQUIA] == parroquia_cod]
    df_res_parr = df_resultados[df_resultados['PARROQUIA'] == parroquia_cod]
    
    # Obtener nombre de parroquia
    nombre_parroquia = config.PARROQUIAS_PASTAZA.get(parroquia_cod, f"PARROQUIA {parroquia_cod}")
    
    # Calcular totales
    votos_validos = int(df_parr[config.COL_VOTOS_VALIDOS].sum())
    votos_blancos = int(df_parr[config.COL_VOTOS_BLANCOS].sum())
    votos_nulos = int(df_parr[config.COL_VOTOS_NULOS].sum())
    votos_total = votos_validos + votos_blancos + votos_nulos
    
    # Verificar que hay datos
    if len(df_res_parr) == 0:
        return {
            "CODPARROQUIA": parroquia_cod,
            "PARROQUIA": nombre_parroquia,
            "votos_validos": votos_validos,
            "votos_blancos": votos_blancos,
            "votos_nulos": votos_nulos,
            "votos_total": votos_total,
            "ganador": None,
            "resultados": {}
        }
    
    # Encontrar al ganador (candidato con más votos)
    fila_ganador = df_res_parr.loc[df_res_parr['Total_Votos'].idxmax()]
    candidato_nombre = fila_ganador['Candidato']
    candidato_info = config.CANDIDATOS.get(candidato_nombre, {})
    partido_ganador = candidato_info.get('partido', 'DESCONOCIDO')
    
    # Construir resultados solo con el ganador
    resultados = {
        partido_ganador: {
            "candidato": candidato_info.get('nombre_completo', candidato_nombre),
            "votos": int(fila_ganador['Total_Votos']),
            "porcentaje": float(fila_ganador['Porcentaje (%)'])
        }
    }
    
    # Estructura JSON
    return {
        "CODPARROQUIA": parroquia_cod,
        "PARROQUIA": nombre_parroquia,
        "votos_validos": votos_validos,
        "votos_blancos": votos_blancos,
        "votos_nulos": votos_nulos,
        "votos_total": votos_total,
        "ganador": partido_ganador,
        "resultados": resultados
    }


def exportar_json(data, filename, output_dir=None):
    """
    Exporta datos a archivo JSON.
    
    Args:
        data (list or dict): Datos a exportar
        filename (str): Nombre del archivo (sin extensión)
        output_dir (str, optional): Directorio de salida
    """
    if output_dir is None:
        output_dir = config.RESULTS_DIR
    
    filepath = os.path.join(output_dir, f"{filename}.json")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Archivo JSON guardado: {filepath}")
