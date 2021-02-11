import sqlite3
from sqlite3 import Error
from fpdf import FPDF
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

class PayCheck:
    def __init__(self, month, year, db = 'payroll.db'):
        self.db = db
        self.month = month
        self.year = year 

    def mail_check(self,filename,email_id):
        try:
            sender_address = #company's mail id
            sender_password =  #company's mail id password
            receiver_address = email_id
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = f"Payment details for {self.month} {self.year}"
            
            body = f"Payment details for {self.month} {self.year} is attahed below"
            message.attach(MIMEText(body,'plain'))

            attachment = open(filename,'rb')
            p = MIMEBase('application','octet-stream')

            p.set_payload((attachment).read())
            encoders.encode_base64(p)

            p.add_header('Content-Disposition',f"attachment; filename = {filename}")
            message.attach(p)
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(sender_address, sender_password)
            text = message.as_string()
            s.sendmail(sender_address, receiver_address, text)
            s.quit()
            print(f"Mail sent to {email_id}")
        except:
            print(f"Failed to send mail to {email_id}")

    def generate(self, id = None):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            if id is None:
                c.execute("select emp_id, name, email, hours_worked, computed_salary from employee")
            else:
                c.execute("select emp_id, name, email, hours_worked, computed_salary from employee where emp_id = ?",(id, ))

            record = c.fetchall()
            for r in record:
                emp_id = r[0]
                name = r[1]
                email = r[2]
                hours_worked = r[3]
                computed_salary = r[4]
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial', size = 15)
                pdf.cell(200,10,txt='Sample Organization',ln=1,align='C')
                pdf.cell(200,10,txt=f'Payment Details - {self.month} {self.year}',ln=1,align='C')
                pdf.set_font('Arial', size = 10)
                pdf.cell(200,10,txt=f'ID: {emp_id}',ln=1)
                pdf.cell(200,10,txt=f'Name: {name}', ln=1)
                pdf.cell(200,10,txt=f'Hours Worked: {hours_worked}',ln=1)
                pdf.cell(200,10,txt=f'Salary: {computed_salary}')
                pdf.output(f'paychecks/{emp_id}_{self.month}_{self.year}.pdf')
                c.execute("update employee \
                            set hours_worked = 0, computed_salary = 0 \
                            where emp_id = ?",(emp_id, ))
                self.mail_check(f'paychecks/{emp_id}_{self.month}_{self.year}.pdf', email)
        except Error as e:
            print(e)
        if conn is not None:
            conn.close()
              

