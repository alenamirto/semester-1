# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

# creating list
numberlist=read_numbers()
if numberlist == []:
    sys.exit("Error: no numbers provided")

# sorting list
sortedlist=sorted(numberlist)
listlength=len(sortedlist)

# min and max
minimum=sortedlist[0]
maximum=sortedlist[listlength-1]

# mean
sum=float(0)
for number in numberlist:
    sum=sum+number
mean=sum/listlength

# median 
median=float(0)
median_position=int(0)
if listlength%2 !=0: # if odd
    median_position=int((listlength+1)/2)-1
    median=sortedlist[median_position]
else: # if even
    median_position=int(listlength/2)
    median+=(sortedlist[median_position-1]+sortedlist[median_position])
    median=median/2

# outputting values
print(f"""
Minimum = {minimum}
Maximum = {maximum}
Mean = {mean}
Median = {median}
""")

