import json
import pandas as pd

# Leer JSON
with open('resultados/provincias_1996.json', encoding='utf-8') as f:
    data = json.load(f)

print('='*80)
print('RESULTADOS ELECTORALES - NAPO Y PASTAZA (1996)')
print('='*80)

for provincia in data:
    print(f"\n📍 {provincia['PROVINCIA']} (Código: {provincia['CODPRO']})")
    print(f"   Votos válidos: {provincia['votos_validos']:,}")
    print(f"   Votos blancos: {provincia['votos_blancos']:,}")
    print(f"   Votos nulos:   {provincia['votos_nulos']:,}")
    print(f"   Total votos:   {provincia['votos_total']:,}")
    print(f"\n   🏆 GANADOR: {provincia['ganador']} - {provincia['resultados'][provincia['ganador']]['candidato']}")
    print(f"      {provincia['resultados'][provincia['ganador']]['porcentaje']}% ({provincia['resultados'][provincia['ganador']]['votos']:,} votos)")

# Leer Excel
print('\n' + '='*80)
print('RESULTADOS COMPLETOS POR CANDIDATO Y PROVINCIA')
print('='*80)

df = pd.read_excel('resultados/Votos_Por_Candidato_Y_Provincia.xlsx')

for prov in df['Provincia'].unique():
    print(f"\n{prov}:")
    # Ordenar por porcentaje descendente y mostrar TODOS los candidatos
    todos = df[df['Provincia'] == prov].sort_values('Porcentaje (%)', ascending=False)
    for i, (_, row) in enumerate(todos.iterrows(), 1):
        # Agregar medallas para el top 3
        medalla = {1: '🥇', 2: '🥈', 3: '🥉'}.get(i, '  ')
        print(f"  {medalla} {i}. {row['Candidato']}: {int(row['Total_Votos']):,} votos ({row['Porcentaje (%)']}%)")

print('\n' + '='*80)
