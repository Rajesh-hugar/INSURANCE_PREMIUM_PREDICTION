import pandas as pd
import numpy as np
import os ,sys
from Insurance.exception import InsuranceException
from Insurance.config import mongo_client
from Insurance.logger import logging
import yaml
import dill


def  get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        logging.info(f"Reading data from database;{database_name} and collection: {collection_name}")  
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Find coloumns:{df.columns}")
        
        if"_id" in df.columns:
            logging.info(f"Dropping columns:_id")
            df = df.drop("_id",axis=1)
        logging.info(f" Rows and Columns in df : {df.shape}")
        
        return df         
    
    except Exception as e:
        raise InsuranceException(e,sys)
    

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    
    for column in df.columns:
        if column not in exclude_columns:
            if df[column].dtypes != "O":
                df[column]= df[column].astype('float')
    
    return df



def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise InsuranceException(e, sys)


    
    
def save_object(file_path:str,obj:object)->None:
    
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    
    except Exception as e:
        raise InsuranceException(e ,sys )
    
    
    
def load_object(file_path: str, ) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise InsuranceException(e, sys) from e
    
    
    
    
def save_numpy_array_data(file_path: str, array: np.array):

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise InsuranceException(e, sys) from e
    
    
# Model Trainer

def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path,'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise InsuranceException(e, sys)
    