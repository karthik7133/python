print("YADAVALLI UDAY KUMAR , 23MIS7330")
import numpy as np

dt = np.dtype([('Employee_ID', np.int32), ('Name', 'U15'), ('Department', 'U10'), ('Salary', np.float64)])

employees = np.array([
    (101, 'Alice', 'HR', 70000),
    (102, 'Bob', 'IT', 80000),
    (103, 'Charlie', 'Finance', 90000),
    (104, 'David', 'IT', 75000),
    (105, 'Eve', 'Manager', 85000)
], dtype=dt)

new_employee = np.array([(106, 'Frank', 'Manager', 95000)], dtype=dt)
employees = np.concatenate((employees, new_employee))

high_salary_employees = employees[employees['Salary'] > 75000]
sorted_employees = np.sort(employees, order='Employee_ID')
employees['Salary'][employees['Department'] == 'IT'] *= 1.10
manager_names = employees['Name'][employees['Department'] == 'Manager']

print("Updated Employee Records:")
print(employees)
print("\nEmployees with Salary > 75,000:")
print(high_salary_employees)
print("\nSorted Employees by Employee_ID:")
print(sorted_employees)
print("\nNames of Employees in 'Manager' Department:")
print(manager_names)