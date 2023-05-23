from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

def login():
    uname = uname_entry.get()
    password = pwd_entry.get()

    if uname == "admin" and password == "admin":
        messagebox.showinfo("Login", "Login Successful")
        subprocess.call(['node', 'otpmail.js'])
        subprocess.Popen(["python", "verifyotp.py"])
        root.destroy()
    else:
        messagebox.showerror("Login", "Check User Name and Password")
        uname_entry.delete(0, END)
        pwd_entry.delete(0, END)

root = Tk()
root.title("Login")
root.geometry("1350x900")

# Load and resize the image
image = Image.open("plane.jpg")
image = image.resize((1350, 900), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

canvas = Canvas(root, width=1350, height=900)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.grid(row=0, column=0)

frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

font_style = ("TkDefaultFont", 13, "bold")
button_width = 15
button_height = 2

uname_label = Label(frame, text="User Name:", font=font_style)
uname_label.grid(row=0, column=0, padx=5, pady=5)
uname_entry = Entry(frame, width=30)
uname_entry.grid(row=0, column=1, padx=5, pady=5)

pwd_label = Label(frame, text="Password:", font=font_style)
pwd_label.grid(row=1, column=0, padx=5, pady=5)
pwd_entry = Entry(frame, show="*", width=30)
pwd_entry.grid(row=1, column=1, padx=5, pady=5)

login_btn = Button(frame, text="Send OTP", command=login, font=font_style, width=button_width, height=button_height, bd=2)
login_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
