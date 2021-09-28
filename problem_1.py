
to_be_added = []

for i in range(1,1000,1):
    if ((i % 3 == 0) and (i % 5 != 0)):
        to_be_added.append(i)
    elif ((i % 5 == 0) and (i % 3 != 0)):
        to_be_added.append(i)
    elif ((i % 5 == 0) and (i % 3 == 0)):
        to_be_added.append(i)
    else:
        None


print(to_be_added)

print(sum(to_be_added))
