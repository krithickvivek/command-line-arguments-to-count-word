import sys
count=0
with open(sys.argv[1],"r") as f1:
    for line in f1:
        word=line.split()
        count+=len(word)
print("Word count in file is:",count)



