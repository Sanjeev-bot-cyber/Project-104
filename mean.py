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

for y in newData :
    sum = sum+y

mean = sum/l
print(mean)