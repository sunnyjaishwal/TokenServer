'''
This script initializes the application by setting up logging and starting the scheduler.
It imports necessary modules, defines the AppStarter class, and contains methods for logging setup and running the application.
'''
import logging
import os
from load_all_token import LoadToken
from core.token_manager import TokenManager

class AppStarter:
    """
    A class to initialize and run the application.
    It sets up logging and starts the scheduler.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.load_token_obj= LoadToken(self.logger)
        self.token_manager_obj= TokenManager(self.logger)
        
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
        self.token_manager_obj.refresh_token()   
        
if __name__ == '__main__':
    ob = AppStarter()
    ob.run()