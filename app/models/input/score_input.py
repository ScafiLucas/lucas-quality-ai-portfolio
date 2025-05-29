from pydantic import BaseModel, Field


class ScoreInput(BaseModel):
    income: float = Field(..., gt=0, description="Monthly income")
    debt: float = Field(..., ge=0, description="Total outstanding debt")
    late_payments: int = Field(
        ..., ge=0, description="Number of late payments in the past year"
    )
    savings: float = Field(..., ge=0, description="Average monthly savings")
