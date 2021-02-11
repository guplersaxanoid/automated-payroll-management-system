import sqlite3
from sqlite3 import Error 

class Roles:
    def __init__(self, db='payroll.db'):
        self.db = db 

    def add_role(self,role: str, salary: int, ot_salary: int, expected_hours: int):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            params = (role, salary, ot_salary, expected_hours)
            c.execute(f"insert into roles values(?, ?, ?, ?);",params)
            conn.commit()
        except Error as e:
            print(e)
        if conn is not None:
            conn.close()

    def update_role(self,role: str, salary: int, ot_salary: int, expected_hours: int):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            params = (salary, ot_salary, expected_hours, role)
            c.execute(f"update roles \
                        set salary=?, ot_salary=?, expected_hours=? \
                        where role=?;",params)
            conn.commit()
        except Error as e:
            print(e)

        if conn is not None:
            conn.close()

    def delete_role(self,role: str):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            c.execute(f"delete from roles where role=?;",(role,))
            conn.commit()
        except Error as e:
            print(e)

        if conn is not None:
            conn.close()

    def get_details(self,role: str):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            c.execute(f"select * from roles where role=?;",(role,))
            record = c.fetchone()
            c.close()
            return record
        except Error as e:
            print(e)

        if conn is not None:
            conn.close()

    def display_details(self,role: str):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            c.execute(f"select * from roles where role=?;",(role,))
            record = c.fetchone()
            c.close()
            print(f'Role: {record[0]}')
            print(f'Salary: {record[1]}')
            print(f'Overtime Salary: {record[2]}')
            print(f'Expected hours of work: {record[3]}')
        except Error as e:
            print(e)

        if conn is not None:
            conn.close()


