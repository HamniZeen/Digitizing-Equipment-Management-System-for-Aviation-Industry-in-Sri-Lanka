from tkinter import *
from PIL import Image, ImageTk
import pyqrcode
import csv

def generate_tool_qr():
    # Get tool ID from entry field
    tool_id = tool_id_entry.get()
    tool_name = tool_name_entry.get()

    # Generate QR code for tool
    tool_qr = pyqrcode.create(f"{tool_id},{tool_name}")
    tool_qr.png(f"{tool_id}-{tool_name}.png", scale=6)

def generate_employee_qr():
    # Get employee ID from entry field
    employee_id = employee_id_entry.get()
    employee_name = employee_name_entry.get()
    employee_email = employee_email_entry.get()

    # Generate QR code for employee
    employee_qr = pyqrcode.create(f"{employee_id},{employee_name},{employee_email}")
    employee_qr.png(f"{employee_id}-{employee_name}.png", scale=6)

def submit_tool():
    # Get tool information from entry fields
    tool_id = tool_id_entry.get()
    tool_name = tool_name_entry.get()
    location = location_entry.get()
    status = "Available"

    # Save tool information in CSV file
    with open("tools.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([tool_id, tool_name, location, status])

    # Clear entry fields
    tool_id_entry.delete(0, END)
    tool_name_entry.delete(0, END)
    location_entry.delete(0, END)

def submit_employee():
    # Get employee information from entry fields
    employee_name = employee_name_entry.get()
    employee_id = employee_id_entry.get()
    employee_email = employee_email_entry.get()

    with open("employees.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([employee_id, employee_name, employee_email])

    # Clear entry fields
    employee_id_entry.delete(0, END)
    employee_name_entry.delete(0, END)
    employee_email_entry.delete(0, END)


root = Tk()
root.geometry("1350x900")
root.title("Tool and Employee QR Generator")

# Load and resize the image
image = Image.open("plane.jpg")
image = image.resize((1350, 900), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

canvas = Canvas(root, width=1350, height=900)
canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.grid(row=0, column=0)

frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

font_style = ("TkDefaultFont", 13, "bold")
button_width = 15
button_width2 = 20
button_height = 2
button_width1 = 25

tool_id_label = Label(frame, text="Tool ID:", font=font_style)
tool_id_label.grid(row=0, column=0, padx=5, pady=5)
tool_id_entry = Entry(frame)
tool_id_entry.configure(width=40)
tool_id_entry.grid(row=0, column=1, padx=5, pady=5)

tool_name_label = Label(frame, text="Tool Name:", font=font_style)
tool_name_label.grid(row=1, column=0)
tool_name_entry = Entry(frame)
tool_name_entry.configure(width=40)
tool_name_entry.grid(row=1, column=1, padx=5, pady=5)

location_label = Label(frame, text="Location:", font=font_style)
location_label.grid(row=2, column=0, padx=5, pady=5)
location_entry = Entry(frame)
location_entry.configure(width=40)
location_entry.grid(row=2, column=1, padx=5, pady=5)

tool_qr_button = Button(frame, text="Generate Tool QR Code", command=generate_tool_qr, font=font_style, width=button_width1, height=button_height, bd=2)
tool_qr_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

employee_id_label = Label(frame, text="Employee ID:", font=font_style)
employee_id_label.grid(row=4, column=0, padx=5, pady=5)
employee_id_entry = Entry(frame)
employee_id_entry.configure(width=40)
employee_id_entry.grid(row=4, column=1, padx=5, pady=5)

employee_name_label = Label(frame, text="Employee Name:", font=font_style)
employee_name_label.grid(row=5, column=0, padx=5, pady=5)
employee_name_entry = Entry(frame)
employee_name_entry.configure(width=40)
employee_name_entry.grid(row=5, column=1, padx=5, pady=5)

employee_email_label = Label(frame, text="Employee Email:", font=font_style)
employee_email_label.grid(row=6, column=0, padx=5, pady=5)
employee_email_entry = Entry(frame)
employee_email_entry.configure(width=40)
employee_email_entry.grid(row=6, column=1, padx=5, pady=5)

employee_qr_button = Button(frame, text="Generate Employee QR Code", command=generate_employee_qr, font=font_style, width=button_width1, height=button_height, bd=2)
employee_qr_button.grid(row=7, column=1, columnspan=2, padx=5, pady=5)

tool_submit_button = Button(frame, text="Submit Tool", command=submit_tool, font=font_style, width=button_width2, height=button_height, bd=2)
tool_submit_button.grid(row=8, column=0, padx=5, pady=5)

employee_submit_button = Button(frame, text="Submit Employee", command=submit_employee, font=font_style, width=button_width2, height=button_height, bd=2)
employee_submit_button.grid(row=8, column=1, padx=5, pady=5)

root.mainloop()
