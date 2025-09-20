import tkinter as tk
from tkinter import messagebox

def submit():
    date = date_entry.get()
    month = month_entry.get()
    year = year_entry.get()
    if date.isdigit() and month.isdigit() and year.isdigit():
        messagebox.showinfo("Birth Date", f"Your birth date is: {date}-{month}-{year}")
    else:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for date, month, and year.")

root = tk.Tk()
root.title("Birth Date Input")

tk.Label(root, text="Date:").grid(row=0, column=0, padx=10, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Month:").grid(row=1, column=0, padx=10, pady=5)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Year:").grid(row=2, column=0, padx=10, pady=5)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1, padx=10, pady=5)

submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()