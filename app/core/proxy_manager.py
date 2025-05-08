import json
import random
import time
import requests
from typing import Optional
from dotenv import load_dotenv
import os
load_dotenv()

class ProxyManager:
    """
    ProxyManager class to manage and cache proxies, with region support and retry logic.
    """

    def __init__(self, log_handler):
        self.logger = log_handler
        self.proxy_data: dict = {}
        self.proxy_provider: str = None
        self.proxy_provider= random.choice ([
            "oxylabs", 
            "smartproxy", 
            "brightdata", 
            "privateproxy", 
            "iproyal", 
            "nodemaven"
        ])

    def _build_proxy_url(self, conn: dict) -> str:
        return f"http://{conn.get('user')}:{conn.get('password')}@{conn.get('host')}:{conn.get('port')}"

    def fetch_proxy(self, region_code: str = 'us', max_retries: int = 3) -> Optional[dict]:
        """
        Fetch proxy from provider with retry and exponential backoff.
        """
        print(os.getenv("X_API_TOKEN"))
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': os.getenv("X_API_TOKEN"),
        }

        for attempt in range(max_retries):
            try:
                self.proxy_provider = self.proxy_provider
                payload = json.dumps({
                    "provider": self.proxy_provider,
                    "region_code": region_code
                })
                print(os.getenv("PROXY_PROVIDER_ENDPOINT"))
                self.logger.info(f"Attempt {attempt + 1}: Requesting proxy for region {region_code}")
                response = requests.post(
                    os.getenv("PROXY_PROVIDER_ENDPOINT"),
                    headers=headers,
                    data=payload,
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()
                self.logger.info("Proxy fetched successfully")
                conn = data.get('proxy_connection')
                if not conn:
                    self.logger.warning("Missing 'proxy_connection' in response data.")
                    return None
                return self._build_proxy_url(conn)
            except requests.RequestException as e:
                wait = 2 ** attempt
                self.logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait}s...")
                time.sleep(wait)

        self.logger.error("All attempts to fetch proxy failed.")
        return None