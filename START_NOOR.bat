@echo off
title NOOR ARCHIVE NIL - Local Bridge
echo [NIL-BRIDGE] Iniciando ecosistema de datos vivos...
echo [NIL-BRIDGE] Verificando entorno Python...

:: Intentar iniciar el bridge en segundo plano
start /B python nil_bridge.py

echo [NIL-BRIDGE] Servidor activo en puerto 5000.
echo [NIL-BRIDGE] Abriendo Noor Archive Nil...

:: Abrir el archivo index.html en el navegador predeterminado
start index.html

echo.
echo ======================================================
echo  NIL-BRIDGE ESTA CORRIENDO. 
echo  No cierres esta ventana si deseas datos en tiempo real.
echo ======================================================
pause
