from abc import ABC, abstractmethod

from app.models.input.score_input import ScoreInput
from app.models.output.score_output import ScoreOutput


class BaseRepository(ABC):
    @abstractmethod
    def save_input(self, job_id: str, score_input: ScoreInput): ...

    @abstractmethod
    def save_output(self, job_id: str, score_output: ScoreOutput): ...

    @abstractmethod
    def get_by_job_id(self, job_id: str): ...
