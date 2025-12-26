"""
Script para visualizar resultados del análisis electoral de DIPUTADOS NACIONALES
Muestra resultados por provincias y cantones
"""

import sys
import os
import pandas as pd

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analisis.diputados import config

def mostrar_resultados_provincias():
    """Muestra resultados por provincias"""
    archivo = os.path.join(config.RESULTS_DIR, 'Votos_Por_Partido_Y_Provincia.xlsx')
    
    if not os.path.exists(archivo):
        print("⚠ No se encontraron resultados por provincias.")
        print("   Ejecuta primero: py main_diputados.py")
        return
    
    df = pd.read_excel(archivo)
    
    print("=" * 80)
    print("RESULTADOS ELECTORALES POR PROVINCIA - DIPUTADOS NACIONALES 1996")
    print("=" * 80)
    print()
    
    # Agrupar por provincia
    provincias = df['Provincia'].unique()
    
    for provincia in sorted(provincias):
        df_prov = df[df['Provincia'] == provincia].sort_values('Total_Votos', ascending=False)
        
        total_votos = df_prov['Total_Votos'].sum()
        ganador = df_prov.iloc[0]
        
        print(f"📍 {provincia}")
        print(f"   Total votos: {total_votos:,}")
        print(f"   🏆 GANADOR: {ganador['Partido']}")
        print(f"      {ganador['Porcentaje (%)']:.2f}% ({ganador['Total_Votos']:,} votos)")
        print()
        
        # Top 5
        print("   Top 5:")
        for idx, (i, row) in enumerate(df_prov.head(5).iterrows(), 1):
            print(f"      {idx}. {row['Partido']}: {row['Total_Votos']:,} votos ({row['Porcentaje (%)']:.2f}%)")
        print()

def mostrar_resultados_cantones():
    """Muestra resultados por cantones"""
    archivo = os.path.join(config.RESULTS_DIR, 'Votos_Por_Partido_Y_Canton.xlsx')
    
    if not os.path.exists(archivo):
        print("⚠ No se encontraron resultados por cantones.")
        return
    
    df = pd.read_excel(archivo)
    
    print("=" * 80)
    print("RESULTADOS ELECTORALES POR CANTÓN - DIPUTADOS NACIONALES 1996")
    print("=" * 80)
    print()
    
    # Mostrar cantones de Pichincha
    if 'Provincia' in df.columns:
        df_pichincha = df[df['Provincia'] == 'PICHINCHA']
        
        if not df_pichincha.empty:
            print("📍 CANTONES DE PICHINCHA:")
            print()
            
            cantones = df_pichincha['Canton'].unique()
            
            for canton in sorted(cantones):
                df_cant = df_pichincha[df_pichincha['Canton'] == canton].sort_values('Total_Votos', ascending=False)
                
                if not df_cant.empty:
                    ganador = df_cant.iloc[0]
                    total_votos = df_cant['Total_Votos'].sum()
                    
                    print(f"   {canton}")
                    print(f"   🏆 {ganador['Partido']}: {ganador['Total_Votos']:,} votos ({ganador['Porcentaje (%)']:.2f}%)")
                    print()

def mostrar_menu():
    """Muestra menú de opciones"""
    print("=" * 80)
    print("       VISUALIZADOR DE RESULTADOS - DIPUTADOS NACIONALES 1996")
    print("=" * 80)
    print()
    print("Selecciona una opción:")
    print("  1. Ver resultados por provincias")
    print("  2. Ver resultados por cantones")
    print("  3. Ver ambos")
    print("  0. Salir")
    print()
    
    opcion = input("Opción: ").strip()
    return opcion

def main():
    """Función principal"""
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            mostrar_resultados_provincias()
            input("\nPresiona Enter para continuar...")
        elif opcion == '2':
            mostrar_resultados_cantones()
            input("\nPresiona Enter para continuar...")
        elif opcion == '3':
            mostrar_resultados_provincias()
            mostrar_resultados_cantones()
            input("\nPresiona Enter para continuar...")
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("⚠ Opción inválida. Intenta de nuevo.")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()

