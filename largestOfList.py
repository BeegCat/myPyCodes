largest=None
print("before", largest)
for i in [2,460,62,300,47,0,19]:
    if largest is None or i>largest:
        largest=i
    print("loop: ", i, largest)
print("largest= ", largest)