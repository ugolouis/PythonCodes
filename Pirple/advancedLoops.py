# Homework Assignment #6: Advanced Loopsdd

def gameBoard(rows, columns):
    for r in range (rows):
        if r % 2 == 0:
            for c in range(columns):
                if c % 2 == 0:
                    if c != columns-1:
                        print(" ", end = "")
                    else:
                        print(" ")
                else:
                    print ("|", end="")
        else:
            print("----")
    return  True 

gameBoard(5, 5)