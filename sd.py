import math
import csv
with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
# find mean


def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + int(x)
    mean = total/n
    return mean


# squareing the values
squrelist = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squrelist.append(a)

# geting sum
sum = 0
for i in squrelist:
    sum = sum+i

# divide sum by n-1
result = sum/(len(data)-1)

# squreroot
sd = math.sqrt(result)
print(sd)