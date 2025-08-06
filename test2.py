import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class Item:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def __str__(self):
        return f"{self.name} | Qty: {self.qty} | Price: {self.price}"

class SupermarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Management System")
        self.inventory = []

        self.create_widgets()

    def create_widgets(self):
        # Main Menu
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(padx=10, pady=10)

        tk.Label(self.menu_frame, text="Supermarket Management System", font=("Arial", 16, "bold")).pack(pady=10)

        btns = [
            ("View Items", self.view_items),
            ("Add Item", self.add_item),
            ("Purchase Item", self.purchase_item),
            ("Search Item", self.search_item),
            ("Edit Item", self.edit_item),
            ("Delete Item", self.delete_item),
            ("Exit", self.root.quit)
        ]

        for text, cmd in btns:
            tk.Button(self.menu_frame, text=text, width=20, command=cmd).pack(pady=3)

    def view_items(self):
        win = tk.Toplevel(self.root)
        win.title("View Items")
        tk.Label(win, text="Items in Inventory:", font=("Arial", 12, "bold")).pack(pady=5)
        if not self.inventory:
            tk.Label(win, text="No items in inventory.").pack()
        else:
            for item in self.inventory:
                tk.Label(win, text=str(item)).pack(anchor="w")

    def add_item(self):
        def save_item():
            name = name_var.get()
            try:
                qty = int(qty_var.get())
                price = float(price_var.get())
            except ValueError:
                messagebox.showerror("Error", "Quantity and Price must be numbers.")
                return
            self.inventory.append(Item(name, qty, price))
            messagebox.showinfo("Success", f"Item '{name}' added successfully!")
            add_win.destroy()

        add_win = tk.Toplevel(self.root)
        add_win.title("Add Item")
        name_var, qty_var, price_var = tk.StringVar(), tk.StringVar(), tk.StringVar()

        tk.Label(add_win, text="Item Name:").pack()
        tk.Entry(add_win, textvariable=name_var).pack()
        tk.Label(add_win, text="Quantity:").pack()
        tk.Entry(add_win, textvariable=qty_var).pack()
        tk.Label(add_win, text="Price:").pack()
        tk.Entry(add_win, textvariable=price_var).pack()
        tk.Button(add_win, text="Add", command=save_item).pack(pady=5)

    def purchase_item(self):
        if not self.inventory:
            messagebox.showinfo("Info", "No items to purchase.")
            return

        purchase_win = tk.Toplevel(self.root)
        purchase_win.title("Purchase Item")

        tk.Label(purchase_win, text="Select Item to Purchase:").pack()
        items = [item.name for item in self.inventory]
        selected = tk.StringVar(value=items[0])
        ttk.Combobox(purchase_win, values=items, textvariable=selected, state="readonly").pack()

        qty_var = tk.StringVar()
        tk.Label(purchase_win, text="Quantity to Purchase:").pack()
        tk.Entry(purchase_win, textvariable=qty_var).pack()

        def purchase():
            item_name = selected.get()
            try:
                qty = int(qty_var.get())
            except ValueError:
                messagebox.showerror("Error", "Quantity must be an integer.")
                return
            for item in self.inventory:
                if item.name == item_name:
                    if item.qty >= qty:
                        item.qty -= qty
                        messagebox.showinfo("Success", f"Purchased {qty} of '{item_name}'.")
                        purchase_win.destroy()
                        return
                    else:
                        messagebox.showerror("Error", "Not enough stock!")
                        return

        tk.Button(purchase_win, text="Purchase", command=purchase).pack(pady=5)

    def search_item(self):
        def search():
            name = name_var.get()
            for item in self.inventory:
                if item.name.lower() == name.lower():
                    messagebox.showinfo("Found", f"Item: {item.name}\nQty: {item.qty}\nPrice: {item.price}")
                    return
            messagebox.showinfo("Not Found", "Item not found.")

        search_win = tk.Toplevel(self.root)
        search_win.title("Search Item")
        name_var = tk.StringVar()
        tk.Label(search_win, text="Enter Item Name:").pack()
        tk.Entry(search_win, textvariable=name_var).pack()
        tk.Button(search_win, text="Search", command=search).pack(pady=5)

    def edit_item(self):
        if not self.inventory:
            messagebox.showinfo("Info", "No items to edit.")
            return

        edit_win = tk.Toplevel(self.root)
        edit_win.title("Edit Item")

        tk.Label(edit_win, text="Select Item to Edit:").pack()
        items = [item.name for item in self.inventory]
        selected = tk.StringVar(value=items[0])
        ttk.Combobox(edit_win, values=items, textvariable=selected, state="readonly").pack()

        qty_var, price_var = tk.StringVar(), tk.StringVar()
        tk.Label(edit_win, text="New Quantity:").pack()
        tk.Entry(edit_win, textvariable=qty_var).pack()
        tk.Label(edit_win, text="New Price:").pack()
        tk.Entry(edit_win, textvariable=price_var).pack()

        def edit():
            item_name = selected.get()
            try:
                qty = int(qty_var.get())
                price = float(price_var.get())
            except ValueError:
                messagebox.showerror("Error", "Quantity and Price must be numbers.")
                return
            for item in self.inventory:
                if item.name == item_name:
                    item.qty = qty
                    item.price = price
                    messagebox.showinfo("Success", f"Item '{item_name}' updated.")
                    edit_win.destroy()
                    return

        tk.Button(edit_win, text="Update", command=edit).pack(pady=5)

    def delete_item(self):
        if not self.inventory:
            messagebox.showinfo("Info", "No items to delete.")
            return

        delete_win = tk.Toplevel(self.root)
        delete_win.title("Delete Item")

        tk.Label(delete_win, text="Select Item to Delete:").pack()
        items = [item.name for item in self.inventory]
        selected = tk.StringVar(value=items[0])
        ttk.Combobox(delete_win, values=items, textvariable=selected, state="readonly").pack()

        def delete():
            item_name = selected.get()
            for i, item in enumerate(self.inventory):
                if item.name == item_name:
                    del self.inventory[i]
                    messagebox.showinfo("Deleted", f"Item '{item_name}' deleted.")
                    delete_win.destroy()
                    return

        tk.Button(delete_win, text="Delete", command=delete).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketApp(root)
    root.mainloop()
