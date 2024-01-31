tuple1 = (1,2,3,4,5)
tuple2 = (4,5,6,7)

l1 = list(tuple1)
l2 = list(tuple2)

for i in range(len(l2)):
    if l2[i] not in l1:
        l1.append(l2[i])

tuple3 = tuple(l1)

print(tuple3)