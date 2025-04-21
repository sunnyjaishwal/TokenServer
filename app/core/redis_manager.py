"""
This module provides methods to set cache data, retrieve cache data,
and check expiry time of cached data.
"""
import random
from services.redis_setup import RedisSetup
from models.constant import Mapping
from typing import Optional, Tuple


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

    def get_cache_data(self) -> Optional[Tuple[Optional[bytes], Optional[bytes]]]:
        """
        Retrieve cache data using the key.
        Returns a tuple of tokens if found, or None if not.
        """
        try:
            number = random.randint(1, 51)
            p_token, xd_token = getattr(Mapping, f"p_token_{number}")

            x_d_token = self.client.get(p_token)
            access_token = self.client.get(xd_token)

            if x_d_token and access_token:
                self.logger.info(f"Cache data retrieved successfully for key: {p_token}: {xd_token}")
                return x_d_token, access_token
            else:
                self.logger.warning(f"Cache data not found for key: {p_token}: {xd_token}. Retrying...")
                # Retry once with a new random number
                number = random.randint(1, 51)
                p_token, xd_token = getattr(Mapping, f"p_token_{number}")
                return self.client.get(p_token), self.client.get(xd_token)

        except Exception as e:
            self.logger.error(f"Failed to retrieve cache data for key: {p_token}:{xd_token}. Error: {e}")
            return None

    def get_expiry_time(self, key: str) -> Optional[int]:
        """
        Get the expiry time of cache data using the key.
        Returns the time-to-live (TTL) in seconds, or None if the key does not exist.
        """
        try:
            ttl = self.client.ttl(key)
            if ttl != -2:  # -2 indicates the key does not exist
                self.logger.info(f"Expiry time for key {key}: {ttl} seconds")
                return ttl
            else:
                self.logger.warning(f"No expiry time found for key: {key}")
                return None
        except Exception as e:
            self.logger.error(f"Failed to get expiry time for key: {key}. Error: {e}")
            return None
