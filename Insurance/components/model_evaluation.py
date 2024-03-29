from Insurance.entity import config_entity,artifact_entity
from Insurance.exception import InsuranceException
from typing import Optional
from Insurance import utils 
import os,sys
from sklearn.pipeline import Pipeline
from Insurance.logger import logging 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from Insurance.predictor import ModelResolver

class ModelEvaluation:
    
    def __init__(self, model_eval_config:config_entity.ModelEvaluationConfig,data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
                 data_transformation_artifact:artifact_entity.DataTransformationArtifact,model_trainer_artifact:artifact_entity.ModelTrainerArtifact):
        
        
        try:
            self.model_eval_config =model_eval_config
            self.data_ingestion_artifact =data_ingestion_artifact
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.modelResolver = ModelResolver()
            
        except Exception as e:
            raise InsuranceException(e,sys)
        
        
    def initiate_model_evaluation(self)-> artifact_entity.ModelEvaluationArtifact:
        
        try:
            latest_dir_path = self.modelResolver.get_latest_dir_path()
            
            if latest_dir_path == None:
                model_eval_artifact = artifact_entity.ModelEvaluationArtifact(is_model_accepted=True,improved_accuracy=None)
                logging.info(f"Model Evaluation artifact: {model_eval_artifact}")
                
                return model_eval_artifact 
            
            
            
            # Find location previous model
            transformer_path = self.modelResolver.get_latest_transformer_path()
            model_path = self.modelResolver.get_latest_model_path()
            target_encoder_path = self.modelResolver.get_latest_target_encoder_path()
        except Exception as e:
            raise InsuranceException(e,sys)
        