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
        if len(values) >=3:
            email=values[2].strip()
        else:
            email=''

        writer.writerow([id,name, email,checkoutDate, Deadline])
        return id, name, email
    else:
        return None

def open_scanner():
    with open ('Scanned_data_EMPLOYEE.csv',mode='a', newline='') as file:
        writer=csv.writer(file)

        writer.writerow(['Scanned EID','Scanned EName','Scanned Email',' ECheck Out', 'EDeadline'])
        cap = cv2.VideoCapture(0)


        while True:
            ret,frame=cap.read()
        

            cv2.imshow("QR Code Scanner",frame)

            if cv2.waitKey(1) ==ord("q"):
                break

            data=decode_qr(frame,writer)
            if data is not None:
                id, name, email = data
                print('QRCode', id, name, email)
    cap.release()
    cv2.destroyAllWindows()

def clean_data():
    input_file='Scanned_data_EMPLOYEE.csv'
    output_file='Employee_Clean_ScannedData.csv'

    with open(input_file,'r') as infile:
        reader= csv.reader(infile)
        data= list(reader)

    data_cleaned=[data[0]]
    for row in data[1:]:
        if row not in data_cleaned and row[0].strip() !="":
            data_cleaned.append(row)

    
    with open(output_file,'w', newline='') as outfile:
        writer= csv.writer(outfile)
        for row in data_cleaned:
            if len(row)==5:
                writer.writerow(row)


def nextcommand():
    subprocess.Popen(["python","Toolscanner.py"])


def nextcommand2():
    clean_data()
    nextcommand()

root = tk.Tk()
root.title("Check-out ")

image=tk.PhotoImage(file="image.png")
canvas=tk.Canvas(root,width=image.width(), height=image.height())
canvas.place(x=0,y=0)

canvas.create_image(0,0,image=image, anchor="nw")

button1=tk.Button(root,text="Scan Employee QR", command= open_scanner)
button1.place(x=200,y=200)

button2=tk.Button(root,text="Next", command=nextcommand2)
button2.place(x=300,y=300)




button1.grid(row=2 ,column=1,padx=150, pady=10,sticky="nsew")
button2.grid(row=3 ,column=1,padx=150, pady=10,sticky="nsew")



button1.grid_anchor("center")
button2.grid_anchor("center")

root.mainloop()
