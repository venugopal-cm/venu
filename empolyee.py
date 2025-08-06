from tkinter import *

root = Tk()
root.title("Employee Record Management")
root.geometry("1400x800")

# Employee Details
Label(root, text="Enter Your Employee Full Name:").place(x=30, y=40)
name_entry = Entry(root, width=25)
name_entry.place(x=260, y=40)
Label(root, text="Enter Your Employee Ph.Number:").place(x=30, y=80)
phone_entry = Entry(root, width=25)
phone_entry.place(x=260, y=80)
Label(root, text="Enter Your Employee Department:").place(x=30, y=120)
dept_entry = Entry(root, width=25)
dept_entry.place(x=260, y=120)
Label(root, text="Enter Your Employee Experience:").place(x=30, y=160)
exp_entry = Entry(root, width=25)
exp_entry.place(x=260, y=160)

Label(root, text="Enter Your Employee ID:").place(x=650, y=40)
id_entry = Entry(root, width=25)
id_entry.place(x=900, y=40)
Label(root, text="Enter Your Employee Email:").place(x=650, y=80)
email_entry = Entry(root, width=25)
email_entry.place(x=900, y=80)
Label(root, text="Enter Your Employee Address:").place(x=650, y=120)
addr_entry = Entry(root, width=25)
addr_entry.place(x=900, y=120)
Label(root, text="Enter Your Employee Education:").place(x=650, y=160)
edu_entry = Entry(root, width=25)
edu_entry.place(x=900, y=160)

# Monthly Data
months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
salary_entries = []
leave_entries = []
pt_entries = []
paid_labels = []
month_labels = []

for i, month in enumerate(months):
    y = 220 + i*35
    Label(root, text=f"Enter {month} Salary Amount:").place(x=30, y=y)
    sal_e = Entry(root, width=12)
    sal_e.place(x=200, y=y)
    salary_entries.append(sal_e)
    Label(root, text=f"Enter {month} Leaves Amount:").place(x=330, y=y)
    leave_e = Entry(root, width=5)
    leave_e.place(x=490, y=y)
    leave_entries.append(leave_e)
    Label(root, text=f"Enter {month} PT Amount:").place(x=600, y=y)
    pt_e = Entry(root, width=8)
    pt_e.place(x=750, y=y)
    pt_entries.append(pt_e)
    # Month label
    ml = Label(root, text=f"Paid {month} Salary:", fg="black", width=18, anchor="w")
    ml.place(x=900, y=y)
    month_labels.append(ml)
    # Paid salary value
    paid_l = Label(root, text="0.00", fg="red", width=10, anchor="e", relief="ridge")
    paid_l.place(x=1050, y=y)
    paid_labels.append(paid_l)

# Summary/Result Labels at Bottom

# First Row (Employee info)
Label(root, text="Employee Full Name:", width=20, anchor="w").place(x=30, y=670)
lbl_name = Label(root, text="", fg="red", width=20, anchor="w")
lbl_name.place(x=180, y=670)
Label(root, text="Employee ID:", width=20, anchor="w").place(x=400, y=670)
lbl_id = Label(root, text="", fg="red", width=20, anchor="w")
lbl_id.place(x=520, y=670)
Label(root, text="Employee Phone Number:", width=20, anchor="w").place(x=700, y=670)
lbl_phone = Label(root, text="", fg="red", width=20, anchor="w")
lbl_phone.place(x=900, y=670)
Label(root, text="Employee Email:", width=20, anchor="w").place(x=1100, y=670)
lbl_email = Label(root, text="", fg="red", width=20, anchor="w")
lbl_email.place(x=1230, y=670)

# Second Row (Employee info)
Label(root, text="Employee Department:", width=20, anchor="w").place(x=30, y=700)
lbl_dept = Label(root, text="", fg="red", width=20, anchor="w")
lbl_dept.place(x=180, y=700)
Label(root, text="Employee Experience:", width=20, anchor="w").place(x=400, y=700)
lbl_exp = Label(root, text="", fg="red", width=20, anchor="w")
lbl_exp.place(x=550, y=700)  # Changed x to 550 for better fit
Label(root, text="Employee Education:", width=20, anchor="w").place(x=700, y=700)
lbl_edu = Label(root, text="", fg="red", width=20, anchor="w")
lbl_edu.place(x=900, y=700)
Label(root, text="Employee Address:", width=20, anchor="w").place(x=1100, y=700)
lbl_addr = Label(root, text="", fg="red", width=20, anchor="w")
lbl_addr.place(x=1230, y=700)

# Third Row (Financial info)
Label(root, text="Total Financial Year Amount:", width=25, anchor="w").place(x=30, y=730)
lbl_total_salary = Label(root, text="", fg="red", width=20, anchor="w")
lbl_total_salary.place(x=230, y=730)
Label(root, text="Total Number Of Leaves:", width=25, anchor="w").place(x=400, y=730)
lbl_total_leaves = Label(root, text="", fg="red", width=20, anchor="w")
lbl_total_leaves.place(x=600, y=730)
Label(root, text="Total PT Amount Debited:", width=25, anchor="w").place(x=700, y=730)
lbl_total_pt = Label(root, text="", fg="red", width=20, anchor="w")
lbl_total_pt.place(x=900, y=730)
Label(root, text="Total Paid Salary:", width=25, anchor="w").place(x=1100, y=730)
lbl_total_paid = Label(root, text="", fg="red", width=20, anchor="w")
lbl_total_paid.place(x=1230, y=730)

def calculate():
    # Employee Details
    lbl_name.config(text=name_entry.get())
    lbl_id.config(text=id_entry.get())
    lbl_phone.config(text=phone_entry.get())
    lbl_email.config(text=email_entry.get())
    lbl_dept.config(text=dept_entry.get())
    lbl_exp.config(text=exp_entry.get())
    lbl_addr.config(text=addr_entry.get())
    lbl_edu.config(text=edu_entry.get())

    # Monthly Calculations
    total_salary = 0
    total_pt = 0
    total_leaves = 0
    total_paid = 0

    for i in range(12):
        try:
            sal = float(salary_entries[i].get())
        except:
            sal = 0
        try:
            pt = float(pt_entries[i.get()])
        except:
            pt = 0
        try:
            leaves = int(leave_entries[i].get())
        except:
            leaves = 0

        paid = (sal - (leaves * 1000)) - pt
        paid_labels[i].config(text=f"{paid:,.2f}")
        total_salary += sal
        total_pt += pt
        total_leaves += leaves
        total_paid += paid

    # TDS Logic (based on total_salary, not total_paid)
    tds = 0
    if total_salary > 3000000:
        tds = total_salary * 0.30
    elif total_salary > 2000000:
        tds = total_salary * 0.20
    elif total_salary > 1500000:
        tds = total_salary * 0.15
    elif total_salary > 1000000:
        tds = total_salary * 0.10
    elif total_salary > 500000:
        tds = total_salary * 0.05

    net_paid = total_paid - tds

    # Update Financial Summary
    lbl_total_salary.config(text=f"{total_salary:,.2f}")
    lbl_total_leaves.config(text=f"{total_leaves}")
    lbl_total_pt.config(text=f"{total_pt:,.2f}")
    lbl_total_paid.config(text=f"{net_paid:,.2f}")

Button(root, text="Calculate", command=calculate, bg="green", fg="white", width=15).place(x=650, y=630)
root.mainloop()
