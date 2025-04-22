from fastapi import FastAPI
import uuid
import json

from fastapi.responses import JSONResponse
from app_starter import AppStarter

from core.redis_manager import RedisManager

app = FastAPI()

app_starter = AppStarter()
app_starter.setup_logging()
redis_manager = RedisManager(app_starter.logger)

@app.get("/generate-tokens")
def generate_tokens():
    """
    Generate and return a unique token.
    """
    x_d_token, access_token = redis_manager.get_cached_token_data()
    return JSONResponse(
        content={
            "tokens": {
                "x_d_token": x_d_token, 
                "access_token": access_token
                }
            }
    )
