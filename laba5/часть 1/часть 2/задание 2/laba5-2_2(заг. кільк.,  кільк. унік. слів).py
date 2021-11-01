import os

fn = "Stranger.txt"
file = open(fn)
sentences = 0
loudsentences = 0
questions = 0
longsentences = 0
for i in file:
            i = i[0:-1]
            for j in i: 
                if j== '.'  or j== '!' or j== '!':
                    sentences+= 1
            for k in i:
                if k=='!':
                    loudsentences+= 1
            for l in i:
                if l=='?':
                    questions+= 1
            for a in i:
                if a=='...':
                    longsentences+= 1
print("sentences:", sentences, "loudsentences:", loudsentences, "questions:", questions, "longsentences:", longsentences)
