'''
This script initializes the application by setting up logging and starting the scheduler.
It imports necessary modules, defines the AppStarter class, and contains methods for logging setup and running the application.
'''
import time
import logging
import os
from core.scheduler import Scheduler
from load_all_token import LoadToken




class AppStarter:
    """
    A class to initialize and run the application.
    It sets up logging and starts the scheduler.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.scheduler_obj = Scheduler(self.logger)
        self.load_token_obj= LoadToken(self.logger)
        
    def setup_logging(self):
        """
        Set up logging configuration.
        """
        log_file_path = os.path.join(os.getcwd(), "token_server.log")
        logging.basicConfig(
            level=logging.INFO,  
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file_path),  # Log to the root-level file
                logging.StreamHandler()             
            ]
        )
        self.logger.info("Logging initialized. Logs will be written to the root file and console.")

    def run(self):
        """
        Run the application.
        This method initializes the logging and starts the scheduler.
        """
        print("Application Started")
        self.setup_logging()
        self.load_token_obj.load_all_token()
        time.sleep(600)
        self.scheduler_obj.run_scheduler()      
        
if __name__ == '__main__':
    ob = AppStarter()
    ob.run()