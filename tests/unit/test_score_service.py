from app.models.input.score_input import ScoreInput
from app.services.score_service import calculate_score


def test_calculate_score_high_income_low_debt():
    input_data = ScoreInput(income=10000, debt=500, late_payments=0, savings=5000)
    # Cálculo:
    # penalties = 500 * 0.1 + 0 * 20 = 50
    # bonuses = 5000 * 0.05 = 250
    # score = 1000 - 50 + 250 = 1200 → limitado para 1000
    result = calculate_score(input_data)
    assert result.score == 1000
    assert result.category == "Excellent"


def test_calculate_score_low_income_high_debt():
    input_data = ScoreInput(income=1000, debt=4000, late_payments=2, savings=100)
    # penalties = 4000 * 0.1 + 2 * 20 = 400 + 40 = 440
    # bonuses = 100 * 0.05 = 5
    # score = 1000 - 440 + 5 = 565
    result = calculate_score(input_data)
    assert result.score == 565
    assert result.category == "Fair"


def test_calculate_score_midrange():
    input_data = ScoreInput(income=5000, debt=2500, late_payments=1, savings=2000)
    # penalties = 2500 * 0.1 + 1 * 20 = 250 + 20 = 270
    # bonuses = 2000 * 0.05 = 100
    # score = 1000 - 270 + 100 = 830
    result = calculate_score(input_data)
    assert result.score == 830
    assert result.category == "Excellent"


def test_calculate_score_zero_income():
    input_data = ScoreInput(income=1, debt=1000, late_payments=0, savings=100)
    # Aqui colocamos income=1 pois income > 0 é validação da Pydantic
    # penalties = 1000 * 0.1 = 100
    # bonuses = 100 * 0.05 = 5
    # score = 1000 - 100 + 5 = 905
    result = calculate_score(input_data)
    assert result.score == 905
    assert result.category == "Excellent"
