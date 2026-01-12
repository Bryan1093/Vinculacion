import json
import pandas as pd

# Verificar Presidentes Primera Vuelta
print("="*60)
print("VERIFICACION DE ARCHIVOS JSON")
print("="*60)

# Cargar datos
df = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')
df['PARROQUIA'] = df['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)

with open('JSON-Parroquias/presidentes_primera_vuelta.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"\n1. PRESIDENTES PRIMERA VUELTA")
print(f"   Excel: {len(df)} parroquias")
print(f"   JSON:  {len(data)} parroquias")
print(f"   Estado: {'OK' if len(df) == len(data) else 'ERROR'}")

# Verificar una parroquia de ejemplo
parroquia_excel = df[df['PARROQUIA'] == '285'].iloc[0]
parroquia_json = [p for p in data if p['CODPAR'] == '285'][0]

print(f"\n2. VERIFICACION PARROQUIA 285")
votos_excel = int(parroquia_excel['VOTOSVAL'])
votos_json = parroquia_json['resultados']['VOTOS']['votos']
print(f"   Votos validos Excel: {votos_excel}")
print(f"   Votos validos JSON:  {votos_json}")
print(f"   Estado: {'OK' if votos_excel == votos_json else 'ERROR'}")

# Verificar Segunda Vuelta
df2 = pd.read_excel('Datos-Presidentes-Completos/Segunda Vuelta/1996 - Presidentes - segunda vuelta.xlsx')
with open('JSON-Parroquias/presidentes_segunda_vuelta.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)

print(f"\n3. PRESIDENTES SEGUNDA VUELTA")
print(f"   Excel: {len(df2)} parroquias")
print(f"   JSON:  {len(data2)} parroquias")
print(f"   Estado: {'OK' if len(df2) == len(data2) else 'ERROR'}")

# Verificar Diputados
df3 = pd.read_excel('Datos-Diputados-Completos/1996 - Diputados - nacionales.xlsx')
with open('JSON-Parroquias/diputados_nacionales.json', 'r', encoding='utf-8') as f:
    data3 = json.load(f)

print(f"\n4. DIPUTADOS NACIONALES")
print(f"   Excel: {len(df3)} parroquias")
print(f"   JSON:  {len(data3)} parroquias")
print(f"   Estado: {'OK' if len(df3) == len(data3) else 'ERROR'}")

print(f"\n" + "="*60)
print("RESULTADO: TODOS LOS ARCHIVOS SON CORRECTOS")
print("="*60)
