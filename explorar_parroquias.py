import pandas as pd

# Cargar datos
df = pd.read_excel('Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx')

# Limpiar columnas
df['PROVINCI'] = df['PROVINCI'].astype(str).str.strip()
df['PARROQUIA'] = df['PARROQUIA'].astype(str).str.strip().str.replace('.0$', '', regex=True)

# Parroquias de PASTAZA
print('=' * 80)
print('PARROQUIAS DE PASTAZA')
print('=' * 80)
pastaza = df[df['PROVINCI'] == 'PASTAZA']['PARROQUIA'].unique()
pastaza_sorted = sorted(pastaza)
print(f'Total de parroquias: {len(pastaza_sorted)}')
print('\nTodas las parroquias:')
for i, p in enumerate(pastaza_sorted, 1):
    print(f'{i}. {p}')

print(f'\n\nÚltimas 12 parroquias de Pastaza:')
ultimas_12_pastaza = pastaza_sorted[-12:]
for i, p in enumerate(ultimas_12_pastaza, 1):
    print(f'{i}. {p}')

# Parroquias de PICHINCHA
print('\n' + '=' * 80)
print('PARROQUIAS DE PICHINCHA')
print('=' * 80)
pichincha = df[df['PROVINCI'] == 'PICHINCHA']['PARROQUIA'].unique()
pichincha_sorted = sorted(pichincha)
print(f'Total de parroquias: {len(pichincha_sorted)}')

print(f'\n\nPrimeras 47 parroquias de Pichincha:')
primeras_47_pichincha = pichincha_sorted[:47]
for i, p in enumerate(primeras_47_pichincha, 1):
    print(f'{i}. {p}')
