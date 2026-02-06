@echo off
echo ========================================
echo Running Dash App Test Suite
echo ========================================

REM Step 1: Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Create it with: python -m venv venv
    exit /b 1
)

REM Step 2: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    exit /b 1
)

REM Step 3: Run pytest tests
echo Running tests with pytest...
pytest test_app.py -v

REM Step 4: Check test results
if errorlevel 1 (
    echo ========================================
    echo ❌ TESTS FAILED! Exit code: 1
    echo ========================================
    exit /b 1
) else (
    echo ========================================
    echo ✅ ALL TESTS PASSED! Exit code: 0
    echo ========================================
    exit /b 0
)