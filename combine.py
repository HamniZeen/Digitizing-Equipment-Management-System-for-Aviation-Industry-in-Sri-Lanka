import csv

# open the two CSV files to be merged
with open('Employee_Clean_ScannedData.csv', 'r') as file1, open('Tool_Clean_ScannedData.csv', 'r') as file2:

    # create a reader object for each file
    reader1 = csv.reader(file1)
    reader2 = csv.reader(file2)

    # create a new CSV file for the merged data
    with open('merged_file.csv', 'w', newline='') as merged_file:

        # create a writer object for the new file with 9 columns
        writer = csv.writer(merged_file, delimiter=',')

        # loop through the rows of both files simultaneously and write them to the new file with 9 columns
        for row1, row2 in zip(reader1, reader2):
            writer.writerow(row1 + row2)
