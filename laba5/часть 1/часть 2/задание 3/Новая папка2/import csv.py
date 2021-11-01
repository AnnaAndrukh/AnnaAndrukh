import csv
import sys
filename = "Stranger2.txt"
text_file=open("Stranger2.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print(str)
text_file.close()

filename2 = "In the restaurant.txt"
text_file=open("In the restaurant.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print(str)
text_file.close()