import logging
import mysql.connector
from app.models import Timesheet

logger = logging.getLogger(__name__)

class TimesheetRepository:
    def __init__(self):
        # Initialize database connection
        self.connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
        )
        self.cursor = self.connection.cursor()

    def save_timesheet(self, timesheet: Timesheet) -> bool:
        try:
            logger.info(f"Saving timesheet for employee {timesheet.employee_id} on {timesheet.date}")
            insert_query = """
            INSERT INTO timesheets (employee_id, hours_worked, date)
            VALUES (%s, %s, %s)
            """
            self.cursor.execute(insert_query, (timesheet.employee_id, timesheet.hours_worked, timesheet.date))
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            logger.error(f"Error saving timesheet: {err}")
            return False
        finally:
            self.cursor.close()
            self.connection.close()

    def fetch_timesheet(self, employee_id: int, date: str) -> Timesheet:
        logger.info(f"Fetching timesheet for employee {employee_id} on {date}")
        # Here you would add code to fetch the timesheet from a database
        # For now, we'll return a mock timesheet
        return Timesheet(employee_id=employee_id, hours_worked=8.0, date=date)