# Documentación - Análisis Electoral por Parroquias 1996

## Resumen General

Este documento detalla el análisis electoral realizado para las elecciones de 1996 en Ecuador, específicamente para:
- **Primera Vuelta Presidencial**
- **Segunda Vuelta Presidencial**
- **Diputados Nacionales**

El análisis se enfoca en **59 parroquias específicas**: 12 de Pastaza y 47 de Pichincha.

---

## 📋 Actividades Realizadas

### Actividad 1: Análisis Primera Vuelta Presidencial

**Nombre de la actividad:** Extracción y análisis de votos por parroquia - Primera vuelta presidencial 1996

**Descripción:**
Se desarrolló un script en Python (`analisis_parroquias_pastaza_pichincha_detallado.py`) que realiza el análisis electoral completo de la primera vuelta presidencial. El script:

1. Carga los datos del archivo Excel de primera vuelta
2. Filtra las 12 parroquias específicas de Pastaza y 47 de Pichincha (en el orden proporcionado)
3. Extrae votos válidos, blancos, nulos y totales por cada parroquia
4. Calcula los votos obtenidos por cada uno de los 9 candidatos presidenciales en cada parroquia
5. Calcula porcentajes de cada candidato respecto a votos válidos
6. Genera 3 archivos Excel con diferentes formatos de presentación
7. Genera archivo JSON con la estructura completa de datos

El script procesa 59 parroquias y analiza los votos de 9 candidatos presidenciales, generando un total de 531 registros detallados (59 parroquias × 9 candidatos).

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 8:30 AM - 9:00 AM

**Script a ejecutar para captura:**
```bash
py analisis_parroquias_pastaza_pichincha_detallado.py
```

**Capturas o fotos:** 
> **NOTA:** Ejecutar el script anterior en la terminal y tomar captura de pantalla mostrando:
> - El proceso de carga de datos
> - El análisis de las parroquias de Pastaza
> - El análisis de las parroquias de Pichincha
> - El resumen final con totales por candidato
> - Los archivos generados

**Archivos generados:**
1. `Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx` (3 hojas)
2. `Votos_Validos_Blancos_Nulos_Por_Parroquia.xlsx`
3. `Votos_Por_Candidato_Transpuesto.xlsx`
4. `parroquias_pastaza_pichincha_detallado_1996.json`

**Resultados:**
- Total de parroquias analizadas: 59 (12 Pastaza + 47 Pichincha)
- Total de candidatos: 9
- Total de registros detallados: 531
- Archivos generados: 4

**Candidatos analizados:**
1. NOBOA RICARDO (PLRE-FRA)
2. PAZ RODRIGO (DP)
3. NEBOT JAIME (PSC)
4. BUCARAM ABDALÁ (PRE)
5. VARGAS FRANK (APRE)
6. CASTELLÓ JUAN (MPD)
7. EHLEARS FREDDY (MUPP-NP)
8. GALLARDO JOSÉ (UCI)
9. VELÁZQUEZ JACINTO (MITI)

---

### Actividad 2: Análisis Segunda Vuelta Presidencial

**Nombre de la actividad:** Extracción y análisis de votos por parroquia - Segunda vuelta presidencial 1996

**Descripción:**
Se desarrolló un script en Python (`analisis_segunda_vuelta_parroquias.py`) que realiza el análisis electoral de la segunda vuelta presidencial. El script:

1. Carga los datos del archivo Excel de segunda vuelta
2. Filtra las mismas 59 parroquias (12 de Pastaza y 47 de Pichincha) manteniendo el orden exacto
3. Extrae votos válidos, blancos, nulos y totales por cada parroquia
4. Calcula los votos obtenidos por cada uno de los 2 candidatos finalistas en cada parroquia
5. Calcula porcentajes de cada candidato respecto a votos válidos
6. Genera archivos Excel en formato detallado y transpuesto
7. Genera archivo JSON con la estructura completa

Posteriormente se ejecutó el script `generar_archivos_segunda_vuelta.py` para crear los formatos adicionales (votos válidos/blancos/nulos y formato transpuesto).

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 9:30 AM - 9:45 AM

**Scripts a ejecutar para capturas:**
```bash
# Script principal
py analisis_segunda_vuelta_parroquias.py

# Script de formatos adicionales
py generar_archivos_segunda_vuelta.py
```

