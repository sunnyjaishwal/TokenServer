'''
'''
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
        for index in range(50):
            p_key='p_token_'+str(index+1)
            xd_key='xd_token_'+str(index+1)
            xd_token= self.redis_obj.get_cache_data(p_key)
            bearer_token= self.redis_obj.get_cache_data(xd_key)
            if xd_token:
                if self.redis_obj.get_expiry_time(p_key) > 2:
                    if bearer_token is None:
                        self.logger.info("xd token is their but bearer token expired")
                        self.bearer_obj.fetch_bearer_token(index)
                        self.logger.info(f"Generated new bearer token for this xd {xd_key}")
                    if self.redis_obj.get_expiry_time(xd_key) < 2:
                        pass
            else:
                self.logger.info("XD token got expired")
                if bearer_token is None:
                    self.logger.info(f"Both XD and Bearer got expired so generating new for {p_key} and {xd_key}")
                    self.xd_obj.fetch_xd_token(index)
                    self.bearer_obj.fetch_bearer_token(index)
                elif bearer_token and self.redis_obj.get_expiry_time(xd_key) > 2:
                    self.logger.info(f"generating xd token for this bearer token {xd_key}")
                    self.xd_obj.fetch_xd_token(index)
                else:
                    self.logger.info(f"Bearer token will get expire within 2 min with {xd_key}")
                    pass