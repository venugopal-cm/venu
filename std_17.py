from tkinter import *
from tkinter import messagebox
import pymysql

root = Tk()

# ---------- StringVars for form fields ----------
Name = StringVar()
Roll_number = StringVar()
Phn_number = StringVar()
Email_id = StringVar()
Branch = StringVar()
Section = StringVar()
Address = StringVar()
Java = StringVar()
Dot_Net = StringVar()
Web_dev = StringVar()
Data_base = StringVar()
Python = StringVar()
Total_marks = StringVar()
Average_marks = StringVar()
Grade = StringVar()
Status = StringVar()

# ---------- Functions ----------

def Student_Details():
    try:
        s_name = name.get()
        roll = roll_number.get()
        phn = phn_number.get()
        mail = email_id.get()
        _branch = branch.get()
        _section = section.get()
        address_ = address.get()
        _java = float(java.get())
        _dot_net = float(dot_net.get())
        _web_dev = float(web_dev.get())
        _data = float(data_base.get())
        _python = float(python.get())
        total = _java + _dot_net + _web_dev + _data + _python
        average = total / 5

        # Grade and status based on average
        if average < 35:
            grade = "Fail"
            status = "Fail"
        elif average >= 90:
            grade = "A"
            status = "Pass"
        elif average >= 80:
            grade = "B"
            status = "Pass"
        elif average >= 70:
            grade = "C"
            status = "Pass"
        else:
            grade = "Fail"
            status = "Fail"

        # Set StringVars for display
        Name.set(s_name)
        Roll_number.set(roll)
        Phn_number.set(phn)
        Email_id.set(mail)
        Branch.set(_branch)
        Section.set(_section)
        Address.set(address_)
        Java.set(str(_java))
        Dot_Net.set(str(_dot_net))
        Web_dev.set(str(_web_dev))
        Data_base.set(str(_data))
        Python.set(str(_python))
        Total_marks.set(str(total))
        Average_marks.set(str(average))
        Grade.set(grade)
        Status.set(status)

        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
        cursor = con.cursor()
        cursor.execute("INSERT INTO std_details(student_roll_number,student_name,student_phone_number,student_email_id,student_branch,student_section,student_address) VALUES(%s,%s,%s,%s,%s,%s,%s)", (roll, s_name, phn, mail, _branch, _section, address_))
        cursor.execute("INSERT INTO student_marks(student_roll_number,student_java_marks,student_Dot_net_marks,student_web_dev_marks,student_data_base_marks,student_python_marks) VALUES(%s,%s,%s,%s,%s,%s)", (roll, _java, _dot_net, _web_dev, _data, _python))
        cursor.execute("INSERT INTO student_grade(student_roll_number,total_marks,average,grade,pass_or_fail) VALUES(%s,%s,%s,%s,%s)", (roll, total, average, grade, status))
        con.commit()
        cursor.close()
        con.close()
        messagebox.showinfo("Success", "Record inserted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update():
    try:
        s_name = name.get()
        roll = roll_number.get()
        phn = phn_number.get()
        mail = email_id.get()
        _branch = branch.get()
        _section = section.get()
        address_ = address.get()
        _java = float(java.get())
        _dot_net = float(dot_net.get())
        _web_dev = float(web_dev.get())
        _data = float(data_base.get())
        _python = float(python.get())
        total = _java + _dot_net + _web_dev + _data + _python
        average = total / 5

        if average < 35:
            grade = "Fail"
            status = "Fail"
        elif average >= 90:
            grade = "A"
            status = "Pass"
        elif average >= 80:
            grade = "B"
            status = "Pass"
        elif average >= 70:
            grade = "C"
            status = "Pass"
        else:
            grade = "Fail"
            status = "Fail"

        con = pymysql.connect(host="localhost", user="root", passwd="Venu@1709", db="std_17")
        cur = con.cursor()
        # Update details
        cur.execute("UPDATE std_details SET student_name=%s, student_phone_number=%s, student_email_id=%s, student_branch=%s, student_section=%s, student_address=%s WHERE student_roll_number=%s", (s_name, phn, mail, _branch, _section, address_, roll))
        # Update marks
        cur.execute("UPDATE student_marks SET student_java_marks=%s, student_Dot_net_marks=%s, student_web_dev_marks=%s, student_data_base_marks=%s, student_python_marks=%s WHERE student_roll_number=%s", (_java, _dot_net, _web_dev, _data, _python, roll))
        # Update grade
        cur.execute("UPDATE student_grade SET total_marks=%s, average=%s, grade=%s, pass_or_fail=%s WHERE student_roll_number=%s", (total, average, grade, status, roll))
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("Success", "Record updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get():
    roll = roll_number.get()
    if not roll:
        messagebox.showwarning("Input Error", "Please enter a Roll Number to search.")
        return
    try:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
        cur = con.cursor()
        cur.execute("""
            SELECT d.student_name, d.student_roll_number, d.student_phone_number, d.student_email_id, d.student_branch, d.student_section, d.student_address,
                   m.student_java_marks, m.student_Dot_net_marks, m.student_web_dev_marks, m.student_data_base_marks, m.student_python_marks,
                   g.total_marks, g.average, g.grade, g.pass_or_fail
            FROM std_details d
            LEFT JOIN student_marks m ON d.student_roll_number = m.student_roll_number
            LEFT JOIN student_grade g ON d.student_roll_number = g.student_roll_number
            WHERE d.student_roll_number=%s
        """, (roll,))
        row = cur.fetchone()
        con.close()
        if row:
            Name.set(row[0])
            Roll_number.set(row[1])
            Phn_number.set(row[2])
            Email_id.set(row[3])
            Branch.set(row[4])
            Section.set(row[5])
            Address.set(row[6])
            Java.set(str(row[7]))
            Dot_Net.set(str(row[8]))
            Web_dev.set(str(row[9]))
            Data_base.set(str(row[10]))
            Python.set(str(row[11]))
            Total_marks.set(str(row[12]))
            Average_marks.set(str(row[13]))
            Grade.set(row[14])
            Status.set(row[15])
            messagebox.showinfo("Search Status", "Record Found!")
        else:
            messagebox.showinfo("Search Status", "No Record Found.")
    except Exception as ex:
        messagebox.showerror("Error", str(ex))

def delete():
    roll = roll_number.get()
    if not roll:
        messagebox.showwarning("Input Error", "Please enter a Roll Number to delete.")
        return
    try:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
        cur = con.cursor()
        cur.execute("DELETE FROM student_grade WHERE student_roll_number=%s", (roll,))
        cur.execute("DELETE FROM student_marks WHERE student_roll_number=%s", (roll,))
        cur.execute("DELETE FROM std_details WHERE student_roll_number=%s", (roll,))
        con.commit()
        con.close()
        Name.set("")
        Roll_number.set("")
        Phn_number.set("")
        Email_id.set("")
        Branch.set("")
        Section.set("")
        Address.set("")
        Java.set("")
        Dot_Net.set("")
        Web_dev.set("")
        Data_base.set("")
        Python.set("")
        Total_marks.set("")
        Average_marks.set("")
        Grade.set("")
        Status.set("")
        messagebox.showinfo("Deleted", f"Record for Roll No {roll} deleted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show():
    try:
        con = pymysql.connect(host='localhost', user='root', passwd="Venu@1709", db="std_17")
        cur = con.cursor()
        cur.execute("""
            SELECT d.student_roll_number, d.student_name, d.student_phone_number, d.student_branch, g.total_marks, g.grade, g.pass_or_fail
            FROM std_details d
            LEFT JOIN student_grade g ON d.student_roll_number = g.student_roll_number
            ORDER BY d.student_roll_number
        """)
        rows = cur.fetchall()
        con.close()
        listbox.delete(0, END)
        for row in rows:
            listbox.insert(END, f"Roll: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Branch: {row[3]}, Total: {row[4]}, Grade: {row[5]}, Status: {row[6]}")
        if not rows:
            listbox.insert(END, "No records found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- GUI Layout ----------

root.title("Student Records")
root.geometry("1100x900")

Label(root, text="Enter Student Name:").grid(row=0, column=0)
Label(root, text="Enter Student Roll Number:").grid(row=1, column=0)
Label(root, text="Enter Student Phone Number:").grid(row=2, column=0)
Label(root, text="Enter Student Email ID:").grid(row=3, column=0)
Label(root, text="Enter Student Branch:").grid(row=4, column=0)
Label(root, text="Enter Student Section:").grid(row=5, column=0)
Label(root, text="Enter Student Address:").grid(row=6, column=0)
Label(root, text="Enter Student Java Marks:").grid(row=7, column=0)
Label(root, text="Enter Student Dot Net Marks:").grid(row=8, column=0)
Label(root, text="Enter Student Web Development Marks:").grid(row=9, column=0)
Label(root, text="Enter Student Database Marks:").grid(row=10, column=0)
Label(root, text="Enter Student Python Marks:").grid(row=11, column=0)

name = Entry(root)
name.grid(row=0, column=1)
roll_number = Entry(root)
roll_number.grid(row=1, column=1)
phn_number = Entry(root)
phn_number.grid(row=2, column=1)
email_id = Entry(root)
email_id.grid(row=3, column=1)
branch = Entry(root)
branch.grid(row=4, column=1)
section = Entry(root)
section.grid(row=5, column=1)
address = Entry(root)
address.grid(row=6, column=1)
java = Entry(root)
java.grid(row=7, column=1)
dot_net = Entry(root)
dot_net.grid(row=8, column=1)
web_dev = Entry(root)
web_dev.grid(row=9, column=1)
data_base = Entry(root)
data_base.grid(row=10, column=1)
python = Entry(root)
python.grid(row=11, column=1)

Button(root, text="Insert", command=Student_Details).grid(row=12, column=0)
Button(root, text="Update", command=update).grid(row=12, column=1)
Button(root, text="Search", command=get).grid(row=12, column=2)
Button(root, text="Delete", command=delete).grid(row=12, column=3)
Button(root, text="Show All", command=show).grid(row=12, column=4)

Label(root, text="-------------Student Details----------- :").grid(row=13, column=0)
Label(root, text="Student Name :").grid(row=14, column=0)
Label(root, text="", textvariable=Name).grid(row=14, column=1)
Label(root, text="Student Roll Number:").grid(row=14, column=2)
Label(root, text="", textvariable=Roll_number).grid(row=14, column=3)
Label(root, text="Student Phone Number:").grid(row=14, column=4)
Label(root, text="", textvariable=Phn_number).grid(row=14, column=5)
Label(root, text="Student Email:").grid(row=15, column=0)
Label(root, text="", textvariable=Email_id).grid(row=15, column=1)
Label(root, text="Student Branch:").grid(row=15, column=2)
Label(root, text="", textvariable=Branch).grid(row=15, column=3)
Label(root, text="Student Section :").grid(row=15, column=4)
Label(root, text="", textvariable=Section).grid(row=15, column=5)
Label(root, text="Student Address:").grid(row=16, column=0)
Label(root, text="", textvariable=Address).grid(row=16, column=1)
Label(root, text="-------------Student Marks Details------------:").grid(row=17, column=0)
Label(root, text="Student Java Marks:").grid(row=18, column=0)
Label(root, text="", textvariable=Java).grid(row=18, column=1)
Label(root, text="Student Dot Net Marks:").grid(row=18, column=2)
Label(root, text="", textvariable=Dot_Net).grid(row=18, column=3)
Label(root, text="Student Web Development Marks :").grid(row=18, column=4)
Label(root, text="", textvariable=Web_dev).grid(row=18, column=5)
Label(root, text="Student Database Marks:").grid(row=19, column=0)
Label(root, text="", textvariable=Data_base).grid(row=19, column=1)
Label(root, text="Student Python Marks:").grid(row=19, column=2)
Label(root, text="", textvariable=Python).grid(row=19, column=3)
Label(root, text="--------Student Total Marks and Average--------:").grid(row=20, column=0)
Label(root, text="Student Total Marks:").grid(row=21, column=0)
Label(root, text="", textvariable=Total_marks).grid(row=21, column=1)
Label(root, text="Student Average Marks:").grid(row=21, column=2)
Label(root, text="", textvariable=Average_marks).grid(row=21, column=3)
Label(root, text="Student Grade:").grid(row=22, column=0)
Label(root, text="", textvariable=Grade).grid(row=22, column=1)
Label(root, text="Student Status:").grid(row=22, column=2)
Label(root, text="", textvariable=Status).grid(row=22, column=3)

# Listbox for showing all records
listbox = Listbox(root, width=120)
listbox.grid(row=23, column=0, columnspan=6)

mainloop()
