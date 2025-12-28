# 📊 DOCUMENTACIÓN DE ANÁLISIS ELECTORAL ECUADOR 1996
## Proyecto de Vinculación con la Comunidad

---

**Fecha:** 26 de diciembre de 2025  
**Institución:** [Tu Institución]  
**Responsable:** [Tu Nombre]  
**Proyecto:** Análisis Electoral Ecuador 1996 - Presidentes y Diputados

---

## 📋 REGISTRO DE ACTIVIDADES

### ACTIVIDAD 1: Análisis Electoral - Presidentes Segunda Vuelta por Provincias

**Nombre de la actividad:** Procesamiento y análisis de datos electorales de presidentes segunda vuelta a nivel provincial

**Descripción:**  
Se realizó el análisis de los resultados de la segunda vuelta presidencial de 1996 para las provincias de NAPO y PASTAZA. Se procesaron los datos del archivo Excel fuente, calculando votos válidos, blancos, nulos y totales, además de los votos obtenidos por cada candidato con sus respectivos porcentajes.

**Fecha:** 26/12/2025

**Hora de inicio y fin:** 08:00 - 09:15 (1 hora 15 minutos)

**Capturas o fotos:**
- Archivo generado: `resultados/segunda_vuelta/Resumen_Segunda_Vuelta_Napo_Pastaza.xlsx`
- Datos JSON: `resultados/segunda_vuelta/provincias_segunda_vuelta_1996.json`

**Resultados obtenidos:**
- 2 provincias analizadas (NAPO y PASTAZA)
- 2 candidatos procesados
- Totales calculados: votos válidos, blancos, nulos y total de votos
- Porcentajes de votación por candidato

---

### ACTIVIDAD 2: Análisis Electoral - Presidentes Segunda Vuelta por Cantones

**Nombre de la actividad:** Procesamiento y análisis de datos electorales de presidentes segunda vuelta a nivel cantonal (Pichincha)

**Descripción:**  
Se realizó el análisis detallado de los resultados de la segunda vuelta presidencial de 1996 para los 8 cantones de la provincia de Pichincha. Se procesaron datos de QUITO, CAYAMBE, MEJIA, PEDRO MONCAYO, RUMIÑAHUI, SANTO DOMINGO, SAN MIGUEL DE LOS BANCOS y PEDRO VICENTE MALDONADO, calculando votos válidos, blancos, nulos y totales por cantón.

**Fecha:** 26/12/2025

**Hora de inicio y fin:** 09:15 - 10:30 (1 hora 15 minutos)

**Capturas o fotos:**
- Archivo generado: `resultados/segunda_vuelta/Resumen_Segunda_Vuelta_Cantones_Pichincha.xlsx`
- Datos JSON: `resultados/segunda_vuelta/cantones_segunda_vuelta_1996.json`

**Resultados obtenidos:**
- 8 cantones de Pichincha analizados
- 2 candidatos procesados por cantón
- Totales calculados por cada cantón
- Identificación del cantón con mayor participación electoral

---

### ACTIVIDAD 3: Configuración de Partidos Políticos - Diputados Nacionales

**Nombre de la actividad:** Identificación y configuración de partidos políticos para análisis de diputados

**Descripción:**  
Se realizó un análisis exhaustivo del archivo Excel de diputados nacionales 1996 para identificar todos los partidos políticos participantes. Se corrigió la configuración inicial que contenía partidos incorrectos, actualizándola con los 14 partidos reales encontrados en el archivo fuente: PCE, CFP, DP, PSC, PRE, AN, ID, APRE, MPD, UPL, PSE, MUPP-NP, MITI y PLRE-FRA.

**Fecha:** 26/12/2025

**Hora de inicio y fin:** 10:30 - 11:00 (30 minutos)

**Capturas o fotos:**
- Archivo de configuración: `analisis/diputados/config.py`
- Script de verificación: `analizar_partidos_diputados.py`

**Resultados obtenidos:**
- 14 partidos políticos identificados correctamente
- Configuración actualizada y validada
- Eliminación de 7 partidos incorrectos
- Adición de 6 partidos que faltaban

---

### ACTIVIDAD 4: Análisis Electoral - Diputados Nacionales por Provincias

**Nombre de la actividad:** Procesamiento y análisis de datos electorales de diputados nacionales a nivel provincial

**Descripción:**  
Se realizó el análisis de los resultados de diputados nacionales de 1996 para las provincias de NAPO y PASTAZA. Se procesaron los datos de los 14 partidos políticos, calculando votos válidos, blancos, nulos y totales. Se corrigió el sistema de filtrado que usaba códigos numéricos por nombres de provincias. Se generó un archivo Excel mejorado con columnas dedicadas para cada tipo de voto.

**Fecha:** 26/12/2025

**Hora de inicio y fin:** 11:00 - 12:45 (1 hora 45 minutos)

**Capturas o fotos:**
- Archivo generado: `resultados/diputados/Resumen_Diputados_Napo_Pastaza.xlsx`
- Datos JSON: `resultados/diputados/provincias_diputados_1996.json`
- Archivo de análisis: `analisis/diputados/analisis_provincias.py`

**Resultados obtenidos:**
- 2 provincias analizadas (NAPO y PASTAZA)
- 14 partidos políticos procesados
- NAPO: 30,069 votos válidos, 4,560 blancos, 5,175 nulos (Total: 39,804)
- PASTAZA: 13,773 votos válidos, 2,378 blancos, 1,794 nulos (Total: 17,945)
- Partido ganador en ambas provincias: MUPP-NP (Pachakutik)
- Excel con columnas: VOTOS VALIDOS, VOTOS BLANCOS, VOTOS NULOS, TOTAL VOTOS

