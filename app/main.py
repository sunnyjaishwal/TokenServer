from fastapi import FastAPI
import ast
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
    token = redis_manager.get_cached_token_data()
    token= ast.literal_eval(token)
    return JSONResponse(
        content={
            "tokens": {
                "x_d_token": token[0], 
                "access_token": token[1]
                }
            }
    )
