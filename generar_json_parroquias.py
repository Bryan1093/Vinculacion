import pandas as pd
import json
import os

# Configuración de archivos
ARCHIVO_PRESIDENTES_1V = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
ARCHIVO_PRESIDENTES_2V = 'Datos-Presidentes-Completos/Segunda Vuelta/1996 - Presidentes - segunda vuelta.xlsx'
ARCHIVO_DIPUTADOS = 'Datos-Diputados-Completos/1996 - Diputados - nacionales.xlsx'
ARCHIVO_NOMBRES_PARROQUIAS = 'parroquias-nombres.xlsx'

# Directorio de salida
DIR_JSON = 'JSON-Parroquias'
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


def cargar_nombres_parroquias():
    """Carga el mapeo de códigos a nombres de parroquias"""
    df = pd.read_excel(ARCHIVO_NOMBRES_PARROQUIAS)
    df.columns = ['PROVINCIA', 'COD_PROV', 'CANTON', 'COD_CANTON', 'PARROQUIA', 'COD_PARROQUIA']

    mapeo = {}
    for _, row in df.iterrows():
        codigo_parroquia = str(int(row['COD_PARROQUIA'])) if pd.notna(row['COD_PARROQUIA']) else None
        nombre_parroquia = str(row['PARROQUIA']).strip() if pd.notna(row['PARROQUIA']) else None
        provincia = str(row['PROVINCIA']).strip() if pd.notna(row['PROVINCIA']) else None
        
        if codigo_parroquia and nombre_parroquia and provincia:
            # Crear clave única: provincia + codigo
            clave = f"{provincia}_{codigo_parroquia}"
            if clave not in mapeo:
                mapeo[clave] = nombre_parroquia
            # También guardar solo por código para casos donde no tengamos provincia
            if codigo_parroquia not in mapeo:
                mapeo[codigo_parroquia] = nombre_parroquia
    
    return mapeo


