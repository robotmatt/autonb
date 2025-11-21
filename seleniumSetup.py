from selenium import webdriver

def seleniumSetup():
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    
    # webdriver_manager automatically downloads and installs the correct chromedriver
    # for the current version of Chrome.
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    return browser

# the following two lines are used for Safari
#    browser = webdriver.Safari()
#    browser.maximize_window()



