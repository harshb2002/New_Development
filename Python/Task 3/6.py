s1 = {"harsh","rutul","kamiyab","harsh","jay"}
s2 = {"diya","jay","parva","jay","harsh"}

print (s1, s2)

#add method
print("\nAdd method")
s1.add("123")
s2.add("123")
print(s1)
print(s2)

#difference method
print("\nDifference method")
s3 = s1.difference(s2)
print (s3)
s3 = s2.difference(s1)
print (s3)

# difference_update method
print("\nDifference update method")
s1.difference_update(s2)
print (s1)

s2.difference_update(s1)
print (s2)

# discard method
print("\nDiscard method")
s1.discard("rutul")
print(s1)
s2.discard("jay")
print(s2)


#interaction method
print("\nIntersection Method")
s4 = s1.intersection(s2)
print(s4)

#interaction_update method
print("\nInteraction update method")
s1.intersection_update(s2)
print(s1)

#disjoint method
print("\nDisjoint Method")
s5 = s1.isdisjoint(s2)
print(s5)

# subset method
print("\nSubset Method")
s6 = s1.issubset(s2)
print(s6)

#superset method
print("\nSuperset Method")
s7 = s1.issuperset(s2)
print(s7)

#pop method
print("\nPop Method")
s2.pop()
print(s2)

#remove method

print("\nRemove Method")
s2.remove("diya")
print(s2)

#symmetric method
print("\nSymmetric Method")
s8 = s1.symmetric_difference(s2)
print(s8)

#symmetric_difference_update method
print("\nSymmetric difference update method")
s2.symmetric_difference_update(s1)
print(s2)

#union method
print("\n Union Method")
s10 = s1.union(s2)
print(s10)

#update method
print("\nUpdate Method")
s2.update(s1)
print(s1)

