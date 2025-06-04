import logging
from models import Timesheet

logger = logging.getLogger(__name__)

class TimesheetService:
    def __init__(self):
        # Initialize any required resources, e.g., database connections
        pass

    def submit_timesheet(self, timesheet: Timesheet) -> dict:
        # Validate timesheet data
        if timesheet.hours_worked < 0:
            logger.error("Invalid hours worked: cannot be negative")
            return {"status": "error", "message": "Invalid hours worked: cannot be negative"}
        
        # Simulate saving to a database
        logger.info(f"Submitting timesheet for employee {timesheet.employee_id} on {timesheet.date}")
        # Here you would typically add code to save the timesheet to a database
        return {"status": "success", "message": "Timesheet submitted successfully"}

    def get_timesheet(self, employee_id: int, date: str) -> dict:
        logger.info(f"Fetching timesheet for employee {employee_id} on {date}")
        # Here you would typically add code to retrieve the timesheet from a database
        # For now, we'll just return a mock timesheet
        return {
            "employee_id": employee_id,
            "hours_worked": 8.0,  # Mock data
            "date": date
        }
