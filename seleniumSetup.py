import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def seleniumSetup():
    # webdriver_manager automatically downloads and installs the correct chromedriver
    # for the current version of Chrome.
    driver_path = ChromeDriverManager().install()
    
    # Debug print to help identify path issues
    print(f"Using ChromeDriver from: {driver_path}")
    
    # Fix for bug where webdriver-manager might return a path containing LICENSE or THIRD_PARTY_NOTICES
    # or just the directory.
    if not (driver_path.endswith(".exe") and os.path.isfile(driver_path)):
        # If it's a directory or a file that isn't the exe, search for the exe inside the same folder
        parent_dir = driver_path if os.path.isdir(driver_path) else os.path.dirname(driver_path)
        
        # Search for chromedriver.exe in the directory
        for root, dirs, files in os.walk(parent_dir):
            if "chromedriver.exe" in files:
                driver_path = os.path.join(root, "chromedriver.exe")
                break
    
    print(f"Final ChromeDriver path: {driver_path}")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Force use of the specific driver path we just found/downloaded
    service = ChromeService(driver_path)
    browser = webdriver.Chrome(service=service, options=options)
    return browser

# the following two lines are used for Safari
#    browser = webdriver.Safari()
#    browser.maximize_window()