**Capturas o fotos:**
> **NOTA:** Ejecutar los scripts anteriores en la terminal y tomar capturas mostrando:
> - La ejecución del script principal con el análisis de ambas provincias
> - La generación de archivos adicionales
> - El resumen final con totales por candidato

**Archivos generados:**
1. `Segunda_Vuelta_Votos_Por_Candidato.xlsx` (3 hojas)
2. `Segunda_Vuelta_Votos_Validos_Blancos_Nulos.xlsx`
3. `Segunda_Vuelta_Votos_Transpuesto.xlsx`
4. `segunda_vuelta_parroquias_1996.json`

**Resultados:**
- Total de parroquias analizadas: 59 (12 Pastaza + 47 Pichincha)
- Total de candidatos: 2
- Total de registros detallados: 118 (59 parroquias × 2 candidatos)
- Archivos generados: 4

**Candidatos analizados:**
1. BUCARAM ABDALÁ (PRE)
2. NEBOT JAIME (PSC)

---

### Actividad 3: Análisis Diputados Nacionales

**Nombre de la actividad:** Extracción y análisis de votos por parroquia - Diputados nacionales 1996

**Descripción:**
Se desarrolló un script en Python (`analisis_diputados_parroquias.py`) que realiza el análisis electoral de diputados nacionales. El script:

1. Carga los datos del archivo Excel de diputados nacionales
2. Filtra las mismas 59 parroquias (12 de Pastaza y 47 de Pichincha) en el orden especificado
3. Extrae votos válidos, blancos, nulos y totales por cada parroquia
4. Calcula los votos obtenidos por cada uno de los 14 partidos/listas en cada parroquia
5. Calcula porcentajes de cada partido respecto a votos válidos
6. Genera archivos Excel con análisis detallado por partido
7. Genera archivo JSON con toda la información estructurada

Posteriormente se ejecutó el script `generar_archivos_diputados.py` para crear los formatos adicionales (votos válidos/blancos/nulos y formato transpuesto con 14 columnas de partidos).

**Fecha:** 28 de diciembre de 2025

**Hora de inicio y fin:** 9:45 AM - 10:05 AM

**Scripts a ejecutar para capturas:**
```bash
# Script principal
py analisis_diputados_parroquias.py

# Script de formatos adicionales
py generar_archivos_diputados.py
```

**Capturas o fotos:**
> **NOTA:** Ejecutar los scripts anteriores en la terminal y tomar capturas mostrando:
> - La ejecución del script principal con el análisis de las 59 parroquias
> - El top 10 de partidos más votados
> - La generación de archivos en formato transpuesto
> - La vista previa del formato transpuesto

**Archivos generados:**
1. `Diputados_Votos_Por_Partido.xlsx` (3 hojas)
2. `Diputados_Votos_Validos_Blancos_Nulos.xlsx`
3. `Diputados_Votos_Transpuesto.xlsx`
4. `diputados_parroquias_1996.json`

**Resultados:**
- Total de parroquias analizadas: 59 (12 Pastaza + 47 Pichincha)
- Total de partidos/listas: 14
- Total de registros detallados: 826 (59 parroquias × 14 partidos)
- Archivos generados: 4

**Partidos/Listas analizados:**
1. PCE - Partido Comunista Ecuatoriano
2. CFP - Concentración de Fuerzas Populares
3. DP - Democracia Popular
4. PSC - Partido Social Cristiano
5. PRE - Partido Roldosista Ecuatoriano
6. AN - Alianza Nacional
7. ID - Izquierda Democrática
8. APRE - Acción Popular Revolucionaria Ecuatoriana
9. MPD - Movimiento Popular Democrático
10. UPL - Unión Popular Latinoamericana
11. PSE - Partido Socialista Ecuatoriano
12. MUPP-NP - Movimiento Unidad Plurinacional Pachakutik - Nuevo País
13. MITI - Movimiento Independiente Tierra Indígena
14. PLRE-FRA - Partido Liberal Radical Ecuatoriano - Frente Radical Alfarista

---

## 📊 Parroquias Analizadas

### Pastaza (12 parroquias - en orden específico)

