import pandas as pd
import json

ARCHIVO_EXCEL = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
ARCHIVO_JSON = 'JSON-Cantones/presidentes_primera_vuelta.json'

# CORREGIDO: El ganador en Quito fue DP5
CANTONES_AUDIT = [
    {"Nombre": "MONTUFAR",  "CodExcel": 10.0,  "CodJson": "10",  "Partido": "MUPP-NP18"},
    {"Nombre": "CUENCA",    "CodExcel": 260.0, "CodJson": "260", "Partido": "MUPP-NP18"},
    {"Nombre": "GUAYAQUIL", "CodExcel": 390.0, "CodJson": "390", "Partido": "PSC6"},
    {"Nombre": "QUITO",     "CodExcel": 60.0,  "CodJson": "60",  "Partido": "DP5"} 
]

try:
    df = pd.read_excel(ARCHIVO_EXCEL)
    with open(ARCHIVO_JSON, encoding='utf-8') as f:
        data_json = json.load(f)

    for canton in CANTONES_AUDIT:
        # Excel
        df_canton = df[df['CANTON'] == canton['CodExcel']]
        v_validos_excel = int(df_canton['VOTOSVAL'].sum())
        v_ganador_excel = int(df_canton[canton['Partido']].sum())

        # Json
        json_canton = next((c for c in data_json if c['CODCAN'] == canton['CodJson']), None)
        v_validos_json = json_canton['votos_validos']
        ganador_data = json_canton['resultados'].get(canton['Partido'], {})
        v_ganador_json = ganador_data.get('votos', 0)
        
        # Comparar
        if v_validos_excel != v_validos_json or v_ganador_excel != v_ganador_json:
            print(f"DISCREPANCIA EN {canton['Nombre']}:")
            print(f"  Excel ({canton['Partido']}): Val={v_validos_excel}, Votos={v_ganador_excel}")
            print(f"  JSON  ({canton['Partido']}): Val={v_validos_json}, Votos={v_ganador_json}")
        else:
            print(f"OK: {canton['Nombre']} - Ganador Correcto: {canton['Partido']} ({v_ganador_json} votos)")

except Exception as e:
    print(f"EXCEPCION: {e}")
