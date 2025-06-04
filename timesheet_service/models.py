from pydantic import BaseModel

class Timesheet(BaseModel):
    employee_id: int
    hours_worked: float
    date: str
