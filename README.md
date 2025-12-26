# Análisis Electoral Ecuador 1996

Proyecto de análisis electoral para las elecciones presidenciales y de diputados de Ecuador 1996.

## 📁 Estructura del Proyecto

```
codigo/
├── datos/
│   ├── presidentes/          # Datos electorales de presidentes
│   │   ├── primera_vuelta/
│   │   └── segunda_vuelta/
│   └── diputados/            # Datos electorales de diputados
│
├── analisis/
│   ├── comun/                # Código compartido
│   ├── presidentes/          # Análisis de presidentes
│   └── diputados/            # Análisis de diputados
│
├── resultados/
│   ├── presidentes/          # Resultados de presidentes
│   └── diputados/            # Resultados de diputados
│
├── scripts/                  # Scripts de utilidad
│
├── main_presidentes.py       # Ejecutar análisis de presidentes
├── main_diputados.py         # Ejecutar análisis de diputados
├── ver_resultados_presidentes.py   # Ver resultados de presidentes
└── ver_resultados_diputados.py     # Ver resultados de diputados
```

## 🚀 Inicio Rápido

### 1. Configurar el Proyecto

Primero, crea la estructura de directorios y migra los archivos existentes:

```bash
# Crear estructura de carpetas
py crear_estructura.py

# Migrar archivos existentes (NO elimina los originales)
py migrar_archivos.py
```

### 2. Análisis de Presidentes

```bash
# Ejecutar análisis completo
py main_presidentes.py

# Ver resultados
py ver_resultados_presidentes.py
```

### 3. Análisis de Diputados

```bash
# Ejecutar análisis completo (cuando esté disponible)
py main_diputados.py

# Ver resultados
py ver_resultados_diputados.py
```

## 📊 Análisis Disponibles

### Presidentes
- ✅ Análisis por provincias (NAPO y PASTAZA)
- ✅ Análisis por cantones (Pichincha)
- ✅ Análisis por parroquias (Pastaza)
- ✅ Generación de archivos Excel y JSON

### Diputados
- ⏳ Pendiente (estructura lista, esperando datos)

## ⚙️ Configuración

### Cambiar Archivo de Datos

Para analizar un archivo diferente, edita el archivo de configuración correspondiente:

**Presidentes:** `analisis/presidentes/config.py`
```python
NOMBRE_ARCHIVO = '1996 - Presidentes - primera vuelta.xlsx'
```

**Diputados:** `analisis/diputados/config.py`
```python
NOMBRE_ARCHIVO = 'tu_archivo_diputados.xlsx'
```

### Seleccionar Provincias

Edita `PROVINCIAS_SELECCIONADAS` en el archivo de configuración:

```python
PROVINCIAS_SELECCIONADAS = {
    'NAPO': '15',
    'PASTAZA': '16',
    # Agregar más provincias según necesidad
}
```

## 📦 Dependencias

```bash
pip install -r requirements.txt
```

Dependencias principales:
- pandas
- openpyxl

## 📝 Resultados Generados

### Archivos Excel
- `Votos_Por_Candidato_Y_Provincia.xlsx` - Votos y porcentajes por provincia
- `Votos_Por_Candidato_Y_Canton.xlsx` - Votos y porcentajes por cantón
- `Votos_Por_Candidato_Y_Parroquia.xlsx` - Votos y porcentajes por parroquia

### Archivos JSON
- `provincias_1996.json` - Datos estructurados por provincia
- `cantones_1996.json` - Datos estructurados por cantón
- `parroquias_1996.json` - Datos estructurados por parroquia

## 🔧 Scripts de Utilidad

En la carpeta `scripts/`:
- `explore_data.py` - Explorar estructura de datos
- `obtener_cantones_pichincha.py` - Listar cantones de Pichincha
- `obtener_nombres_cantones.py` - Obtener nombres de cantones
- `verificar_orden_candidatos.py` - Verificar orden de candidatos

## 📚 Uso Avanzado

### Agregar Nuevo Análisis

1. Crear módulo en `analisis/presidentes/` o `analisis/diputados/`
2. Importar configuración: `from analisis.presidentes import config`
3. Usar funciones de carga de datos
4. Guardar resultados en `config.RESULTS_DIR`

### Compartir con Otros

Para que otra persona use este código con diferentes datos:

1. Compartir toda la carpeta del proyecto
2. Indicar que coloquen su archivo en `datos/presidentes/` o `datos/diputados/`
3. Actualizar `NOMBRE_ARCHIVO` en el `config.py` correspondiente
4. Ejecutar `py main_presidentes.py` o `py main_diputados.py`

## ⚠️ Notas Importantes

- Los scripts de migración **NO eliminan** los archivos originales
- Verifica que todo funcione antes de eliminar archivos antiguos
- Los resultados se guardan en carpetas separadas por tipo de elección
- Cada análisis (presidentes/diputados) es independiente

## 🤝 Contribuir

Para agregar análisis de diputados:

1. Colocar archivo de datos en `datos/diputados/`
2. Actualizar `analisis/diputados/config.py` con candidatos/partidos
3. Crear módulos de análisis siguiendo el patrón de presidentes
4. Actualizar `main_diputados.py` y `ver_resultados_diputados.py`

---

**Versión:** 2.0  
**Última actualización:** Diciembre 2025
