import pandas as pd

# Cargar datos
df = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')

# Limpiar datos
df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
df['CANTON'] = df['CANTON'].astype(str).str.strip().str.replace('.0$', '', regex=True)

# Filtrar Pichincha
df_pich = df[df['PROVINCI'] == 'PICHINCHA']

# Obtener cantones únicos
cantones = df_pich['CANTON'].unique()
cantones = [c for c in cantones if c != 'nan']

print("Cantones de PICHINCHA encontrados:")
print(f"Total: {len(cantones)} cantones\n")

for canton in sorted(cantones):
    # Obtener nombre si está disponible
    print(f"  '{canton}': 'CANTON_{canton}',")
