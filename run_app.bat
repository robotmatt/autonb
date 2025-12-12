@echo off
echo Upgrading pip...
pip install --upgrade pip

echo Installing dependencies...
pip install streamlit selenium webdriver-manager --only-binary=:all:

echo Starting AutoNB...
python -m streamlit run app.py
pause
