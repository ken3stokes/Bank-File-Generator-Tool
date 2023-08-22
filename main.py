import tkinter as tk
from tkinter import ttk  # for combobox
from tkinter import filedialog, messagebox
import random
import datetime
import os

# Helper Functions

def current_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# For MT940 Wire File Generation
def generate_mt940_wire_file(filename, currency):
    try:
        timestamp = current_timestamp()
        file_path = f"{filename}_{timestamp}.txt"
        # ... [MT940 wire generation logic here]
        return True
    except:
        return False

# For ACH File Generation
def generate_ach_file(filename):
    try:
        timestamp = current_timestamp()
        with open(f"{filename}_{timestamp}.txt", 'w') as f:
            f.write('ACH File Header\n')
            for i in range(10):
                f.write(f'Transaction {i+1}: ${random.randint(100, 10000)}\n')
            f.write('ACH File Footer\n')
        return True
    except:
        return False

# For POSPAY File Generation
prefixes = ["Alpha", "Beta", "Delta", "Gamma", "Omega"]
suffixes = ["Tech", "Solutions", "Industries", "Enterprises", "Global"]

def generate_company_name():
    return f"{random.choice(prefixes)}{random.choice(suffixes)}"

def generate_filename(company_name):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%m%d%H")
    return f"{company_name}_pospay.{formatted_time}.txt"

payees = ["John Doe", "Jane Smith", "Acme Corp.", "Tech Solutions", "Global Industries"]
starting_check_number = 10000

def generate_positive_pay_content():
    content = []
    content.append("Payee,CheckNumber,CheckDate")
    for _ in range(5):  # Generate 5 records per file for demonstration
        payee = random.choice(payees)
        check_number = starting_check_number + _
        check_date = datetime.datetime.now().strftime("%Y-%m-%d")
        content.append(f"{payee},{check_number},{check_date}")
    return "\n".join(content)

def generate_pospay_file():
    try:
        pospay_path = 'C:/Users/kenne/PycharmProjectt/Bank File Generator Tool/files/pospay'
        company_name = generate_company_name()
        filename = generate_filename(company_name)
        with open(os.path.join(pospay_path, filename), "w") as file:
            file.write(generate_positive_pay_content())
        return True
    except:
        return False

# Show Success or Error Message
def show_message(status, filetype):
    if status:
        messagebox.showinfo("Success", f"{filetype} file generation was successful!")
    else:
        messagebox.showerror("Error", f"An error occurred while generating the {filetype} file.")

# GUI Functions
def choose_directory():
    global staging_path
    staging_path = filedialog.askdirectory()
    directory_label.config(text=f"Staging Path: {staging_path}")

def generate_wire():
    wire_path = 'C:/Users/kenne/PycharmProjectt/Bank File Generator Tool/files/wire/wire'
    currency = currency_combobox.get()
    status = generate_mt940_wire_file(wire_path, currency)
    show_message(status, "Wire")

def generate_ach():
    ach_path = 'C:/Users/kenne/PycharmProjectt/Bank File Generator Tool/files/ach/ach'
    status = generate_ach_file(ach_path)
    show_message(status, "ACH")

def generate_pospay():
    status = generate_pospay_file()
    show_message(status, "POSPAY")

# GUI Setup
app = tk.Tk()
app.title("Generate Transaction Files")
app.geometry("600x300")

# Font configuration
font_config = ("Arial", 12)

# Main Frame for better padding and positioning
main_frame = ttk.Frame(app, padding="20 20 20 20")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

# Directory selection button
directory_button = ttk.Button(main_frame, text="Choose Staging Directory", command=choose_directory)
directory_button.grid(column=0, row=0, sticky=tk.W, pady=5, columnspan=3)

# Directory label
directory_label_text = f"Staging Path: Not Selected"
directory_label = ttk.Label(main_frame, text=directory_label_text, font=font_config)
directory_label.grid(column=0, row=1, sticky=tk.W, pady=5, columnspan=3)

# Currency selection
currency_label = ttk.Label(main_frame, text="Select Currency for Wire File:", font=font_config)
currency_label.grid(column=0, row=2, sticky=tk.W, pady=5)

currency_combobox = ttk.Combobox(main_frame, values=["USD", "EUR"], state="readonly", font=font_config, width=10)
currency_combobox.set("USD")
currency_combobox.grid(column=1, row=2, sticky=tk.W, pady=5)

# Buttons
generate_wire_button = ttk.Button(main_frame, text="Generate Wire File", command=generate_wire)
generate_wire_button.grid(column=0, row=3, sticky=tk.W, pady=10, padx=10)

generate_ach_button = ttk.Button(main_frame, text="Generate ACH File", command=generate_ach)
generate_ach_button.grid(column=1, row=3, sticky=tk.W, pady=10, padx=10)

generate_pospay_button = ttk.Button(main_frame, text="Generate POSPAY File", command=generate_pospay)
generate_pospay_button.grid(column=2, row=3, sticky=tk.W, pady=10, padx=10)

app.mainloop()
