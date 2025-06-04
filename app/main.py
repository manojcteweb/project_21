from fastapi import FastAPI
import logging
from pydantic import BaseModel

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

class Timesheet(BaseModel):
    employee_id: int
    hours_worked: float
    date: str

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"Hello": "World"}

@app.post("/submit_timesheet")
async def submit_timesheet(timesheet: Timesheet):
    logger.info(f"Timesheet submitted for employee {timesheet.employee_id} on {timesheet.date}")
    # Here you would typically add code to save the timesheet to a database
    return {"status": "success", "message": "Timesheet submitted successfully"}

# Additional setup for security and other configurations can be added here
