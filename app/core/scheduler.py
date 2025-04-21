'''

'''
from core.token_manager import TokenManager
import schedule
class Scheduler:
    
    def __init__(self, logger):
        self.logger=logger
        self.token_manager= TokenManager(self.logger)
        
    def run_scheduler(self):
        self.logger.info("Scheduler Started")
        schedule.every(2).minutes.do(self.token_manager.refresh_token)
        
        while True:
            schedule.run_pending()
            