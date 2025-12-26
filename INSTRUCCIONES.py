"""
INSTRUCCIONES PARA REESTRUCTURAR EL PROYECTO
=============================================

Este proyecto ha sido reestructurado para separar el análisis de PRESIDENTES y DIPUTADOS.

PASOS PARA COMPLETAR LA REESTRUCTURACIÓN:
==========================================

1. CREAR ESTRUCTURA DE DIRECTORIOS
   Ejecuta:
   >>> py crear_estructura.py
   
   Esto creará todas las carpetas necesarias.

2. MIGRAR ARCHIVOS EXISTENTES
   Ejecuta:
   >>> py migrar_archivos.py
   
   Esto copiará (NO eliminará) los archivos a sus nuevas ubicaciones:
   - Datos de presidentes → datos/presidentes/
   - Código de análisis → analisis/presidentes/
   - Resultados → resultados/presidentes/

3. VERIFICAR QUE TODO FUNCIONA
   Ejecuta:
   >>> py main_presidentes.py
   
   Debe ejecutarse sin errores y generar resultados en resultados/presidentes/

4. VER RESULTADOS
   Ejecuta:
   >>> py ver_resultados_presidentes.py
   
   Verás un menú interactivo para ver resultados por provincia o cantón.

5. AGREGAR DATOS DE DIPUTADOS (CUANDO ESTÉN DISPONIBLES)
   - Coloca el archivo Excel en: datos/diputados/
   - Edita: analisis/diputados/config.py
   - Actualiza NOMBRE_ARCHIVO con el nombre del archivo
   - Define la estructura de partidos/candidatos
   - Crea los módulos de análisis (similar a presidentes)

6. LIMPIAR ARCHIVOS ANTIGUOS (OPCIONAL)
   Una vez que verifiques que todo funciona correctamente:
   - Puedes eliminar la carpeta: analisis_electoral_1996/
   - Puedes eliminar la carpeta: Datos-Presidentes-Completos/
   - Puedes eliminar los archivos: main.py, ver_resultados.py, validar_resultados.py
   
   IMPORTANTE: Solo hazlo después de verificar que la nueva estructura funciona.

ESTRUCTURA FINAL:
=================

codigo/
├── datos/
│   ├── presidentes/
│   │   ├── primera_vuelta/
│   │   │   └── 1996 - Presidentes - primera vuelta.xlsx
│   │   └── segunda_vuelta/
│   │       └── 1996 - Presidentes - segunda vuelta.xlsx
│   └── diputados/
│       └── (tus archivos de diputados aquí)
│
├── analisis/
│   ├── comun/
│   ├── presidentes/
│   │   ├── config.py
│   │   ├── data_loader.py
│   │   ├── analisis_provincias.py
│   │   ├── analisis_cantones.py
│   │   └── analisis_parroquias.py
│   └── diputados/
│       └── config.py
│
├── resultados/
│   ├── presidentes/
│   └── diputados/
│
├── main_presidentes.py
├── main_diputados.py
├── ver_resultados_presidentes.py
└── ver_resultados_diputados.py

COMANDOS RÁPIDOS:
=================

# Análisis de presidentes
py main_presidentes.py

# Ver resultados de presidentes
py ver_resultados_presidentes.py

# Análisis de diputados (cuando esté listo)
py main_diputados.py

# Ver resultados de diputados
py ver_resultados_diputados.py

PARA TU AMIGO:
==============

Si compartes este código con un amigo para que analice otros datos:

1. Solo necesita cambiar UNA línea en el archivo de configuración:
   - Presidentes: analisis/presidentes/config.py → NOMBRE_ARCHIVO
   - Diputados: analisis/diputados/config.py → NOMBRE_ARCHIVO

2. Colocar su archivo en la carpeta correspondiente:
   - datos/presidentes/primera_vuelta/ (o segunda_vuelta/)
   - datos/diputados/

3. Ejecutar el script principal correspondiente

¡Eso es todo! 🎉
"""

print(__doc__)
