import pandas as pd

print("=" * 80)
print("RESUMEN COMPLETO - SEGUNDA VUELTA PRESIDENCIAL 1996")
print("=" * 80)
print()

# Totales por provincia
print("=" * 80)
print("TOTALES DE VOTOS POR PROVINCIA")
print("=" * 80)
df_prov = pd.read_excel('resultados/segunda_vuelta/Totales_Por_Provincia_2daVuelta.xlsx')
print(df_prov.to_string(index=False))
print()

# Votos por candidato y provincia
print("=" * 80)
print("VOTOS POR CANDIDATO Y PROVINCIA")
print("=" * 80)
df_cand_prov = pd.read_excel('resultados/segunda_vuelta/Votos_Por_Candidato_Y_Provincia_2daVuelta.xlsx')
print(df_cand_prov.to_string(index=False))
print()

# Totales por cantón
print("=" * 80)
print("TOTALES DE VOTOS POR CANTÓN (PICHINCHA)")
print("=" * 80)
df_cant = pd.read_excel('resultados/segunda_vuelta/Totales_Por_Canton_2daVuelta.xlsx')
print(df_cant.to_string(index=False))
print()

# Votos por candidato y cantón
print("=" * 80)
print("VOTOS POR CANDIDATO Y CANTÓN (PICHINCHA)")
print("=" * 80)
df_cand_cant = pd.read_excel('resultados/segunda_vuelta/Votos_Por_Candidato_Y_Canton_2daVuelta.xlsx')
print(df_cand_cant.to_string(index=False))
print()

print("=" * 80)
print("ARCHIVOS GENERADOS:")
print("=" * 80)
print("✓ Totales_Por_Provincia_2daVuelta.xlsx")
print("✓ Votos_Por_Candidato_Y_Provincia_2daVuelta.xlsx")
print("✓ Totales_Por_Canton_2daVuelta.xlsx")
print("✓ Votos_Por_Candidato_Y_Canton_2daVuelta.xlsx")
print("✓ provincias_segunda_vuelta_1996.json")
print("✓ cantones_segunda_vuelta_1996.json")
print("=" * 80)
