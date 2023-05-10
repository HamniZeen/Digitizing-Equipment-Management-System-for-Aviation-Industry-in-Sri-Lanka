import subprocess
from tkinter import *
from tkinter import messagebox

def login():
    uname = uname_entry.get()
    password = pwd_entry.get()

    if uname == "admin" and password == "admin":
        messagebox.showinfo("Login", "Login Successful")
        subprocess.call(['node', 'otpmail.js'])
        subprocess.Popen(["python", "verifyotp.py"])
    else:
        messagebox.showerror("Login", "Check User Name and Password")

root = Tk()
root.title("Login")

uname_label = Label(root, text="User Name:")
uname_label.pack()
uname_entry = Entry(root)
uname_entry.pack()

pwd_label = Label(root, text="Password:")
pwd_label.pack()
pwd_entry = Entry(root, show="*")
pwd_entry.pack()

login_btn = Button(root, text="Send OTP", command=login)
login_btn.pack()

root.mainloop()
