import math
import csv

with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)

data=fileData[0]

def mean(data):
    n=len(data)
    sum=0

    for x in data:
      sum+=int(x)

    mean=sum/n
    return mean

squaredList=[]

for number in data:
    a=int(number)-mean(data)
    a=a**2
    squaredList.append(a)

grandSum=0

for i in squaredList:
    grandSum+=i

result=grandSum/(len(data)-1)

strdDeviation=math.sqrt(result)
print("standard deviation= "+str(strdDeviation))
