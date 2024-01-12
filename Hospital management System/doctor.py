import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from db1 import Database

db = Database("DoctorManagement.db")
root = Tk()
root.title("Doctor MANAGEMENT SYSTEM")
root.geometry("1920x1080+0+0")
root.config(bg="#2b2d4a")
root.state("zoomed")

# Creating the StringVar  variables: Stores the name, age, dob, gender, doctor, and contact you entered in the form.
name = StringVar()
field = StringVar()
dob = StringVar()
gender = StringVar()
age = StringVar()
contact = StringVar()
SEARCH = StringVar()
# Entries Frame
entries_frame = Frame(root, bg="#2b2d4a")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Doctor Management System", font=("Calibri", 18, "bold"), bg="#2b2d4a", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=15, sticky="w")

lbl_txtsearch = Label(entries_frame, text="Search", font=('Calibri', 15),bg="#2b2d4a", fg="white")
lbl_txtsearch.grid(row=0, column=2, padx=10, pady=10, sticky="w")
search = Entry(entries_frame, textvariable=SEARCH, font=("Calibri", 16), width=30)
search.grid(row=0, column=3, padx=10, pady=10, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#2b2d4a", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblField = Label(entries_frame, text="Field", font=("Calibri", 16), bg="#2b2d4a", fg="white")
lblField.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtField = Entry(entries_frame, textvariable=field, font=("Calibri", 16), width=30)
txtField.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lbldob = Label(entries_frame, text="D.O.B", font=("Calibri", 16), bg="#2b2d4a", fg="white")
lbldob.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtdob = Entry(entries_frame, textvariable=dob, font=("Calibri", 16), width=30)
txtdob.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#2b2d4a", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#2b2d4a", fg="white")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")


lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#2b2d4a", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#2b2d4a", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtAddress = Text(entries_frame, width=65, height=5, font=("Calibri", 16))
txtAddress.grid(row=4, column=1, columnspan=1, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    field.set(row[2])
    dob.set(row[3])
    gender.set(row[4])
    age.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_doctor():
    if txtName.get() == txtField.get() == "" or "" or txtdob.get() == "" or comboGender.get() == "" or txtAge.get() == "" or  txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(), txtField.get() , txtdob.get() , comboGender.get(), txtAge.get(), txtContact.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayAll()



def update_doctor():
    if txtName.get() == "" or txtAge.get() == "" or txtdob.get() == "" or txtField.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    db.update(row[0], txtName.get(), txtAge.get(), txtdob.get(), txtField.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    displayAll()


def delete_doctor():
    answer = askyesno (title='Confirmation',
                       message='Are you sure that you want to delete?')
    if answer:
     db.remove(row[0])
     clearAll()
     displayAll()


def clearAll():
    name.set("")
    field.set("")
    dob.set("")
    gender.set("")
    age.set("")
    contact.set("")
    SEARCH.set("")
    txtAddress.delete(1.0, END)

#function to search data
def SearchRecord():
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tv.delete(*tv.get_children())
        #open database
        conn = sqlite3.connect('DoctorManagement.db')
        #select query with where clause
        cursor=conn.execute("SELECT * FROM doctor WHERE name LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tv.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        clearAll()

def VIEW():
    displayAll()


btn_frame = Frame(entries_frame, bg="#2b2d4a")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_doctor, text="Add Details", width=15,font=("Calibri", 16, "bold"), fg="steelblue",
                bg="WHITE", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_doctor, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="steelblue", bg="WHITE",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_doctor, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="steelblue", bg="WHITE",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="steelblue",
                  bg="WHITE",
                  bd=0).grid(row=0, column=3, padx=10)
btn_search = Button(btn_frame, command=SearchRecord, text="Search", width=15, font=("Calibri", 16, "bold"), fg="steelblue",
                  bg="WHITE",
                  bd=0).grid(row=0, column=4, padx=10)
btn_display = Button (btn_frame, command=VIEW, text="View all", width=15, font=("Calibri", 16, "bold"), fg="steelblue",
                  bg="WHITE",
                  bd=0).grid(row=0, column=5, padx=10)

# Table Frame
tree_frame = Frame(root, bg="BLACK")
tree_frame.place(x=0, y=415, width=1367, height=400)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('VERDANA', 10),  background="silver",
                rowheight=85)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('VERDANA', 11))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=4)
tv.heading("2", text="Name")
tv.heading("3", text="Field")
tv.column("3", width=15)
tv.heading("4", text="D.O.B")
tv.column("4", width=20)
tv.heading("5", text="Gender")
tv.column("5", width=15)
tv.heading("6", text="Age")
tv.column("6", width=15)
tv.heading("7", text="Contact")
tv.column("7", width=15)
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)


displayAll()
root.mainloop()