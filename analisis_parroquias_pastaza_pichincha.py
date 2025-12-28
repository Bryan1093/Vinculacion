"""
Análisis de votos por parroquia - Últimas 12 de Pastaza y Primeras 47 de Pichincha
Primera Vuelta Presidencial 1996
"""

import pandas as pd
import json
import os

# Configuración
ARCHIVO_DATOS = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
DIR_RESULTADOS = 'resultados'

# Asegurar que existe el directorio de resultados
os.makedirs(DIR_RESULTADOS, exist_ok=True)

# Candidatos y sus columnas
CANDIDATOS = {
    'NOBOA RICARDO': {
        'columnas': ['PLRE - FRA'],
        'partido': 'PLRE-FRA',
        'nombre_completo': 'RICARDO NOBOA BEJARANO'
    },
    'PAZ RODRIGO': {
        'columnas': ['DP5'],
        'partido': 'DP',
        'nombre_completo': 'RODRIGO PAZ DELGADO'
    },
    'NEBOT JAIME': {
        'columnas': ['PSC6'],
        'partido': 'PSC',
        'nombre_completo': 'JAIME NEBOT SAADI'
    },
    'BUCARAM ABDALÁ': {
        'columnas': ['PRE10'],
        'partido': 'PRE',
        'nombre_completo': 'ABDALÁ BUCARAM ORTIZ'
    },
    'VARGAS FRANK': {
        'columnas': ['APRE13'],
        'partido': 'APRE',
        'nombre_completo': 'FRANK VARGAS PAZZOS'
    },
    'CASTELLÓ JUAN': {
        'columnas': ['MPD15'],
        'partido': 'MPD',
        'nombre_completo': 'JUAN JOSÉ CASTELLÓ MANZANO'
    },
    'EHLEARS FREDDY': {
        'columnas': ['MUPP-NP18'],
        'partido': 'MUPP-NP',
        'nombre_completo': 'FREDDY EHLERS ZURITA'
    },
    'GALLARDO JOSÉ': {
        'columnas': ['UCI19'],
        'partido': 'UCI',
        'nombre_completo': 'JOSÉ GALLARDO ZAVALA'
    },
    'VELÁZQUEZ JACINTO': {
        'columnas': ['MITI20'],
        'partido': 'MITI',
        'nombre_completo': 'JACINTO VELÁZQUEZ ROSALES'
    }
}

# Nombres de columnas
COL_PROVINCIA = 'PROVINCI'
COL_PARROQUIA = 'PARROQUIA'
COL_VOTOS_VALIDOS = 'VOTOSVAL'
COL_VOTOS_NULOS = 'VOTOSNUL'
COL_VOTOS_BLANCOS = 'VOTOSBLA'


def cargar_y_limpiar_datos():
    """Carga y limpia los datos del archivo Excel"""
    print("Cargando datos...")
    df = pd.read_excel(ARCHIVO_DATOS)
    
    # Limpiar columnas
    df[COL_PROVINCIA] = df[COL_PROVINCIA].astype(str).str.strip()
    df[COL_PARROQUIA] = df[COL_PARROQUIA].astype(str).str.strip().str.replace('.0$', '', regex=True)
    
    print(f"✓ Datos cargados: {len(df)} registros")
    return df


def obtener_parroquias_seleccionadas(df):
    """Obtiene las últimas 12 parroquias de Pastaza y las primeras 47 de Pichincha"""
    # Parroquias de PASTAZA
    pastaza = df[df[COL_PROVINCIA] == 'PASTAZA'][COL_PARROQUIA].unique()
    pastaza_sorted = sorted(pastaza)
    ultimas_12_pastaza = pastaza_sorted[-12:]
    
    # Parroquias de PICHINCHA
    pichincha = df[df[COL_PROVINCIA] == 'PICHINCHA'][COL_PARROQUIA].unique()
    pichincha_sorted = sorted(pichincha)
    primeras_47_pichincha = pichincha_sorted[:47]
    
    return ultimas_12_pastaza, primeras_47_pichincha


