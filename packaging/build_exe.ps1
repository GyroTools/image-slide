# Builds dist\image-slide.exe (standalone, no Python needed on the target machine).
# Run from the repository root:  powershell -File packaging\build_exe.ps1
$ErrorActionPreference = "Stop"
python -m pip install -e ".[exe]"
python -m PyInstaller --noconfirm --clean --onefile --windowed `
    --name image-slide `
    --paths . `
    --exclude-module PyQt5 --exclude-module PyQt6 --exclude-module PySide6 `
    packaging\run_image_slide.py
Write-Host "Built dist\image-slide.exe"
