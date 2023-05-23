import tkinter as tk
import subprocess
from PIL import ImageTk, Image

def runfunction():
    subprocess.Popen(["python", "login.py"])

def checkoutfunction():
    subprocess.Popen(["python", "Employeescanner.py"])

def checktoolfunction():
    subprocess.Popen(["python", "toolsearch.py"])

def checkinfunction():
    subprocess.Popen(["python", "ToolsReturn.py"])

root = tk.Tk()
root.title("Aviation Tool Management System")
root.geometry("1350x900")

# Load and resize the image
image = Image.open("plane.jpg")
image = image.resize((1350, 900), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=1350, height=900)
canvas.place(relx=0.5, rely=0.5, anchor="center")
canvas.create_image(0, 0, image=photo, anchor="nw")

button_width = 50
button_height = 3
button_font = ("TkDefaultFont", 13, "bold")

loginbutton = tk.Button(root, text="Login", width=button_width, height=button_height, font=button_font, command=runfunction)
checkoutbutton = tk.Button(root, text="Check Out", width=button_width, height=button_height, font=button_font, command=checkoutfunction)
checktoolbutton = tk.Button(root, text="Check Tool", width=button_width, height=button_height, font=button_font, command=checktoolfunction)
checkinbutton = tk.Button(root, text="Check In", width=button_width, height=button_height, font=button_font, command=checkinfunction)

loginbutton.place(relx=0.5, rely=0.3, anchor="center", y=30)
checkoutbutton.place(relx=0.5, rely=0.4, anchor="center", y=30)
checktoolbutton.place(relx=0.5, rely=0.5, anchor="center", y=30)
checkinbutton.place(relx=0.5, rely=0.6, anchor="center", y=30)

root.mainloop()
