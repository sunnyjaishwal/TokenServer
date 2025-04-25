"""
This module provides methods to set cache data, retrieve cache data,
and check expiry time of cached data.
"""
import random
from services.redis_setup import RedisSetup
from models.constant import Mapping
from typing import Optional, Tuple
from fastapi import HTTPException


class RedisManager:
    """
    RedisManager class for managing all cache data.
    """

    def __init__(self, logger):
        self.logger = logger
        self.redis_obj = RedisSetup(self.logger)
        self.client = self.redis_obj.get_client()

    def set_cache_data(self, key: str, expiry: int, value: str) -> None:
        """
        Set cache data with a key, expiry time, and value.
        The expiry time is in seconds.
        """
        try:
            self.client.setex(key, expiry, value)
            self.logger.info(f"Cache data set successfully for key: {key}")
        except Exception as e:
            self.logger.error(f"Failed to set cache data for key: {key}. Error: {e}")

    # def get_cache_data(self, key) :
    #     return self.client.get(key)

    def get_cached_token_data(self):
        """
        Retrieve cache data.
        Returns a tuple of tokens if found, or None if not.
        """
       
        try:
            for attempt in range(3):
                key = self.client.randomkey()
                # p_token, xd_token = f"p_token_{number}", f"xd_token_{number}"
                # x_d_token = self.client.get(p_token)
                # access_token = self.client.get(xd_token)
                token = self.client.get(key)

                if token:
                    self.logger.info(f"Cache data retrieved successfully")
                    return token
                else:
                    self.logger.warning(f"Attempt {attempt + 1}: Cache data not found. Retrying...")
                
        except Exception as e:
            self.logger.error(f"All three attempts failed to retrieve cache data Error: {e}")
            raise HTTPException(status_code=400, detail=str(e))

    