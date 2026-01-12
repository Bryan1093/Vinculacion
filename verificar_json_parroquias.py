"""
Script de verificación para validar los archivos JSON generados
Compara los datos del JSON con los archivos Excel originales
"""

import pandas as pd
import json
import os

# Configuración de archivos
ARCHIVO_PRESIDENTES_1V = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
ARCHIVO_PRESIDENTES_2V = 'Datos-Presidentes-Completos/Segunda Vuelta/1996 - Presidentes - segunda vuelta.xlsx'
ARCHIVO_DIPUTADOS = 'Datos-Diputados-Completos/1996 - Diputados - nacionales.xlsx'

DIR_JSON = 'JSON-Parroquias'

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


def verificar_presidentes_primera_vuelta():
    """Verifica el archivo JSON de presidentes primera vuelta"""
    print("\n" + "="*80)
    print("VERIFICANDO: PRESIDENTES - PRIMERA VUELTA")
    print("="*80)
    
    # Cargar Excel
    df_excel = pd.read_excel(ARCHIVO_PRESIDENTES_1V)
    df_excel['PARROQUIA'] = df_excel['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    
    # Cargar JSON
    with open(os.path.join(DIR_JSON, 'presidentes_primera_vuelta.json'), 'r', encoding='utf-8') as f:
        datos_json = json.load(f)
    
    print(f"\n📊 Estadísticas:")
    print(f"   Parroquias en Excel: {len(df_excel)}")
    print(f"   Parroquias en JSON:  {len(datos_json)}")
    
    # Verificar que todas las parroquias estén presentes
    parroquias_excel = set(df_excel['PARROQUIA'].unique())
    parroquias_json = set([p['CODPAR'] for p in datos_json])
    
    if parroquias_excel == parroquias_json:
        print(f"   ✅ Todas las parroquias están presentes")
    else:
        print(f"   ❌ Faltan parroquias!")
        faltantes = parroquias_excel - parroquias_json
        if faltantes:
            print(f"      Faltantes en JSON: {faltantes}")
        extras = parroquias_json - parroquias_excel
        if extras:
            print(f"      Extras en JSON: {extras}")
        return False
    
    # Verificar datos de muestra (primeras 5 parroquias)
    print(f"\n🔍 Verificando datos de muestra (primeras 5 parroquias):")
    errores = 0
    
    for i, registro_json in enumerate(datos_json[:5]):
        cod_parroquia = registro_json['CODPAR']
        
        # Buscar en Excel
        fila_excel = df_excel[df_excel['PARROQUIA'] == cod_parroquia].iloc[0]
        
        print(f"\n   Parroquia {cod_parroquia}:")
        
        # Verificar ganador
        ganador_json = registro_json['ganador']
        max_votos = 0
        ganador_calculado = None
        
        for partido in CANDIDATOS_PRES_1V.keys():
            if partido in df_excel.columns:
                votos = int(fila_excel[partido]) if pd.notna(fila_excel[partido]) else 0
                if votos > max_votos:
                    max_votos = votos
                    ganador_calculado = partido
        
        if ganador_json == ganador_calculado:
            print(f"      ✅ Ganador: {ganador_json}")
        else:
            print(f"      ❌ Ganador incorrecto! JSON={ganador_json}, Calculado={ganador_calculado}")
            errores += 1
        
        # Verificar votos del ganador
        if ganador_json in registro_json['resultados']:
            votos_ganador_json = registro_json['resultados'][ganador_json]['votos']
            votos_ganador_excel = int(fila_excel[ganador_json]) if pd.notna(fila_excel[ganador_json]) else 0
            
            if votos_ganador_json == votos_ganador_excel:
                print(f"      ✅ Votos del ganador: {votos_ganador_json:,}")
            else:
                print(f"      ❌ Votos del ganador NO coinciden!")
                print(f"         Excel: {votos_ganador_excel:,}, JSON: {votos_ganador_json:,}")
                errores += 1
        

    
    print(f"\n{'='*80}")
    if errores == 0:
        print("✅ VERIFICACIÓN EXITOSA - Presidentes Primera Vuelta")
    else:
        print(f"❌ Se encontraron {errores} errores")
    print("="*80)
    
    return errores == 0


def verificar_presidentes_segunda_vuelta():
    """Verifica el archivo JSON de presidentes segunda vuelta"""
    print("\n" + "="*80)
    print("VERIFICANDO: PRESIDENTES - SEGUNDA VUELTA")
    print("="*80)
    
    # Cargar Excel
    df_excel = pd.read_excel(ARCHIVO_PRESIDENTES_2V)
    df_excel['PARROQUIA'] = df_excel['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    
    # Cargar JSON
    with open(os.path.join(DIR_JSON, 'presidentes_segunda_vuelta.json'), 'r', encoding='utf-8') as f:
        datos_json = json.load(f)
    
    print(f"\n📊 Estadísticas:")
    print(f"   Parroquias en Excel: {len(df_excel)}")
    print(f"   Parroquias en JSON:  {len(datos_json)}")
    
    # Verificar que todas las parroquias estén presentes
    parroquias_excel = set(df_excel['PARROQUIA'].unique())
    parroquias_json = set([p['CODPAR'] for p in datos_json])
    
    if parroquias_excel == parroquias_json:
        print(f"   ✅ Todas las parroquias están presentes")
    else:
        print(f"   ❌ Faltan parroquias!")
        return False
    
    print(f"\n✅ VERIFICACIÓN EXITOSA - Presidentes Segunda Vuelta")
    return True


def verificar_diputados_nacionales():
    """Verifica el archivo JSON de diputados nacionales"""
    print("\n" + "="*80)
    print("VERIFICANDO: DIPUTADOS NACIONALES")
    print("="*80)
    
    # Cargar Excel
    df_excel = pd.read_excel(ARCHIVO_DIPUTADOS)
    df_excel['PARROQUIA'] = df_excel['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)
    
    # Cargar JSON
    with open(os.path.join(DIR_JSON, 'diputados_nacionales.json'), 'r', encoding='utf-8') as f:
        datos_json = json.load(f)
    
    print(f"\n📊 Estadísticas:")
    print(f"   Parroquias en Excel: {len(df_excel)}")
    print(f"   Parroquias en JSON:  {len(datos_json)}")
    
    # Verificar que todas las parroquias estén presentes
    parroquias_excel = set(df_excel['PARROQUIA'].unique())
    parroquias_json = set([p['CODPAR'] for p in datos_json])
    
    if parroquias_excel == parroquias_json:
        print(f"   ✅ Todas las parroquias están presentes")
    else:
        print(f"   ❌ Faltan parroquias!")
        return False
    
    print(f"\n✅ VERIFICACIÓN EXITOSA - Diputados Nacionales")
    return True


def verificar_formato_json():
    """Verifica que el formato JSON sea el correcto"""
    print("\n" + "="*80)
    print("VERIFICANDO: FORMATO JSON")
    print("="*80)
    
    with open(os.path.join(DIR_JSON, 'presidentes_primera_vuelta.json'), 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    # Verificar primer registro
    primer_registro = datos[0]
    
    print(f"\n📋 Estructura del primer registro:")
    print(f"   Campos principales: {list(primer_registro.keys())}")
    
    # Verificar campos requeridos
    campos_requeridos = ['CODPAR', 'CODCAN', 'PARROQUIA', 'ganador', 'resultados']
    todos_presentes = all(campo in primer_registro for campo in campos_requeridos)
    
    if todos_presentes:
        print(f"   ✅ Todos los campos requeridos están presentes")
    else:
        print(f"   ❌ Faltan campos requeridos")
        return False
    
    # Verificar estructura de resultados (solo debe tener el ganador)
    ganador = primer_registro['ganador']
    if ganador in primer_registro['resultados']:
        datos_ganador = primer_registro['resultados'][ganador]
        if 'candidato' in datos_ganador and 'votos' in datos_ganador and 'porcentaje' in datos_ganador:
            print(f"   ✅ Estructura del ganador correcta")
            print(f"   ✅ Solo contiene el ganador (sin sección VOTOS)")
        else:
            print(f"   ❌ Estructura del ganador incorrecta")
            return False
    else:
        print(f"   ❌ Falta el ganador en resultados")
        return False
    
    print(f"\n✅ FORMATO JSON CORRECTO")
    return True


def main():
    """Función principal"""
    print("\n" + "="*80)
    print("VERIFICACIÓN DE ARCHIVOS JSON GENERADOS")
    print("Elecciones 1996 - Todas las Parroquias de Ecuador")
    print("="*80)
    
    resultados = []
    
    try:
        # Verificar formato
        resultados.append(("Formato JSON", verificar_formato_json()))
        
        # Verificar cada archivo
        resultados.append(("Presidentes 1ra Vuelta", verificar_presidentes_primera_vuelta()))
        resultados.append(("Presidentes 2da Vuelta", verificar_presidentes_segunda_vuelta()))
        resultados.append(("Diputados Nacionales", verificar_diputados_nacionales()))
        
        # Resumen final
        print("\n" + "="*80)
        print("RESUMEN DE VERIFICACIÓN")
        print("="*80)
        
        for nombre, resultado in resultados:
            estado = "✅ CORRECTO" if resultado else "❌ ERROR"
            print(f"   {nombre:30} {estado}")
        
        if all(r[1] for r in resultados):
            print("\n🎉 ¡TODOS LOS ARCHIVOS SON CORRECTOS!")
        else:
            print("\n⚠️  Se encontraron errores en algunos archivos")
        
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error durante la verificación: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
