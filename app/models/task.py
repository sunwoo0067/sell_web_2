from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_type = Column(String)  # 작업 유형 (이미지 처리, 상품 등록 등)
    status = Column(String)  # 작업 상태 (대기중, 처리중, 완료, 실패)
    result = Column(JSON)  # 작업 결과 저장
    error_message = Column(String, nullable=True)  # 에러 메시지
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True) 