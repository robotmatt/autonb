# 🛫 AutoNB: Automated Navblue PBS Runs
AutoNB is a Python-based automation tool designed to simplify and streamline the process of running Navblue PBS schedule runs, customized for C5's version of Navblue PBS.

## 🖥️ Installation & Setup

### 1. Install Python
**MacOS**
- **Option A (Recommended):** Install via Homebrew: `brew install python`
- **Option B:** Download the installer from [python.org](https://www.python.org/downloads/macos/)

**Windows**
- **Option A (Recommended):** Install via Chocolatey: `choco install python`
  - If you don't have Chocolatey, install it from [chocolatey.org](https://chocolatey.org/install)
- **Option B:** Download the installer from [python.org](https://www.python.org/downloads/windows/)
  - **IMPORTANT:** Check the box **"Add Python to PATH"** during installation.

### 2. Setup & Run
**MacOS / Linux**
1. Open Terminal.
2. Navigate to the project folder.
3. Run: `./run_app.sh`

**Windows**
1. Open the project folder.
2. Double-click `run_app.bat`.

This will automatically install all dependencies (including Selenium and the correct ChromeDriver) and launch the AutoNB interface.

## Usage
### Credentials
Enter your NavBlue Username and Password into the `userInfo.py` file (renamed from secrets.py). If it doesn't exist just create a `userInfo.py` that looks like this:

`username = 'Username'`<br /> 
`password = 'Password'`<br />

**Note:** If you leave `userInfo.py` empty or don't create it, the app will automatically prompt you for credentials in the UI.

### config.py
Most of the settings you need are contained in config.py. See the inline documentation for usage of all the variables. You can now also configure these directly in the UI!

## 📁 Project Structure
| File      | Purpose                                                                                                 |
|-----------|----------------------------------------------------------------------------------------------------------|
| **app.py** | **Main Streamlit UI application - run this to use the web interface** |
| **run_app.sh** | Helper script to install dependencies and launch the app (Mac/Linux) |
| **run_app.bat** | Helper script to install dependencies and launch the app (Windows) |
| main.py   | Legacy CLI entry point for executing schedule runs |
| mainUnstack.py | Legacy CLI entry point for unstack runs |
| config.py | Default configuration settings (can be overridden in the UI) |
| userInfo.py | NavBlue PBS credentials (username/password) |
| basicRun.py | Handles the basic PBS run scenarios |
| unstackRun.py | Handles unstack PBS run scenarios |
| run_logic.py | Logic for generating run parameters |
| browserSetup.py | Selenium browser setup and login |
| seleniumSetup.py | ChromeDriver setup using webdriver-manager |
| requirements.txt | Python dependencies | 


## 📄 License

Distributed under the BSD-3-Clause License — free to use and modify with attribution.