from pydantic import BaseModel


class ScoreOutput(BaseModel):
    score: int
    category: str
    explanation: str
