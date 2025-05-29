from sqlalchemy import Column, Float, Integer, String

from app.db.database import Base


class CreditScore(Base):
    __tablename__ = "credit_scores"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)
    explanation = Column(String(255), nullable=False)
    job_id = Column(String(100), index=True, nullable=False)


class CreditScoreInput(Base):
    __tablename__ = "credit_score_inputs"

    id = Column(Integer, primary_key=True, index=True)
    income = Column(Float, nullable=False)
    debt = Column(Float, nullable=False)
    savings = Column(Float, nullable=False)
    late_payments = Column(Integer, nullable=False)
    job_id = Column(String(100), index=True, nullable=False)


class JobTracker(Base):
    __tablename__ = "job_tracker"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String(100), unique=True, index=True, nullable=False)
    status = Column(String(50), nullable=False, default="pending")
