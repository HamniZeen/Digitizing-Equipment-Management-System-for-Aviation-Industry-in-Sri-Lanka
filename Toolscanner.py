import cv2
import tkinter as tk
import qrcode
import numpy as np
import csv
import datetime
import subprocess
from PIL import Image, ImageTk

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
root.geometry("1350x900")

# Load and resize the image
image = Image.open("plane.jpg")
image = image.resize((1350, 900), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=1350, height=900)
canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.place(relx=0.5, rely=0.5, anchor="center")

button_width = 50
button_height = 3
button_font = ("TkDefaultFont", 13, "bold")

button1 = tk.Button(root, text="Scan Tool QR", command=open_scanner, width=button_width, height=button_height, font=button_font)
button1.place(relx=0.5, rely=0.4, anchor="center")
button2 = tk.Button(root, text="Submit", command=submitcommand, width=button_width, height=button_height, font=button_font)
button2.place(relx=0.5, rely=0.5, anchor="center")
button3 = tk.Button(root, text="Exit", command=exitt, width=button_width, height=button_height, font=button_font)
button3.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
