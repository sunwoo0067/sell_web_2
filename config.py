import os

class Config:
    DATABASE_URL = "mysql+pymysql://root:ehdgod1101*@localhost/sell_web_2"
    SECRET_KEY = "your-secret-key-here"
    API_KEYS = {
        "ownerclan": "your-ownerclan-api-key",
        "funshopping": "your-funshopping-api-key",
        "gentrade": "your-gentrade-api-key"
    }
    NAVER_ACCESS_TOKEN = "your-naver-access-token"
    COUPANG_ACCESS_KEY = "your-coupang-access-key"
    COUPANG_SECRET_KEY = "your-coupang-secret-key"
    # ... 