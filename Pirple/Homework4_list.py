#
# Homework 4: list
#

# define initial list and assign nothing
myUniqueList= []

# create function to append item
def addItems(phrase):
    if phrase in myUniqueList:
        return False
    else:
        myUniqueList.append(phrase)
    return True

# code to test the function
# populate myUniqueList with number 1 to 5
for i in range(1, 6):
    myUniqueList.append(i)
print("Before function test: " + str(myUniqueList))

# add 1 but because 1 is already in the list it doesn't add it to the list
addItems(1)
print("After function non unique test: " + str(myUniqueList))

# test add a number that is not in the list; 7 is added because it is not in the list
addItems(7)
print("After function unique test: " + str(myUniqueList))

# Extra Credit
# function to take rejected items
myLeftOvers = []
def rejectedItems(phrase):
    if phrase in myUniqueList:
        myLeftOvers.append(phrase)
    else:
        myUniqueList.append(phrase)
    return True

# testing new function
rejectedItems(1)
print(myLeftOvers)