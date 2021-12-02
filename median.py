import csv
with open("Height-Weight.csv", newline='') as f:
    r = csv.reader(f)
    fd = list(r)

fd.pop(0)
newData = []
for x in range(len(fd)):
    n = fd[x][1]
    newData.append(float(n))

l = len(newData)
sum = 0 

newData.sort()

if l%2 == 0:
    m1 = float(newData[l//2])
    m2 = float(newData[(l//2)+1])
    median = (m1+m2)/2
else:
    median = newData[l//2]

print(median)