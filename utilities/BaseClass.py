import pytest
import inspect
import logging



@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger():
        """
        This method is used for generating the log file  and storing logs in the log File
        """
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(funcName)s() : %(message)s ",
                                      datefmt='%d - %m - %Y  %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

