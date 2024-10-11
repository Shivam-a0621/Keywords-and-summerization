import pymongo
import logging

logging.basicConfig(filename='pdf_processing.log', level= logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')


class Pusher():
    def __init__(self):
        self.client= pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        self.mydb = self.client['PdfData']
        self.info = self.mydb.data
        
    
    def push_one(self,data):
        
        try:
            self.info.insert_one(data)
            
        except Exception as e:
            logging.error(f"Error in inserting {data}")
    
    def push_many(self,data):
        try:
             self.info.insert_many(data)
             
        except Exception as e:
            logging.error(f"Error in inserting many data") 
            
    def update_data(self,filename,keywords,summary):
        
        
        try:
        
            self.info.update_one(
                {'file_name':f'{filename}'},
                {'$set':{'keywords':f"{keywords}",'summary':f"{summary}"},
                "$currentDate":{'lastModified':True}}
                
            )      
            
            logging.info(f"keyword and summary updated for {filename}")
        except Exception as e:
            logging.error(f"error during update of keyword and summary for {filename}, {e}")                  
                    
        
        
            