1. 3180
2. 3195
3. 3785
4. 3985
5. 4005
6. 4205
7. 4510
8. 5825
9. 2310
10. 3840
11. 5650
12. 6395

### Pichincha (47 parroquias - en orden específico)

1. 30
2. 80
3. 195
4. 430
5. 440
6. 625
7. 725
8. 855
9. 865
10. 1400
11. 1440
12. 1475
13. 2055
14. 2265
15. 2275
16. 2525
17. 2530
18. 2540
19. 2560
20. 2690
21. 2825
22. 2855
23. 2895
24. 2925
25. 2980
26. 2985
27. 3100
28. 3325
29. 3475
30. 3925
31. 4085
32. 4290
33. 4325
34. 5015
35. 5110
36. 5220
37. 5235
38. 5260
39. 5325
40. 5410
41. 5435
42. 5530
43. 5535
44. 5540
45. 5575
46. 5935
47. 5985

**NOTA IMPORTANTE:** El orden de las parroquias se mantiene exactamente como fue especificado, sin ningún tipo de ordenamiento alfabético o numérico.

---

## 📁 Archivos Generados

### Primera Vuelta Presidencial

#### 1. `Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx`
**Descripción:** Archivo principal con análisis completo
**Hojas:**
- **Detalle_Por_Candidato**: 531 registros (59 parroquias × 9 candidatos)
  - Columnas: Provincia, Codigo_Parroquia, Parroquia, Candidato, Partido, Nombre_Completo, Votos, Porcentaje
- **Resumen_General**: 59 registros (totales por parroquia)
  - Columnas: Provincia, Codigo_Parroquia, Parroquia, Votos_Validos, Votos_Blancos, Votos_Nulos, Total_Votos
- **Totales_Por_Candidato**: 9 registros (suma total por candidato)
  - Columnas: Candidato, Partido, Votos

#### 2. `Votos_Validos_Blancos_Nulos_Por_Parroquia.xlsx`
**Descripción:** Resumen de votos válidos, blancos, nulos y totales por parroquia
**Contenido:** 59 parroquias con sus totales de votos

#### 3. `Votos_Por_Candidato_Transpuesto.xlsx`
**Descripción:** Formato transpuesto - parroquias en filas, candidatos en columnas
**Estructura:** 59 filas (parroquias) × 12 columnas (Provincia, Codigo_Parroquia, Parroquia + 9 candidatos)

#### 4. `parroquias_pastaza_pichincha_detallado_1996.json`
**Descripción:** Datos en formato JSON estructurado por provincia y parroquia

---

### Segunda Vuelta Presidencial

#### 1. `Segunda_Vuelta_Votos_Por_Candidato.xlsx`
**Descripción:** Archivo principal con análisis completo
**Hojas:**
- **Detalle_Por_Candidato**: 118 registros (59 parroquias × 2 candidatos)
- **Resumen_General**: 59 registros (totales por parroquia)
- **Totales_Por_Candidato**: 2 registros (suma total por candidato)

#### 2. `Segunda_Vuelta_Votos_Validos_Blancos_Nulos.xlsx`
**Descripción:** Resumen de votos válidos, blancos, nulos y totales por parroquia

#### 3. `Segunda_Vuelta_Votos_Transpuesto.xlsx`
**Descripción:** Formato transpuesto - parroquias en filas, candidatos en columnas
**Estructura:** 59 filas (parroquias) × 5 columnas (Provincia, Codigo_Parroquia, Parroquia + 2 candidatos)

#### 4. `segunda_vuelta_parroquias_1996.json`
**Descripción:** Datos en formato JSON estructurado

---

### Diputados Nacionales

#### 1. `Diputados_Votos_Por_Partido.xlsx`
**Descripción:** Archivo principal con análisis completo
**Hojas:**
- **Detalle_Por_Partido**: 826 registros (59 parroquias × 14 partidos)
- **Resumen_General**: 59 registros (totales por parroquia)
- **Totales_Por_Partido**: 14 registros (suma total por partido)

#### 2. `Diputados_Votos_Validos_Blancos_Nulos.xlsx`
**Descripción:** Resumen de votos válidos, blancos, nulos y totales por parroquia

