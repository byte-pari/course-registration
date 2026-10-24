import sqlite3
class database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY,
        fname TEXT,lname TEXT , course TEXT , password INTEGER)
        """)
        self.con.commit()
    def insert(self,fname,lname,course,password):
        self.cur.execute("""INSERT INTO contact VALUES(NULL,?,?,?,?)""",(fname,lname,course,password))
        self.con.commit()
    def delete(self,id):
        sql_delete =self.cur.execute('DELETE FROM contact WHERE id = ?',(id,))
        self.con.commit()
    def select_record(self):
            self.cur.execute('select * from contact')
            return self.cur.fetchall()
    def find(self,password):
            self.cur.execute('SELECT * FROM contact WHERE password = ?' ,(password,))
            return self.cur.fetchall()
