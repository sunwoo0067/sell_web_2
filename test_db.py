from sqlalchemy import create_engine
from config import Config

def test_connection():
    try:
        engine = create_engine(Config.DATABASE_URL)
        with engine.connect() as connection:
            print("데이터베이스 연결 성공!")
    except Exception as e:
        print(f"연결 오류: {e}")

if __name__ == "__main__":
    test_connection() 