# Create Tic-tac-Toe 
# Create a draw input filed

# tick -tac-toc field

def drawfield(field):
    for row in range(5):
        if row%2 ==0:
            practicalrow = int(row / 2)
            # print  " | | "
            for column in range(5):#0, 1, 2, 3, 4
                practicalcolumn = int(column / 2)                 #0, ., 1, ., 2
                if column % 2 == 0:
                    if column != 4:
                        print(field[practicalcolumn][practicalrow], end = "")
                    else:
                        print(field[practicalcolumn][practicalrow])
                else:
                    print("|", end = "")
        else:
            print("-------")

# Create the input lines
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
Player = 1
drawfield(currentField)
while (True):
    print("current player is: ", Player)
    moveRow = int(input("Please enter the row value: "))
    moveColumn = int(input("Please enter the column value: "))
    if Player == 1:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "X"
            Player = 2
    else:
        if currentField[moveColumn][moveRow] ==" ":
           currentField[moveColumn][moveRow] = "O"
           Player = 1
    drawfield(currentField)

