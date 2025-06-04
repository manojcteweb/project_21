from pydantic import BaseModel, Field, validator
from datetime import datetime

class Timesheet(BaseModel):
    employee_id: int = Field(..., gt=0, description="The ID of the employee must be greater than 0")
    hours_worked: float = Field(..., ge=0, le=24, description="Hours worked must be between 0 and 24")
    date: str

    @validator('date')
    def validate_date(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in the format YYYY-MM-DD")
        return value
