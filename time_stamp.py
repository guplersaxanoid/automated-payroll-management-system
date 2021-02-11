import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import ZBarSymbol
import sqlite3
from sqlite3 import Error
import time 

class TimeStamp:
    def __init__(self, db = 'payroll.db'):
        self.db = db 

    def scan_qr(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        font = cv2.FONT_HERSHEY_PLAIN
        while True:
            _, frame = cap.read()
            cv2.normalize(frame, frame, 0, 255, cv2.NORM_MINMAX)
            decodedObjects = pyzbar.decode(frame, symbols=[ZBarSymbol.QRCODE])
            for obj in decodedObjects:
                return obj.data 
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
    
    def get_timeStamp(self):
        try:
            emp_id = int(self.scan_qr())
            time.sleep(2)
        except:
            return
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            c.execute('select isWorking, entry_time from employee where emp_id = ?',(emp_id,))
            record = c.fetchone()
            if record[0]==0:
                c.execute("select datetime('now');")
                time_stamp = c.fetchone()
                entry_time = time_stamp[0]
                c.execute("update employee \
                            set entry_time = ?, isWorking = ? \
                            where emp_id = ?",(entry_time, 1, emp_id))
                conn.commit()
            else:
                entry_time = record[1]
                c.execute("Select Cast (( JulianDay('now') - JulianDay(?) ) * 24 As Integer);",(entry_time,))
                hours_worked = c.fetchone()
                hours_worked = hours_worked[0]
                c.execute("update employee \
                            set hours_worked = ?, isWorking = 0, entry_time = NULL \
                            where emp_id = ?",(int(hours_worked) if hours_worked else 0, emp_id))
                self.compute_salary(emp_id, c)
                conn.commit()
        except Error as e:
            print(e)
        if conn is not None:
            conn.close()
        

    def compute_salary(self, id, c):
        try:
            c.execute("select employee.hours_worked, roles.salary, roles.ot_salary, roles.expected_hours \
                        from employee inner join roles \
                        on employee.role = roles.role \
                        where employee.emp_id = ?",(id,))
            record = c.fetchone()
            hours_worked = record[0]
            salary = record[1]
            ot_salary = record[2]
            expected_hours = record[3]
            ot = 0 if hours_worked < expected_hours else (hours_worked-expected_hours)
            hours_worked -= ot 
            computed_salary = salary * hours_worked + ot_salary * ot 
            c.execute("update employee \
                        set computed_salary = ? \
                        where emp_id = ?", (computed_salary,id))
        except Error as e:
            print(e)
