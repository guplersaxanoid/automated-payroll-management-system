
import sqlite3
from sqlite3 import Error 
import pyqrcode
import png 
from pyqrcode import QRCode

class Employee:
    def __init__(self, db = 'payroll.db'):
        self.db = db 

    def generate_id(self):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            c.execute("select max(emp_id) from employee;");
            id  = c.fetchone()
            c.close()
            conn.close()
            print(id)
            if id[0] is None:
                return 1
            return id[0]+1 
        except Error as e:
            print(e)
        if conn is not None:
            conn.close() 

    def generate_qr(self,id: int):
        try:
            qr = pyqrcode.create(id)
            qr.png(f'QRs/{id}_qr.png',scale = 6)
            return True
        except:
            return False

    def add_employee(self, name: str, email: str, role: str):
        id =  self.generate_id()
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            params = (id, name, email, role,0,0,0)
            c.execute(f"insert into employee values(?, ?, ?, ?, ?, ?, NULL, ?);",params)
            conn.commit()
        except Error as e:
            print(e)
        while(not self.generate_qr(id)):
            print('QR code generation failed!')
        print(f'QR code generated and save at QRs/{id}_qr.png')
        if conn is not None:
            conn.close()

    def update_employee(self, id: int, name: str, email: str, role: str):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            params = (name, email, role,id)
            c.execute(f"update employee \
                        set name=?, email=?, role=? \
                        where emp_id=?;",params)
            conn.commit()
        except Error as e:
            print(e)

        if conn is not None:
            conn.close()

    def delete_employee(self, id: int):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            c.execute(f"delete from employee where emp_id=?;",(id,))
            conn.commit()
        except Error as e:
            print(e)

        if conn is not None:
            conn.close()

    def get_details(self, id: int):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            c.execute(f"select * from employee where emp_id=?;",(role,))
            record = c.fetchone()
            c.close()
            return record
        except Error as e:
            print(e)

        if conn is not None:
            conn.close()

    def display_details(self, id: int):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            c.execute(f"select * from employee where emp_id=?;",(id,))
            record = c.fetchone()
            c.close()
            print(f'ID: {record[0]}')
            print(f'Name: {record[1]}')
            print(f'Email: {record[2]}')
            print(f'Role: {record[3]}')
            print(f'Hours Worked: {record[4]}')
            
        except Error as e:
            print(e)

        if conn is not None:
            conn.close()

