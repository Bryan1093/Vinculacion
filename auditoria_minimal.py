import pandas as pd
import json

ARCHIVO_EXCEL = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
ARCHIVO_JSON = 'JSON-Cantones/presidentes_primera_vuelta.json'

CANTONES_AUDIT = [
    {"Nombre": "MONTUFAR",  "CodExcel": 10.0,  "CodJson": "10",  "Partido": "MUPP-NP18"},
    {"Nombre": "CUENCA",    "CodExcel": 260.0, "CodJson": "260", "Partido": "MUPP-NP18"},
    {"Nombre": "GUAYAQUIL", "CodExcel": 390.0, "CodJson": "390", "Partido": "PSC6"},
    {"Nombre": "QUITO",     "CodExcel": 60.0,  "CodJson": "60",  "Partido": "MUPP-NP18"}
]

try:
    df = pd.read_excel(ARCHIVO_EXCEL)
    with open(ARCHIVO_JSON, encoding='utf-8') as f:
        data_json = json.load(f)

    for canton in CANTONES_AUDIT:
        # Excel
        df_canton = df[df['CANTON'] == canton['CodExcel']]
        if len(df_canton) == 0:
            print(f"ERROR: No hay datos Excel para {canton['Nombre']}")
            continue
            
        v_validos_excel = int(df_canton['VOTOSVAL'].sum())
        v_ganador_excel = int(df_canton[canton['Partido']].sum())

        # Json
        json_canton = next((c for c in data_json if c['CODCAN'] == canton['CodJson']), None)
        if not json_canton:
            print(f"ERROR: No se hay datos JSON para {canton['Nombre']} (Cod: {canton['CodJson']})")
            continue
            
        v_validos_json = json_canton['votos_validos']
        ganador_data = json_canton['resultados'].get(canton['Partido'], {})
        v_ganador_json = ganador_data.get('votos', 0)
        
        # Comparar e imprimir SIEMPRE los valores
        if v_validos_excel != v_validos_json or v_ganador_excel != v_ganador_json:
            print(f"DISCREPANCIA EN {canton['Nombre']}:")
            print(f"  Excel: Val={v_validos_excel}, Ganador={v_ganador_excel}")
            print(f"  JSON : Val={v_validos_json}, Ganador={v_ganador_json}")
        else:
            print(f"OK: {canton['Nombre']}")

except Exception as e:
    print(f"EXCEPCION: {e}")
