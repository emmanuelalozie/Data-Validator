import pandas as pd
from main.python.dto.Employee import Employees

def load_excel():
    df = pd.read_excel('path/to/your/excel/file.xlsx', sheet_name='Employee')

    # Get the column headers
    column_headers = df.columns.tolist()

    # Check if the attributes of the Employee class exist as column headers
    if all(attr in column_headers for attr in ['name', 'email', 'store_manager_id', 'store_id']):
        print("All column headers found in the Excel file.")

        # Create a list to store the employee objects
        employees = []

        # Iterate over each row in the dataframe
        for index, row in df.iterrows():
            # Create a new employee object
            employee = Employee()

            # Set the attributes of the employee object
            employee.name = row['name']
            employee.email = row['email']
            employee.store_manager_id = row['store_manager_id']
            employee.store_id = row['store_id']

            # Append the employee object to the list
            employees.append(employee)

        # Print the list of employee objects
        for employee in employees:
            print(employee.__dict__)

    else:
        print("Some column headers are missing in the Excel file.")


if __name__ == "__main__":
    load_excel()
