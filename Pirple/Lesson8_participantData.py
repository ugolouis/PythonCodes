""" 
Program about participant data
  - writes participant details into a file

Created by Louis

"""

# define variables we need

registredparticipants = []
outputFile = open("C:\\Users\LOzougwu\Desktop\W3Schools\participants.txt", "w")
maxParticipants = 2
incrementmentParticipants = 0

while(incrementmentParticipants < maxParticipants):
    participantData =  []
    name = input("Please enter your name: ")
    country = input("Please enter name of country: ")
    age = input("Please enter your age: ")
    participantData.append(name)
    participantData.append(country)
    participantData.append(str(age))

    registredparticipants.append(participantData)
    print(participantData)

    incrementmentParticipants += 1
    print(registredparticipants)

for participant in registredparticipants:

    for data in participant:
        outputFile.write(data)
        outputFile.write(" ")
    outputFile.write("\n")
    
    
outputFile.close()

