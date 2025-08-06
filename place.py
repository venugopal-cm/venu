#1. Creating window
from tkinter import *
root = Tk()
# 7. Creating functions
def Student_Details():
    s_name=name.get()
    Name.set(s_name)
    roll=roll_number.get()
    Roll_number.set(roll)
    phn=phn_number.get()
    Phn_number.set(phn)
    mail=email_id.get()
    Email_id.set(mail)
    _branch=branch.get()
    Branch.set(_branch)
    _section=section.get()
    Section.set(_section)
    address_=address.get()
    Address.set(address_)
    _java=float(java.get())
    Java.set(_java)
    _dot_net=float(dot_Net.get())
    Dot_Net.set(_dot_net)
    _web_dev=float(web_dev.get())
    Web_dev.set(_web_dev)
    _data=float(data_base.get())
    Data_base.set(_data)
    _python=float(python.get())
    Python.set(_python)
    total=_java+_dot_net+_web_dev+_data+_python
    Total_marks.set(total)
    average=total/5
    Average_marks.set(average)
    
    if _java<=35:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)
    elif _java>=90:
        grade="A"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _java>=80 and _java<90:
        grade="B"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _java>=70 and _java<80:
        grade="C"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    else:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)
    if _dot_net<=35:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)
    elif _dot_net>=90:
        grade="A"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _dot_net>=80 and _dot_net<90:
        grade="B"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _dot_net>=70 and _dot_net<80:
        grade="C"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    else:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)
    if _web_dev<=35:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)
    elif _web_dev>=90:
        grade="A"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _web_dev>=80 and _web_dev<90:
        grade="B"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _web_dev>=70 and _web_dev<80:
        grade="C"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    else:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)
    if _data<=35:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)
    elif _data>=90:
        grade="A"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _data>=80 and _data<90:
        grade="B"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _data>=70 and _data<80:
        grade="C"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    else:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status) 
    if _python<=35:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)
    elif _python>=90:
        grade="A"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _python>=80 and _python<90:
        grade="B"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    elif _python>=70 and _python<80:
        grade="C"
        Grade.set(grade)
        status="Pass"
        Status.set(status)
    else:
        grade="Fail"
        Grade.set(grade)
        status="Fail"
        Status.set(status)


    
# 2. Creating window size and Tittle
root.title("Student Records")
root.geometry("900x800")
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

# 3. Creating Window Labels
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

# 4. Creating Text Boxes
name= Entry(root)
name.grid(row=0, column=1)
roll_number= Entry(root)
roll_number.grid(row=1, column=1)
phn_number= Entry(root)
phn_number.grid(row=2, column=1)
email_id= Entry(root)
email_id.grid(row=3, column=1)
branch= Entry(root)
branch.grid(row=4, column=1)
section= Entry(root)
section.grid(row=5, column=1)
address= Entry(root)
address.grid(row=6, column=1)
java= Entry(root)
java.grid(row=7, column=1)
dot_Net= Entry(root)
dot_Net.grid(row=8, column=1)
web_dev= Entry(root)
web_dev.grid(row=9, column=1)
data_base= Entry(root)
data_base.grid(row=10, column=1)
python= Entry(root)
python.grid(row=11, column=1)


# 5. Creating a Button for submitting
Button(root, text="Submit", command=Student_Details).grid(row=12, column=3)
#Button(root,text="Submit", command=Grading).grid(row=12, column=1)
# 6. Result
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

mainloop()