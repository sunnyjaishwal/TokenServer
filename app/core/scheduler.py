'''
This script initializes the application by setting up logging and starting the scheduler.
It imports necessary modules, defines the Scheduler class, and contains methods for logging setup and running the application.
'''
import schedule
import time
from core.token_manager import TokenManager

class Scheduler:
    '''
    A class to manage the scheduling of tasks.
    It uses the schedule library to run tasks at specified intervals.
    '''

    def __init__(self, logger):
        self.logger=logger
        self.token_manager= TokenManager(self.logger)
        
    def run_scheduler(self):
        '''
        Run the scheduler to execute tasks at specified intervals.
        '''
        self.logger.info("Scheduler Started")
        schedule.every(20).seconds.do(self.token_manager.refresh_token)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
            