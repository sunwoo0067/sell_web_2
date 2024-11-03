from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config

# MySQL 연결 URL에 charset 추가
DATABASE_URL = Config.DATABASE_URL + "?charset=utf8mb4"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # 연결 상태 확인
    pool_recycle=3600,   # 1시간마다 연결 재생성
    echo=True            # SQL 로그 출력 (디버깅용)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 