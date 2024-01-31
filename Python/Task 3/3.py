l1 = [1,2,3,4,5,6,7,8]
l2 = [4,5,6,7,8,9,10]

common = []

for i in l1:
    if i in l2:
        common.append(i)
print(common)