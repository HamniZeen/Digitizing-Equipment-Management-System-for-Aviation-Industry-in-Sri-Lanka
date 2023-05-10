import csv
import datetime

current_date = datetime.date.today()

with open('Tool_Clean_ScannedData.csv', 'r') as file1, open('tools.csv', 'r') as file2:
    reader1 = csv.DictReader(file1)
    reader2 = csv.DictReader(file2)
    rows2 = [row2 for row2 in reader2]  # Read all rows from file2 into memory
    
    for row1 in reader1:
        id1 = row1['TScanned ID']
        deadline1 = datetime.datetime.strptime(row1['TDeadline'], '%Y-%m-%d').date()  # Parse deadline as date
        
        for row2 in rows2:
            if row2['ID'] == id1:
                if deadline1 > current_date:
                    row2['Status'] = 'Not Available'
                break  # Stop looking for matching rows in file2 once we've updated the status

with open('tools.csv', 'w', newline='') as file2:
    writer = csv.DictWriter(file2, fieldnames=reader2.fieldnames)
    writer.writeheader()
    writer.writerows(rows2)  # Write updated rows back to file2
