from tkinter import *
import subprocess
from PIL import Image, ImageTk

def check_file():
    
    with open('otp.txt', 'r') as file:
        file_contents = file.read().replace('\n', '')

    user_input = entry.get()

   
    if user_input == file_contents:
        
        subprocess.run(['python', 'qrgenerator.py'])
        
    else:
       
        output_label.config(text="Invalid OTP ", fg="red", font=("Arial Bold", 10))

root = Tk()
root.title("OTP Verification")
root.geometry("1350x900")

image = Image.open("plane.jpg")
image = image.resize((1350, 900), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

canvas = Canvas(root, width=1350, height=900)
canvas.place(relx=0.5, rely=0.5, anchor="center")

canvas.create_image(0, 0, anchor="nw", image=photo)
font_style = ("TkDefaultFont", 13, "bold")
button_width = 15
button_height = 2

frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

input_label = Label(frame, text="Enter the OTP Sent:", font=font_style)
input_label.grid(row=0, column=0, padx=5, pady=5)
entry = Entry(frame, width=20)
entry.grid(row=0, column=1, padx=5, pady=5)

output_label = Label(frame, text="", font=font_style)
output_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

button = Button(frame, text="Verify OTP", command=check_file, font=font_style, width=button_width, height=button_height, bd=2)
button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
