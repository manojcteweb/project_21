import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Timesheet
from app.repositories import TimesheetRepository

client = TestClient(app)

# Mock database connection for testing
test_db_connection = {
    'host': 'localhost',
    'user': 'test_user',
    'password': 'test_password',
    'database': 'test_database'
}

@pytest.fixture(scope="module")
def timesheet_repository():
    # Setup the TimesheetRepository with a test database connection
    repository = TimesheetRepository()
    repository.connection = mysql.connector.connect(**test_db_connection)
    repository.cursor = repository.connection.cursor()
    yield repository
    # Teardown
    repository.cursor.close()
    repository.connection.close()


def test_save_timesheet(timesheet_repository):
    # Arrange
    timesheet = Timesheet(employee_id=1, hours_worked=8.0, date="2023-10-01")

    # Act
    result = timesheet_repository.save_timesheet(timesheet)

    # Assert
    assert result is True


def test_fetch_timesheet(timesheet_repository):
    # Arrange
    employee_id = 1
    date = "2023-10-01"

    # Act
    timesheet = timesheet_repository.fetch_timesheet(employee_id, date)

    # Assert
    assert timesheet.employee_id == employee_id
    assert timesheet.hours_worked == 8.0
    assert timesheet.date == date


def test_get_timesheet_history(timesheet_repository):
    # Arrange
    user_id = 1

    # Act
    timesheet_history = timesheet_repository.get_timesheet_history(user_id)

    # Assert
    assert len(timesheet_history) > 0
    for timesheet in timesheet_history:
        assert timesheet.employee_id == user_id
        assert isinstance(timesheet.hours_worked, float)
        assert isinstance(timesheet.date, str)