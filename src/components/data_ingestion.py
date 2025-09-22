import os 
import sys
import pandas as pd
from src.exception import CustomException
from dataclasses import dataclass
from src.logger import logging
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig :
    raw_data_path=os.path.join("artifacts","data.csv")
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestionconfig=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Ingestion process starts")
        try:
            df=pd.read_csv("notebook\data\data.csv")
            logging.info("Data Readed from the source")

            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path),exist_ok=True)
            df.to_csv(self.ingestionconfig.raw_data_path,index=False,header=True)

            logging.info("Data Readed")
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            train_set.to_csv(self.ingestionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)
            logging.info("Ingestion of data completed")
            return (
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path
            )
        except Exception as e:
            CustomException(e,sys)
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
        





