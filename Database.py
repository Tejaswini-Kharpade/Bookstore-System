import sqlite3

def createTable():
    conn=sqlite3.connect("BK.db")
    cur=conn.cursor()
    cur.execute("create table if not exists bookstore(id integer primary key autoincrement,Title text,Author text,Price real,Year integer)")
    conn.commit()
    cur.close()
    conn.close()

createTable()

def insertTable(T,A,P,Y):
    conn=sqlite3.connect("BK.db")
    cur=conn.cursor()
    cur.execute("insert into bookstore values(null,?,?,?,?)",(T,A,P,Y))
    conn.commit()
    cur.close()
    conn.close()
# Ti=input("enter titile")
# Au=input("enter Author")
# Pc=float(input("enter price"))
# Ye=int(input("enter year"))

#insertTable("Think like a monk","Jay shetty",550,2020)


def readTable():
    conn=sqlite3.connect("BK.db")
    cur=conn.cursor()
    cur.execute("select * from bookstore")
    r=cur.fetchall()
    cur.close()
    conn.close()
    return r

#print(readTable())

def searchTable(T='',A='',P=0,Y=0):
    conn=sqlite3.connect("BK.db")
    cur=conn.cursor()
    cur.execute("select * from bookstore where title=? or author=? or price=? or year=?",(T,A,P,Y))
    r = cur.fetchall()
    cur.close()
    conn.close()
    return r
#print(searchTable)

def delTable(i):
    conn = sqlite3.connect("BK.db")
    cur = conn.cursor()
    cur.execute("delete from bookstore where id=?",(i,))
    conn.commit()
    cur.close()
    conn.close()


def updateTable(T,A,P,Y,i):
    conn=sqlite3.connect("BK.db")
    cur=conn.cursor()
    cur.execute("update bookstore set title=?,author=?,price=?,year=? where id=?",(T,A,P,Y,i))
    conn.commit()
    cur.close()
    conn.close()
