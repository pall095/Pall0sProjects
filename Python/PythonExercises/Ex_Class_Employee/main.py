 
"""
ASSIGNEMENT 

Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))


"""

import Employee as emp


if __name__ == "__main__" :
    
    e1 = emp.Employee( "ADAMS", "E7876", 50000, "ACCOUNTING" )
    e2 = emp.Employee( "JONES", "E7499", 45000, "RESEARCH" )
    e3 = emp.Employee( "MARTIN", "E7900", 50000, "SALES" )
    e4 = emp.Employee( "SMITH", "E7698", 55000, "OPERATIONS" )
    
    print( e1.dep )
    e1.dep = "NUOVO"
    print( e1.dep )
    
    
    for item in emp.Employee.employee_list :
        print( repr( item ) )
