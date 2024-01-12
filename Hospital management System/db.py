import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS patient(
            id Integer Primary Key,
            name text,
            age text,
            dob text,
            doctor text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, dob, doctor, gender, contact, address):
        self.cur.execute("insert into patient values (NULL,?,?,?,?,?,?,?)",
                         (name, age, dob, doctor, gender, contact, address))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from patient")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from patient where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, dob, doctor, gender, contact, address):
        self.cur.execute(
            "update patient set name=?, age=?, dob=?, doctor=?, gender=?, contact=?, address=? where id=?",
            [name, age, dob, doctor, gender, contact, address, id])
        self.con.commit()



