import inspect
import logging
import allure
import os

def customLogger():
    # Asegura que el directorio exista
    log_dir = os.path.join(os.path.dirname(__file__), '../reports')
    os.makedirs(log_dir, exist_ok=True)
    # 1.) This is used to get the  class / method name from where this customLogger method is called
    logName = inspect.stack()[1][3]

    # 2.) Create the logging object and pass the logName in it
    logger = logging.getLogger(logName)

    # 3.) Set the Log level
    logger.setLevel(logging.DEBUG)

    # 4.) Create the fileHandler to save the logs in the file
    #fileHandler = logging.FileHandler("../SeleniumBDDFW/reports/Code2lead.log", mode='a')
    # Obtener la ruta absoluta del directorio actual
    base_dir = os.path.abspath(os.path.dirname(__file__))

    # Ruta absoluta a la carpeta reports
    reports_dir = os.path.join(base_dir, '..', 'reports')
    os.makedirs(reports_dir, exist_ok=True)

    # Ruta completa al archivo de log
    log_file = os.path.join(reports_dir, 'Code2lead.log')
    fileHandler = logging.FileHandler(log_file, mode='a')
    # 5.) Set the logLevel for fileHandler
    fileHandler.setLevel(logging.DEBUG)

    # 6.) Create the formatter in which format do you like to save the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # 7.) Set the formatter to fileHandler
    fileHandler.setFormatter(formatter)

    # 8.) Add file handler to logging
    logger.addHandler(fileHandler)

    #  9.) Finally return the logging object

    return logger


def allureLogs(text):
    with allure.step(text):
        pass
