import os

from selenium import webdriver

if os.name == 'nt': # check if on windows 'nt'
    def seleniumSetup():
        service = webdriver.ChromeService()
        browser = webdriver.Chrome(service=service)
        return browser

if os.name == 'posix': # check if on mac 'postix'
    def seleniumSetup():
        #might have to point to a different location depending on where your chromedriver is installed
        service = webdriver.ChromeService(executable_path= '/opt/homebrew/bin/chromedriver')
        browser = webdriver.Chrome(service=service)
        return browser

# the following two lines are used for Safari
#    browser = webdriver.Safari()
#    browser.maximize_window()



