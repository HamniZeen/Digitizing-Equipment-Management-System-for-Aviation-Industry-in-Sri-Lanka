import tkinter as tk
import subprocess
def runfunction():
    subprocess.Popen(["python","login.py"])


def checkoutfunction():
    subprocess.Popen(["python","Employeescanner.py"])


def checktoolfunction():
    subprocess.Popen(["python","toolsearch.py"])

def checkinfunction():
    subprocess.Popen(["python","ToolsReturn.py"])
    
root = tk.Tk()
root.title("Aviation Tool Management System ")

image=tk.PhotoImage(file="image.png")
canvas=tk.Canvas(root,width=image.width(), height=image.height())
canvas.place(x=0,y=0)

canvas.create_image(0,0,image=image, anchor="nw")
loginbutton=tk.Button(root,text="Login" ,command=runfunction)
loginbutton.place(x=100,y=100)

ChekOutbutton=tk.Button(root,text="Check Out" ,command=checkoutfunction)
ChekOutbutton.place(x=200,y=200)

CheckToolbutton=tk.Button(root,text="Check Tool" ,command=checktoolfunction)
CheckToolbutton.place(x=300,y=300)

CheckInbutton=tk.Button(root,text="Check In" ,command=checkinfunction)
CheckInbutton.place(x=400,y=400)



loginbutton.grid(row=1 ,column=1,padx=150, pady=10,sticky="nsew")
ChekOutbutton.grid(row=2 ,column=1,padx=150, pady=10,sticky="nsew")
CheckToolbutton.grid(row=3 ,column=1,padx=150, pady=10,sticky="nsew")
CheckInbutton.grid(row=4 ,column=1,padx=150, pady=10,sticky="nsew")

loginbutton.grid_anchor("center")
ChekOutbutton.grid_anchor("center")
CheckToolbutton.grid_anchor("center")
CheckInbutton.grid_anchor("center")
root.mainloop()