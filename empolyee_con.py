from tkinter import *
from tkinter import messagebox
import pymysql

root = Tk()

# ---------- StringVars ----------
EmpID = StringVar()
Name = StringVar()
Phone = StringVar()
Department = StringVar()
Experience = StringVar()
Email = StringVar()
Address = StringVar()
Education = StringVar()

Monthly_Salaries = [StringVar() for _ in range(12)]
Leaves = [StringVar() for _ in range(12)]
PTs = [StringVar() for _ in range(12)]

# ---------- Functions ----------

def insert_employee():
    try:
        emp_id = EmpID.get()
        name = Name.get()
        phone = Phone.get()
        dept = Department.get()
        exp = Experience.get()
        email = Email.get()
        addr = Address.get()
        edu = Education.get()

        con = pymysql.connect(host='localhost', user='root', passwd='password', db='employee_db')
        cur = con.cursor()
        
        cur.execute("INSERT INTO employee_details VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (emp_id, name, phone, email, dept, exp, addr, edu))

        for i, month in enumerate([
            'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']):
            salary = float(Monthly_Salaries[i].get()) if Monthly_Salaries[i].get() else 0
            leave = int(Leaves[i].get()) if Leaves[i].get() else 0
            pt = float(PTs[i].get()) if PTs[i].get() else 0
            cur.execute("INSERT INTO employee_monthly VALUES(%s,%s,%s,%s,%s)",
                        (emp_id, month, salary, leave, pt))

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Employee record inserted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- GUI ----------
root.title("Employee Record System")
root.geometry("1200x900")

Label(root, text="Employee ID").grid(row=0, column=0)
Label(root, text="Name").grid(row=1, column=0)
Label(root, text="Phone").grid(row=2, column=0)
Label(root, text="Email").grid(row=3, column=0)
Label(root, text="Department").grid(row=4, column=0)
Label(root, text="Experience").grid(row=5, column=0)
Label(root, text="Address").grid(row=6, column=0)
Label(root, text="Education").grid(row=7, column=0)

Entry(root, textvariable=EmpID).grid(row=0, column=1)
Entry(root, textvariable=Name).grid(row=1, column=1)
Entry(root, textvariable=Phone).grid(row=2, column=1)
Entry(root, textvariable=Email).grid(row=3, column=1)
Entry(root, textvariable=Department).grid(row=4, column=1)
Entry(root, textvariable=Experience).grid(row=5, column=1)
Entry(root, textvariable=Address).grid(row=6, column=1)
Entry(root, textvariable=Education).grid(row=7, column=1)

Label(root, text="--- Monthly Details ---").grid(row=8, column=0, columnspan=2)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

for i, month in enumerate(months):
    Label(root, text=f"{month} Salary").grid(row=9+i, column=0)
    Entry(root, textvariable=Monthly_Salaries[i]).grid(row=9+i, column=1)
    Label(root, text=f"{month} Leave").grid(row=9+i, column=2)
    Entry(root, textvariable=Leaves[i]).grid(row=9+i, column=3)
    Label(root, text=f"{month} PT").grid(row=9+i, column=4)
    Entry(root, textvariable=PTs[i]).grid(row=9+i, column=5)

Button(root, text="Insert", command=insert_employee).grid(row=21, column=0, columnspan=2)

mainloop()
