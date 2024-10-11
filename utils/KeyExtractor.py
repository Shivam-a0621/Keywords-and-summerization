from keybert import KeyBERT
from yake import KeywordExtractor

import logging

model = KeyBERT('distilbert-base-nli-mean-tokens')
keye3xtractor= KeywordExtractor()

class KeyExtractor():
    def __init__(self):
        self.model= model
        self.keyword_extractor= keye3xtractor
        
    def extract(self,text):
        kws=set()
        try:
           
            
            keywords1= model.extract_keywords(text)
            for k in keywords1:
                kws.add(k)
                
            keywords2= keye3xtractor.extract_keywords(text)
            for k in keywords2:
                    kws.add(k)
            logging.info("suucess extract_keywords")        
        except Exception as e:
            logging.error("error in extract_keywords")
        
        return kws        
            
           
            
    