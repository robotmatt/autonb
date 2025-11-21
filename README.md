# 🛫 AutoNB: Automated Navblue PBS Runs
AutoNB is a Python-based automation tool designed to simplify and streamline the process of running Navblue PBS schedule runs, customized for C5's version of Navblue PBS.

## 🖥️ Installation & Setup

### 1. Install Python
**MacOS**
- **Option A (Recommended):** Install via Homebrew: `brew install python`
- **Option B:** Download the installer from [python.org](https://www.python.org/downloads/macos/)

**Windows**
- Download the installer from [python.org](https://www.python.org/downloads/windows/)
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

### config.py
Most of the settings you need are contained in config.py. See the inline documentation for usage of all the variables. You can now also configure these directly in the UI!

## 📁 Project Structure
| File      | Purpose                                                                                                 |
|-----------|---------------------------------------------------------------------------------------------------------|
| main.py   | Entry point for executing schedule runs. This is the file you should be running when you execute autonb |
| config.py | Most of the configuration settings are available here                                                   |
| basicRun.py | Handles the basic PBS run scenarios                                                                     |
| complexRun.py | TBD, attempt to try to auto unstack | 
| browserSetup.py| Selenium browser setup | 


## 📄 License

Distributed under the BSD-3-Clause License — free to use and modify with attribution.