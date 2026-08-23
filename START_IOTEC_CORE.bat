@echo off
title IOTEC LIVE CORE

:loop

cls

echo.
echo ===================================================
echo           IOTEC LIVE CORE
echo ===================================================
echo.
echo URL:
echo http://localhost:8080/frontend
echo.
echo ===================================================
echo.

taskkill /F /IM python.exe >nul 2>nul

cd /d C:\IOTEC_OPERATING_ECOSYSTEM\frontend

python server.py

echo.
echo ===================================================
echo SERVIDOR CAIU
echo REINICIANDO EM 5 SEGUNDOS
echo ===================================================
echo.

timeout /t 5 >nul

goto loop
