# Documentación de Actividades - Análisis Electoral por Parroquias 1996

---

## Resumen de Actividades y Horas

| Actividad | Tiempo |
|-----------|--------|
| 1. Exploración y preparación de datos electorales | 1 h |
| 2. Desarrollo del script de análisis - Primera vuelta presidencial | 1.5 h |
| 3. Generación de formato transpuesto - Primera vuelta | 1 h |
| 4. Desarrollo del script de análisis - Segunda vuelta presidencial | 1 h |
| 5. Generación de formatos adicionales - Segunda vuelta | 1 h |
| 6. Desarrollo del script de análisis - Diputados nacionales | 1.5 h |
| 7. Generación de formatos adicionales - Diputados | 1 h |
| 8. Verificación y validación de resultados | 1 h |
| 9. Traslado de datos a Excel compartido del grupo | 1 h |
| **TOTAL** | **9 h** |

---

## Actividad 1: Exploración y preparación de datos electorales

**Nombre de la actividad:** Exploración de estructura de datos y identificación de parroquias

**Descripción:**
Se realizó la exploración inicial de los archivos Excel de datos electorales (presidentes primera vuelta, segunda vuelta y diputados nacionales). Se identificaron las columnas disponibles, se verificó la estructura de los datos y se determinaron las 59 parroquias específicas a analizar (12 de Pastaza y 47 de Pichincha). Se validó que todas las parroquias especificadas tuvieran datos disponibles en los tres archivos.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 8:00 AM - 9:00 AM

**Capturas o fotos:** 
Ejecutar en terminal: `py explorar_parroquias.py` y capturar la salida mostrando las parroquias encontradas.

---

## Actividad 2: Desarrollo del script de análisis - Primera vuelta presidencial

**Nombre de la actividad:** Creación del script de análisis para primera vuelta presidencial

**Descripción:**
Se desarrolló el script `analisis_parroquias_pastaza_pichincha_detallado.py` que carga los datos de primera vuelta, filtra las 59 parroquias en el orden especificado, extrae votos válidos, blancos, nulos y totales, calcula los votos de los 9 candidatos presidenciales por parroquia, y genera archivos Excel y JSON con los resultados.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 9:00 AM - 10:30 AM

**Capturas o fotos:** 
Ejecutar en terminal: `py analisis_parroquias_pastaza_pichincha_detallado.py` y capturar la ejecución completa.

---

## Actividad 3: Generación de formato transpuesto - Primera vuelta

**Nombre de la actividad:** Creación de archivo en formato transpuesto para primera vuelta

**Descripción:**
Se desarrolló el script `generar_votos_transpuesto.py` que convierte los datos de primera vuelta a formato transpuesto (parroquias en filas, candidatos en columnas). Se implementó la lógica para mantener el orden exacto de las parroquias sin aplicar ordenamiento alfabético o numérico.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 10:30 AM - 11:30 AM

**Capturas o fotos:** 
Ejecutar en terminal: `py generar_votos_transpuesto.py` y capturar la generación del archivo transpuesto.

---

## Actividad 4: Desarrollo del script de análisis - Segunda vuelta presidencial

**Nombre de la actividad:** Creación del script de análisis para segunda vuelta presidencial

**Descripción:**
Se desarrolló el script `analisis_segunda_vuelta_parroquias.py` adaptado para analizar la segunda vuelta presidencial con solo 2 candidatos. El script mantiene la misma estructura de las 59 parroquias, extrae votos válidos, blancos, nulos y totales, y genera los archivos de resultados en formato Excel y JSON.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 11:30 AM - 12:30 PM

**Capturas o fotos:** 
Ejecutar en terminal: `py analisis_segunda_vuelta_parroquias.py` y capturar el análisis de segunda vuelta.

---

## Actividad 5: Generación de formatos adicionales - Segunda vuelta

**Nombre de la actividad:** Creación de archivos adicionales para segunda vuelta

**Descripción:**
Se desarrolló el script `generar_archivos_segunda_vuelta.py` que genera el archivo de votos válidos/blancos/nulos y el formato transpuesto para segunda vuelta. Se verificó que el orden de las parroquias se mantuviera correcto en todos los archivos generados.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 1:00 PM - 2:00 PM

**Capturas o fotos:** 
Ejecutar en terminal: `py generar_archivos_segunda_vuelta.py` y capturar la generación de archivos.

---

## Actividad 6: Desarrollo del script de análisis - Diputados nacionales

**Nombre de la actividad:** Creación del script de análisis para diputados nacionales

**Descripción:**
Se desarrolló el script `analisis_diputados_parroquias.py` para analizar los votos de diputados nacionales. El script procesa 14 partidos/listas políticas, mantiene las mismas 59 parroquias en orden, extrae todos los tipos de votos y genera archivos con el análisis detallado por partido y parroquia.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 2:00 PM - 3:30 PM

**Capturas o fotos:** 
Ejecutar en terminal: `py analisis_diputados_parroquias.py` y capturar el análisis de diputados.

---

## Actividad 7: Generación de formatos adicionales - Diputados

**Nombre de la actividad:** Creación de archivos adicionales para diputados nacionales

**Descripción:**
Se desarrolló el script `generar_archivos_diputados.py` que genera el archivo de votos válidos/blancos/nulos y el formato transpuesto con 14 columnas de partidos. Se validó que todas las parroquias mantuvieran el orden especificado en el archivo transpuesto.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 3:30 PM - 4:30 PM

**Capturas o fotos:** 
Ejecutar en terminal: `py generar_archivos_diputados.py` y capturar la generación de formatos.

---

## Actividad 8: Verificación y validación de resultados

**Nombre de la actividad:** Validación de datos y verificación de orden de parroquias

**Descripción:**
Se desarrollaron scripts de verificación (`verificar_orden_parroquias.py`, `verificar_orden_transpuesto.py`, `ver_resumen_parroquias.py`) para validar que los datos generados sean correctos, que el orden de las parroquias se mantenga en todos los archivos, y que los totales de votos coincidan entre los diferentes formatos. Se verificó la integridad de los 12 archivos generados.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 4:30 PM - 5:30 PM

**Capturas o fotos:** 
Ejecutar en terminal: `py verificar_orden_transpuesto.py` y `py ver_resumen_parroquias.py` y capturar las validaciones.

---

## Actividad 9: Traslado de datos a Excel compartido del grupo

**Nombre de la actividad:** Transferencia manual de datos al Excel compartido del grupo 3

**Descripción:**
Se realizó el traslado manual de los datos generados (votos válidos, blancos, nulos y totales por parroquia, así como los votos por candidato/partido) desde los archivos Excel generados hacia el archivo Excel compartido del grupo 3. Se organizaron los datos por secciones (Primera Vuelta Presidencial, Segunda Vuelta Presidencial y Diputados Nacionales) y se verificó que toda la información se transfiriera correctamente manteniendo el formato y orden de las parroquias.

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 5:30 PM - 6:30 PM

**Capturas o fotos:** 
Captura del Excel compartido del grupo mostrando los datos transferidos organizados por secciones.

---

**Total de horas trabajadas:** 9 horas  
**Fecha de generación del documento:** 28 de diciembre de 2025
