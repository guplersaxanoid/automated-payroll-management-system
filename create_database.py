import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('payroll.db')
except Error as e:
    print(e)

if conn is not None:
    create_emp_table = """create table if not exists employee(
                            emp_id integer primary key,
                            name text not null,
                            email text not null,
                            role text not null,
                            hours_worked integer not null,
                            isWorking integer,
                            entry_time text,
                            computed_salary number not null
                            );"""
    create_roles_table = """create table if not exists roles(
                                role text primary key,
                                salary integer not null,
                                ot_salary integer not null,
                                expected_hours integer not null
                                );"""
    try:
        c = conn.cursor()
        c.execute(create_emp_table)
        c.execute(create_roles_table)
        c.execute
    except Error as e:
        print(e)

conn.close()