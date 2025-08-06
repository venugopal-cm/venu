import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("1100x600")
root.title("Restaurant Billing Systems")

# Prices for items (customize as needed)
item_prices = [10, 20, 15, 30, 25, 12, 18, 22, 14, 16, 11, 19, 13, 17, 21, 23]

# Variables for checkboxes and entries
vars_chk = [tk.IntVar() for _ in range(16)]
vars_qty = [tk.StringVar(value='0') for _ in range(16)]

# Cost variables
cost_drinks = tk.StringVar()
cost_cakes = tk.StringVar()
service_charge = tk.StringVar()
paid_tax = tk.StringVar()
subtotal = tk.StringVar()
total_cost = tk.StringVar()

# Calculator variables
calc_input = tk.StringVar()

# Functions
def total():
    drinks = 0
    cakes = 0
    for i in range(8):
        if vars_chk[i].get():
            qty = int(vars_qty[i].get())
            drinks += qty * item_prices[i]
    for i in range(8, 16):
        if vars_chk[i].get():
            qty = int(vars_qty[i].get())
            cakes += qty * item_prices[i]
    cost_drinks.set(f"₹ {drinks:.2f}")
    cost_cakes.set(f"₹ {cakes:.2f}")
    serv_charge = (drinks + cakes) * 0.0025
    service_charge.set(f"₹ {serv_charge:.2f}")
    tax = (drinks + cakes) * 0.12
    paid_tax.set(f"₹ {tax:.2f}")
    sub = drinks + cakes + serv_charge
    subtotal.set(f"₹ {sub:.2f}")
    total = sub + tax
    total_cost.set(f"₹ {total:.2f}")

def reset():
    for v in vars_chk:
        v.set(0)
    for v in vars_qty:
        v.set('0')
    cost_drinks.set('')
    cost_cakes.set('')
    service_charge.set('')
    paid_tax.set('')
    subtotal.set('')
    total_cost.set('')
    calc_input.set('')
    text_receipt.delete('1.0', tk.END)

def exit_app():
    root.destroy()

def calc_click(val):
    calc_input.set(calc_input.get() + str(val))

def calc_clear():
    calc_input.set('')

def calc_equal():
    try:
        result = str(eval(calc_input.get()))
        calc_input.set(result)
    except:
        calc_input.set('Error')

def receipt():
    text_receipt.delete('1.0', tk.END)
    text_receipt.insert(tk.END, "Receipt\n")
    for i in range(16):
        if vars_chk[i].get():
            text_receipt.insert(tk.END, f"item{i+1}: {vars_qty[i].get()} x {item_prices[i]}\n")
    text_receipt.insert(tk.END, f"\nCost Of Drinks: {cost_drinks.get()}")
    text_receipt.insert(tk.END, f"\nCost Of Cakes: {cost_cakes.get()}")
    text_receipt.insert(tk.END, f"\nService Charge: {service_charge.get()}")
    text_receipt.insert(tk.END, f"\nPaid Tax: {paid_tax.get()}")
    text_receipt.insert(tk.END, f"\nSubTotal: {subtotal.get()}")
    text_receipt.insert(tk.END, f"\nTotal Cost: {total_cost.get()}")

# Layout
lbl_title = tk.Label(root, text="Restaurant Billing Systems", font=('Arial', 36, 'bold'), bg='#8fd3d6')
lbl_title.pack(fill=tk.X)

frame_left = tk.Frame(root, bd=10, relief=tk.RIDGE, bg='#b6d9d7')
frame_left.place(x=0, y=80, width=400, height=500)

frame_right = tk.Frame(root, bd=10, relief=tk.RIDGE, bg='#b6d9d7')
frame_right.place(x=400, y=80, width=350, height=500)

frame_calc = tk.Frame(root, bd=10, relief=tk.RIDGE, bg='#b6d9d7')
frame_calc.place(x=750, y=80, width=340, height=250)

frame_receipt = tk.Frame(root, bd=10, relief=tk.RIDGE, bg='#b6d9d7')
frame_receipt.place(x=750, y=330, width=340, height=250)

# Left side items
for i in range(8):
    tk.Checkbutton(frame_left, text=f"item{i+1}", variable=vars_chk[i], bg='#b6d9d7').grid(row=i, column=0, sticky='w')
    tk.Entry(frame_left, textvariable=vars_qty[i], width=5).grid(row=i, column=1)

for i in range(8, 16):
    tk.Checkbutton(frame_right, text=f"item{i+1}", variable=vars_chk[i], bg='#b6d9d7').grid(row=i-8, column=0, sticky='w')
    tk.Entry(frame_right, textvariable=vars_qty[i], width=5).grid(row=i-8, column=1)

# Cost display
tk.Label(frame_left, text="Cost Of Drinks", bg='#b6d9d7').grid(row=8, column=0, sticky='w')
tk.Entry(frame_left, textvariable=cost_drinks, state='readonly', width=15).grid(row=8, column=1)
tk.Label(frame_left, text="Cost of Cakes", bg='#b6d9d7').grid(row=9, column=0, sticky='w')
tk.Entry(frame_left, textvariable=cost_cakes, state='readonly', width=15).grid(row=9, column=1)
tk.Label(frame_left, text="Service Charge", bg='#b6d9d7').grid(row=10, column=0, sticky='w')
tk.Entry(frame_left, textvariable=service_charge, state='readonly', width=15).grid(row=10, column=1)

tk.Label(frame_right, text="Paid Tax", bg='#b6d9d7').grid(row=8, column=0, sticky='w')
tk.Entry(frame_right, textvariable=paid_tax, state='readonly', width=15).grid(row=8, column=1)
tk.Label(frame_right, text="SubTotal", bg='#b6d9d7').grid(row=9, column=0, sticky='w')
tk.Entry(frame_right, textvariable=subtotal, state='readonly', width=15).grid(row=9, column=1)
tk.Label(frame_right, text="Total Cost", bg='#b6d9d7').grid(row=10, column=0, sticky='w')
tk.Entry(frame_right, textvariable=total_cost, state='readonly', width=15).grid(row=10, column=1)

# Calculator
tk.Entry(frame_calc, textvariable=calc_input, font=('Arial', 16), bd=5, relief=tk.RIDGE, justify='right').grid(row=0, column=0, columnspan=4)
btns = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('/',4,3),
]
for (text, r, c) in btns:
    if text == 'C':
        cmd = calc_clear
    elif text == '=':
        cmd = calc_equal
    else:
        cmd = lambda val=text: calc_click(val)
    tk.Button(frame_calc, text=text, width=5, height=2, command=cmd).grid(row=r, column=c)

# Receipt area
text_receipt = tk.Text(frame_receipt, width=38, height=12)
text_receipt.pack()

# Bottom buttons
btns_frame = tk.Frame(root, bd=10, relief=tk.RIDGE)
btns_frame.place(x=0, y=580, width=1100, height=60)
tk.Button(btns_frame, text="Total", width=15, command=total).pack(side=tk.LEFT, padx=10)
tk.Button(btns_frame, text="Receipt", width=15, command=receipt).pack(side=tk.LEFT, padx=10)
tk.Button(btns_frame, text="Reset", width=15, command=reset).pack(side=tk.LEFT, padx=10)
tk.Button(btns_frame, text="Exit", width=15, command=exit_app).pack(side=tk.LEFT, padx=10)

root.mainloop()
