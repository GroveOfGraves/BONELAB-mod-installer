@echo off

REM Install Python
winget install --id Python.Python -e

REM Install the necessary Python packages
pip install requests
pip install tqdm

REM Install 7-Zip
winget install --id 7zip.7zip -e

REM Pause the script to allow the user to read any output messages
pause
