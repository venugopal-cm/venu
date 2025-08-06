from tkinter import *
import tkinter.messagebox as messageBox
import pymysql

# Creating the Window
root = Tk()

# Creating a function for inserting the data
def insert():
    roll_number = roll_number.get()
    name = name.get()
    phone_number = phone_number.get()
    email_id = email_id.get()
    branch = branch.get()
    section = section.get()
    address = address.get()


    if(roll_number=="" or name=="" or phone_number=="" or email_id=="" or branch=="" or section=="" or address==""):
        messageBox.showwarning("Insert Status", "All Fields are required to submit")
    else:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
        cursor = con.cursor()
        cursor.execute("INSERT INTO student_details(roll_number,name,ph_number,email_id,branch,section,address) Values (%s,%s,%s,%s,%s,%s)",(roll_number,name,phone_number,email_id,branch,section,address))
        con.commit()
        cursor.close()
        con.close()

        roll_number.delete(0, 'end')
        name.delete(0, 'end')
        phone_number.delete(0, 'end')
        email_id.delete(0, 'end')
        branch.delete(0, 'end')
        section.delete(0,'end')
        address.delete(0, 'end')


        messageBox.showinfo("Insert Status", "You Record Inserted Successfully...")


def update():
    roll_number = roll_number.get() 
    name = name.get()  
    phone_number = phone_number.get()
    email_id = email_id.get()
    branch = branch.get()
    section = section.get()
    address = address.get() 

    if(roll_number == "" or name == "" or phone_number == "" or email_id=="" or branch=="" or section=="" or address==""):
        messageBox.showwarning("Update Status", "All Fields are required to submit")
    else:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
        cursor = con.cursor()
        cursor.execute("UPDATE  student_details SET id=%s ,name=%s ,ph_num=%s",(roll_number,name,phone_number,email_id,branch,section,address))
        con.commit()
        cursor.close()
        con.close()

        name.delete(0, 'end')
        phone_number.delete(0, 'end')
        email_id.delete(0, 'end')
        branch.delete(0, 'end')
        section.delete(0,'end')
        address.delete(0, 'end')

        messageBox.showinfo("Update Status", "You Record Inserted Successfully...")

def delete():
    id = roll_number.get() 
    if(id == ""):
        messageBox.showwarning("Delete Status", "Enter ID to Delete data")
    else:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
        cursor = con.cursor()
        cursor.execute("DELETE FROM student_details Where id=%s",(roll_number))
        con.commit()
        cursor.close()
        con.close()

        name.delete(0, 'end')
        phone_number.delete(0, 'end')
        email_id.delete(0, 'end')
        branch.delete(0, 'end')
        section.delete(0,'end')
        address.delete(0, 'end')

        messageBox.showinfo("Deleted Status", "You Record Deleted Successfully...")
def get():
    id = roll_number.get()
    if id == "":
        messageBox.showwarning("Search Status", "Enter ID to search")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM student_details WHERE id=%s", (roll_number,))
            row = cursor.fetchone()
            cursor.close()
            con.close()

            if row:
                name.delete(0, 'end')
                phone_number.delete(0, 'end')
                email_id.delete(0, 'end')
                branch.delete(0, 'end')
                section.delete(0,'end')
                address.delete(0, 'end')
                messageBox.showinfo("Search Status", "Record Found!")
            else:
                messageBox.showinfo("Search Status", "No Record Found.")
        except Exception as ex:
            messageBox.showerror("Search Error", str (ex))



def show():
    con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM student_details")
    rows = cursor.fetchall()
    cursor.close()
    con.close()

    list.delete(0, END)
    for row in rows:
        list.insert(END, f"ROLL_NUMBER: {row[0]}, Name: {row[1]}, Phone: {row[2]}")        


# Creting Window size and Title
root.title("MySQL & Python CRUD")
root.geometry("900x800")

#result
roll_number=Label(root, text="Enter A ROLL_NUMBER:", font=('bold', 15))
roll_number.place(x= 20, y=45)

name =Label(root, text="Enter A NAME:", font=('bold', 15))
name.place(x= 20, y=90)

phone_number=Label(root, text="Enter A PHONE_NUMBER:", font=('bold', 15))
phone_number.place(x= 20, y=135)

email_id=Label(root, text="Enter A EMAIL_ID:", font=('bold', 15))
email_id.place(x= 20, y=180)

branch=Label(root, text="Enter A BRANCH:", font=('bold', 15))
branch.place(x= 20, y=225)

section=Label(root, text="Enter A SECTION:", font=('bold', 15))
section.place(x= 20, y=270)

address=Label(root, text="Enter A ADDRESS:", font=('bold', 15))
address.place(x= 20, y=315)


# Creating the text boxes
roll_number=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
roll_number.place(x=280, y= 45)

name=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
name.place(x=280, y= 90)

phone_number=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
phone_number.place(x=280, y= 135)

email_id=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
email_id.place(x=280, y= 180)

branch=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
branch.place(x=280, y= 225)

section=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
section.place(x=280, y= 270)

address=Entry(root,text="",font=('bold', 15), bd=5, bg="pink")
address.place(x=280, y= 315)


# Creating Buttons:
insert_btn = Button(root, text='Insert', font=("italic", 15), bg="orange", bd=5, fg="white", command=insert)
insert_btn.place(x = 300, y= 350)

update_btn = Button(root, text='Update', font=("italic", 15), bg="blue", bd=5, fg="white", command=update)
update_btn.place(x = 400, y= 350)

delete_btn = Button(root, text='Delete', font=("italic", 15), bg="red",bd=5, fg="white", command=delete)
delete_btn.place(x = 500, y= 350)

search_btn = Button(root, text='Search', font=("italic", 15), bg="light green", bd=5, fg="white", command=get)
search_btn.place(x = 600, y= 350)

show_btn = Button(root, text='Show', font=("italic", 15), bg="green", bd=5, fg="white",  command=show)
show_btn.place(x = 700, y= 350)



mainloop()