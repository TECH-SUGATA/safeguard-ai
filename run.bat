@echo off
echo ==========================================
echo   SafeGuard AI - Starting Backend Server
echo ==========================================
echo.
echo Installing dependencies...
pip install fastapi uvicorn pydantic python-multipart
echo.
echo Starting backend on http://localhost:8000
echo Press CTRL+C to stop
echo.
python -m uvicorn main:app --reload --port 8000
pause
