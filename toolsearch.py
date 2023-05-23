import csv
from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk

root = Tk()
root.title("Tool Search")
root.geometry("1350x900")

canvas = Canvas(root, width=1350, height=900)
bg_image = Image.open("plane.jpg")
bg_image = bg_image.resize((1350, 900), Image.LANCZOS)
photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.grid(row=0, column=0)

frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

font_style = ("TkDefaultFont", 13, "bold")
button_width = 15
button_height = 2
   
def search_tool():
    global id_entry, name_entry, result_label
    tool_id=id_entry.get()
    tool_name=name_entry.get()
        
    with open('tools.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0]==tool_id and row[1]==tool_name:
                    if row[3]=="Available":
                        result_label.config(text=f"Tool Found in {row[2]}" , fg="green")
                    else:
                        result_label.config(text="Tool is not yet Found!" , fg="blue")
                    break
                    
            else:
                 result_label.config(text="Tool not Found!", fg="red")

id_label = Label(frame, text="ID:", font=font_style)
id_label.grid(row=0, column=0, padx=5, pady=5)
id_entry = Entry(frame, width=30)
id_entry.grid(row=0, column=1, padx=5, pady=5)

name_label = Label(frame, text="Tool Name:", font=font_style)
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = Entry(frame, width=30)
name_entry.grid(row=1, column=1, padx=5, pady=5)

search_btn = Button(frame, text="Search", command=search_tool, font=font_style, width=button_width, height=button_height, bd=2)
search_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

result_label = Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2)
root.mainloop()
