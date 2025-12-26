"""
Script principal para ejecutar análisis electoral completo
Elecciones Presidenciales Ecuador 1996 - Primera Vuelta
"""

import sys
from analisis_electoral_1996.analisis_provincias import analizar_provincias
from analisis_electoral_1996.analisis_cantones import analizar_cantones
from analisis_electoral_1996.analisis_parroquias import analizar_parroquias


def main():
    """
    Ejecuta el análisis electoral completo en los tres niveles geográficos.
    """
    print("\n" + "="*80)
    print(" " * 20 + "ANÁLISIS ELECTORAL ECUADOR 1996")
    print(" " * 25 + "PRIMERA VUELTA")
    print("="*80)
    
    try:
        # Análisis por provincias
        print("\n[1/3] Ejecutando análisis por provincias...")
        analizar_provincias()
        
        # Análisis por cantones
        print("\n[2/3] Ejecutando análisis por cantones...")
        analizar_cantones()
        
        # Análisis por parroquias
        print("\n[3/3] Ejecutando análisis por parroquias...")
        analizar_parroquias()
        
        # Resumen final
        print("\n" + "="*80)
        print(" " * 25 + "ANÁLISIS COMPLETADO")
        print("="*80)
        print("\n✓ Todos los análisis se ejecutaron exitosamente")
        print("\n📁 Archivos generados en el directorio 'resultados/':")
        print("   • Votos_Por_Candidato_Y_Provincia.xlsx")
        print("   • Votos_Por_Candidato_Y_Canton.xlsx")
        print("   • Votos_Por_Candidato_Y_Parroquia.xlsx")
        print("   • provincias_1996.json")
        print("   • cantones_1996.json")
        print("   • parroquias_1996.json")
        print("\n" + "="*80 + "\n")
        
        return 0
        
    except Exception as e:
        print(f"\n✗ Error durante la ejecución: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
