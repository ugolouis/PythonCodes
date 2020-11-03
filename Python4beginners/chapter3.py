firstname = ["Johnny", "George", "Rowan", "Ford", "Roberta"]
lastName = ["Masaki", "Laurie", "Bean", "Harrison", "Meyers"]
age = ["25", "25", "67", "53", "36"]
gender = ["Male", "Male","Female","Male", "Female"]
position = ["Security", "Messenger", "Receptionist", "Manager", "Chief Financial Officer"]
location = ["Cleveland, Ohio", "San Francisco, California", "London, UK", "New York, New York", "Prenceton, New Jersey"]

employees = {}
for i in range(1, 6):
    employees["employee" + str(i)] = {
        "firstName": firstname[i -1],
        "lastName": lastName[i -1],
        "age": age[i - 1],
        "gender": gender[i -1],
        "position": position[i -1],
        "location": location[i - 1]
    }

for i in range (1, 6):
    x = "employee" + str(i)
   # print(x + ":"  )
    print(
           x + ":" + 
           employees[x] ["firstName"] + "," +
           employees[x] ["lastName"] + "," + 
           employees[x] ["age"] + "," +
           employees[x] ["gender"] + "," +
           employees[x] ["position"] + "," + 
           employees[x] ["location"] 
        )
