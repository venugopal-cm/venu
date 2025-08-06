from tkinter import *
import tkinter.messagebox as messageBox
import pymysql

# Creating the Window
root = Tk()

# Creating a function for inserting the data
def insert():
    id = e_id.get() 
    name = e_name.get() 
    phone_number = e_phone.get()  

    if(id=="" or name=="" or phone_number==""):
        messageBox.showwarning("Insert Status", "All Fields are required to submit")
    else:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="rs_45")
        cursor = con.cursor()
        cursor.execute("INSERT INTO surya(id,name,ph_num) Values (%s,%s,%s)",(id,name,phone_number))
        con.commit()
        cursor.close()
        con.close()

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        messageBox.showinfo("Insert Status", "You Record Inserted Successfully...")

def update():
    id = e_id.get() 
    name = e_name.get()  
    phone_number = e_phone.get() 

    if (id == "" or name == "" or phone_number == ""):
        messageBox.showwarning("Update Status", "All Fields are required to submit")
    else:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="rs_45")
        cursor = con.cursor()
        cursor.execute("UPDATE  surya SET id=%s ,name=%s ,ph_num=%s",(id,name,phone_number))
        con.commit()
        cursor.close()
        con.close()

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        messageBox.showinfo("Update Status", "You Record Inserted Successfully...")

def delete():
    id = e_id.get() 
    if(id == ""):
        messageBox.showwarning("Delete Status", "Enter ID to Delete data")
    else:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="rs_45")
        cursor = con.cursor()
        cursor.execute("DELETE FROM surya Where id=%s",(id))
        con.commit()
        cursor.close()
        con.close()

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        messageBox.showinfo("Deleted Status", "You Record Deleted Successfully...")
def get():
    id = e_id.get()
    if id == "":
        messageBox.showwarning("Search Status", "Enter ID to search")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="rs_45")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM surya WHERE id=%s", (id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()

            if row:
                e_name.delete(0, 'end')
                e_phone.delete(0, 'end')
                e_name.insert(0, row[1])
                e_phone.insert(0, row[2])
                messageBox.showinfo("Search Status", "Record Found!")
            else:
                messageBox.showinfo("Search Status", "No Record Found.")
        except Exception as ex:
            messageBox.showerror("Search Error", str (ex))



def show():
    con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="rs_45")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM surya")
    rows = cursor.fetchall()
    cursor.close()
    con.close()

    list.delete(0, END)
    for row in rows:
        list.insert(END, f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

# Crating Window size and Title
root.title("MySQL & Python CRUD")
root.geometry("700x500")

# Creating the properties
id =Label(root, text="Enter A ID:", font=('bold', 15))
id.place(x= 20, y=45)

name =Label(root, text="Enter A Name:", font=('bold', 15))
name.place(x= 20, y=90)

phone =Label(root, text="Enter A Phone No.:", font=('bold', 15))
phone.place(x= 20, y=135)

# Creating the text boxes
e_name=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
e_name.place(x=180, y= 90)

e_id=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
e_id.place(x=180, y= 45)

e_phone=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
e_phone.place(x=180, y= 135)

# Creating Buttons:
insert_btn = Button(root, text='Insert', font=("italic", 15), bg="orange", bd=5, fg="white", command=insert)
insert_btn.place(x = 20, y= 220)

update_btn = Button(root, text='Update', font=("italic", 15), bg="blue", bd=5, fg="white", command=update)
update_btn.place(x = 120, y= 220)

delete_btn = Button(root, text='Delete', font=("italic", 15), bg="red",bd=5, fg="white", command=delete)
delete_btn.place(x = 220, y= 220)

search_btn = Button(root, text='Search', font=("italic", 15), bg="light green", bd=5, fg="white", command=get)
search_btn.place(x = 320, y= 220)

show_btn = Button(root, text='Show', font=("italic", 15), bg="green", bd=5, fg="white",  command=show)
show_btn.place(x = 420, y= 220)

# List Box:
list = Listbox(root, width=100, height=10)
list.place(x=20, y=300)


mainloop()