#### 3. `Diputados_Votos_Transpuesto.xlsx`
**Descripción:** Formato transpuesto - parroquias en filas, partidos en columnas
**Estructura:** 59 filas (parroquias) × 17 columnas (Provincia, Codigo_Parroquia, Parroquia + 14 partidos)

#### 4. `diputados_parroquias_1996.json`
**Descripción:** Datos en formato JSON estructurado

---

## 🔧 Scripts Creados

### Scripts Principales

1. **`analisis_parroquias_pastaza_pichincha_detallado.py`**
   - Análisis de primera vuelta presidencial
   - Genera archivos Excel y JSON con detalle completo

2. **`analisis_segunda_vuelta_parroquias.py`**
   - Análisis de segunda vuelta presidencial
   - Genera archivos Excel y JSON con detalle completo

3. **`analisis_diputados_parroquias.py`**
   - Análisis de diputados nacionales
   - Genera archivos Excel y JSON con detalle completo

### Scripts de Generación de Formatos

4. **`generar_votos_transpuesto.py`**
   - Genera formato transpuesto para primera vuelta presidencial

5. **`generar_archivos_segunda_vuelta.py`**
   - Genera archivos adicionales para segunda vuelta

6. **`generar_archivos_diputados.py`**
   - Genera archivos adicionales para diputados

### Scripts de Verificación

7. **`verificar_orden_parroquias.py`**
   - Verifica que el orden de parroquias sea correcto

8. **`verificar_orden_transpuesto.py`**
   - Verifica el orden en archivos transpuestos

9. **`ver_resumen_parroquias.py`**
   - Muestra resumen rápido de resultados

---

## 📈 Datos Extraídos

Para cada parroquia se extrajo:

### Totales Generales
- **Votos Válidos**: Total de votos válidos emitidos
- **Votos Blancos**: Total de votos en blanco
- **Votos Nulos**: Total de votos nulos
- **Total Votos**: Suma de válidos + blancos + nulos

### Detalle por Candidato/Partido
- **Votos**: Cantidad de votos obtenidos
- **Porcentaje**: Porcentaje respecto a votos válidos de esa parroquia

---

## 🎯 Características Importantes

1. **Orden Preservado**: Las parroquias mantienen el orden exacto especificado, sin ordenamiento alfabético ni numérico.

2. **Formato Transpuesto**: Los archivos transpuestos facilitan la visualización con:
   - Parroquias en filas (eje vertical)
   - Candidatos/Partidos en columnas (eje horizontal)

3. **Múltiples Formatos**: Datos disponibles en:
   - Excel (formato detallado y transpuesto)
   - JSON (para procesamiento programático)

4. **Validación**: Todos los datos fueron validados para asegurar consistencia entre:
   - Suma de votos por candidato = Votos válidos
   - Votos válidos + blancos + nulos = Total votos

---

## 📍 Ubicación de Archivos

Todos los archivos generados se encuentran en:
```
c:\Users\VIVTUS\Desktop\Vinculacion\codigo\Vinculacion\resultados\
```

---

## 🔍 Fuentes de Datos

- **Primera Vuelta Presidencial**: `Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx`
- **Segunda Vuelta Presidencial**: `Datos-Presidentes-Completos/Segunda Vuelta/1996 - Presidentes - segunda vuelta.xlsx`
- **Diputados Nacionales**: `Datos-Diputados-Completos/1996 - Diputados - nacionales.xlsx`

---

## ✅ Validaciones Realizadas

1. ✓ Verificación de que todas las parroquias especificadas tienen datos
2. ✓ Validación del orden correcto de parroquias
3. ✓ Comprobación de totales (suma de votos por candidato = votos válidos)
4. ✓ Verificación de integridad de datos (sin valores nulos o negativos)
5. ✓ Confirmación de formato transpuesto correcto

---

## 📝 Notas Adicionales

- El análisis se realizó sin modificar ningún código existente del proyecto
- Todos los scripts son standalone y pueden ejecutarse independientemente
- Los archivos JSON permiten fácil integración con otras herramientas
- El formato transpuesto facilita la visualización y análisis comparativo

---

**Fecha de generación:** 28 de diciembre de 2025  
**Análisis realizado por:** Sistema de Análisis Electoral  
**Versión:** 1.0
