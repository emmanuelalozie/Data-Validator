from src.test.conftest import sample_json_data
from src.main.python.dto import EmployeeDTO
import random

def test_validate_json_data():
    # Create a random EmployeeDTO object
    employee = EmployeeDTO(
        name="John Doe",
        age=random.randint(18, 60),
        salary=random.uniform(1000, 5000)
    )

    # Test the sample JSON data against the EmployeeDTO object
    assert sample_json_data["name"] == employee.name
    assert sample_json_data["age"] == employee.age
    assert sample_json_data["salary"] == employee.salary