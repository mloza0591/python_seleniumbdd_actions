
import time
from behave import step
from base.BasePage import BaseClass
from base.DriverClass import WebDriverClass
import utilities.CustomLogger as cl
#import configurationfiles.DeviceConfig as dc

log = cl.customLogger()


def before_all(context):
    try:
        log.info("Automation Started")
        context.testVariable = "This is a Test variable"
        context.driver1 = WebDriverClass()
        context.driver = context.driver1.getWebDriver("chrome")
        #context.driver = context.driver1.getWebDriver(dc.bName)
        context.bp = BaseClass(context.driver)
        context.bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")
        #context.bp.launchWebPage(dc.url, dc.title)
    except Exception as e:
        log.error(f" Error in before_all: {e}", exc_info=True)
        raise

def after_all(context):
    time.sleep(5)
    context.driver.quit()
    log.info("Automation Ended")
