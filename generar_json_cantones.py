"""
Generador de archivos JSON agregados por CANTON
Formato específico para Presidentes (1ra y 2da vuelta) y Diputados Nacionales
Elecciones 1996
"""

import pandas as pd
import json
import os

# Configuración de archivos
ARCHIVO_PRESIDENTES_1V = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
ARCHIVO_PRESIDENTES_2V = 'Datos-Presidentes-Completos/Segunda Vuelta/1996 - Presidentes - segunda vuelta.xlsx'
ARCHIVO_DIPUTADOS = 'Datos-Diputados-Completos/1996 - Diputados - nacionales.xlsx'
ARCHIVO_NOMBRES_PARROQUIAS = 'parroquias-nombres.xlsx'

# Directorio de salida
DIR_JSON = 'JSON-Cantones'
os.makedirs(DIR_JSON, exist_ok=True)

# Mapeo de candidatos para PRESIDENTES PRIMERA VUELTA
CANDIDATOS_PRES_1V = {
    'DP5': 'RODRIGO PAZ DELGADO',
    'PSC6': 'JAIME NEBOT SAADI',
    'PRE10': 'ABDALÁ BUCARAM ORTIZ',
    'APRE13': 'FRANK VARGAS PAZZOS',
    'MPD15': 'JUAN JOSÉ CASTELLÓ MANZANO',
    'MUPP-NP18': 'FREDDY EHLERS ZURITA',
    'UCI19': 'JOSÉ GALLARDO ZAVALA',
    'MITI20': 'JACINTO VELÁZQUEZ ROSALES',
    'PLRE - FRA': 'RICARDO NOBOA BEJARANO'
}

# Mapeo de candidatos para PRESIDENTES SEGUNDA VUELTA
CANDIDATOS_PRES_2V = {
    'PRE10': 'ABDALÁ BUCARAM ORTIZ',
    'PSC6': 'JAIME NEBOT SAADI'
}


def cargar_mapeo_cantones():
    """Carga el mapeo de códigos de cantones a nombres y provincias"""
    df = pd.read_excel(ARCHIVO_NOMBRES_PARROQUIAS)
    df.columns = ['PROVINCIA', 'CODIGOPROV', 'CANTON', 'CODIGOCANT', 'PARROQUIA', 'CODIGO']
    
    # Crear diccionario: código cantón -> info completa
    canton_info = {}
    
    for _, row in df.iterrows():
        nombre_cant = str(row['CANTON']).strip() if pd.notna(row['CANTON']) else None
        codigo_cant = str(int(row['CODIGOCANT'])) if pd.notna(row['CODIGOCANT']) else None
        codigo_prov = str(int(row['CODIGOPROV'])) if pd.notna(row['CODIGOPROV']) else None
        nombre_prov = str(row['PROVINCIA']).strip() if pd.notna(row['PROVINCIA']) else None
        
        if nombre_cant and codigo_cant and codigo_prov and nombre_prov:
            # Usar código del cantón como clave (así viene en los datos originales)
            if codigo_cant not in canton_info:
                canton_info[codigo_cant] = {
                    'CODCAN': codigo_cant,
                    'CANTON': nombre_cant,
                    'CODPRO': codigo_prov,
                    'PROVINCIA': nombre_prov
                }
    
    return canton_info


