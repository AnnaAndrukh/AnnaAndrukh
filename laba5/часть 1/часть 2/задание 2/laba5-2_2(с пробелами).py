import os

fn = "Stranger.txt"
file = open(fn, 'r')
symvols = 0
for line in file:
    line = line.strip(os.linesep)
    wordslist = line.split()
    symvols = symvols + len(wordslist)
print("Symvols:", symvols)
