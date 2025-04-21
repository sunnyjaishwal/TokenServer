'''
This module provide methods to set cache data, get cache data and get expiry time of data
'''
from redis_setup import RedisSetup

class RedisManager:
    '''
    RedisManager class is for managing all cache data
    '''
    def __init__(self,logger):
        self.logger=logger
        self.redis_obj= RedisSetup(self.logger)
        self.client= self.redis_obj.get_client()
        
    def set_cache_data(self, key, expiry, value):
        self.client.setex(key, expiry, value)
        
    def get_cache_data(self,key):
        return self.client.get(key)
    
    def get_expiry_time(self,key):
        return self.client.ttl(key)