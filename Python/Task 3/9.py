dict1 = {
    "Name" : "Harsh",
    "Environment" : "111122223333"
}

dict2 = {
    "department" : "computer",
    "age" : 21
}


merge = dict1.copy()

merge.update(dict2)
print(merge)