def analizar_parroquia(df_parroquia, codigo_parroquia, provincia):
    """Analiza una parroquia específica y retorna sus estadísticas"""
    if df_parroquia.empty:
        return None
    
    # Calcular totales
    votos_validos = int(df_parroquia[COL_VOTOS_VALIDOS].sum())
    votos_blancos = int(df_parroquia[COL_VOTOS_BLANCOS].sum())
    votos_nulos = int(df_parroquia[COL_VOTOS_NULOS].sum())
    total_votos = votos_validos + votos_blancos + votos_nulos
    
    # Calcular votos por candidato
    votos_candidatos = {}
    for candidato, info in CANDIDATOS.items():
        votos_total = 0
        for columna in info['columnas']:
            if columna in df_parroquia.columns:
                votos = pd.to_numeric(df_parroquia[columna], errors='coerce').fillna(0).sum()
                votos_total += votos
        
        if votos_total > 0:
            votos_candidatos[candidato] = {
                'votos': int(votos_total),
                'porcentaje': round((votos_total / votos_validos * 100) if votos_validos > 0 else 0, 2)
            }
    
    return {
        'provincia': provincia,
        'codigo_parroquia': codigo_parroquia,
        'votos_validos': votos_validos,
        'votos_blancos': votos_blancos,
        'votos_nulos': votos_nulos,
        'total_votos': total_votos,
        'candidatos': votos_candidatos
    }


