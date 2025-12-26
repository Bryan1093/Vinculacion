# Análisis Electoral Ecuador 1996 - Primera Vuelta

Sistema profesional de análisis de datos electorales para las elecciones presidenciales de Ecuador 1996 (Primera Vuelta). Analiza resultados a nivel de **provincias**, **cantones** y **parroquias**, generando reportes en formato Excel y JSON.

## 🎯 Características

- ✅ Análisis a tres niveles geográficos (provincias, cantones, parroquias)
- ✅ Cálculo automático de votos y porcentajes por candidato
- ✅ Validación de datos contra fuente original
- ✅ Exportación a Excel y JSON con estructura estandarizada
- ✅ Arquitectura modular y reutilizable
- ✅ Identificación automática del ganador por región

## 📁 Estructura del Proyecto

```
codigo/
├── analisis_electoral_1996/      # Paquete principal
│   ├── __init__.py
│   ├── config.py                 # Configuración y constantes
│   ├── data_loader.py            # Carga y filtrado de datos
│   ├── utils.py                  # Utilidades compartidas
│   ├── json_exporter.py          # Exportación a JSON
│   ├── analisis_provincias.py    # Análisis por provincias
│   ├── analisis_cantones.py      # Análisis por cantones
│   └── analisis_parroquias.py    # Análisis por parroquias
├── Datos-Presidentes-Completos/  # Datos fuente
│   └── Primera Vuelta/
│       └── 1996 - Presidentes - primera vuelta.xlsx
├── resultados/                   # Archivos de salida
├── main.py                       # Script principal
└── requirements.txt              # Dependencias
```

## 🚀 Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Uso

### Ejecutar análisis completo

```bash
cd c:\Users\VIVTUS\Desktop\Vinculacion\codigo
py main.py
```

Este comando ejecutará:
1. Análisis por provincias (Zamora Chinchipe, Galápagos, Sucumbíos)
2. Análisis por cantones (13 cantones de Guayas)
3. Análisis por parroquias (2 parroquias de Pastaza)

### Ejecutar análisis individual

```python
from analisis_electoral_1996.analisis_provincias import analizar_provincias

# Solo análisis de provincias
df_resultados, df_original = analizar_provincias()
```

## 📊 Archivos Generados

### Excel Files
- `Votos_Por_Candidato_Y_Provincia.xlsx` - Resultados por provincia
- `Votos_Por_Candidato_Y_Canton.xlsx` - Resultados por cantón
- `Votos_Por_Candidato_Y_Parroquia.xlsx` - Resultados por parroquia

### JSON Files

Estructura estandarizada para cada nivel geográfico:

```json
{
  "CODPRO": "19",
  "PROVINCIA": "ZAMORA CHINCHIPE",
  "votos_validos": 18916,
  "votos_blancos": 1234,
  "votos_nulos": 567,
  "votos_total": 20717,
  "ganador": "PRE",
  "resultados": {
    "PRE": {
      "candidato": "ABDALÁ BUCARAM ORTIZ",
      "votos": 6125,
      "porcentaje": 32.38
    },
    "PSC": {
      "candidato": "JAIME NEBOT SAADI",
      "votos": 3582,
      "porcentaje": 18.94
    }
  }
}
```

## 👥 Candidatos Analizados

1. **RICARDO NOBOA BEJARANO** (PLRE-FRA)
2. **RODRIGO PAZ DELGADO** (DP)
3. **JAIME NEBOT SAADI** (PSC)
4. **ABDALÁ BUCARAM ORTIZ** (PRE)
5. **FRANK VARGAS PAZZOS** (APRE)
6. **JUAN JOSÉ CASTELLÓ MANZANO** (MPD)
7. **FREDDY EHLERS ZURITA** (MUPP-NP)
8. **JOSÉ GALLARDO ZAVALA** (UCI)
9. **JACINTO VELÁZQUEZ ROSALES** (MITI)

## 🔍 Validación de Datos

El sistema incluye validación automática que compara:
- Votos calculados por candidato
- Votos totales del dataset original
- Muestra ✅ si coinciden o ⚠️ si hay discrepancias

## 📝 Notas Técnicas

- Los porcentajes se calculan sobre `votos_validos`, no sobre `votos_total`
- Los códigos de provincia/cantón/parroquia mantienen formato original
- El ganador se determina por mayor número de votos en cada región
- Todos los archivos JSON usan codificación UTF-8

## 🛠️ Desarrollo

### Agregar nuevas provincias

Editar `config.py`:
```python
PROVINCIAS_SELECCIONADAS = {
    'NUEVA_PROVINCIA': 'CODIGO',
    # ...
}
```

### Personalizar candidatos

Editar `config.py` en la sección `CANDIDATOS`.

## 📄 Licencia

Proyecto educativo para análisis de datos electorales históricos de Ecuador.

---

**Desarrollado para:** Análisis Electoral Ecuador 1996  
**Versión:** 1.0.0
