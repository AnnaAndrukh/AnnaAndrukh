import csv
import sys
filename = "Stranger.txt"
text_file=open("Stranger.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print(str)
text_file.close()