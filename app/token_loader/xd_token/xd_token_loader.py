'''

'''
import json
import requests
import time
import os
from core.redis_manager import RedisManager

class XDTokenLoader:
    
    def __init__(self,logger):
        self.expiry=None
        self.logger=logger
        self.payload= None
        self.header= None
        self.body=None
        self.api_url= "https://digital.etihad.com/rubie-Fease-no-sall-be-intome-Deat-seemselfe-Mot"
        self.redis_object = RedisManager(self.logger)
               
    def fetch_xd_token(self,count):
        try:
            p_token_file= os.path.join("token_loader","xd_token","p_tokens.json")
            with open(p_token_file, "r", encoding='utf-8') as p:
                self.payload= json.load(p)
        except:
            self.logger.error("P Token file not loaded")
        try:
            header_file_path= os.path.join("token_loader","xd_token","headers.json")
            with open(header_file_path, "r", encoding='utf-8') as h:
                self.header= json.load(h)
        except:
            self.logger.error("header file not loaded")
        self.body= json.dumps(self.payload[count].get('p_token_'+str(count+1)))        
        response= requests.post(
                url=self.api_url,
                headers=self.header,
                data= self.body,
                timeout= 10
            )   
        if response.status_code == 200:
            self.logger.info(f"X-d token fetched - {response.status_code} for {count+1}")
            responses = response.json()
            key= 'p_token_'+str(count+1)
            value = responses.get('token')
            self.expiry = int(responses.get('renewInSec'))
            self.redis_object.set_cache_data(key, int(self.expiry), str(value))
            self.logger.info(f"successfully set xd token to redis as {key}")
            return responses
        else:
            self.logger.error(f"Unable to fetch xd, problem with p-token - {response.status_code}")
    
   
            
      