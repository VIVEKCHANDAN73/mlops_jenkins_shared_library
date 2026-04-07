import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class DataProcessing:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None
        self.features = None
        
        os.makedirs(self.output_path, exist_ok=True)
        logger.info(f"DataProcessing initialized with input: {self.input_path} and output: {self.output_path}")
        
    def load_data(self):
        try:
            self.df = pd.read_csv(self.input_path)
            logger.info(f"Data loaded successfully from {self.input_path}")
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise CustomException(f"Error loading data: {e}")
        
    def preprocess_data(self):
        try:
            self.df["Timestamp"] = pd.to_datetime(self.df["Timestamp"], errors='coerce')
            categorical_cols = ['Operation_Mode', 'Efficiency_Status']
            for col in categorical_cols:
                self.df[col] = self.df[col].astype('category')
            
            self.df["Year"] = self.df["Timestamp"].dt.year
            self.df["Month"] = self.df["Timestamp"].dt.month
            self.df["Day"] = self.df["Timestamp"].dt.day
            self.df["Hour"] = self.df["Timestamp"].dt.hour
            
            self.df.drop(columns=['Timestamp', 'Machine_ID'], inplace=True)
            
            columns_to_encode = ['Operation_Mode', 'Efficiency_Status']
            
            for col in columns_to_encode:
                le = LabelEncoder()  
                self.df[col] = le.fit_transform(self.df[col])         
          
            logger.info("Data preprocessing completed successfully.")
            
        except Exception as e:
            logger.error(f"Error during preprocessing: {e}")
            raise CustomException(f"Error during preprocessing: {e}")
        
    def split_and_scale(self):
        pass