def main():
    """Función principal"""
    print("\n" + "="*80)
    print("ANÁLISIS DE PARROQUIAS - PRIMERA VUELTA PRESIDENCIAL 1996")
    print("Últimas 12 parroquias de PASTAZA y Primeras 47 parroquias de PICHINCHA")
    print("="*80 + "\n")
    
    # Cargar datos
    df = cargar_y_limpiar_datos()
    
    # Obtener parroquias seleccionadas
    parroquias_pastaza, parroquias_pichincha = obtener_parroquias_seleccionadas(df)
    
    print(f"\n✓ Parroquias de Pastaza seleccionadas: {len(parroquias_pastaza)}")
    print(f"✓ Parroquias de Pichincha seleccionadas: {len(parroquias_pichincha)}")
    
    # Preparar estructuras para resultados
    resultados_excel = []
    resultados_json = {
        'PASTAZA': {},
        'PICHINCHA': {}
    }
    
    # ========== ANÁLISIS DE PASTAZA ==========
    print("\n" + "="*80)
    print("PASTAZA - ÚLTIMAS 12 PARROQUIAS")
    print("="*80 + "\n")
    
    df_pastaza = df[df[COL_PROVINCIA] == 'PASTAZA'].copy()
    
    for i, parroquia_cod in enumerate(sorted(parroquias_pastaza), 1):
        df_parroquia = df_pastaza[df_pastaza[COL_PARROQUIA] == parroquia_cod]
        
        resultado = analizar_parroquia(df_parroquia, parroquia_cod, 'PASTAZA')
        if resultado:
            # Guardar en JSON
            resultados_json['PASTAZA'][parroquia_cod] = {
                'nombre': f'PARROQUIA_{parroquia_cod}',
                'votos_validos': resultado['votos_validos'],
                'votos_blancos': resultado['votos_blancos'],
                'votos_nulos': resultado['votos_nulos'],
                'total_votos': resultado['total_votos'],
                'candidatos': resultado['candidatos']
            }
            
            # Guardar para Excel
            resultados_excel.append({
                'Provincia': 'PASTAZA',
                'Codigo_Parroquia': parroquia_cod,
                'Parroquia': f'PARROQUIA_{parroquia_cod}',
                'Votos_Validos': resultado['votos_validos'],
                'Votos_Blancos': resultado['votos_blancos'],
                'Votos_Nulos': resultado['votos_nulos'],
                'Total_Votos': resultado['total_votos']
            })
            
            # Mostrar en consola
            print(f"{i}. Parroquia {parroquia_cod}:")
            print(f"   Votos Válidos:  {resultado['votos_validos']:>10,}")
            print(f"   Votos Blancos:  {resultado['votos_blancos']:>10,}")
            print(f"   Votos Nulos:    {resultado['votos_nulos']:>10,}")
            print(f"   TOTAL:          {resultado['total_votos']:>10,}")
            print()
    
    # ========== ANÁLISIS DE PICHINCHA ==========
    print("\n" + "="*80)
    print("PICHINCHA - PRIMERAS 47 PARROQUIAS")
    print("="*80 + "\n")
    
    df_pichincha = df[df[COL_PROVINCIA] == 'PICHINCHA'].copy()
    
    for i, parroquia_cod in enumerate(sorted(parroquias_pichincha), 1):
        df_parroquia = df_pichincha[df_pichincha[COL_PARROQUIA] == parroquia_cod]
        
        resultado = analizar_parroquia(df_parroquia, parroquia_cod, 'PICHINCHA')
        if resultado:
            # Guardar en JSON
            resultados_json['PICHINCHA'][parroquia_cod] = {
                'nombre': f'PARROQUIA_{parroquia_cod}',
                'votos_validos': resultado['votos_validos'],
                'votos_blancos': resultado['votos_blancos'],
                'votos_nulos': resultado['votos_nulos'],
                'total_votos': resultado['total_votos'],
                'candidatos': resultado['candidatos']
            }
            
            # Guardar para Excel
            resultados_excel.append({
                'Provincia': 'PICHINCHA',
                'Codigo_Parroquia': parroquia_cod,
                'Parroquia': f'PARROQUIA_{parroquia_cod}',
                'Votos_Validos': resultado['votos_validos'],
                'Votos_Blancos': resultado['votos_blancos'],
                'Votos_Nulos': resultado['votos_nulos'],
                'Total_Votos': resultado['total_votos']
            })
            
            # Mostrar en consola
            print(f"{i}. Parroquia {parroquia_cod}:")
            print(f"   Votos Válidos:  {resultado['votos_validos']:>10,}")
            print(f"   Votos Blancos:  {resultado['votos_blancos']:>10,}")
            print(f"   Votos Nulos:    {resultado['votos_nulos']:>10,}")
            print(f"   TOTAL:          {resultado['total_votos']:>10,}")
            print()
    
    # ========== GUARDAR RESULTADOS ==========
    df_resultados = pd.DataFrame(resultados_excel)
    
    archivo_excel = os.path.join(DIR_RESULTADOS, 'Votos_Parroquias_Pastaza_Pichincha.xlsx')
    archivo_json = os.path.join(DIR_RESULTADOS, 'parroquias_pastaza_pichincha_1996.json')
    
    df_resultados.to_excel(archivo_excel, index=False)
    print(f"\n✓ Archivo Excel guardado: {archivo_excel}")
    
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(resultados_json, f, ensure_ascii=False, indent=2)
    print(f"✓ Archivo JSON guardado: {archivo_json}")
    
    # ========== RESUMEN FINAL ==========
    print("\n" + "="*80)
    print("RESUMEN GENERAL")
    print("="*80)
    
    total_pastaza = len([r for r in resultados_excel if r['Provincia'] == 'PASTAZA'])
    total_pichincha = len([r for r in resultados_excel if r['Provincia'] == 'PICHINCHA'])
    
    print(f"\nTotal de parroquias analizadas: {len(resultados_excel)}")
    print(f"  - Pastaza:   {total_pastaza} parroquias")
    print(f"  - Pichincha: {total_pichincha} parroquias")
    
    total_votos_validos = df_resultados['Votos_Validos'].sum()
    total_votos_blancos = df_resultados['Votos_Blancos'].sum()
    total_votos_nulos = df_resultados['Votos_Nulos'].sum()
    total_general = df_resultados['Total_Votos'].sum()
    
    print(f"\nTOTAL GENERAL DE VOTOS:")
    print(f"  Votos Válidos:  {total_votos_validos:>12,}")
    print(f"  Votos Blancos:  {total_votos_blancos:>12,}")
    print(f"  Votos Nulos:    {total_votos_nulos:>12,}")
    print(f"  {'─'*30}")
    print(f"  TOTAL:          {total_general:>12,}")
    
    print("\n" + "="*80)
    print("✓ ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("="*80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n✗ Error durante el análisis: {str(e)}")
        import traceback
        traceback.print_exc()
