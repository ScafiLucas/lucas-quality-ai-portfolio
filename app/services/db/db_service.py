from sqlalchemy.orm import Session
from app.db.models import CreditScore
from app.models.output.score_output import ScoreOutput

def save_score_to_db(db: Session, job_id: str, score_output: ScoreOutput):
    db_score = CreditScore(
        job_id=job_id,
        score=score_output.score,
        category=score_output.category,
        explanation=score_output.explanation
    )
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def get_scores_by_job_id(db: Session, job_id: str):
    return db.query(CreditScore).filter(CreditScore.job_id == job_id).all()
