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

    def fetch_timesheet(self, employee_id: int, date: str) -> Timesheet:
        logger.info(f"Fetching timesheet for employee {employee_id} on {date}")
        # Here you would add code to fetch the timesheet from a database
        # For now, we'll return a mock timesheet
        return Timesheet(employee_id=employee_id, hours_worked=8.0, date=date)

    def get_timesheet_history(self, user_id: int) -> list:
        try:
            logger.info(f"Fetching timesheet history for user {user_id}")
            select_query = """
            SELECT employee_id, hours_worked, date FROM timesheets WHERE employee_id = %s
            """
            self.cursor.execute(select_query, (user_id,))
            rows = self.cursor.fetchall()
            timesheet_history = [Timesheet(employee_id=row[0], hours_worked=row[1], date=row[2]) for row in rows]
            return timesheet_history
        except mysql.connector.Error as err:
            logger.error(f"Error fetching timesheet history: {err}")
            return []
        finally:
            self.cursor.close()
            self.connection.close()