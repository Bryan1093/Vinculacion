import traceback

try:
    from analisis.presidentes_segunda_vuelta.analisis_provincias import analizar_provincias
    analizar_provincias()
except Exception as e:
    print("ERROR COMPLETO:")
    print(traceback.format_exc())
