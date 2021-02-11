import os  
import time
from threading import Thread
from employee import Employee
from roles import Roles
from time_stamp import TimeStamp
from paycheck import PayCheck
import warnings

def edit_employee_menu():
    os.system('cls')
    print("Edit Employee Database")
    print("-"*50)
    print("1.) Add an employee information")
    print("2.) Delete an employee information")
    print("3.) Update an employee information")
    print("4.) Go back")
    print("-"*50)
    ch = int(input("Your choice: "))
    if ch not in [1,2,3,4]:
        print("Invalid choice")
        time.sleep(5)
        return edit_employee_menu()
    E = Employee()
    if ch == 1:
        name = input("Name of the employee: ")
        email = input("Email ID: ")
        role = input("Role: ")
        E.add_employee(name, email, role)
        print("Employee added")
    elif ch == 2:
        emp_id = int(input("Employee ID: "))
        E.delete_employee(emp_id)
        print("Employee info deleted")
    elif ch == 3:
        emp_id = int(input("Employee ID: "))
        name = input("Updated name: ")
        email = input("Updated email: ")
        role = input("Updated role: ")
        E.update_employee(emp_id, name, email, role)
        print("Employee info updated")
    else:
        return 
    time.sleep(5)
    return edit_employee_menu()


def edit_roles_menu():
    os.system('cls')
    print("Edit Roles Database")
    print("-"*50)
    print("1.) Add a new role")
    print("2.) Delete a role")
    print("3.) Update a role")
    print("4.) Go back")
    print("-"*50)
    ch = int(input("Your choice: "))
    if ch not in [1,2,3,4]:
        print("Invalid choice")
        time.sleep(5)
        return edit_employee_menu()
    R = Roles()
    if ch == 1:
        role = input("Role: ")
        salary = int(input("Salary per hour: "))
        ot_salary = int(input("Overtime salary per hour: "))
        expected_hours = int(input("Expected hours of work: "))
        R.add_role(role, salary, ot_salary, expected_hours)
        print("Role info added")
    elif ch == 2:
        role = input("Role: ")
        R.delete_role(role)
        print("Role deleted")
    elif ch == 3:
        role = input("Role: ")
        salary = int(input("Updated salary: "))
        ot_salary = int(input("Updated overtime salary: "))
        expected_hours = int(input("Updated expected hours of work: "))
        R.update_role(role, salary, ot_salary, expected_hours)
        print("Role info updated")
    else:
        return
    time.sleep(5)
    return edit_roles_menu()

def menu():
    os.system("cls")
    print("Payroll Management System")
    print("-"*50)
    print("1.) Generate paycheck")
    print("2.) Edit employee database")
    print("3.) Edit roles database")
    print("4.) Search for an employee info")
    print("5.) Search for a role info")
    print("6.) Exit")
    print("-"*50)
    ch = int(input("Your choice: "))
    if ch not in range(1,7):
        print("Invalid choice")
        time.sleep(5)
        return menu()
    if ch == 1:
        month = input("Month: ")
        year = int(input("Year: "))
        P = PayCheck(month, year)
        P.generate()
    elif ch == 2:
        edit_employee_menu()
    elif ch == 3:
        edit_roles_menu()
    elif ch == 4:
        E = Employee()
        emp_id = int(input("Enter employee id: "))
        E.display_details(emp_id)
    elif ch == 5:
        R = Roles()
        role = input("Role: ")
        R.display_details(role)
    else:
        return 
    time.sleep(5)
    return menu()

def wrapper():
    T = TimeStamp()
    while True:
        T.get_timeStamp()

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    T = TimeStamp()
    t = Thread(target = menu)
    t.start()
    while t.is_alive():
        T.get_timeStamp()
