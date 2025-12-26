"""
Script para migrar archivos existentes a la nueva estructura
IMPORTANTE: Este script NO elimina los archivos originales, solo los copia
"""
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def copiar_archivo(origen, destino):
    """Copia un archivo de forma segura"""
    try:
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        shutil.copy2(origen, destino)
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def migrar_archivos():
    """Migra archivos a la nueva estructura"""
    print("=" * 80)
    print("MIGRANDO ARCHIVOS A NUEVA ESTRUCTURA")
    print("=" * 80)
    print()
    
    # Migrar datos de presidentes
    print("[1/3] Migrando datos de presidentes...")
    datos_origen = os.path.join(BASE_DIR, 'Datos-Presidentes-Completos')
    
    if os.path.exists(datos_origen):
        # Primera vuelta
        archivo_1v = os.path.join(datos_origen, 'Primera Vuelta', '1996 - Presidentes - primera vuelta.xlsx')
        if os.path.exists(archivo_1v):
            destino_1v = os.path.join(BASE_DIR, 'datos', 'presidentes', 'primera_vuelta', '1996 - Presidentes - primera vuelta.xlsx')
            if copiar_archivo(archivo_1v, destino_1v):
                print(f"  ✓ Copiado: 1996 - Presidentes - primera vuelta.xlsx")
        
        # Segunda vuelta
        archivo_2v = os.path.join(datos_origen, 'Segunda Vuelta', '1996 - Presidentes - segunda vuelta.xlsx')
        if os.path.exists(archivo_2v):
            destino_2v = os.path.join(BASE_DIR, 'datos', 'presidentes', 'segunda_vuelta', '1996 - Presidentes - segunda vuelta.xlsx')
            if copiar_archivo(archivo_2v, destino_2v):
                print(f"  ✓ Copiado: 1996 - Presidentes - segunda vuelta.xlsx")
    
    # Migrar código de análisis
    print()
    print("[2/3] Migrando código de análisis...")
    analisis_origen = os.path.join(BASE_DIR, 'analisis_electoral_1996')
    
    if os.path.exists(analisis_origen):
        archivos_a_migrar = [
            ('config.py', 'analisis/presidentes/config.py'),
            ('data_loader.py', 'analisis/presidentes/data_loader.py'),
            ('analisis_provincias.py', 'analisis/presidentes/analisis_provincias.py'),
            ('analisis_cantones.py', 'analisis/presidentes/analisis_cantones.py'),
            ('analisis_parroquias.py', 'analisis/presidentes/analisis_parroquias.py'),
        ]
        
        for archivo_origen, archivo_destino in archivos_a_migrar:
            origen = os.path.join(analisis_origen, archivo_origen)
            destino = os.path.join(BASE_DIR, archivo_destino)
            if os.path.exists(origen):
                if copiar_archivo(origen, destino):
                    print(f"  ✓ Copiado: {archivo_origen}")
    
    # Migrar resultados
    print()
    print("[3/3] Migrando resultados...")
    resultados_origen = os.path.join(BASE_DIR, 'resultados')
    
    if os.path.exists(resultados_origen):
        resultados_destino = os.path.join(BASE_DIR, 'resultados', 'presidentes')
        
        for archivo in os.listdir(resultados_origen):
            if archivo.endswith(('.xlsx', '.json')):
                origen = os.path.join(resultados_origen, archivo)
                destino = os.path.join(resultados_destino, archivo)
                if os.path.isfile(origen):
                    if copiar_archivo(origen, destino):
                        print(f"  ✓ Copiado: {archivo}")
    
    print()
    print("=" * 80)
    print("MIGRACIÓN COMPLETADA")
    print("=" * 80)
    print()
    print("IMPORTANTE: Los archivos originales NO fueron eliminados.")
    print("Verifica que todo funcione correctamente antes de eliminar los archivos antiguos.")

if __name__ == "__main__":
    migrar_archivos()
