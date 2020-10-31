import inspect
import logging


class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # file handler object
        # Here setLevel() method will ingnore the debug part and starts from info as we set the level from info
        logger.setLevel(logging.INFO)
        return logger

