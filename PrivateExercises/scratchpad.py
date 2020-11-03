for row in range(7):
    if row % 2 == 0:
        for column in range(1, 8):
            if column % 2 == 1:
                if column != 5:
                    print(" ", end="")
                else:
                    print(" ")
            else:
                print ("|", end ="")
    else:
        print("-----")