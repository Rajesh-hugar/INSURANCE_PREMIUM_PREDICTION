from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
from warnings import filterwarnings
filterwarnings('ignore')
import sys
print(dir(sys))


def test_logger_and_exception():
    try:
        logging.info('Starting the test logger and the exception')
        result = 3/0
        
        print(result)
        
        logging.info('Ending Pointof the test logger and the exception')
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e,sys)
    

if __name__ =='__main__':
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)