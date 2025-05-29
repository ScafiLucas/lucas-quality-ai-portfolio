from sqlalchemy.orm import Session

from app.db.models import CreditScore, CreditScoreInput, JobTracker
from app.models.input.score_input import ScoreInput
from app.models.output.score_output import ScoreOutput


def save_score_to_db(db: Session, job_id: str, score_output: ScoreOutput):
    db_score = CreditScore(
        job_id=job_id,
        score=score_output.score,
        category=score_output.category,
        explanation=score_output.explanation,
    )
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score


def get_scores_by_job_id(db: Session, job_id: str):
    return db.query(CreditScore).filter(CreditScore.job_id == job_id).all()


def save_input_to_db(db: Session, job_id: str, score_input: ScoreInput):
    db_input = CreditScoreInput(
        job_id=job_id,
        income=score_input.income,
        debt=score_input.debt,
        savings=score_input.savings,
        late_payments=score_input.late_payments,
    )
    db.add(db_input)
    db.commit()
    db.refresh(db_input)
    return db_input


def get_pending_jobs(db: Session):
    return db.query(JobTracker).filter(JobTracker.status == "pending").all()


def get_inputs_by_job_id(db: Session, job_id: str):
    return db.query(CreditScoreInput).filter(CreditScoreInput.job_id == job_id).all()


def update_job_status(db: Session, job_id: str, status: str):
    job = db.query(JobTracker).filter(JobTracker.job_id == job_id).first()
    if job:
        job.status = status
        db.commit()


def persist_score_result(db: Session, score_output: ScoreOutput, job_id: str):
    return save_score_to_db(db, job_id, score_output)
