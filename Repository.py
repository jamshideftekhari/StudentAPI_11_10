from distutils.log import error
import sqlite3
class Repo():
    def __init__(self):
        try:
            self.conn=sqlite3.connect("student_db.db")
            self.cursor = self.conn.cursor()
            print("data base connection created and connected")
            sqlLiteQuery = "select sqlite_version()"
            self.cursor.execute (sqlLiteQuery)
            record = self.cursor.fetchall()
            print("sqllite data base version is: ", record) 
            
        except sqlite3.Error as error:
            print("connection error: ", error)
    
    def GetAll(self):
        records=self.cursor.execute("select * from People")
        return records 

    def InsertRow(self, fname, lname):
        self.cursor.execute("insert into People (FirstName, LastName) values (?,?)", (fname,lname))
        self.conn.commit()

    def DeleteAll(self):
        self.cursor.execute("delete from People")

    def __del__(self):
        self.cursor.close()
        self.conn.close()