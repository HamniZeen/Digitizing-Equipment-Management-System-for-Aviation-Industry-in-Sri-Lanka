import tkinter as tk
import subprocess

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

image = tk.PhotoImage(file="image.png")
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.place(relx=0.5, rely=0.5, anchor="center")

canvas.create_image(0, 0, image=image, anchor="nw")

button_width = 50
button_height = 3
button_font = ("TkDefaultFont", 13, "bold")

loginbutton = tk.Button(root, text="Login", width=button_width, height=button_height, font=button_font, command=runfunction)
ChekOutbutton = tk.Button(root, text="Check Out", width=button_width, height=button_height, font=button_font, command=checkoutfunction)
CheckToolbutton = tk.Button(root, text="Check Tool", width=button_width, height=button_height, font=button_font, command=checktoolfunction)
CheckInbutton = tk.Button(root, text="Check In", width=button_width, height=button_height, font=button_font, command=checkinfunction)

loginbutton.place(relx=0.5, rely=0.3, anchor="center", y=30)
ChekOutbutton.place(relx=0.5, rely=0.4, anchor="center", y=30)
CheckToolbutton.place(relx=0.5, rely=0.5, anchor="center", y=30)
CheckInbutton.place(relx=0.5, rely=0.6, anchor="center", y=30)

root.mainloop()
