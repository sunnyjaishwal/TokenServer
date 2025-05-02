'''
This module provides functionality to generate, retrieve, and store authentication tokens in redis.
It is useful for handling API authentication by managing token expiration and renewal.
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
        self.xd_token = None
        self.bearer_token = None
    
    def get_tokens(self,count):
        try:
            xd_response = self.xd_obj.fetch_xd_token(count)
            self.xd_token= xd_response.get('token')
            if self.xd_token:
                access_response = self.bearer_obj.fetch_bearer_token(self.xd_token)
                if access_response:
                    self.bearer_token = access_response.get('access_token')
                    xd_expiry_time = int(xd_response.get('renewInSec'))
                    value = [self.xd_token, self.bearer_token]
                    key= f"P_Token_{count+1}"
                    self.redis_obj.set_cache_data(key, int(xd_expiry_time), str(value))
                else:
                    self.logger.error(f"Unable to generate Bearer token for token - {count+1}")
            else:
                self.logger.error(f"Unable to generate X-D-Token for token - {count+1}")
            
        except Exception as e:
            self.logger.error(f"Error occurred while Bearer tokens: {e}")    
            
    def load_first_time_token(self):
        for index in range(5):   
            self.get_tokens(index)
            time.sleep(60)
    # def refresh_token(self):
    #     for index in range(11):
    #         self.get_tokens(index)
    #         time.sleep(5)
    #         if index == 10:
    #             time.sleep(600)
    #             self.refresh_token()
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
                    