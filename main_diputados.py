"""
Script principal para ejecutar análisis electoral de DIPUTADOS NACIONALES 1996
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analisis.diputados import config
from analisis.diputados.data_loader import cargar_datos
from analisis.diputados.analisis_provincias import analizar_provincias
from analisis.diputados.analisis_cantones import analizar_cantones

def main():
    """Ejecuta todos los análisis de diputados"""
    print("=" * 80)
    print("                    ANÁLISIS ELECTORAL ECUADOR 1996")
    print("                    DIPUTADOS NACIONALES")
    print("=" * 80)
    print("\n")
    
    # Análisis por provincias
    print("[1/2] Ejecutando análisis por provincias...")
    analizar_provincias()
    print()
    
    # Análisis por cantones
    print("[2/2] Ejecutando análisis por cantones (Pichincha)...")
    analizar_cantones()
    print()
    
    print("=" * 80)
    print("                         ANÁLISIS COMPLETADO")
    print("=" * 80)
    print("✓ Todos los análisis se ejecutaron exitosamente")
    print()
    print(f"📁 Archivos generados en el directorio 'resultados/diputados/':")
    print("   • Votos_Por_Partido_Y_Provincia.xlsx")
    print("   • Votos_Por_Partido_Y_Canton.xlsx")
    print("   • provincias_diputados_1996.json")
    print("   • cantones_diputados_1996.json")
    print("=" * 80)
    print()
    print("💡 Para ver los resultados, ejecuta:")
    print("   py ver_resultados_diputados.py")

if __name__ == "__main__":
    main()

