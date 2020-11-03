
"""

myList = []
a_exists = []
b_exists = []

for i in range(1, 6):
    myList.append(i)
print("initial list: " + str(myList))

for x in range(1, 10, 2):
    b_exist = [b_exists.append(x) if x in myList else myList.append(x)]

print("myList after population: " + str(myList))
print("b_exists after population: " + str(b_exists))

"""

odd_list = []
even_list = []
count_even = 0
count_odd = 0
for i in range(1, 30):
    if i%2 == 0:
        even_list.append(i)
        count_even = count_even + 1
    else:
        odd_list.append(i)
        count_odd = count_odd + 1

print("These are even numbers: " + str(even_list))
print("These are odd numbers: " + str(odd_list))
print(str(count_even))
print(str(count_odd))


