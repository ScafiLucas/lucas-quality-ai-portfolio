from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class CreditScore(Base):
    __tablename__ = "credit_scores"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)
    explanation = Column(String(255), nullable=False)
    job_id = Column(String(100), index=True, nullable=False)
