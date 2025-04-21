from fastapi import FastAPI
import uuid
import json
from app_starter import AppStarter

from core.redis_manager import RedisManager

app = FastAPI()

app_starter = AppStarter()
app_starter.setup_logging()
ResisManager = RedisManager(app_starter.logger)

@app.get("/generate-tokens")
def generate_tokens():
    """
    Generate and return a unique token.
    """
    token = ResisManager.get_cache_data()
    return json.dumps(token)