from selenium.webdriver.support.wait import WebDriverWait
from secrets import *


def browserSetup(browser, productionServer):
    if productionServer:
        # browser.get('https://transstates.navtechpbs.com/cgi-bin-xml/class/login.cgi')
        browser.get('https://uca.pbs.vmc.navblue.cloud/cgi-bin-xml/class/main.cgi')
        try:
            empNum = browser.find_element("name", "EmployeeNumber")
            empNum.send_keys(username)
            passwordElem = browser.find_element("name", "Password")
            passwordElem.send_keys(password)
            passwordElem.submit()
            print('Logged in')
            print()
        except Exception as e:
            print(e)
            print('Might already be logged in')
    else:
        browser.get('https://uca-uat.pbs.vmc.navblue.cloud/cgi-bin-xml/class/login.cgi')
        try:
            empNum = browser.find_element_by_name('EmployeeNumber')
            empNum.send_keys('######')
            passwordElem = browser.find_element_by_name('Password')
            passwordElem.send_keys('######')
            passwordElem.submit()
            print('Logged in')
            print()
        except:
            print('Might already be logged in')