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
        checkinDate = datetime.date.today().strftime('%Y-%m-%d')
        
        values = data.split(',')
        if len(values) >=1:
            id=values[0].strip()
        else:
            id=''
        if len(values) >=2:
            name=values[1].strip()
        else:
            name=''
        

        writer.writerow([id,name, checkinDate])
        return id, name, 
    else:
        return None

def open_scanner():
    with open ('CheckedIn_data_TOOL.csv',mode='a', newline='') as file:
        writer=csv.writer(file)

        writer.writerow(['TScanned ID','TScanned Name','TCheck In'])
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
    input_file='CheckedIn_data_TOOL.csv'
    output_file='CheckedInTool_Clean_ScannedData.csv'

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
            if len(row)==3:
                writer.writerow(row)

def statuschangedcommand():
    
    with open('CheckedInTool_Clean_ScannedData.csv', 'r') as file1, open('tools.csv', 'r') as file2:
        reader1 = csv.DictReader(file1)
        reader2 = csv.DictReader(file2)
        rows2 = [row2 for row2 in reader2]  # Read all rows from file2 into memory
        
        for row1 in reader1:
            id1 = row1['TScanned ID']
            
            for row2 in rows2:
                if row2['ID'] == id1:
                    row2['Status'] = 'Available'   
                    break  
               

    with open('tools.csv', 'w', newline='') as file2:
        writer = csv.DictWriter(file2, fieldnames=reader2.fieldnames)
        writer.writeheader()
        writer.writerows(rows2)  # Write updated rows back to file2


def submitcommand():
    clean_data()
    statuschangedcommand()

root = tk.Tk()
root.title("Check-In ")
root.geometry("1350x900")

image = Image.open("plane.jpg")
image = image.resize((1350, 900), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=1350, height=900)
canvas.place(relx=0.5, rely=0.5, anchor="center")

canvas.create_image(0, 0, anchor="nw", image=photo)
button_width = 50
button_height = 3
button_font = ("TkDefaultFont", 13, "bold")


button1 = tk.Button(root, text="Scan Tool QR", command=open_scanner, width=button_width, height=button_height, font=button_font)
button1.place(relx=0.5, rely=0.45, anchor="center")

button2 = tk.Button(root, text="Submit", command=submitcommand, width=button_width, height=button_height, font=button_font)
button2.place(relx=0.5, rely=0.6, anchor="center")


root.mainloop()
