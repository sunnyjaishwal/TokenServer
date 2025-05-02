'''
Background scheduler that checks Redis DB size every minute.
If the size is less than 5, it calls `get_tokens(count)` from tokenManager.py.
'''
import schedule
import time
#from core.token_manager import TokenManager
from core.redis_manager import RedisManager

class BotScheduler:
    def __init__(self,logger):
        self.logger = logger
        self.token_manager = None
        self.redis_manager = RedisManager(self.logger)
        self.count = 5
    
    def check_and_refresh(self):
        try:
            db_size = self.redis_manager.get_key_count()
            self.logger.info(f"Redis DB size: {db_size}")

            if db_size < 5:
                self.token_manager.get_tokens(self.count)
                self.count += 1
                if self.count == 25:
                    self.count = 0
            else:
                self.logger.info("DB size is >= 5, no action taken.")
        except Exception as e:
            self.logger.error(f"Error checking Redis: {e}")

    def run_scheduler(self, token_manager):
        self.token_manager=token_manager
        schedule.every(1).minutes.do(self.check_and_refresh)
        while True:
            schedule.run_pending()
            time.sleep(1)