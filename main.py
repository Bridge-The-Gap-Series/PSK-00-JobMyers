import statistics
name=input("Enter your name: ")
age=int(input("Enter your age(20+): "))
print("\n\n")
print("Hello world\n")
print("my name is",name)
print("I am ",age," years of age.Young, right?\U0001F600\n")
numlist=[]
numlist.append(12)
numlist.append(4)
numlist.append(56)
numlist.append(17)
numlist.append(8)
numlist.append(99)
x=max(numlist)
print("The maximum number in this list:",numlist,"is",x)
y=statistics.mean(numlist)
print("The mean:",numlist,"is",y,"\n")
allist=["A for Apple","B for Boy","C for Cow","...","Z for Zebra"]
print(*allist, sep = "\n")
