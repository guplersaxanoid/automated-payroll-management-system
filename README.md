# automated-payroll-management-system
An attempt on automating a payroll management system by reducing the human intervention in the process that does not requires any kind of authorization from an administrator at every juncture. The project is python based, and used SQLite as database engine

Automating every aspect of a payroll management system is a major focus for every large organizations. Making use of SQLite back-end, our proposal is an automated payroll management system in which every process is handled by a python program without any human intervention with the exception of create and delete operations on a table which requires data input and/or authorization from a user. The calculation of number of hours that an employee spent inside the organization can be automated by timestamping their entry and exit by scanning a graphically encoded data that contains the employee’s identity details. The salary of an employee is calculated with the number of hours they spent inside the organization, and those details are endowed into a PDF file and sent to the employee via email using SMTP protocol.

The data corresponding to each of the employee and that of work roles(or positions) available in the organization are stored in two separate tables in a .db file
A.	Employee table
As shown in Fig. 1. a), the employee table consists of fields regarding identity information, contact information and information about the number of hours worked by an employee. It also records the entry time of an employee if they are inside the organization. The column named isWorking is used as a binary field to record the employee’s presence inside the organization. If isWorking is 0, then the employee did not timestamp their entry inside the organization yet. Else if, isWorking is 1, then the employee has timestamped their entry 

into the organization and they have not checked out yet. The field computed_salary holds the computed salary of the employee for the number of hours they worked till date.
B.	Roles table
As shown in Fig. 1. b), the roles table contains information about the available roles in the organization, including the salary information and the number of hours of work expected off an employee in the role.

![alt text](https://github.com/DeveloperInProgress/automated-payroll-management-system/blob/main/images/tables.jpg)
 
Fig. 1. (a) employee table to hold employee details. (b) roles tables to hold details about work roles available in the organization

The employee ID of each of the employees are encoded in a QR code. At the time of entry or exit from the organization, employees may scan their QR code with a QR code scanner. 
The system running the QR code scanner obtains the employee ID from scanned QR code and updates the entry time of the employee as the current local time. In case, an employee is exiting the organization, the number of hours that the employee spent in the organization is computed by the system and updated in the employee table.


An interface is installed between the user and the database to let the user to add, update or delete information in the employee and the roles table. Those operations cannot be performed when an employee is time stamping their entry or exit because the database is locked by this process. This ensures that two conflicting transactions are not performed on the table at the same point in time.

At each payment cycle in the organization, the salary of each of the employees are computed using the number of hours they worked and their salary per hour. The former information is recorded in the employee table and the later is recorded in the roles table. The payment details along with the employee’s identity details are recorded in a PDF file  and saved in the local system. The number of hours worked by the employee is reset to 0 as soon as the payment details are generated. 

The PDF files containing the payment details are encapsulated with a MIME-Version header and encoded in base 64 format. This payload is sent the corresponding employee’s email  using SMTP protocol.

<h2> Executing the Program </h2>

The program executes on the assumption that a database file(.db) that contains **employee** and **roles** table. The python file **create_database.py** can be used to create such database, and it will be saved as **payroll.db** in the same directory.

```
python create_database.py
```

After the database has been created, run the main.py program to load the interface along with the QR Code Scanner. 
```
python main.py
```

<h2> Additional Details </h2>

1.) The QR Codes for employees will be generated after adding their details into the table using the interface. These QR codes will be stored in a folder named **QRs**
2.) The pdf files containing employee's payment details will be generated when the user chooses to generate paycheck using the interface. These pdf files will be stored in a folder named **paychecks**
3.) In line 18 of paycheck.py, assign the company's email address to sender_address . This email address will be used to send the payment details of employees. In line 19 of paycheck.py, assign the company email's password to sender_password

<h2> Possible Improvements to be made <h2>
  
  1.) Documentation of the programs is needed
  2.) Better error handling on user inputs is necessary
  3.) Timestamping process could be made more secure. For example, a biometric scanner can be used to timestamp.
