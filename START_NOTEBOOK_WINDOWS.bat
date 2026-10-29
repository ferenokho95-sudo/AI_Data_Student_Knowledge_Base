@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe py -3 -m venv .venv
if errorlevel 1 goto fail
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto fail
.venv\Scripts\python.exe -m notebook
pause
exit /b 0
:fail
echo Setup failed. Read the error above. Python 3.11 or 3.12 is required.
pause
exit /b 1
