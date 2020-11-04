# program using check fruit inventory

fruits = {"orange": 5, "apple": 3, "mango": 1, "grape":2, "banana": 1}

while(True):
    fruitpurchase = str(input("Fruits: \n"))
    #fruits[fruitpurchase] -= 1
    if fruitpurchase == "quit":
        break
    elif fruits[fruitpurchase] == 0:
        print("We've ran out of: " + str(fruitpurchase))
    else:
        fruits[fruitpurchase] -= 1
    print(fruits)