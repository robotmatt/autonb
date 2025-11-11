# 🛫 AutoNB: Automated Navblue PBS Runs
AutoNB is a Python-based automation tool designed to simplify and streamline the process of running Navblue PBS schedule runs, customized for C5's version of Navblue PBS.

## 🖥️ Environment Setup Instructions
See [INSTALL.md](INSTALL.md)

## Usage
### Credentials
Enter your NavBlue Username and Password into the secrets.py file. If it doesn't exist just create a secrets.py that looks like this:

`username = 'Username'`<br /> 
`password = 'Password'`<br />

### config.py
Most of the settings you need are contained in config.py. See the inline documentation for usage of all the variables

### Running the Program
Execute the script by running `main.py` after setting all of the configuration variables in config.py

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