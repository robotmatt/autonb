from selenium.webdriver.support.wait import WebDriverWait
try:
    from userInfo import username as file_username, password as file_password
except ImportError:
    file_username = None
    file_password = None

def browserSetup(browser, productionServer, username=None, password=None):
    # Use provided credentials or fall back to file credentials
    final_username = username or file_username
    final_password = password or file_password

    if productionServer:
        # browser.get('https://transstates.navtechpbs.com/cgi-bin-xml/class/login.cgi')
        browser.get('https://uca.pbs.vmc.navblue.cloud/cgi-bin-xml/class/main.cgi')
        try:
            if final_username and final_password:
                empNum = browser.find_element("name", "EmployeeNumber")
                empNum.send_keys(final_username)
                passwordElem = browser.find_element("name", "Password")
                passwordElem.send_keys(final_password)
                passwordElem.submit()
                print('Logged in')
                print()
            else:
                print("No credentials provided. Please log in manually.")
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