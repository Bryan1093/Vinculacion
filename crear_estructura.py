"""
Script para crear la estructura de directorios del proyecto
Ejecutar este script para crear todas las carpetas necesarias de forma segura
"""
import os

# Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Definir estructura de directorios
DIRECTORIOS = [
    # Datos
    'datos/presidentes/primera_vuelta',
    'datos/presidentes/segunda_vuelta',
    'datos/diputados',
    
    # Análisis
    'analisis/comun',
    'analisis/presidentes',
    'analisis/diputados',
    
    # Resultados
    'resultados/presidentes',
    'resultados/diputados',
]

def crear_estructura():
    """Crea la estructura de directorios del proyecto"""
    print("=" * 80)
    print("CREANDO ESTRUCTURA DE DIRECTORIOS")
    print("=" * 80)
    print()
    
    for directorio in DIRECTORIOS:
        ruta_completa = os.path.join(BASE_DIR, directorio)
        try:
            os.makedirs(ruta_completa, exist_ok=True)
            print(f"✓ Creado: {directorio}")
        except Exception as e:
            print(f"✗ Error al crear {directorio}: {e}")
    
    print()
    print("=" * 80)
    print("ESTRUCTURA CREADA EXITOSAMENTE")
    print("=" * 80)
    print()
    print("Próximos pasos:")
    print("1. Ejecutar 'py migrar_archivos.py' para mover los archivos existentes")
    print("2. Ejecutar 'py main_presidentes.py' para probar el análisis de presidentes")

if __name__ == "__main__":
    crear_estructura()
