from transformers import BartTokenizer, BartForConditionalGeneration
import logging

logging.basicConfig(filename='pdf_processing.log', level= logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

model_name = 'sshleifer/distilbart-cnn-12-6'


class Summerization():
    def __init__(self):
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)
        
        
    
    def summarize_text(self,text):
        
        
        summery=""
        try:
            text_length = len(text.split())  

            
            if text_length < 400:
                max_length = 100  
                min_length = 10
            elif text_length < 1000:
                max_length = 200  
                min_length = 30
            else:
                max_length = 300  
                min_length = 50
                
                
            inputs =  self.tokenizer(text, max_length=max_length, return_tensors='pt', truncation=True)

            summary_ids = self.model.generate(
                inputs['input_ids'],
                max_length=max_length,
                min_length=min_length,
                length_penalty=2.0,
                num_beams=4,
                early_stopping=True
            )
            
            summary =  self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            
            logging.info("Summerized Successfully")

        except Exception as e:
            logging.error("Error in summerization")       
        return summary    
              
        