# Análisis de Parroquias - Primera Vuelta Presidencial 1996

## Resumen del Análisis Realizado

Este análisis extrae los votos válidos, blancos, nulos y totales, así como el detalle de votos por candidato/partido político para:

### Parroquias Analizadas

**PASTAZA - 12 Parroquias Específicas (en orden):**
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

**PICHINCHA - 47 Parroquias Específicas (en orden):**
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

**IMPORTANTE:** El orden de las parroquias se mantiene exactamente como fue proporcionado, sin ordenamiento alfabético ni numérico.

---

## Archivos Generados

### 1. Excel Principal: `Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx`

Este archivo contiene **3 hojas**:

#### Hoja 1: "Detalle_Por_Candidato"
Contiene el detalle completo de votos de cada candidato en cada parroquia.

**Columnas:**
- `Provincia`: PASTAZA o PICHINCHA
- `Codigo_Parroquia`: Código numérico de la parroquia
- `Parroquia`: Nombre de la parroquia
- `Candidato`: Nombre del candidato
- `Partido`: Siglas del partido político
- `Nombre_Completo`: Nombre completo del candidato
- `Votos`: Cantidad de votos obtenidos
- `Porcentaje`: Porcentaje respecto a votos válidos de esa parroquia

**Total de registros:** 531 (59 parroquias × 9 candidatos)

#### Hoja 2: "Resumen_General"
Contiene los totales de votos por parroquia (válidos, blancos, nulos y total).

**Columnas:**
- `Provincia`: PASTAZA o PICHINCHA
- `Codigo_Parroquia`: Código numérico de la parroquia
- `Parroquia`: Nombre de la parroquia
- `Votos_Validos`: Total de votos válidos
- `Votos_Blancos`: Total de votos en blanco
- `Votos_Nulos`: Total de votos nulos
- `Total_Votos`: Suma total de todos los votos

**Total de registros:** 59 parroquias (12 de Pastaza + 47 de Pichincha)

#### Hoja 3: "Totales_Por_Candidato"
Contiene la suma total de votos por candidato en todas las parroquias analizadas.

**Columnas:**
- `Candidato`: Nombre del candidato
- `Partido`: Siglas del partido político
- `Votos`: Total de votos en las 59 parroquias

**Total de registros:** 9 candidatos

---

### 2. JSON: `parroquias_pastaza_pichincha_detallado_1996.json`

Archivo JSON estructurado con toda la información organizada por provincia y parroquia.

**Estructura:**
```json
{
  "PASTAZA": {
    "codigo_parroquia": {
      "nombre": "PARROQUIA_XXXX",
      "votos_validos": 0,
      "votos_blancos": 0,
      "votos_nulos": 0,
      "total_votos": 0,
      "candidatos": {
        "CANDIDATO": {
          "partido": "XXX",
          "votos": 0,
          "porcentaje": 0.00
        }
      }
    }
  },
  "PICHINCHA": { ... }
}
```

---

## Candidatos Analizados

1. **NOBOA RICARDO** - PLRE-FRA (Partido Liberal Radical Ecuatoriano - Frente Radical Alfarista)
2. **PAZ RODRIGO** - DP (Democracia Popular)
3. **NEBOT JAIME** - PSC (Partido Social Cristiano)
4. **BUCARAM ABDALÁ** - PRE (Partido Roldosista Ecuatoriano)
5. **VARGAS FRANK** - APRE (Acción Popular Revolucionaria Ecuatoriana)
6. **CASTELLÓ JUAN** - MPD (Movimiento Popular Democrático)
7. **EHLEARS FREDDY** - MUPP-NP (Movimiento Unidad Plurinacional Pachakutik - Nuevo País)
8. **GALLARDO JOSÉ** - UCI (Unión de Ciudadanos Independientes)
9. **VELÁZQUEZ JACINTO** - MITI (Movimiento Independiente de Trabajadores e Indígenas)

---

## Scripts Creados

### Script Principal
**Archivo:** `analisis_parroquias_pastaza_pichincha_detallado.py`

Este es el script principal que realiza todo el análisis. Ejecutar con:
```bash
py analisis_parroquias_pastaza_pichincha_detallado.py
```

**Funcionalidades:**
- Carga los datos del archivo Excel de presidentes primera vuelta 1996
- Filtra las 12 parroquias específicas de Pastaza
- Filtra las primeras 47 parroquias de Pichincha
- Calcula votos válidos, blancos, nulos y totales por parroquia
- Calcula votos por candidato en cada parroquia
- Genera archivos Excel y JSON con los resultados
- Muestra resumen en consola

### Script de Visualización
**Archivo:** `ver_resumen_parroquias.py`

Script para ver un resumen rápido de los resultados. Ejecutar con:
```bash
py ver_resumen_parroquias.py
```

**Muestra:**
- Información general del análisis
- Totales generales de votos
- Totales por candidato/partido
- Lista de parroquias analizadas
- Top 5 candidatos en Pastaza
- Top 5 candidatos en Pichincha

---

## Ubicación de Resultados

Todos los archivos de resultados se guardan en:
```
c:\Users\VIVTUS\Desktop\Vinculacion\codigo\Vinculacion\resultados\
```

---

## Notas Importantes

1. **No se modificó ningún código existente** - Todos los scripts son nuevos y standalone
2. **Los datos se extraen de:** `Datos-Presidentes-Completos/Primera Vuelta/1996 - Presidentes - primera vuelta.xlsx`
3. **El análisis incluye TODOS los candidatos** que participaron en la primera vuelta
4. **Los porcentajes se calculan sobre votos válidos** de cada parroquia
5. **Los códigos de parroquia son los originales** del archivo de datos

---

## Cómo Usar los Resultados

### Para ver datos de una parroquia específica:
1. Abrir `Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx`
2. Ir a la hoja "Detalle_Por_Candidato"
3. Filtrar por `Codigo_Parroquia` o `Provincia`

### Para ver totales generales:
1. Ir a la hoja "Resumen_General" para totales por parroquia
2. Ir a la hoja "Totales_Por_Candidato" para suma total por candidato

### Para análisis programático:
- Usar el archivo JSON `parroquias_pastaza_pichincha_detallado_1996.json`
- Estructura fácil de parsear y procesar

---

**Fecha de generación:** 28 de diciembre de 2025
**Análisis de:** Primera Vuelta Presidencial 1996
