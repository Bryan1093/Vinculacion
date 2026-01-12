import pandas as pd
import json

# Configuración
ARCHIVO_EXCEL = 'Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx'
ARCHIVO_JSON = 'JSON-Cantones/presidentes_primera_vuelta.json'

# Cantones a auditar (Nombre, Código en Excel (float), Código en JSON (string))
CANTONES_AUDIT = [
    {"Nombre": "MONTUFAR",  "CodExcel": 10.0,  "CodJson": "10",  "Partido": "MUPP-NP18"},
    {"Nombre": "CUENCA",    "CodExcel": 260.0, "CodJson": "260", "Partido": "MUPP-NP18"},
    {"Nombre": "GUAYAQUIL", "CodExcel": 390.0, "CodJson": "390", "Partido": "PSC6"},
    {"Nombre": "QUITO",     "CodExcel": 60.0,  "CodJson": "60",  "Partido": "MUPP-NP18"}
]

print("="*80)
print("AUDITORÍA DE DATOS: EXCEL vs JSON")
print("="*80)

# 1. Leer Excel
print(f"Leyendo Excel: {ARCHIVO_EXCEL}...")
df = pd.read_excel(ARCHIVO_EXCEL)

# 2. Leer JSON
print(f"Leyendo JSON: {ARCHIVO_JSON}...")
with open(ARCHIVO_JSON, encoding='utf-8') as f:
    data_json = json.load(f)

print("\n" + "-"*80)
print(f"{'CANTON':<15} | {'ORIGEN':<8} | {'V.VALIDOS':>10} | {'V.GANADOR':>10} | {'% CALC':>8}")
print("-"*80)

todo_correcto = True

for canton in CANTONES_AUDIT:
    # --- Datos EXCEL ---
    df_canton = df[df['CANTON'] == canton['CodExcel']]
    
    # Calcular sumas
    v_validos_excel = int(df_canton['VOTOSVAL'].sum())
    v_ganador_excel = int(df_canton[canton['Partido']].sum())
    
    # Calcular porcentaje
    porcentaje_excel = round((v_ganador_excel / v_validos_excel * 100), 2) if v_validos_excel > 0 else 0
    
    print(f"{canton['Nombre']:<15} | EXCEL    | {v_validos_excel:10,d} | {v_ganador_excel:10,d} | {porcentaje_excel:8.2f}%")
    
    # --- Datos JSON ---
    # Buscar cantón en JSON
    json_canton = next((c for c in data_json if c['CODCAN'] == canton['CodJson']), None)
    
    if json_canton:
        v_validos_json = json_canton['votos_validos']
        
        # Datos del ganador
        ganador_data = json_canton['resultados'].get(canton['Partido'], {})
        v_ganador_json = ganador_data.get('votos', 0)
        porcentaje_json = ganador_data.get('porcentaje', 0)
        
        print(f"{'':<15} | JSON     | {v_validos_json:10,d} | {v_ganador_json:10,d} | {porcentaje_json:8.2f}%")
        
        # Comparación
        if v_validos_excel != v_validos_json or v_ganador_excel != v_ganador_json:
            print(f"⚠️ DISCREPANCIA EN {canton['Nombre']} ⚠️")
            todo_correcto = False
        else:
             print(f"{'':<15}  >>> ✅ OK")
    else:
        print(f"⚠️ NO SE ENCONTRÓ EL CANTÓN {canton['Nombre']} EN EL JSON")
        todo_correcto = False
        
    print("-" * 80)

print("\n" + "="*80)
if todo_correcto:
    print("✅ RESULTADO: TODOS LOS DATOS COINCIDEN PERFECTAMENTE")
else:
    print("❌ RESULTADO: SE ENCONTRARON ERRORES")
print("="*80)
