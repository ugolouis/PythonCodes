
#Homework Assignment 6: Advanced Loop

max_width_size = 37 # maximum width size of screen
max_height_size = 26 # max height of screen

def playBoard(row, column):
    for i in range(row):
        if row > max_width_size or column > max_height_size: # added to check the max width and height
            print("check that you have not exceeded the max row or columns size") # print when the max of either height or wide is exceeded
            return False  
            break 
        elif i % 2 == 0:
            for c in range(column):
                if c % 2 == 0:
                    if c != column -1:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print ("|", end="")
        else:
            print("-----")
    return  True

# print result using values row = 5, column = 5
print(playBoard(5, 5))

# Extra marks testing the values exceeding the max_width_size or max_height_size
#print(playBoard(51, 5))
#print(playBoard(5, 49))

