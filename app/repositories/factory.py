# from app.repositories.memory.score_repository_memory import ScoreRepositoryMemory
from app.db.database import SessionLocal
from app.repositories.db.score_repository_db import ScoreRepositoryDB


def get_repository():
    db = SessionLocal()
    return ScoreRepositoryDB(db)
