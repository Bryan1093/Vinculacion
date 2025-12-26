import pandas as pd

print('=== TOTALES POR PROVINCIA ===')
df_tot = pd.read_excel('resultados/segunda_vuelta/Totales_Por_Provincia_2daVuelta.xlsx')
print(df_tot)

print('\n=== VOTOS POR CANDIDATO ===')
df_cand = pd.read_excel('resultados/segunda_vuelta/Votos_Por_Candidato_Y_Provincia_2daVuelta.xlsx')
print(df_cand)

print('\n=== VERIFICACIÓN DE CÁLCULOS ===')
for prov in ['NAPO', 'PASTAZA']:
    votos_candidatos = df_cand[df_cand['Provincia']==prov]['Total_Votos'].sum()
    votos_validos = df_tot[df_tot['Provincia']==prov]['Votos_Validos'].values[0]
    print(f'{prov}:')
    print(f'  Suma de votos de candidatos: {votos_candidatos}')
    print(f'  Votos válidos en totales: {votos_validos}')
    print(f'  ¿Coinciden? {votos_candidatos == votos_validos}')
    
    # Verificar porcentajes
    print(f'  Detalle por candidato:')
    for _, row in df_cand[df_cand['Provincia']==prov].iterrows():
        porcentaje_calculado = (row['Total_Votos'] / votos_validos * 100)
        print(f'    {row["Candidato"]}: {row["Total_Votos"]} votos = {porcentaje_calculado:.2f}% (mostrado: {row["Porcentaje (%)"]}%)')
