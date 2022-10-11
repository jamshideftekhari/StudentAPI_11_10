import sqlite3

create_table = " CREATE TABLE People( FirstName TEXT, LastName  TEXT );"

#Connection and Cursor object 
with sqlite3.connect("student_db.db") as connection:
    cursor = connection.cursor()
    cursor.execute(create_table)
    cursor.execute("INSERT INTO People VALUES('Jamshid', 'Eftekhari');")
    people = cursor.execute("SELECT * FROM People").fetchall() 

for p in people:
    print(p)