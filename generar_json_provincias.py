"""
Generador de archivos JSON agregados por PROVINCIA
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
DIR_JSON = 'JSON-Provincias'
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


def cargar_codigos_provincias():
    """Carga el mapeo de códigos a nombres de provincias (bidireccional)"""
    df = pd.read_excel(ARCHIVO_NOMBRES_PARROQUIAS)
    df.columns = ['PROVINCIA', 'CODIGOPROV', 'CANTON', 'CODIGOCANT', 'PARROQUIA', 'CODIGO']
    
    # Crear diccionarios bidireccionales
    codigo_a_nombre = {}
    nombre_a_codigo = {}
    
    for _, row in df.iterrows():
        codigo_prov = str(int(row['CODIGOPROV'])) if pd.notna(row['CODIGOPROV']) else None
        nombre_prov = str(row['PROVINCIA']).strip() if pd.notna(row['PROVINCIA']) else None
        
        if codigo_prov and nombre_prov:
            if codigo_prov not in codigo_a_nombre:
                codigo_a_nombre[codigo_prov] = nombre_prov
            if nombre_prov not in nombre_a_codigo:
                nombre_a_codigo[nombre_prov] = codigo_prov
    
    # Mapeo manual para provincias faltantes
    mapeo_manual = {
        'BOLÍVAR': '2',
        'GALÁPAGOS': '20',
        'LOS RÍOS': '12',
        'MANABÍ': '13',
        'SUCUMBÍOS': '21'
    }
    
    for nombre, codigo in mapeo_manual.items():
        if nombre not in nombre_a_codigo:
            nombre_a_codigo[nombre] = codigo
            codigo_a_nombre[codigo] = nombre
    
    return codigo_a_nombre, nombre_a_codigo



def procesar_presidentes_primera_vuelta():
    """Procesa datos de presidentes primera vuelta agregados por provincia"""
    print("\n" + "="*80)
    print("PROCESANDO: PRESIDENTES - PRIMERA VUELTA (Por Provincia)")
    print("="*80)
    
    # Cargar mapeos de provincias
    codigo_a_nombre, nombre_a_codigo = cargar_codigos_provincias()
    
    df = pd.read_excel(ARCHIVO_PRESIDENTES_1V)
    
    # Limpiar datos y filtrar registros sin provincia
    df = df[df['PROVINCI'].notna()]  # Eliminar filas con provincia nula
    df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
    df = df[df['PROVINCI'] != 'nan']  # Eliminar si quedó como string 'nan'
    
    # Agrupar por provincia
    provincias = df.groupby('PROVINCI')
    
    resultados = []
    
    for nombre_provincia, grupo in provincias:
        # Obtener código de la provincia
        cod_provincia = nombre_a_codigo.get(nombre_provincia, nombre_provincia)
        
        # Sumar votos por provincia
        votos_validos = int(grupo['VOTOSVAL'].sum()) if 'VOTOSVAL' in grupo.columns else 0
        votos_blancos = int(grupo['VOTOSBLA'].sum()) if 'VOTOSBLA' in grupo.columns else 0
        votos_nulos = int(grupo['VOTOSNUL'].sum()) if 'VOTOSNUL' in grupo.columns else 0
        votos_total = votos_validos + votos_blancos + votos_nulos
        
        # Determinar ganador
        ganador_partido = None
        ganador_votos = 0
        ganador_candidato = None
        
        votos_por_partido = {}
        
        for partido, candidato in CANDIDATOS_PRES_1V.items():
            if partido in df.columns:
                votos = int(grupo[partido].sum())
                votos_por_partido[partido] = votos
                
                if votos > ganador_votos:
                    ganador_votos = votos
                    ganador_partido = partido
                    ganador_candidato = candidato
        
        # Crear estructura de resultados (solo ganador)
        resultados_provincia = {}
        
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_provincia[ganador_partido] = {
                'candidato': ganador_candidato,
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPRO': cod_provincia,
            'PROVINCIA': nombre_provincia,
            'votos_validos': votos_validos,
            'votos_blancos': votos_blancos,
            'votos_nulos': votos_nulos,
            'votos_total': votos_total,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_provincia
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'presidentes_primera_vuelta.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesadas {len(resultados)} provincias")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def procesar_presidentes_segunda_vuelta():
    """Procesa datos de presidentes segunda vuelta agregados por provincia"""
    print("\n" + "="*80)
    print("PROCESANDO: PRESIDENTES - SEGUNDA VUELTA (Por Provincia)")
    print("="*80)
    
    # Cargar mapeos de provincias
    codigo_a_nombre, nombre_a_codigo = cargar_codigos_provincias()
    
    df = pd.read_excel(ARCHIVO_PRESIDENTES_2V)
    
    # Limpiar datos y filtrar registros sin provincia
    df = df[df['PROVINCI'].notna()]  # Eliminar filas con provincia nula
    df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
    df = df[df['PROVINCI'] != 'nan']  # Eliminar si quedó como string 'nan'
    
    # Agrupar por provincia
    provincias = df.groupby('PROVINCI')
    
    resultados = []
    
    for nombre_provincia, grupo in provincias:
        # Obtener código de la provincia
        cod_provincia = nombre_a_codigo.get(nombre_provincia, nombre_provincia)
        
        # Sumar votos por provincia
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
        resultados_provincia = {}
        
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_provincia[ganador_partido] = {
                'candidato': ganador_candidato,
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPRO': cod_provincia,
            'PROVINCIA': nombre_provincia,
            'votos_validos': votos_validos,
            'votos_blancos': votos_blancos,
            'votos_nulos': votos_nulos,
            'votos_total': votos_total,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_provincia
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'presidentes_segunda_vuelta.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesadas {len(resultados)} provincias")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def procesar_diputados_nacionales():
    """Procesa datos de diputados nacionales agregados por provincia"""
    print("\n" + "="*80)
    print("PROCESANDO: DIPUTADOS NACIONALES (Por Provincia)")
    print("="*80)
    
    # Cargar mapeos de provincias
    codigo_a_nombre, nombre_a_codigo = cargar_codigos_provincias()
    
    df = pd.read_excel(ARCHIVO_DIPUTADOS)
    
    # Limpiar datos y filtrar registros sin provincia
    df = df[df['PROVINCI'].notna()]  # Eliminar filas con provincia nula
    df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
    df = df[df['PROVINCI'] != 'nan']  # Eliminar si quedó como string 'nan'
    
    # Identificar columnas de partidos
    columnas_excluir = ['AÑO', 'DIGNIDAD', 'REGION', 'PROVINCI', 'CANTON', 'PARROQUIA', 
                        'JUNTAS', 'ELECTORES', 'VOTOSVAL', 'VOTOSNUL', 'VOTOSBLA', 
                        'VOTOSESC', 'ABSTENCI', 'ACTASVAL']
    
    columnas_partidos = [col for col in df.columns if col not in columnas_excluir]
    
    print(f"✓ Columnas de partidos identificadas: {len(columnas_partidos)}")
    
    # Agrupar por provincia
    provincias = df.groupby('PROVINCI')
    
    resultados = []
    
    for nombre_provincia, grupo in provincias:
        # Obtener código de la provincia
        cod_provincia = nombre_a_codigo.get(nombre_provincia, nombre_provincia)
        
        # Sumar votos por provincia
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
        resultados_provincia = {}
        
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_provincia[ganador_partido] = {
                'candidato': ganador_partido,  # Para diputados usamos el nombre del partido
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPRO': cod_provincia,
            'PROVINCIA': nombre_provincia,
            'votos_validos': votos_validos,
            'votos_blancos': votos_blancos,
            'votos_nulos': votos_nulos,
            'votos_total': votos_total,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_provincia
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'diputados_nacionales.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesadas {len(resultados)} provincias")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def main():
    """Función principal"""
    print("\n" + "="*80)
    print("GENERADOR DE ARCHIVOS JSON - ELECCIONES 1996")
    print("Agregado por PROVINCIAS de Ecuador")
    print("="*80)
    
    total_provincias = 0
    
    try:
        # Procesar Presidentes Primera Vuelta
        total_provincias += procesar_presidentes_primera_vuelta()
        
        # Procesar Presidentes Segunda Vuelta
        total_provincias += procesar_presidentes_segunda_vuelta()
        
        # Procesar Diputados Nacionales
        total_provincias += procesar_diputados_nacionales()
        
        # Resumen final
        print("\n" + "="*80)
        print("✓ GENERACIÓN COMPLETADA EXITOSAMENTE")
        print("="*80)
        print(f"\nArchivos generados en: {DIR_JSON}/")
        print(f"  1. presidentes_primera_vuelta.json")
        print(f"  2. presidentes_segunda_vuelta.json")
        print(f"  3. diputados_nacionales.json")
        print(f"\nTotal de registros procesados: {total_provincias}")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error durante la generación: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
