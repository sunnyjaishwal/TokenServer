'''
AccessToken class handles fetching of bearer token using X-D-Token.
'''
import requests
import os
import json
from core.redis_manager import RedisManager
from token_loader.xd_token.xd_token_loader import XDTokenLoader 
from dotenv import load_dotenv
load_dotenv()
class BearerToken:
    
    def __init__(self,logger, proxy_manager):
        self.logger = logger
        self.header=None
        self.proxy_manager = proxy_manager
        self.proxy = None
        #self.xd_obj= XDTokenLoader(self.logger)
        self.payload='client_id=TEAP1EPUAR97S1aWCpEkWe9L3VvhtBIK&client_secret=j9sP1PK9cEJKbL1o&fact=%7B%22keyValuePairs%22%3A%5B%7B%22key%22%3A%22flow%22%2C%22value%22%3A%22REVENUE%22%7D%2C%7B%22key%22%3A%22market%22%2C%22value%22%3A%22IN%22%7D%2C%7B%22key%22%3A%22originCity%22%2C%22value%22%3A%22JFK%22%7D%2C%7B%22key%22%3A%22originCountry%22%2C%22value%22%3A%22US%22%7D%2C%7B%22key%22%3A%22currencyCode%22%2C%22value%22%3A%22%22%7D%2C%7B%22key%22%3A%22channel%22%2C%22value%22%3A%22DESKTOP%22%7D%5D%7D&grant_type=client_credentials'
        self.redis_obj= RedisManager(self.logger)
        self.api_url= os.getenv('ACCESS_API_URL')
        self.p_key=None
    
    def fetch_bearer_token(self,token):
        try:
            file_path= os.path.join("token_loader","bearer_token","headers.json")
            with open(file_path, "r") as h:
                self.header=json.load(h)
        except Exception as e:
            print("file not loaded - ", e)
        self.proxy= self.proxy_manager.fetch_proxy()
        if self.proxy :
            self.logger.info("Proxy fetched ..")
            proxies = {"http": self.proxy, "https": self.proxy}
        else : 
            self.logger.error("Proxy not fetched")

        self.header['x-d-token'] = token
        response= requests.post(
                url = self.api_url,
                headers= self.header,
                data= self.payload,
                proxies = proxies,
                timeout=10
            )
        if response.status_code == 200 :
            responses= response.json()
            return responses
        else:
            self.logger.error(f"Unable to fetch Access token")
            
    
