from fastapi import FastAPI, HTTPException
import logging
from app.models import Timesheet
from app.services import TimesheetService

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Initialize TimesheetService
timesheet_service = TimesheetService()

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"Hello": "World"}

@app.post("/submit_timesheet")
async def submit_timesheet(timesheet: Timesheet):
    logger.info(f"Timesheet submitted for employee {timesheet.employee_id} on {timesheet.date}")
    result = timesheet_service.submit_timesheet(timesheet)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result
