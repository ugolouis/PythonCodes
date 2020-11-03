
participants = ["Joe", "Alex", "Tina", "James", "Paul"]


position = 0
for name in participants:
    if name == "Tina":
        #print(name)
        break
    position += 1
 

#print(position)
        

currentIndex = 0
for currentIndex in range(len(participants)):
    if currentIndex == 3:
        break
    currentIndex += 1

print(participants[currentIndex])


