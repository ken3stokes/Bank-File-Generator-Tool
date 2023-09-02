import tkinter as tk
from tkinter import messagebox
import datetime
import os


# Ensure directory exists or create it
def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


# Generate PosPay file
def generate_pospay_file():
    path = r"C:\Users\kenne\PycharmProjectt\Bank File Generator Tool\files\pospay"
    ensure_directory_exists(path)
    filename = "ACME_Pospay_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    full_path = os.path.join(path, filename)
    content = f"{filename}, John Doe, 1000.50, {datetime.datetime.now().strftime('%Y-%m-%d')}"

    with open(full_path, 'w') as file:
        file.write(content)

    messagebox.showinfo("Info", "PosPay File Generated Successfully!")


# Generate ACH file
def generate_ach_file():
    path = r"C:\Users\kenne\PycharmProjectt\Bank File Generator Tool\files\ach"
    ensure_directory_exists(path)
    filename = "ACME_ACH_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    full_path = os.path.join(path, filename)
    content = f"{filename}, Bank of Tomorrow, 1234567890, 2000.00, {datetime.datetime.now().strftime('%Y-%m-%d')}"

    with open(full_path, 'w') as file:
        file.write(content)

    messagebox.showinfo("Info", "ACH File Generated Successfully!")


# Generate Wire file
def generate_wire_file():
    path = r"C:\Users\kenne\PycharmProjectt\Bank File Generator Tool\files\wires"
    ensure_directory_exists(path)
    filename = "ACME_Wire_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    full_path = os.path.join(path, filename)
    content = f"{filename}, TRX12345, ACCT9876, Credit, 5000.00, USD, {datetime.datetime.now().strftime('%Y-%m-%d')}"

    with open(full_path, 'w') as file:
        file.write(content)

    messagebox.showinfo("Info", "MT940 Wire File Generated Successfully!")


# GUI setup
root = tk.Tk()
root.title("Bank File Generator Tool")

btn_ach = tk.Button(root, text="Generate ACH", command=generate_ach_file)
btn_ach.pack(pady=20)

btn_pospay = tk.Button(root, text="Generate PosPay", command=generate_pospay_file)
btn_pospay.pack(pady=20)

btn_wire = tk.Button(root, text="Generate MT940 Wire", command=generate_wire_file)
btn_wire.pack(pady=20)

root.mainloop()
