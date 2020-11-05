
# Favourites song description list in a dictionary songDesc

songDesc = {"Artist": "Rihana", "Postion In Chart": 1, "Release Date": 2011, "Gendre":"Pop", "Supporting Artisit":"Calvin Harris",\
            "Album":"Talk that Talk", "Grammy Award Win Category": "2013 Grammy Award for Best Music Video", "Producer": "Calvin Harris", \
            "Song Video Director": "Malina Matsoukas"}

#refactored print statement that prints keys and values in the dictionary songDesc
for keys, values in songDesc.items():
    print(keys + ": " + str(values))


def songFunction(a, b):
    for i in songDesc:
        if a == i:
            if songDesc[a] == b:
                print("Both key and value are Correct")
                break
            else:
                print("Your value is wrong")
        else:
            continue

# Testing the function
songFunction("Gendre", "Pop")
