import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import PyPDF2
import json
from utils.MongoPusher import Pusher




logging.basicConfig(filename='pdf_processing.log', level= logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

class ParallelDataExtractor():
    
    def __init__(self,folder_path):
        self.folder_path = folder_path
        self.pusher = Pusher()
        
  
    def extract_pdf_data(self,pdf_path):
    
    
        try:
            file_size= os.path.getsize(pdf_path)
            # print(f"File size is {file_size}")
            
            with open(pdf_path,'rb') as pp:
                reader = PyPDF2.PdfReader(pp)
                
                
                num_pages = len(reader.pages)
                # print(f"Number of pages {num_pages}")
                file_name= os.path.basename(pdf_path)
                # print(f"File name {file_name}")
                text=""
                
                for page_num in range(num_pages):
                    text+= reader.pages[page_num].extract_text()
                    
                
                pdf_metadata= {
                    "file_name": file_name,
                    "file_size": file_size,
                    "num_pages":num_pages,
                       
                }   
                
                
                
                      
                
                text_data={
                    "file_name": file_name,
                    "text":text
                }
                
                
                # print(pdf_data)
                
                
                
                logging.info(f"Successfully processed {pdf_path}")
                
                return pdf_metadata , text_data
            
        except Exception as e:
            logging.error(f"Error in processing {pdf_path}")
            return None    
    
    
    def parallel_procewss(self):
    
        pdf_files = [os.path.join(self.folder_path ,file) for file in os.listdir(self.folder_path ) if file.endswith('.pdf')]
        
        if not pdf_files:
            logging.info(f"No pdf files found in the filder {self.folder_path }")
            return 
        
        pdf_metadata= []
        text_data=[]
        
        with ThreadPoolExecutor() as exe:
            to_pdf = {exe.submit(self.extract_pdf_data,pdf): pdf for pdf in pdf_files}
            
            
            for paralle in as_completed(to_pdf):
                pdf_path= to_pdf[paralle]
                
                
                try:
                    results,text = paralle.result()
                    
                    if results:
                        pdf_metadata.append(results)
                        
                        text_data.append(text)
                        print(f"processed {pdf_path}")
                    else:
                        print(f"skipped {pdf_path} due to error") 
                        
                       
                        
                except Exception as e:
                    logging.error(f"exception occured while processing {pdf_path}: {e}")
                    
         
                    
        with open('pdf_data_before_update.json','w') as outfile:
            json.dump(pdf_metadata, outfile, indent=4)
             
            
        return text_data     
    
        