# 📋 GUÍA RÁPIDA: Cómo Cambiar Provincias y Cantones

## 🎯 Para cambiar las PROVINCIAS a analizar:

### Archivo: `analisis/presidentes_segunda_vuelta/config.py`

Busca esta sección (línea ~62):

```python
# Provincias a analizar (las mismas que primera vuelta)
PROVINCIAS_SELECCIONADAS = {
    'NAPO': '15',
    'PASTAZA': '16',
}
```

**Cambia a las provincias que quieras:**

```python
PROVINCIAS_SELECCIONADAS = {
    'GUAYAS': '09',
    'AZUAY': '01',
    'PICHINCHA': '17',
}
```

---

## 🎯 Para cambiar la PROVINCIA de CANTONES:

### Archivo: `analisis/presidentes_segunda_vuelta/config.py`

Busca esta sección (línea ~79):

```python
# ========== CONFIGURACIÓN SIMPLE DE CANTONES ==========
# Solo cambia esta línea para analizar cantones de otra provincia:
PROVINCIA_PARA_CANTONES = 'PICHINCHA'  # Cambia a 'GUAYAS', 'AZUAY', etc.
# ======================================================
```

**Cambia solo esa línea:**

```python
PROVINCIA_PARA_CANTONES = 'GUAYAS'  # Ahora analizará cantones de GUAYAS
```

---

## ✅ Ejecutar el análisis:

```bash
py main_presidentes_segunda_vuelta.py
```

---

## 📝 Notas importantes:

1. **Los nombres de provincia deben estar en MAYÚSCULAS** y exactamente como aparecen en el Excel
2. **Cierra los archivos Excel** antes de ejecutar el script
3. Los resultados se guardan en `resultados/segunda_vuelta/`
4. Los cantones se detectan automáticamente, no necesitas definir el mapeo

---

## 🗺️ Lista de provincias disponibles:

```
AZUAY, BOLÍVAR, CAÑAR, CARCHI, COTOPAXI, CHIMBORAZO, 
EL ORO, ESMERALDAS, GUAYAS, IMBABURA, LOJA, LOS RÍOS, 
MANABÍ, MORONA SANTIAGO, NAPO, PASTAZA, PICHINCHA, 
TUNGURAHUA, ZAMORA CHINCHIPE, GALÁPAGOS, SUCUMBÍOS, 
ORELLANA, SANTO DOMINGO DE LOS TSÁCHILAS, SANTA ELENA
```

---

## 💡 Ejemplo completo:

Para analizar **GUAYAS** (provincias) y **AZUAY** (cantones):

```python
# En config.py

PROVINCIAS_SELECCIONADAS = {
    'GUAYAS': '09',
}

PROVINCIA_PARA_CANTONES = 'AZUAY'
```

Luego ejecuta:
```bash
py main_presidentes_segunda_vuelta.py
```

¡Listo! 🎉
