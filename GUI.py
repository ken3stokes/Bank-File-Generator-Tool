def generate_wire_file():
    try:
        path = r"C:\Users\kenne\PycharmProjectt\Bank File Generator Tool\files\wires"
        ensure_directory_exists(path)
        filename = "ACME_Wire_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        full_path = os.path.join(path, filename)
        content = f"{filename}, TRX12345, ACCT9876, Credit, 5000.00, USD, {datetime.datetime.now().strftime('%Y-%m-%d')}"

        with open(full_path, 'w') as file:
            file.write(content)

        print(f"Wire file successfully written to {full_path}.")
        messagebox.showinfo("Info", "MT940 Wire File Generated and staged in the wires folder.")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
