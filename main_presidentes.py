"""
Script principal para ejecutar análisis electoral de PRESIDENTES 1996
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Usar los módulos originales de analisis_electoral_1996
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from analisis_electoral_1996 import config
from analisis_electoral_1996.analisis_provincias import analizar_provincias
from analisis_electoral_1996.analisis_cantones import analizar_cantones
from analisis_electoral_1996.analisis_parroquias import analizar_parroquias

def main():
    """Ejecuta todos los análisis de presidentes"""
    print("=" * 80)
    print("                    ANÁLISIS ELECTORAL ECUADOR 1996")
    print("                         PRESIDENTES - PRIMERA VUELTA")
    print("=" * 80)
    print("\n")
    
    # Análisis por provincias
    print("[1/3] Ejecutando análisis por provincias...")
    analizar_provincias()
    print()
    
    # Análisis por cantones
    print("[2/3] Ejecutando análisis por cantones...")
    analizar_cantones()
    print()
    
    # Análisis por parroquias
    print("[3/3] Ejecutando análisis por parroquias...")
    analizar_parroquias()
    print()
    
    print("=" * 80)
    print("                         ANÁLISIS COMPLETADO")
    print("=" * 80)
    print("✓ Todos los análisis se ejecutaron exitosamente")
    print()
    print(f"📁 Archivos generados en el directorio 'resultados/':")
    print("   • Votos_Por_Candidato_Y_Provincia.xlsx")
    print("   • Votos_Por_Candidato_Y_Canton.xlsx")
    print("   • Votos_Por_Candidato_Y_Parroquia.xlsx")
    print("   • provincias_1996.json")
    print("   • cantones_1996.json")
    print("   • parroquias_1996.json")
    print("=" * 80)
    print()
    print("💡 Para ver los resultados, ejecuta:")
    print("   py ver_resultados_presidentes.py")

if __name__ == "__main__":
    main()

