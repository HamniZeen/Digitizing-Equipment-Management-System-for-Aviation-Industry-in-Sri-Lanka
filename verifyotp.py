import tkinter as tk
import subprocess
root = tk.Tk()

root.title("OTP Verification")


input_label = tk.Label(root, text="Enter the OTP Sent:")
input_label.pack()


entry = tk.Entry(root)
entry.pack()


output_label = tk.Label(root, text="")
output_label.pack()


def check_file():
    
    with open('otp.txt', 'r') as file:
        file_contents = file.read().replace('\n', '')

   
    user_input = entry.get()

   
    if user_input == file_contents:
        
        subprocess.run(['python', 'qrgenerator.py'])
    else:
       
        output_label.config(text="Invalid OTP ", fg="red", font=("Arial Bold", 10))


button = tk.Button(root, text="Verify OTP", command=check_file)
button.pack()


root.mainloop()
