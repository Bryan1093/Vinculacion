import pandas as pd

df = pd.read_excel('resultados/Votos_Por_Candidato_Y_Canton.xlsx')

print("="*70)
print("VERIFICACIÓN: Orden de cantones para cada candidato")
print("="*70)

# Mostrar primeros 3 candidatos con todos sus cantones
candidatos = df['Candidato'].unique()[:3]

for candidato in candidatos:
    print(f"\n{candidato}:")
    df_cand = df[df['Candidato'] == candidato]
    for i, (idx, row) in enumerate(df_cand.iterrows(), 1):
        print(f"  {i}. {row['Canton_Nombre']}: {row['Total_Votos']:,} votos ({row['Porcentaje (%)']}%)")

print("\n" + "="*70)
