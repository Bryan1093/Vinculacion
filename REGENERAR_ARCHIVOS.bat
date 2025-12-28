@echo off
echo ================================================================================
echo REGENERANDO ARCHIVOS CON PARROQUIAS CORRECTAS
echo ================================================================================
echo.
echo Por favor, asegurate de que el archivo Excel este CERRADO antes de continuar.
echo.
pause
echo.
echo Eliminando archivos antiguos...
del /F "resultados\Votos_Por_Candidato_Parroquias_Pastaza_Pichincha.xlsx" 2>nul
del /F "resultados\parroquias_pastaza_pichincha_detallado_1996.json" 2>nul
echo.
echo Ejecutando analisis con parroquias correctas...
py analisis_parroquias_pastaza_pichincha_detallado.py
echo.
echo ================================================================================
echo VERIFICANDO RESULTADOS...
echo ================================================================================
echo.
py ver_pastaza_detalle.py
echo.
pause
