list=[]

while True:
    num=int(input("enter a number to add to list"))
    list.append(num)
    go=input("continue adding? y or n:\n")
    if go == "n":
        break

sum=0
for num in list:
    sum=sum+num

mean=sum/len(list)
print(list)
print(mean)

