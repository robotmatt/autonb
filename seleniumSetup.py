import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def seleniumSetup():
    # webdriver_manager automatically downloads and installs the correct chromedriver
    # for the current version of Chrome.
    driver_path = ChromeDriverManager().install()
    
    # Fix for bug where webdriver-manager returns the license file instead of the binary
    if "THIRD_PARTY_NOTICES" in driver_path:
        directory = os.path.dirname(driver_path)
        binary_name = "chromedriver.exe" if os.name == 'nt' else "chromedriver"
        binary_path = os.path.join(directory, binary_name)
        if os.path.exists(binary_path):
            driver_path = binary_path
            
    # Ensure binary is executable on Unix-like systems
    if os.name != 'nt' and os.path.exists(driver_path):
        current_mode = os.stat(driver_path).st_mode
        if not (current_mode & 0o111):  # Check if any execute bit is set
            os.chmod(driver_path, current_mode | 0o111)
    
    service = ChromeService(driver_path)
    browser = webdriver.Chrome(service=service)
    return browser

# the following two lines are used for Safari
#    browser = webdriver.Safari()
#    browser.maximize_window()