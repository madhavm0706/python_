import array

a = array.array('i',[1,2,3,4,5,6,7])

b = input("enter a no ")

for i in range(len(a)):
    if (i+b < len(a)):

        print(a[i+b]),