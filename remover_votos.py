import re

# Leer el archivo
with open('generar_json_parroquias.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Patrón a buscar (VOTOS section)
pattern = r"""        # Crear estructura de resultados \(solo VOTOS \+ ganador\)
        resultados_parroquia = \{
            'VOTOS': \{
                'candidato': 'VALIDOS',
                'votos': votos_validos,
                'porcentaje': 100\.0
            \}
        \}"""

# Reemplazo
replacement = """        # Crear estructura de resultados (solo ganador)
        resultados_parroquia = {}"""

# Realizar el reemplazo
new_content = content.replace(pattern, replacement)

# Si no funcionó con el patrón exacto, intentar con regex más flexible
if new_content == content:
    pattern2 = r"resultados_parroquia = \{\s+'VOTOS': \{\s+'candidato': 'VALIDOS',\s+'votos': votos_validos,\s+'porcentaje': 100\.0\s+\}\s+\}"
    replacement2 = "resultados_parroquia = {}"
    new_content = re.sub(pattern2, replacement2, content)

# Guardar
with open('generar_json_parroquias.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ Archivo actualizado - VOTOS section removida")