---

### ACTIVIDAD 5: Análisis Electoral - Diputados Nacionales por Cantones

**Nombre de la actividad:** Procesamiento y análisis de datos electorales de diputados nacionales a nivel cantonal (Pichincha)

**Descripción:**  
Se realizó el análisis detallado de los resultados de diputados nacionales de 1996 para los 8 cantones de la provincia de Pichincha. Se procesaron datos de los 14 partidos políticos para cada cantón: QUITO (745,279 votos), SANTO DOMINGO (91,117 votos), RUMIÑAHUI (26,046 votos), MEJIA (24,730 votos), CAYAMBE (23,543 votos), PEDRO MONCAYO (8,051 votos), SAN MIGUEL DE LOS BANCOS (4,786 votos) y PEDRO VICENTE MALDONADO (2,442 votos). Se corrigió el filtrado de provincia y se generó Excel mejorado.

**Fecha:** 26/12/2025

**Hora de inicio y fin:** 12:45 - 14:15 (1 hora 30 minutos)

**Capturas o fotos:**
- Archivo generado: `resultados/diputados/Resumen_Diputados_Cantones_Pichincha.xlsx`
- Datos JSON: `resultados/diputados/cantones_diputados_1996.json`
- Archivo de análisis: `analisis/diputados/analisis_cantones.py`

**Resultados obtenidos:**
- 8 cantones de Pichincha analizados
- 14 partidos políticos procesados por cantón
- Totales calculados: votos válidos, blancos, nulos y total por cada cantón
- Cantón con mayor participación: QUITO (745,279 votos)
- Excel con columnas: VOTOS VALIDOS, VOTOS BLANCOS, VOTOS NULOS, TOTAL VOTOS
- 127 filas de datos (8 cantones × ~16 filas cada uno)

---

## 📊 RESUMEN GENERAL DE ACTIVIDADES

### Tiempo Total Invertido
**6 horas 15 minutos** (08:00 - 14:15)

### Distribución del Tiempo
- Presidentes Segunda Vuelta - Provincias: 1h 15min
- Presidentes Segunda Vuelta - Cantones: 1h 15min
- Configuración Diputados: 30min
- Diputados - Provincias: 1h 45min
- Diputados - Cantones: 1h 30min

### Archivos Generados

#### Presidentes Segunda Vuelta
1. `Resumen_Segunda_Vuelta_Napo_Pastaza.xlsx`
2. `Resumen_Segunda_Vuelta_Cantones_Pichincha.xlsx`
3. `provincias_segunda_vuelta_1996.json`
4. `cantones_segunda_vuelta_1996.json`

#### Diputados Nacionales
1. `Resumen_Diputados_Napo_Pastaza.xlsx`
2. `Resumen_Diputados_Cantones_Pichincha.xlsx`
3. `provincias_diputados_1996.json`
4. `cantones_diputados_1996.json`

### Datos Procesados

#### Presidentes Segunda Vuelta
- **Provincias:** 2 (NAPO, PASTAZA)
- **Cantones:** 8 (Pichincha)
- **Candidatos:** 2

#### Diputados Nacionales
- **Provincias:** 2 (NAPO, PASTAZA)
- **Cantones:** 8 (Pichincha)
- **Partidos Políticos:** 14

### Correcciones Técnicas Realizadas
1. Actualización de configuración de partidos políticos (14 partidos correctos)
2. Corrección de filtrado de provincias (nombres en lugar de códigos)
3. Corrección de filtrado de cantones (nombres en lugar de códigos)
4. Mejora de estructura de archivos Excel (columnas dedicadas para tipos de votos)

---

## 🎯 LOGROS Y RESULTADOS

### Análisis Completados
✅ Presidentes Segunda Vuelta - Provincias (NAPO y PASTAZA)  
✅ Presidentes Segunda Vuelta - Cantones (8 cantones de Pichincha)  
✅ Diputados Nacionales - Provincias (NAPO y PASTAZA)  
✅ Diputados Nacionales - Cantones (8 cantones de Pichincha)

### Formato de Datos
✅ Archivos Excel con columnas estructuradas  
✅ Archivos JSON para integración programática  
✅ Datos validados y verificados  
✅ Porcentajes calculados correctamente

### Calidad del Trabajo
✅ Datos completos (votos válidos, blancos, nulos y totales)  
✅ Información por partido/candidato con porcentajes  
✅ Código modular y reutilizable  
✅ Documentación técnica generada

---

## 📝 OBSERVACIONES Y NOTAS

1. **Datos Fuente:** Se utilizaron archivos Excel oficiales de las elecciones de 1996
2. **Herramientas:** Python, pandas, openpyxl para procesamiento de datos
3. **Validación:** Todos los totales fueron verificados y validados
4. **Formato:** Se priorizó la claridad y facilidad de uso en los archivos Excel generados

---

## ✍️ FIRMAS Y VALIDACIÓN

**Responsable del Análisis:**  
Nombre: ___________________________  
Firma: ____________________________  
Fecha: 26/12/2025

**Supervisor/Tutor:**  
Nombre: ___________________________  
Firma: ____________________________  
Fecha: ___________________________

---

**Fin del Documento**
