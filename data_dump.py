import pymongo 
import pandas as pd
import json 


client = pymongo.MongoClient("mongodb+srv://hugar_rajesh:Rajesh_0808@rajesh.ud2bw.mongodb.net/?retryWrites=true&w=majority")

DATABASE='INSURANCE'
COLLECTION_NAME='INSURANCE_PROJECT'

if __name__ =="__main__":
    df=pd.read_csv('insurance.csv')
    print(f'Rows and columns :{df.shape}')
    
    df.reset_index(drop=True,inplace=True)
    
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    client[DATABASE][COLLECTION_NAME].insert_many(json_record)
    print('Data Inserted ')