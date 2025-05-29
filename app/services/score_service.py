from app.core.logger import get_logger
from app.models.input.score_input import ScoreInput
from app.models.output.score_output import ScoreOutput

logger = get_logger(__name__)

def calculate_score(data: ScoreInput) -> ScoreOutput:
    logger.info("Calculating score", extra=data.dict())

    base_score = 1000
    penalties = (data.debt * 0.1) + (data.late_payments * 20)
    bonuses = data.savings * 0.05

    score = int(base_score - penalties + bonuses)
    score = max(1, min(score, 1000))

    if score >= 800:
        category = "Excellent"
    elif score >= 650:
        category = "Good"
    elif score >= 500:
        category = "Fair"
    else:
        category = "Poor"

    logger.info(
        "Score calculated",
        extra={"score": score, "category": category}
    )

    return ScoreOutput(
        score=score,
        category=category,
        explanation="Score calculated using income, debt, savings and payment history."
    )
