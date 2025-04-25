'''
This module provides a singleton-based Redis client setup using the redis-py library.
It ensures only one Redis connection is established and reused across the application.
'''
import redis
import os
from dotenv import load_dotenv
load_dotenv()
class RedisSetup:
    '''
    Singleton class to manage Redis Client connection
    '''
    _instance = None
    _client = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RedisSetup, cls).__new__(cls)
        return cls._instance

    def __init__(self, logger,host='redis', port=6379, db=0):
        self.logger = logger
        self.host = os.getenv('REDIS_HOST')
        self.port = int(os.getenv('REDIS_PORT'))
        self.db = db
        RedisSetup._client = self.create_client()

    def create_client(self):
        '''
        Create a Redis client instance.
        This method is called only once during the initialization of the class.
        '''

        try:
            client = redis.Redis(host=self.host,
                                 port=self.port,
                                 db=self.db,
                                 decode_responses=True
                    )
            client.ping()  # Test the connection
            self.logger.info("Redis client created successfully.")
        except ConnectionError as e:
            print(f"Failed to connect to Redis: {e}")
        return client
        
    def get_client(self):
        '''
        Get the Redis client instance.
        This method returns the existing client if already created.
        '''
        return RedisSetup._client
     