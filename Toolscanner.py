import cv2
import tkinter as tk
import qrcode
import numpy as np
import csv
import datetime
import subprocess


def decode_qr(image, writer):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.QRCodeDetector()
    data, vertices, _ = detector.detectAndDecode(gray)
    if vertices is not None:
        checkoutDate = datetime.date.today().strftime('%Y-%m-%d')
        Deadline = (datetime.date.today() + datetime.timedelta(days=365)).strftime('%Y-%m-%d')
        values = data.split(',')
        if len(values) >=1:
            id=values[0].strip()
        else:
            id=''
        if len(values) >=2:
            name=values[1].strip()
        else:
            name=''
        

        writer.writerow([id,name, checkoutDate, Deadline])
        return id, name, 
    else:
        return None

def open_scanner():
    with open ('Scanned_data_TOOL.csv',mode='a', newline='') as file:
        writer=csv.writer(file)

        writer.writerow(['TScanned ID','TScanned Name','TCheck Out', 'TDeadline'])
        cap = cv2.VideoCapture(0)


        while True:
            ret,frame=cap.read()
        

            cv2.imshow("QR Code Scanner",frame)

            if cv2.waitKey(1) ==ord("q"):
                break

            data=decode_qr(frame,writer)
            if data is not None:
                id, name = data
                print('QRCode', id, name)
    cap.release()
    cv2.destroyAllWindows()

def clean_data():
    input_file='Scanned_data_TOOL.csv'
    output_file='Tool_Clean_ScannedData.csv'

    with open(input_file,'r') as infile:
        reader= csv.reader(infile)
        data= list(reader)

    data_cleaned=[data[0]]
    for row in data[1:]:
        if row and row not in data_cleaned and row[1].strip() !="":
            data_cleaned.append(row)

    
    with open(output_file,'w', newline='') as outfile:
        writer= csv.writer(outfile)
        for row in data_cleaned:
            if len(row)==4:
                writer.writerow(row)


def combinecommand():
    subprocess.Popen(["python","combine.py"])



def statuschangecommand():
    subprocess.Popen(["python","ToolStatusChange.py"])


def submitcommand():
    clean_data()
    combinecommand()
    statuschangecommand()

def run_nodejs_file():
    subprocess.call(['node', 'mail.js'])

def exitt():
    run_nodejs_file()
    root.destroy()
root = tk.Tk()
root.title("Check-out ")

image=tk.PhotoImage(file="image.png")
canvas=tk.Canvas(root,width=image.width(), height=image.height())
canvas.place(x=0,y=0)

canvas.create_image(0,0,image=image, anchor="nw")

button1=tk.Button(root,text="Scan Tool QR", command=open_scanner)
button1.place(x=200,y=200)

button2=tk.Button(root,text="Submit",command=submitcommand)
button2.place(x=300,y=300)

button3=tk.Button(root,text="Exit",command=exitt)
button3.place(x=600,y=600)


button1.grid(row=2 ,column=1,padx=150, pady=10,sticky="nsew")
button2.grid(row=3 ,column=1,padx=150, pady=10,sticky="nsew")
button3.grid(row=5 ,column=1,padx=150, pady=10,sticky="nsew")


button1.grid_anchor("center")
button2.grid_anchor("center")
button3.grid_anchor("center")

root.mainloop()