import pandas as pd

# Cargar datos
df = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')

# Limpiar datos
df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
df['CANTON'] = df['CANTON'].astype(str).str.strip().str.replace('.0$', '', regex=True)

# Verificar si existe columna con nombre de cantón
print("Columnas disponibles:")
print(df.columns.tolist())
print("\n")

# Filtrar Pichincha
df_pich = df[df['PROVINCI'] == 'PICHINCHA']

# Obtener cantones únicos
cantones_codigos = ['60', '65', '70', '75', '80', '85', '770', '895']

print("Cantones de PICHINCHA:")
for codigo in cantones_codigos:
    df_canton = df_pich[df_pich['CANTON'] == codigo]
    if len(df_canton) > 0:
        # Mostrar primera fila para ver qué columnas tienen
        print(f"\nCódigo {codigo}:")
        print(df_canton[['CANTON', 'PARROQUIA']].head(3))
