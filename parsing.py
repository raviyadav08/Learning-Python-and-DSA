import csv
import os
os.chdir('C:/Users/iamsu/Desktop/Demo/Files')

with open('names.csv','r') as name_file:
    csv_reader = csv.DictReader(name_file)
    
    with open('edited_names.csv','w') as edited_file:
        fieldnames = ['first_name','last_name']
        csv_writer = csv.DictWriter(edited_file,fieldnames=fieldnames,delimiter='\t')
        csv_writer.writeheader()

        for lines in csv_reader:
            del lines['email']
            csv_writer.writerow(lines)
            