def procesar_presidentes_primera_vuelta():
    """Procesa datos de presidentes primera vuelta y genera JSON"""
    print("\n" + "="*80)
    print("PROCESANDO: PRESIDENTES - PRIMERA VUELTA")
    print("="*80)
    
    # Cargar nombres de parroquias
    nombres_parroquias = cargar_nombres_parroquias()
    
    df = pd.read_excel(ARCHIVO_PRESIDENTES_1V)
    
    # Limpiar datos y filtrar registros inválidos
    df = df[df['PARROQUIA'].notna()]  # Eliminar nulos
    df['PARROQUIA'] = df['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    df = df[df['PARROQUIA'] != 'nan']  # Eliminar "nan" texto
    
    df['CANTON'] = df['CANTON'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    
    resultados = []
    
    # Procesar cada parroquia
    for idx, row in df.iterrows():
        cod_parroquia = str(row['PARROQUIA'])
        cod_canton = str(row['CANTON'])
        
        # Obtener nombre de la parroquia usando provincia + codigo
        provincia = str(row['PROVINCI']).strip() if pd.notna(row['PROVINCI']) else ''
        clave_unica = f"{provincia}_{cod_parroquia}"
        nombre_parroquia = nombres_parroquias.get(clave_unica, nombres_parroquias.get(cod_parroquia, f"PARROQUIA_{cod_parroquia}"))
        
        votos_validos = int(row['VOTOSVAL']) if pd.notna(row['VOTOSVAL']) else 0
        
        # Determinar ganador
        ganador_partido = None
        ganador_votos = 0
        ganador_candidato = None
        
        for partido, candidato in CANDIDATOS_PRES_1V.items():
            if partido in df.columns:
                votos = int(row[partido]) if pd.notna(row[partido]) else 0
                
                if votos > ganador_votos:
                    ganador_votos = votos
                    ganador_partido = partido
                    ganador_candidato = candidato
        
        # Crear estructura de resultados (solo VOTOS + ganador)
        resultados_parroquia = {}
        
        # Agregar solo el ganador
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_parroquia[ganador_partido] = {
                'candidato': ganador_candidato,
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPAR': cod_parroquia,
            'CODCAN': cod_canton,
            'PARROQUIA': nombre_parroquia,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_parroquia
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'presidentes_primera_vuelta.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesadas {len(resultados)} parroquias")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def procesar_presidentes_segunda_vuelta():
    """Procesa datos de presidentes segunda vuelta y genera JSON"""
    print("\n" + "="*80)
    print("PROCESANDO: PRESIDENTES - SEGUNDA VUELTA")
    print("="*80)
    
    # Cargar nombres de parroquias
    nombres_parroquias = cargar_nombres_parroquias()
    
    df = pd.read_excel(ARCHIVO_PRESIDENTES_2V)
    
    # Limpiar datos y filtrar registros inválidos
    df = df[df['PARROQUIA'].notna()]  # Eliminar nulos
    df['PARROQUIA'] = df['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    df = df[df['PARROQUIA'] != 'nan']  # Eliminar "nan" texto
    
    df['CANTON'] = df['CANTON'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    
    resultados = []
    
    # Procesar cada parroquia
    for idx, row in df.iterrows():
        cod_parroquia = str(row['PARROQUIA'])
        cod_canton = str(row['CANTON'])
        
        # Obtener nombre de la parroquia usando provincia + codigo
        provincia = str(row['PROVINCI']).strip() if pd.notna(row['PROVINCI']) else ''
        clave_unica = f"{provincia}_{cod_parroquia}"
        nombre_parroquia = nombres_parroquias.get(clave_unica, nombres_parroquias.get(cod_parroquia, f"PARROQUIA_{cod_parroquia}"))
        
        votos_validos = int(row['VOTOSVAL']) if pd.notna(row['VOTOSVAL']) else 0
        
        # Determinar ganador
        ganador_partido = None
        ganador_votos = 0
        ganador_candidato = None
        
        for partido, candidato in CANDIDATOS_PRES_2V.items():
            if partido in df.columns:
                votos = int(row[partido]) if pd.notna(row[partido]) else 0
                
                if votos > ganador_votos:
                    ganador_votos = votos
                    ganador_partido = partido
                    ganador_candidato = candidato
        
        # Crear estructura de resultados (solo VOTOS + ganador)
        resultados_parroquia = {}
        
        # Agregar solo el ganador
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_parroquia[ganador_partido] = {
                'candidato': ganador_candidato,
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPAR': cod_parroquia,
            'CODCAN': cod_canton,
            'PARROQUIA': nombre_parroquia,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_parroquia
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'presidentes_segunda_vuelta.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesadas {len(resultados)} parroquias")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def procesar_diputados_nacionales():
    """Procesa datos de diputados nacionales y genera JSON"""
    print("\n" + "="*80)
    print("PROCESANDO: DIPUTADOS NACIONALES")
    print("="*80)
    
    # Cargar nombres de parroquias
    nombres_parroquias = cargar_nombres_parroquias()
    
    df = pd.read_excel(ARCHIVO_DIPUTADOS)
    
    # Limpiar datos y filtrar registros inválidos
    df = df[df['PARROQUIA'].notna()]  # Eliminar nulos
    df['PARROQUIA'] = df['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    df = df[df['PARROQUIA'] != 'nan']  # Eliminar "nan" texto
    
    df['CANTON'] = df['CANTON'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    
    # Identificar columnas de partidos (excluir columnas de metadatos)
    columnas_excluir = ['AÑO', 'DIGNIDAD', 'REGION', 'PROVINCI', 'CANTON', 'PARROQUIA', 
                        'JUNTAS', 'ELECTORES', 'VOTOSVAL', 'VOTOSNUL', 'VOTOSBLA', 
                        'VOTOSESC', 'ABSTENCI', 'ACTASVAL']
    
    columnas_partidos = [col for col in df.columns if col not in columnas_excluir]
    
    print(f"✓ Columnas de partidos identificadas: {len(columnas_partidos)}")
    
    resultados = []
    
    # Procesar cada parroquia
    for idx, row in df.iterrows():
        cod_parroquia = str(row['PARROQUIA'])
        cod_canton = str(row['CANTON'])
        
        # Obtener nombre de la parroquia usando provincia + codigo
        provincia = str(row['PROVINCI']).strip() if pd.notna(row['PROVINCI']) else ''
        clave_unica = f"{provincia}_{cod_parroquia}"
        nombre_parroquia = nombres_parroquias.get(clave_unica, nombres_parroquias.get(cod_parroquia, f"PARROQUIA_{cod_parroquia}"))
        
        votos_validos = int(row['VOTOSVAL']) if pd.notna(row['VOTOSVAL']) else 0
        
        # Determinar ganador
        ganador_partido = None
        ganador_votos = 0
        
        for partido in columnas_partidos:
            votos = int(row[partido]) if pd.notna(row[partido]) else 0
            
            if votos > ganador_votos:
                ganador_votos = votos
                ganador_partido = partido
        
        # Crear estructura de resultados (solo ganador)
        resultados_parroquia = {}
        
        # Agregar solo el ganador
        if ganador_partido and ganador_votos > 0:
            porcentaje = round((ganador_votos / votos_validos * 100), 2) if votos_validos > 0 else 0.0
            resultados_parroquia[ganador_partido] = {
                'candidato': ganador_partido,  # Para diputados usamos el nombre del partido
                'votos': ganador_votos,
                'porcentaje': porcentaje
            }
        
        # Crear registro completo
        registro = {
            'CODPAR': cod_parroquia,
            'CODCAN': cod_canton,
            'PARROQUIA': nombre_parroquia,
            'ganador': ganador_partido if ganador_partido else 'N/A',
            'resultados': resultados_parroquia
        }
        
        resultados.append(registro)
    
    # Guardar JSON
    archivo_salida = os.path.join(DIR_JSON, 'diputados_nacionales.json')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Procesadas {len(resultados)} parroquias")
    print(f"✓ Archivo guardado: {archivo_salida}")
    
    return len(resultados)


def main():
    """Función principal"""
    print("\n" + "="*80)
    print("GENERADOR DE ARCHIVOS JSON - ELECCIONES 1996")
    print("Todas las parroquias de Ecuador")
    print("="*80)
    
    total_parroquias = 0
    
    try:
        # Procesar Presidentes Primera Vuelta
        total_parroquias += procesar_presidentes_primera_vuelta()
        
        # Procesar Presidentes Segunda Vuelta
        total_parroquias += procesar_presidentes_segunda_vuelta()
        
        # Procesar Diputados Nacionales
        total_parroquias += procesar_diputados_nacionales()
        
        # Resumen final
        print("\n" + "="*80)
        print("✓ GENERACIÓN COMPLETADA EXITOSAMENTE")
        print("="*80)
        print(f"\nArchivos generados en: {DIR_JSON}/")
        print(f"  1. presidentes_primera_vuelta.json")
        print(f"  2. presidentes_segunda_vuelta.json")
        print(f"  3. diputados_nacionales.json")
        print(f"\nTotal de registros procesados: {total_parroquias}")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error durante la generación: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
