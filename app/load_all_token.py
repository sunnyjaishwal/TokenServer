'''
It is used to load all 50 token 
Its for future use
'''
import time
from core.redis_manager import RedisManager
from token_loader.bearer_token.bearer_token_loader import BearerToken
from token_loader.xd_token.xd_token_loader import XDTokenLoader

class LoadToken:
    
    def __init__(self,logger):
        self.logger= logger
        self.redis_obj= RedisManager(self.logger)
        self.bearer_obj = BearerToken(self.logger)
        self.xd_obj = XDTokenLoader(self.logger)
    
    def load_all_token(self):
        self.logger.info("Token Loading to cache started")
        for index in range(50):
            self.xd_obj.fetch_xd_token(index)
            time.sleep(3)
            self.bearer_obj.fetch_bearer_token(index)           
            

        
    
   
        
        
   
        