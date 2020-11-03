

myList = []
#a_exists = []
b_exists = []

for i in range(1, 6):
    myList.append(i)
print("initial list: " + str(myList))

for x in range(1, 10, 2):
    b_exist = [b_exists.append(x) if x in myList else myList.append(x)]

print("myList after population: " + str(myList))
print("b_exists after population: " + str(b_exists))



