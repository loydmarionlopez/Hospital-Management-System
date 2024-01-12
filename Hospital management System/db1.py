import sqlite3

class Database:
    def __init__(self, db1):
        self.con = sqlite3.connect(db1)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS doctor(
            id Integer Primary Key,
            name text,
            field text,
            dob text,
            gender text,
            age text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()
        
        #Insert data into database
    def insert(self, name, field, dob, gender, age, contact, address):
            self.cur.execute("insert into doctor values (NULL,?,?,?,?,?,?,?)",
                 (name, field, dob, gender, age, contact, address))
            self.con.commit()
        
         # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from doctor")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from doctor where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, dob, field, gender, contact, address):
        self.cur.execute(
            "update doctor set name=?, field=?, dob=?, gender=?, age=?, contact=?, address=? where id=?",
            [name, field, dob, gender, age, contact, address, id])
        self.con.commit()

