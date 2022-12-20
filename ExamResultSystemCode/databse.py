
import sqlite3

con = sqlite3.connect("Student_Databases.db")
cur = con.cursor()


def PrimaryData():
    cur.execute("CREATE TABLE IF NOT EXISTS primary_student( StuID INTEGER PRIMARY KEY, StuName TEXT,\
                 Subject1 INTEGER, \
                 Subject2 INTEGER, \
                 Subject3 INTEGER, \
                 Subject4 INTEGER, \
                 Subject5 INTEGER, \
                 Subject6 INTEGER, \
                 Total INTEGER, Average INTEGER)")
    con.commit()





def OrdinaryData():
    cur.execute("CREATE TABLE IF NOT EXISTS ordinary_student( StuID INTEGER PRIMARY KEY, StuName TEXT,\
                 Subject1 INTEGER, \
                 Subject2 INTEGER, \
                 Subject3 INTEGER, \
                 Subject4 INTEGER, \
                 Subject5 INTEGER, \
                 Subject6 INTEGER, \
                 Subject7 INTEGER, \
                 Subject8 INTEGER, \
                 Subject9 INTEGER, \
                 Total INTEGER, Average INTEGER)")
    con.commit()


def AdvancedData():
    cur.execute("CREATE TABLE IF NOT EXISTS advanced_student( StuID INTEGER PRIMARY KEY, StuName TEXT,\
                 SubjectStream TEXT, \
                 Subject1 INTEGER, \
                 Subject2 INTEGER, \
                 Subject3 INTEGER, \
                 Total INTEGER, Average INTEGER)")
    con.commit()


def InsertPrimaryData(StuID, StuName, Subject1, Subject2, Subject3, Subject4, Subject5, Subject6, StuTot, StuAver):

    cur.execute("INSERT INTO primary_student VALUES (?,?,?,?,?,?,?,?,?,?)",\
                (StuID, StuName, Subject1, Subject2, Subject3, Subject4, Subject5, Subject6, StuTot, StuAver))
    con.commit()




def InsertOrdinaryData(StuID, StuName, Subject1, Subject2, Subject3, Subject4, Subject5, Subject6, Subject7, Subject8, Subject9, StuTot, StuAver):

    cur.execute("INSERT INTO ordinary_student VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",\
                (StuID, StuName, Subject1, Subject2, Subject3, Subject4, Subject5, Subject6, Subject7, Subject8, Subject9, StuTot, StuAver))
    con.commit()


def InsertAdvancedData(StuID, StuName, SubjectStream, Subject1, Subject2, Subject3, StuTot, StuAver):

    cur.execute("INSERT INTO advanced_student VALUES (?,?,?,?,?,?,?,?)",\
                (StuID, StuName, SubjectStream, Subject1, Subject2, Subject3, StuTot, StuAver))
    con.commit()



PrimaryData()
OrdinaryData()
AdvancedData()
