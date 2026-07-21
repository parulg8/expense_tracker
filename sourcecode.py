import mysql.connector 
#database setup 
try: 
con=mysql.connector.connect(host='localhost', 
user='root', password='Parul@2008', 
database='expenses') 
except mysql.connector.Error as err: 
print(f"Error: {err}") 
exit() 
cur=con.cursor() 
#dropping table if it exists already 
q1='drop table if exists expenses' 
cur.execute(q1) 
#creating table 
q2 = 'CREATE TABLE expenses (id INT PRIMARY KEY 
AUTO_INCREMENT, description VARCHAR(50) NOT 
NULL, amount FLOAT NOT NULL, date DATE NOT 
NULL, category VARCHAR(50) NOT NULL)' 
cur.execute(q2) 
con.commit() 
#functions to manage expenses 
from datetime import datetime 
def validate_date(date): 
"""Validate date format as YYYY-MM-DD.""" 
try: 
datetime.strptime(date, '%Y-%m-%d') 
return True 
except ValueError: 
return False 
def add_expense(): 
description=input("Enter the description of the 
expense:") 
try: 
amount=float(input("Enter the amount:")) 
except ValueError: 
print("Invalid amount. Please enter a numeric 
value.") 
return 
date=input("Enter the date (YYYY-MM-DD):") 
if not validate_date(date): 
print("Invalid date format. Please use YYYY
MM-DD.") 
return 
category=input("Enter the category(e.g., Food, 
Travel, Shopping):") 
if description and category: 
q3='insert into expenses (description, 
amount, date, category) values (%s,%s,%s,%s)' 
        cur.execute(q3, (description, amount, date, 
category)) 
        con.commit() 
        print("Expense added successfully!") 
    else: 
        print("All fields are required!") 
 
def view_expenses(): 
    q4 = 'select * from expenses' 
    cur.execute(q4) 
    rows = cur.fetchall() 
    if not rows: 
        print("No expenses found!") 
        return 
    print("\nExpenses:") 
    print(f"{'ID':<5} {'Description':<20} 
{'Amount':<10} {'Date':<15} {'Category':<15}") 
    print("-" * 70) 
    for row in rows: 
formatted_date = row[3].strftime('%d-%m
%Y') 
if isinstance: 
(row[3], datetime.date) 
else: 
row[3] 
print(f"{row[0]:<5} {row[1]:<20} 
₹{row[2]:<10.2f} {formatted_date:<15} 
{row[4]:<15}") 
print("-" * 70) 
def delete_expense(): 
try: 
expense_id=int(input("Enter the ID of the 
expense to delete:")) 
except ValueError: 
print("Invalid ID. Please enter a numeric 
value.") 
return 
q5='delete from expenses where id = %s' 
cur.execute(q5, (expense_id,)) 
con.commit() 
if cur.rowcount > 0: 
print("Expense deleted successfully!") 
else: 
print("Expense not found.") 
def find_max_expense(): 
q6='select description, amount, date, category 
from expenses order by amount desc limit 1' 
cur.execute(q6) 
result=cur.fetchone() 
if result: 
print(f"Maximum Expense: {result[0]}, 
₹{result[1]:.2f}, Date: {result[2]}, Category: 
{result[3]}") 
else: 
print("No expenses found!") 
def find_min_expense(): 
q7='select description, amount, date, category 
from expenses order by amount asc limit 1' 
cur.execute(q7) 
result=cur.fetchone() 
if result: 
print(f"Minimum Expense: {result[0]}, 
₹{result[1]:.2f}, Date: {result[2]}, Category: 
{result[3]}") 
else: 
print("No expenses found!") 
def view_by_month(): 
month=input("Enter the month(MM):") 
q8='select * from expenses where 
MONTH(date) = %s' 
cur.execute(q8, (month,)) 
rows=cur.fetchall() 
    if rows: 
        print(f"\nExpenses for Month {month}:") 
        print(f"{'ID':<5} {'Description':<20} 
{'Amount':<10} {'Date':<15} {'Category':<15}") 
        print("-"*70) 
        for row in rows: 
            formatted_date = row[3].strftime('%d-%m
%Y') 
            if isinstance: 
                (row[3], datetime.date) 
            else: 
                row[3] 
            print(f"{row[0]:<5} {row[1]:<20} 
₹{row[2]:<10.2f} {formatted_date:<15} 
{row[4]:<15}") 
        print("-"*70) 
    else: 
        print(f"No expenses found for Month 
{month}.") 
 
#Menu-based interaction 
def menu(): 
    while True: 
        print("\n--- Expense Tracker Menu ---") 
        print("1. Add an Expense") 
        print("2. View all Expenses") 
        print("3. Delete an Expense") 
        print("4. Find Maximum Expense") 
        print("5. Find Minimum Expense") 
        print("6. View Expenses by Month") 
        print("7. Exit") 
        choice=int(input("Enter your choice:")) 
 
        if choice==1: 
            add_expense() 
        elif choice==2: 
            view_expenses() 
        elif choice==3: 
            delete_expense() 
elif choice==4: 
find_max_expense() 
elif choice==5: 
find_min_expense() 
elif choice==6: 
view_by_month() 
elif choice==7: 
print("Exiting... Goodbye!") 
break 
else: 
print("Invalid choice. Please try again.") 
#Run the program 
menu() 
#Close the database connection when done 
con.close()
