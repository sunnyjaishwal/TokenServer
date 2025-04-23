'''
'''
import time
from core.redis_manager import RedisManager
from token_loader.bearer_token.bearer_token_loader import BearerToken
from token_loader.xd_token.xd_token_loader import XDTokenLoader

class TokenManager:
    
    def __init__(self,logger):
        self.logger=logger
        self.redis_obj= RedisManager(self.logger)
        self.bearer_obj = BearerToken(self.logger)
        self.xd_obj = XDTokenLoader(self.logger)
        
    def refresh_token(self):
        for index in range(100):
            # p_key='p_token_'+str(index+1)
            # xd_key='xd_token_'+str(index+1)
            
            self.bearer_obj.fetch_bearer_token(index)
            time.sleep(20)
            if index == 99:
                self.refresh_token()
            # xd_token= self.redis_obj.get_cache_data(p_key)
            # bearer_token= self.redis_obj.get_cache_data(xd_key)
            
            # if xd_token is None:
            #     self.logger.info(f"XD token got expired of - {p_key}")
            #     if bearer_token is None:
            #         self.logger.info(f"Both XD and Bearer got expired so generating new for {p_key} and {xd_key}")
            #         time.sleep(4)
            #         self.xd_obj.fetch_xd_token(index)
            #         time.sleep(4)
            #         self.bearer_obj.fetch_bearer_token(index)
            #     elif self.redis_obj.get_expiry_time(xd_key) > 600:
            #         self.logger.info(f"Generating xd token for this bearer token {xd_key}")
            #         self.xd_obj.fetch_xd_token(index)
            #     else:
            #         self.logger.info(f"Bearer token will get expire within 10 min with {xd_key}")
                    