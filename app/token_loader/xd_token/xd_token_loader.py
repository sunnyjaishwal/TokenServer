'''
Handles the retrieval and management of the X-D-Token for API authentication.
'''
import json
import requests
import os
from core.redis_manager import RedisManager
from core.proxy_manager import ProxyManager
from dotenv import load_dotenv
load_dotenv()
class XDTokenLoader:
    
    def __init__(self,logger, proxy_manager):
        self.expiry=None
        self.logger=logger
        self.payload= None
        self.header= None
        self.body=None
        self.proxy= None
        self.proxy_manager = proxy_manager
        self.api_url= os.getenv('XD_API_URL')
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
        self.proxy = self.proxy_manager.fetch_proxy()
        if self.proxy :
            self.logger.info("Proxy fetched ..")
            proxies = {"http": self.proxy, "https": self.proxy}
        else : 
            self.logger.error("Proxy not fetched")
       
        response= requests.post(
                url=self.api_url,
                headers=self.header,
                data= self.body,
                proxies = proxies,
                timeout= 10
            )   
        if response.status_code == 200:
            self.logger.info(f"X-d token fetched - {response.status_code} for {count+1}")
            responses = response.json()
            return responses
        else:
            self.logger.error(f"Unable to fetch xd, problem with p-token - {response.status_code}")
    
   
            
      