import os

fn = "Stranger.txt"
file = open(fn, 'r')
symvols = 0
with open("Stranger.txt") as file:
    for line in file:
        wordslist = line.split()
        wordslist2=str(wordslist)
        wordslist2.replace(' ', '')
        wordslist3=list(wordslist2)
        symvols = symvols + len(wordslist3)
print("Symvols without space:", symvols)