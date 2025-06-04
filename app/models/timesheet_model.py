from pydantic import BaseModel

class TimesheetModel(BaseModel):
    date: str
    hours_worked: float
    task_description: str
