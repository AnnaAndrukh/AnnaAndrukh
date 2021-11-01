import os

fn = "In the restaurant.txt"
file1 = open(fn)

fn2 = "Stranger2.txt"
file2 = open(fn2)

repeatingsentences = 0

words1=file1.readlines()
words2=file2.readlines()


for word1 in words1:
    for word2 in words2:
      if word1==word2:
          repeatingsentences+= 1
          print("repeatingsentences:", repeatingsentences)
        
file1.close()
file2.close()


