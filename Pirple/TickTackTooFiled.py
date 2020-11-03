# use nested loop to create tik tick too field
# end product 
# | |
# ---
# | |
# ----
# | |
def gameBoard(rows, columns):
    for r in range (rows):
        if r % 2 == 0:
            for c in range(columns):
                if c % 2 == 0:
                    if c != 4:
                        print(" ", end = "")
                    else:
                        print(" ")
                else:
                    print ("|", end="")
        else:
            print("----")
        #return True
    return  True 

gameBoard(5, 5)