def procesar_presidentes_primera_vuelta():
    """Procesa datos de presidentes primera vuelta agregados por cantón"""
    print("\n" + "="*80)
    print("PROCESANDO: PRESIDENTES - PRIMERA VUELTA (Por Cantón)")
    print("="*80)
    
    # Cargar mapeos de cantones
    canton_info = cargar_mapeo_cantones()
    
    df = pd.read_excel(ARCHIVO_PRESIDENTES_1V)
    
    # Limpiar datos y filtrar registros sin cantón
    df = df[df['CANTON'].notna()]  # Eliminar filas con cantón nulo
    # Convertir código de cantón a string (viene como float: 260.0, 265.0, etc.)
    df['CANTON'] = df['CANTON'].apply(lambda x: str(int(x)) if pd.notna(x) else None)
    df = df[df['CANTON'].notna()]  # Eliminar si quedó como None
    
    # También filtrar provincias nulas
    df = df[df['PROVINCI'].notna()]
    df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
    
    # Agrupar por código de cantón
    cantones = df.groupby('CANTON')
    
    resultados = []
    
    for codigo_canton, grupo in cantones:
        # Obtener información del cantón desde el mapeo usando el código
        info = canton_info.get(codigo_canton, {})
        cod_canton = info.get('CODCAN', codigo_canton)
        nombre_canton = info.get('CANTON', f'CANTON_{codigo_canton}')
        cod_provincia = info.get('CODPRO', 'N/A')
        nombre_provincia = info.get('PROVINCIA', grupo['PROVINCI'].iloc[0] if len(grupo) > 0 else 'N/A')
        
        # Sumar votos por cantón
        votos_validos = int(grupo['VOTOSVAL'].sum()) if 'VOTOSVAL' in grupo.columns else 0
        votos_blancos = int(grupo['VOTOSBLA'].sum()) if 'VOTOSBLA' in grupo.columns else 0
        votos_nulos = int(grupo['VOTOSNUL'].sum()) if 'VOTOSNUL' in grupo.columns else 0
        votos_total = votos_validos + votos_blancos + votos_nulos
        
        # Determinar ganador
        ganador_partido = None
        ganador_votos = 0
        ganador_candidato = None
        
        for partido, candidato in CANDIDATOS_PRES_1V.items():
            if partido in df.columns:
                votos = int(grupo[partido].sum())
                
                if votos > ganador_votos:
                    ganador_votos = votos
                    ganador_partido = partido
                    ganador_candidato = candidato
        
        # Crear estructura de resultados (solo ganador)
        resultados_canton = {}
        
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_canton[ganador_partido] = {
                'candidato': ganador_candidato,
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPRO': cod_provincia,
            'PROVINCIA': nombre_provincia,
            'CODCAN': cod_canton,
            'CANTON': nombre_canton,
            'votos_validos': votos_validos,
            'votos_blancos': votos_blancos,
            'votos_nulos': votos_nulos,
            'votos_total': votos_total,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_canton
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'presidentes_primera_vuelta.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesados {len(resultados)} cantones")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def procesar_presidentes_segunda_vuelta():
    """Procesa datos de presidentes segunda vuelta agregados por cantón"""
    print("\n" + "="*80)
    print("PROCESANDO: PRESIDENTES - SEGUNDA VUELTA (Por Cantón)")
    print("="*80)
    
    # Cargar mapeos de cantones
    canton_info = cargar_mapeo_cantones()
    
    df = pd.read_excel(ARCHIVO_PRESIDENTES_2V)
    
    # Limpiar datos y filtrar registros sin cantón
    df = df[df['CANTON'].notna()]  # Eliminar filas con cantón nulo
    # Convertir código de cantón a string (viene como float: 260.0, 265.0, etc.)
    df['CANTON'] = df['CANTON'].apply(lambda x: str(int(x)) if pd.notna(x) else None)
    df = df[df['CANTON'].notna()]  # Eliminar si quedó como None
    
    # También filtrar provincias nulas
    df = df[df['PROVINCI'].notna()]
    df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
    
    # Agrupar por código de cantón
    cantones = df.groupby('CANTON')
    
    resultados = []
    
    for codigo_canton, grupo in cantones:
        # Obtener información del cantón desde el mapeo usando el código
        info = canton_info.get(codigo_canton, {})
        cod_canton = info.get('CODCAN', codigo_canton)
        nombre_canton = info.get('CANTON', f'CANTON_{codigo_canton}')
        cod_provincia = info.get('CODPRO', 'N/A')
        nombre_provincia = info.get('PROVINCIA', grupo['PROVINCI'].iloc[0] if len(grupo) > 0 else 'N/A')
        
        # Sumar votos por cantón
        votos_validos = int(grupo['VOTOSVAL'].sum()) if 'VOTOSVAL' in grupo.columns else 0
        votos_blancos = int(grupo['VOTOSBLA'].sum()) if 'VOTOSBLA' in grupo.columns else 0
        votos_nulos = int(grupo['VOTOSNUL'].sum()) if 'VOTOSNUL' in grupo.columns else 0
        votos_total = votos_validos + votos_blancos + votos_nulos
        
        # Determinar ganador
        ganador_partido = None
        ganador_votos = 0
        ganador_candidato = None
        
        for partido, candidato in CANDIDATOS_PRES_2V.items():
            if partido in df.columns:
                votos = int(grupo[partido].sum())
                
                if votos > ganador_votos:
                    ganador_votos = votos
                    ganador_partido = partido
                    ganador_candidato = candidato
        
        # Crear estructura de resultados (solo ganador)
        resultados_canton = {}
        
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_canton[ganador_partido] = {
                'candidato': ganador_candidato,
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPRO': cod_provincia,
            'PROVINCIA': nombre_provincia,
            'CODCAN': cod_canton,
            'CANTON': nombre_canton,
            'votos_validos': votos_validos,
            'votos_blancos': votos_blancos,
            'votos_nulos': votos_nulos,
            'votos_total': votos_total,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_canton
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'presidentes_segunda_vuelta.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesados {len(resultados)} cantones")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def procesar_diputados_nacionales():
    """Procesa datos de diputados nacionales agregados por cantón"""
    print("\n" + "="*80)
    print("PROCESANDO: DIPUTADOS NACIONALES (Por Cantón)")
    print("="*80)
    
    # Cargar mapeos de cantones
    canton_info = cargar_mapeo_cantones()
    
    df = pd.read_excel(ARCHIVO_DIPUTADOS)
    
    # Limpiar datos y filtrar registros sin cantón
    df = df[df['CANTON'].notna()]  # Eliminar filas con cantón nulo
    # Convertir código de cantón a string (viene como float: 260.0, 265.0, etc.)
    df['CANTON'] = df['CANTON'].apply(lambda x: str(int(x)) if pd.notna(x) else None)
    df = df[df['CANTON'].notna()]  # Eliminar si quedó como None
    
    # También filtrar provincias nulas
    df = df[df['PROVINCI'].notna()]
    df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
    
    # Identificar columnas de partidos
    columnas_excluir = ['AÑO', 'DIGNIDAD', 'REGION', 'PROVINCI', 'CANTON', 'PARROQUIA', 
                        'JUNTAS', 'ELECTORES', 'VOTOSVAL', 'VOTOSNUL', 'VOTOSBLA', 
                        'VOTOSESC', 'ABSTENCI', 'ACTASVAL']
    
    columnas_partidos = [col for col in df.columns if col not in columnas_excluir]
    
    print(f"✓ Columnas de partidos identificadas: {len(columnas_partidos)}")
    
    # Agrupar por código de cantón
    cantones = df.groupby('CANTON')
    
    resultados = []
    
    for codigo_canton, grupo in cantones:
        # Obtener información del cantón desde el mapeo usando el código
        info = canton_info.get(codigo_canton, {})
        cod_canton = info.get('CODCAN', codigo_canton)
        nombre_canton = info.get('CANTON', f'CANTON_{codigo_canton}')
        cod_provincia = info.get('CODPRO', 'N/A')
        nombre_provincia = info.get('PROVINCIA', grupo['PROVINCI'].iloc[0] if len(grupo) > 0 else 'N/A')
        
        # Sumar votos por cantón
        votos_validos = int(grupo['VOTOSVAL'].sum()) if 'VOTOSVAL' in grupo.columns else 0
        votos_blancos = int(grupo['VOTOSBLA'].sum()) if 'VOTOSBLA' in grupo.columns else 0
        votos_nulos = int(grupo['VOTOSNUL'].sum()) if 'VOTOSNUL' in grupo.columns else 0
        votos_total = votos_validos + votos_blancos + votos_nulos
        
        # Determinar ganador
        ganador_partido = None
        ganador_votos = 0
        
        for partido in columnas_partidos:
            votos = int(grupo[partido].sum())
            
            if votos > ganador_votos:
                ganador_votos = votos
                ganador_partido = partido
        
        # Crear estructura de resultados (solo ganador)
        resultados_canton = {}
        
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_canton[ganador_partido] = {
                'candidato': ganador_partido,  # Para diputados usamos el nombre del partido
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPRO': cod_provincia,
            'PROVINCIA': nombre_provincia,
            'CODCAN': cod_canton,
            'CANTON': nombre_canton,
            'votos_validos': votos_validos,
            'votos_blancos': votos_blancos,
            'votos_nulos': votos_nulos,
            'votos_total': votos_total,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_canton
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'diputados_nacionales.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesados {len(resultados)} cantones")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def main():
    """Función principal"""
    print("\n" + "="*80)
    print("GENERADOR DE ARCHIVOS JSON - ELECCIONES 1996")
    print("Agregado por CANTONES de Ecuador")
    print("="*80)
    
    total_cantones = 0
    
    try:
        # Procesar Presidentes Primera Vuelta
        total_cantones += procesar_presidentes_primera_vuelta()
        
        # Procesar Presidentes Segunda Vuelta
        total_cantones += procesar_presidentes_segunda_vuelta()
        
        # Procesar Diputados Nacionales
        total_cantones += procesar_diputados_nacionales()
        
        # Resumen final
        print("\n" + "="*80)
        print("✓ GENERACIÓN COMPLETADA EXITOSAMENTE")
        print("="*80)
        print(f"\nArchivos generados en: {DIR_JSON}/")
        print(f"  1. presidentes_primera_vuelta.json")
        print(f"  2. presidentes_segunda_vuelta.json")
        print(f"  3. diputados_nacionales.json")
        print(f"\nTotal de registros procesados: {total_cantones}")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error durante la generación: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
