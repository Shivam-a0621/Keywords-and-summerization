from utils.Downloader import PDFDownload
from utils.extracter import ParallelDataExtractor
from utils.MongoPusher import Pusher
import json
import logging
from utils.KeyExtractor import KeyExtractor
from utils.Summerizor import Summerization
KE= KeyExtractor()
SUMER= Summerization()


pusher=Pusher()

logging.basicConfig(filename='pdf_processing.log', level= logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')



json_pdf = "Dataset.json"
download_folder= "downloads"


def pdf_download(json_pdf, download_folder):
    pdf_downloading= PDFDownload(json_file_path=json_pdf,download_folder=download_folder)
    pdf_downloading.download_all_pdf()
    return
  

def mogngo_pusher(data):
    pusher.push_many(data)
    return    

    
def extractor(download_folder):
    
    extactr = ParallelDataExtractor(download_folder)
    text_data=extactr.parallel_procewss()    
    
    return text_data

def key_extractor(text):
    words_with_score=KE.extract(text)
    return words_with_score

 
def summery(text):
      summry= SUMER.summarize_text(text)
      return summry  


def summery_keywords(text_data):
    # mogngo_pusher(text_data)
    
    for data in text_data:
        file_name = data['file_name']
        texts= data['text']
        
        keyword= key_extractor(texts)

        summaryyyy=summery(texts)
        
        pusher.update_data(file_name,keyword,summaryyyy)
                          
        
        
    




if __name__ == '__main__':
    pdf_download(json_pdf,download_folder)
    
    text_data= extractor(download_folder)
    with open("pdf_data_before_update.json",'r') as pp:
        data= json.load(pp)
        try:
            mogngo_pusher(data)
            logging.info(f"Pushed the data to mongodb")
        except Exception as e:
            logging.error("Failed to ppush the data to mongodb")    
    
    summery_keywords(text_data)
    
    
    
    
    
    



    


    


    