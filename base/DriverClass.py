from selenium import webdriver
import utilities.CustomLogger as cl
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebDriverClass:
    log = cl.customLogger()

    sauce_username = "code2lead"
    sauce_access_key = "xxxxxxxx-8f43-xxxx-8339-xxxxxxxxxxxx"

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            #driver_path = r"C:\Users\Display\PycharmProjects\SeleniumBDDFW\Drivers\chromedriver.exe"
            #service = ChromeService(executable_path=driver_path)

            # 👉 Aquí están las opciones para silenciar logs
            options = Options()
            options.add_argument("--log-level=3")  # Solo errores graves
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

            #driver = webdriver.Chrome(service=service, options=options)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.log.info("Chrome Driver is initializing")

        elif browserName == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
            #driver_path = r"C:\Users\Display\PycharmProjects\SeleniumBDDFW\Drivers\geckodriver.exe"
            #service = FirefoxService(executable_path=driver_path)
            #driver = webdriver.Firefox(service=service)
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
            self.log.info("Firefox Driver is initializing")

        return driver

    def cloudDriver(self,pName,bName,bVersion):
        SauceOptions = {
            'name': 'Dummy Point Test FrameWork',
            'build': 'Version 1',
            'screenResolution': '1280x768',
            'username': self.sauce_username,
            'accessKey': self.sauce_access_key,
            # tags to filter test reporting.
            'tags': ['Framework', 'pytest', 'module4'],
        }

        capabilities = {
            'browserName': bName,
            'browserVersion': bVersion,
            'platformName': pName,
            'sauce:options': SauceOptions
        }

        url = "https://ondemand.saucelabs.com:443/wd/hub"

        driver = webdriver.Remote(command_executor=url, desired_capabilities=capabilities, keep_alive=True)

        return driver
