import pandas as pd
import json

# Configuración
ARCHIVO_EXCEL = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
ARCHIVO_JSON = 'JSON-Cantones/presidentes_primera_vuelta.json'

# Cantones a auditar
# Usamos float para excel porque así se leyó antes (10.0, 260.0)
# Usamos string para json porque así lo generamos ("10", "260")
CANTONES_AUDIT = [
    {"Nombre": "MONTUFAR",  "CodExcel": 10.0,  "CodJson": "10",  "Partido": "MUPP-NP18"},
    {"Nombre": "CUENCA",    "CodExcel": 260.0, "CodJson": "260", "Partido": "MUPP-NP18"},
    {"Nombre": "GUAYAQUIL", "CodExcel": 390.0, "CodJson": "390", "Partido": "PSC6"},
    {"Nombre": "QUITO",     "CodExcel": 60.0,  "CodJson": "60",  "Partido": "MUPP-NP18"}
]

print("="*60)
print("AUDITORIA DETALLADA")
print("="*60)

try:
    df = pd.read_excel(ARCHIVO_EXCEL)
    with open(ARCHIVO_JSON, encoding='utf-8') as f:
        data_json = json.load(f)

    errores = 0

    for canton in CANTONES_AUDIT:
        print(f"\nVerificando: {canton['Nombre']}...")
        
        # 1. Obtener datos de Excel
        # IMPORTANTE: Filtrar como lo hicimos en la generación
        # Asegurar que CANTON sea del mismo tipo (float)
        df_canton = df[df['CANTON'] == canton['CodExcel']]
        
        if len(df_canton) == 0:
            print(f"  ERROR EXCEL: No se encontraron datos para código {canton['CodExcel']}")
            errores += 1
            continue
            
        v_validos_excel = int(df_canton['VOTOSVAL'].sum())
        v_ganador_excel = int(df_canton[canton['Partido']].sum())
        
        print(f"  Datos Excel -> Validos: {v_validos_excel}, Ganador ({canton['Partido']}): {v_ganador_excel}")

        # 2. Obtener datos de JSON
        json_canton = next((c for c in data_json if c['CODCAN'] == canton['CodJson']), None)
        
        if not json_canton:
            print(f"  ERROR JSON: No se encontró cantón con código '{canton['CodJson']}'")
            errores += 1
            continue
            
        v_validos_json = json_canton['votos_validos']
        ganador_data = json_canton['resultados'].get(canton['Partido'], {})
        v_ganador_json = ganador_data.get('votos', 0)
        
        print(f"  Datos JSON  -> Validos: {v_validos_json}, Ganador ({canton['Partido']}): {v_ganador_json}")
        
        # 3. Comparar
        if v_validos_excel == v_validos_json and v_ganador_excel == v_ganador_json:
            print(f"   [OK] CORRECTO")
        else:
            print(f"   [ERROR] DISCREPANCIA!")
            errores += 1

    print("\n" + "="*60)
    if errores == 0:
        print("RESULTADO FINAL: EXITOSO - Todos los datos coinciden")
    else:
        print(f"RESULTADO FINAL: FALLIDO - Se encontraron {errores} errores")

except Exception as e:
    print(f"\nERROR CRITICO EN SCRIPT: {str(e)}")
