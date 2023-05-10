import tkinter as tk
import pyqrcode
import csv



class ToolEmployeeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tool and Employee QR Generator")

        # Create tool labels and entry fields
        self.tool_id_label = tk.Label(master, text="Tool ID:")
        self.tool_id_label.grid(row=0, column=0)
        self.tool_id_entry = tk.Entry(master)
        self.tool_id_entry.grid(row=0, column=1)

        self.tool_name_label = tk.Label(master, text="Tool Name:")
        self.tool_name_label.grid(row=1, column=0)
        self.tool_name_entry = tk.Entry(master)
        self.tool_name_entry.grid(row=1, column=1)

        self.location_label = tk.Label(master, text="Location:")
        self.location_label.grid(row=2, column=0)
        self.location_entry = tk.Entry(master)
        self.location_entry.grid(row=2, column=1)

        # Create tool and employee QR code buttons
        self.tool_qr_button = tk.Button(master, text="Generate Tool QR Code", command=self.generate_tool_qr)
        self.tool_qr_button.grid(row=3, column=1)

        self.employee_id_label = tk.Label(master, text="Employee ID:")
        self.employee_id_label.grid(row=4, column=0)
        self.employee_id_entry = tk.Entry(master)
        self.employee_id_entry.grid(row=4, column=1)

        self.employee_name_label = tk.Label(master, text="Employee Name:")
        self.employee_name_label.grid(row=5, column=0)
        self.employee_name_entry = tk.Entry(master)
        self.employee_name_entry.grid(row=5, column=1)

        self.employee_email_label = tk.Label(master, text="Employee Email:")
        self.employee_email_label.grid(row=6, column=0)
        self.employee_email_entry = tk.Entry(master)
        self.employee_email_entry.grid(row=6, column=1)

        self.employee_qr_button = tk.Button(master, text="Generate Employee QR Code", command=self.generate_employee_qr)
        self.employee_qr_button.grid(row=7, column=1)

        # Create tool and employee submit buttons
        self.tool_submit_button = tk.Button(master, text="Submit Tool", command=self.submit_tool)
        self.tool_submit_button.grid(row=8, column=0)

        self.employee_submit_button = tk.Button(master, text="Submit Employee", command=self.submit_employee)
        self.employee_submit_button.grid(row=8, column=1)

    def generate_tool_qr(self):
        # Get tool ID from entry field
        tool_id = self.tool_id_entry.get()
        tool_name = self.tool_name_entry.get()

        # Generate QR code for tool
        tool_qr = pyqrcode.create(f"{tool_id},{tool_name}")
        tool_qr.png(f"{tool_id}-{tool_name}.png", scale=6)

    def generate_employee_qr(self):
        # Get employee ID from entry field
        employee_id = self.employee_id_entry.get()
        employee_name = self.employee_name_entry.get()
        employee_email = self.employee_email_entry.get()

        # Generate QR code for employee
        employee_qr = pyqrcode.create(f"{employee_id},{employee_name},{employee_email}")
        employee_qr.png(f"{employee_id}-{employee_name}.png", scale=6)

    def submit_tool(self):
        # Get tool information from entry fields
        tool_id = self.tool_id_entry.get()
        tool_name = self.tool_name_entry.get()
        location = self.location_entry.get()
        status = "Available"

        # Save tool information in CSV file
        with open("tools.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([tool_id, tool_name, location, status])

        # Clear entry fields
        self.tool_id_entry.delete(0, tk.END)
        self.tool_name_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)

    def submit_employee(self):
        # Get employee information from entry fields
        employee_name = self.employee_name_entry.get()
        employee_id = self.employee_id_entry.get()
        employee_email=self.employee_email_entry.get()

        with open("employees.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([employee_id, employee_name, employee_email])

        # Clear entry fields
        self.employee_id_entry.delete(0, tk.END)
        self.employee_name_entry.delete(0, tk.END)
        self.employee_email_entry.delete(0,tk.END)
      

root = tk.Tk()
app = ToolEmployeeGUI(root)
root.mainloop()