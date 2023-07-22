from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
from warnings import filterwarnings
filterwarnings('ignore')
import sys
#print(dir(sys))

from Insurance.utils import get_collection_as_dataframe


#def test_logger_and_exception():
 #   try:
  #      logging.info('Starting the test logger and the exception')
   #     result = 3/0
    #    
     ##  
       # logging.info('Ending Pointof the test logger and the exception')
    #except Exception as e:
     #   logging.debug(str(e))
      #  raise InsuranceException(e,sys)
    

if __name__ =='__main__':
    try:
        # test_logger_and_exception()
        get_collection_as_dataframe(database_name ="INSURANCE",collection_name ="INSURANCE_PROJECT")
    
    except Exception as e:
        print(e)