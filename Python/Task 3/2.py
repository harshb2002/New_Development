l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(l1)
print("Even numbers in list is : ")
for i in l1:
    if i % 2 != 0:
        l1.remove(i)
print(l1)