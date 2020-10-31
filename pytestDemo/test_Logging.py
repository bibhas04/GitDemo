import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)   #file handler object

    # Here setLevel() method will ingnore the debug part and starts from info as we set the level from info
    logger.setLevel(logging.INFO)
    logger.debug('A debug statement is executed')
    logger.info('Information statement')
    logger.warning('Something is in warning mode')
    logger.error('A major error has happend')
    logger.critical('Critical issue')
