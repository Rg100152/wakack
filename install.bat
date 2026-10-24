@echo off
REM WAKACK v6.0 ULTRA — Installer (Windows)
REM Made by Raj
setlocal enabledelayedexpansion

color 0A
echo.
echo  ====================================================
echo    WAKACK v6.0 ULTRA - Installer (Windows)
echo    Made by Raj
echo  ====================================================
echo.

REM --- 1. Check Python ---
echo [1/3] Checking Python...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo.
    echo [!] Python not found.
    echo     Download from: https://www.python.org/downloads/
    echo     Important: tick "Add Python to PATH" during install.
    echo.
    pause
    exit /b 1
)
python --version
echo [OK] Python found.

REM --- 2. Check git ---
echo.
echo [2/3] Checking git...
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] git not found. Download from: https://git-scm.com/download/win
    pause
    exit /b 1
)
echo [OK] git found.

REM --- 3. Clone or update ---
echo.
echo [3/3] Fetching WAKACK...
set "INSTALL_DIR=%USERPROFILE%\wakack"
if exist "%INSTALL_DIR%\.git" (
    cd /d "%INSTALL_DIR%"
    git pull --quiet
    echo [OK] Updated existing install at %INSTALL_DIR%
) else (
    git clone --quiet https://github.com/rg100152/wakack.git "%INSTALL_DIR%"
    echo [OK] Cloned to %INSTALL_DIR%
)

REM --- Create launcher ---
echo @echo off > "%USERPROFILE%\Desktop\WAKACK.bat"
echo python "%INSTALL_DIR%\wakack.py" >> "%USERPROFILE%\Desktop\WAKACK.bat"
echo [OK] Created shortcut on Desktop: WAKACK.bat

echo.
echo  ====================================================
echo    Installation complete!
echo  ====================================================
echo.
echo  Run it by:
echo    - Double-click the WAKACK.bat on your Desktop
echo    - Or open CMD and type:  python %INSTALL_DIR%\wakack.py
echo.
echo  Simulation only. Real hacking is illegal.
echo.
pause
