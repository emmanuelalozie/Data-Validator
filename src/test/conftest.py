import pytest

@pytest.fixture
def sample_json_data():
    json_data = """
    {
        "Name": "John Doe",
        "Age": 30,
        "EmployeeID": "EMP123",
        "Email": "johndoesit@gmail.com"
        "StoreManagerID": "MGR001"
        "Stores": [
            {
                "storeID": 01,
                "storeLocation": "Los Angeles",
                "storeRegion": "US SouthWest"
            },
            {
                "storeID": 02,
                "storeLocation": "California City",
                "storeRegion": "US Southwest"
            }
        ]
    }
    """
    
    return json_data