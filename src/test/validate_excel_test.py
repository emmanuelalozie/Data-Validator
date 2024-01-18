from src.test.conftest import sample_json_data
from main.python.dto import Employee
from src.main.python.load_excel import load_excel
import random

def test_validate_json_data():
    # Create a random EmployeeDTO object
    employee = Employee(
        name="John Doe",
        age=random.randint(18, 60),
        salary=random.uniform(1000, 5000)
    )
    employee_dto: Employee = load_excel()

    # Test the sample JSON data against the EmployeeDTO object
    assert sample_json_data["name"] == employee.name
    assert sample_json_data["age"] == employee.age
    assert sample_json_data["salary"] == employee.salary