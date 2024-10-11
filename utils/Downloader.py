import json
import os
import requests
import logging


logging.basicConfig(filename='pdf_processing.log', level= logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')


class PDFDownload:
    def __init__(self, json_file_path, download_folder):
        self.json_file_path = json_file_path
        self.download_folder = download_folder
        

    def download_all_pdf(self):
    
        with open(self.json_file_path,'r') as file:
            data= json.load(file)
        
        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)
        
        
        for i in range(len(data)):
            pdf_url= data[f'pdf{i+1}']
            file_name= f"document{i+1}.pdf"
            file_path= os.path.join(self.download_folder,file_name) 
            
            
            try:
                response = requests.get(pdf_url)
                response.raise_for_status()
                
                
                with open(file_path,'wb') as f:
                    f.write(response.content)
                
                logging.info(f"sucessfully downloaded file {file_name}")    
                    
                print(f"Downloaded {file_name}")
                
            except requests.exceptions.RequestException as e:
                logging.error(f"Error in downloading {file_name} : {e}")
                