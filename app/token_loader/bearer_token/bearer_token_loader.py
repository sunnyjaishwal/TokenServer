'''
This module 
'''
import requests
import os
import json
from core.redis_manager import RedisManager

class BearerToken:
    
    def __init__(self,logger):
        self.logger = logger
        self.header=None
        self.payload='client_id=TEAP1EPUAR97S1aWCpEkWe9L3VvhtBIK&client_secret=j9sP1PK9cEJKbL1o&fact=%7B%22keyValuePairs%22%3A%5B%7B%22key%22%3A%22flow%22%2C%22value%22%3A%22REVENUE%22%7D%2C%7B%22key%22%3A%22market%22%2C%22value%22%3A%22IN%22%7D%2C%7B%22key%22%3A%22originCity%22%2C%22value%22%3A%22JFK%22%7D%2C%7B%22key%22%3A%22originCountry%22%2C%22value%22%3A%22US%22%7D%2C%7B%22key%22%3A%22currencyCode%22%2C%22value%22%3A%22%22%7D%2C%7B%22key%22%3A%22channel%22%2C%22value%22%3A%22DESKTOP%22%7D%5D%7D&grant_type=client_credentials'
        self.redis_obj= RedisManager(self.logger)
        self.api_url= "https://api-des.etihad.com/v1/security/oauth2/token/initialization"
        self.p_key=None
    
    def fetch_bearer_token(self,count):
        try:
            file_path= os.path.join("token_loader","bearer_token","headers.json")
            with open(file_path, "r") as h:
                self.header=json.load(h)
        except Exception as e:
            print("file not loaded - ", e)
        self.p_key= 'p_token_'+str(count+1)
        self.header['x-d-token']= self.redis_obj.get_cache_data(self.p_key)
        response= requests.post(
                url = self.api_url,
                headers= self.header,
                data= self.payload,
                timeout=10
            )
        if response.status_code == 403 :
            self.logger.error(f"Unable to fetch access token using {self.p_key}")
        else:
            responses= response.json()
            key= 'xd_token_'+str(count+1)
            value= responses.get('access_token')
            expiry= int(responses.get('expires_in'))
            self.redis_obj.set_cache_data(key, int(expiry), str(value))
            self.logger.info(f"Bearer token has been fetched and set in redis as {key}")
    
