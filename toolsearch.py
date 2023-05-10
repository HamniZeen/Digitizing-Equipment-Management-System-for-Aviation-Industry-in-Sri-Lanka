import csv
import tkinter as tk
from datetime import datetime


class ToolGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tool Search")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master,text="ID").grid(row=0,column=0)
        self.id_entry=tk.Entry(self.master)
        self.id_entry.grid(row=0,column=1)

        tk.Label(self.master,text="Tool Name").grid(row=1,column=0)
        self.name_entry=tk.Entry(self.master)
        self.name_entry.grid(row=1,column=1)
    
       

        tk.Button(self.master,text="Search", command=self.search_tool ).grid(row=3,column=0, columnspan=2)


        self.result_label=tk.Label(self.master,text="")
        self.result_label.grid(row=4,column=0, columnspan=2)


    
    def search_tool(self):
        tool_id=self.id_entry.get()
        tool_name=self.name_entry.get()
        #tool_date=self.date_entry.get()
        

        with open('tools.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0]==tool_id and row[1]==tool_name:
                    if row[3]=="Available":
                        self.result_label.config(text=f"Tool Found in {row[2]}" , fg="green")
                    else:
                        self.result_label.config(text="Tool is not yet Found!" , fg="blue")
                    break
                    
            else:
                 self.result_label.config(text="Tool not Found!", fg="red")
       

if __name__=="__main__":

    root=tk.Tk()
   
    app=ToolGUI(root)
    root.mainloop()


