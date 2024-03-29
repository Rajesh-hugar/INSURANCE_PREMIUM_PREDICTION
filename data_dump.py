import pymongo 
import pandas as pd
import json 
import os

from dotenv import load_dotenv
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

client = pymongo.MongoClient(MONGO_DB_URL)

DATA_FILE_PATH ='insurance.csv'
DATABASE='INSURANCE'
COLLECTION_NAME='INSURANCE_PROJECT'

if __name__ =="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and columns :{df.shape}')
    
    df.reset_index(drop=True,inplace=True)
    
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    client[DATABASE][COLLECTION_NAME].insert_many(json_record)
    print('Data Inserted ')