import csv
import advanced_python_regex as apr

emails = open("emails.csv", "wb")
open_file_object = csv.writer(emails)
for i in apr.df['email'].tolist():
    open_file_object.writerow([i])
emails.close()
