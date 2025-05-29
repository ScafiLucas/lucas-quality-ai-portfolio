from sqlalchemy.orm import Session

from app.models.input.score_input import ScoreInput
from app.models.output.score_output import ScoreOutput
from app.repositories.interfaces.base_repository import BaseRepository
from app.db.models import ScoreInputModel, CreditScore


class ScoreRepositoryDB(BaseRepository):
    def __init__(self, db: Session):
        self.db = db

    def save_input(self, job_id: str, score_input: ScoreInput):
        db_input = ScoreInputModel(
            job_id=job_id,
            income=score_input.income,
            debt=score_input.debt,
            late_payments=score_input.late_payments,
            savings=score_input.savings,
        )
        self.db.add(db_input)
        self.db.commit()
        self.db.refresh(db_input)
        return db_input

    def save_output(self, job_id: str, score_output: ScoreOutput):
        db_output = CreditScore(
            job_id=job_id,
            score=score_output.score,
            category=score_output.category,
            explanation=score_output.explanation,
        )
        self.db.add(db_output)
        self.db.commit()
        self.db.refresh(db_output)
        return db_output

    def get_by_job_id(self, job_id: str):
        return self.db.query(ScoreInputModel).filter(ScoreInputModel.job_id == job_id).all()
