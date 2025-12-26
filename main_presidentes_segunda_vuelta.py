"""
Script principal para ejecutar análisis electoral de PRESIDENTES - SEGUNDA VUELTA 1996
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analisis.presidentes_segunda_vuelta import config
from analisis.presidentes_segunda_vuelta.data_loader import cargar_datos
from analisis.presidentes_segunda_vuelta.analisis_provincias import analizar_provincias
from analisis.presidentes_segunda_vuelta.analisis_cantones import analizar_cantones

def main():
    """Ejecuta todos los análisis de segunda vuelta presidencial"""
    print("=" * 80)
    print("                    ANÁLISIS ELECTORAL ECUADOR 1996")
    print("                    PRESIDENTES - SEGUNDA VUELTA")
    print("=" * 80)
    print("\n")
    
    # Análisis por provincias
    print("[1/2] Ejecutando análisis por provincias...")
    analizar_provincias()
    print()
    
    # Análisis por cantones
    print(f"[2/2] Ejecutando análisis por cantones ({config.PROVINCIA_PARA_CANTONES})...")
    analizar_cantones()
    print()
    
    print("=" * 80)
    print("                         ANÁLISIS COMPLETADO")
    print("=" * 80)
    print("✓ Todos los análisis se ejecutaron exitosamente")
    print()
    print(f"📁 Archivos generados en el directorio 'resultados/segunda_vuelta/':")
    print("   • Votos_Por_Candidato_Y_Provincia_2daVuelta.xlsx")
    print("   • Totales_Por_Provincia_2daVuelta.xlsx")
    print("   • Votos_Por_Candidato_Y_Canton_2daVuelta.xlsx")
    print("   • Totales_Por_Canton_2daVuelta.xlsx")
    print("   • provincias_segunda_vuelta_1996.json")
    print("   • cantones_segunda_vuelta_1996.json")
    print("=" * 80)
    print()
    print("💡 Para ver los resultados, ejecuta:")
    print("   py ver_resultados_segunda_vuelta.py")

if __name__ == "__main__":
    main()
