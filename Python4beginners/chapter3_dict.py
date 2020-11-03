emp1 = {"firstName": "Johnny", "lastName": "Masaki", "age": "25", "gender": "Male", "position": "Security", "location": "Cleveland, Ohio"}
emp2 = {"firstName": "George", "lastName": "Laurie", "age": "36", "gender": "Female", "position": "Messenger", "location": "San Francisco, California"}
employees = {
    "employee1": emp1,
    "employee2": emp2
}

#print(employees["employee1"]["firstName"])
#print(employees)
#print(emp1)

for i in range(1, 3):
    x = "employee" + str(i)
    print(
    x + ":" +
    employees[x]["firstName"] + "," + 
    employees[x]["lastName"] + "," + 
    employees[x]["age"] + "," + 
    employees[x]["gender"] + "," + 
    employees[x]["position"] + "," + 
    employees[x]["location"] 
    )
    #print("employees[" + x + "]" + "[" + "firstName]")

