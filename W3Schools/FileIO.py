# file handling

# Step 1

# f = open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData1.txt", "r")

#print(f.read())

#print("-------------\n")

#print(f.read(5))

# read 2 lines
#print(f.readline())
#print(f.readline())

# for x in f:
#     print(x)
# f.close()

# Step 2
# open file in append mode
# f = open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData1.txt", "a")
# f.write("\nWe will teach python programming")
# f.close()

# # open and read the file after appending
# f = open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData1.txt", "r")
# print(f.read())
# f.close()

# step 3
# create a new file

# f = open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData3.txt", "a")
# f.write("\n3rd line added")
# f.close()

# f= open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData3.txt", "r")
# print(f.read())
# f.close()

# step 4
# delete file

# import os

# os.remove("C:\\Users\LOzougwu\Desktop\W3Schools\TestData3.txt") # remove file without checking

# # check if file exist before removing
# if os.path.exists("C:\\Users\LOzougwu\Desktop\W3Schools\TestData3.txt"):
#     print("File exist")
#     os.remove("C:\\Users\LOzougwu\Desktop\W3Schools\TestData3.txt")
# else:
#     print("File does not exist")


# # remove folder

# import os

# os.rmdir("C:\\Users\LOzougwu\Desktop\W3Schools")

# Step 5
# append contents of one file into another file

# appendFile = open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData2.txt", "r")
# myvar = appendFile.read()
# #print(myvar)

# File = open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData1.txt", "a")
# File.write("\n" + myvar )
# File.close()

# File = open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData1.txt")
# #print(File.read())

# # You can also print value of File above line by line using loop
# for line in File:
#     print(line, end="")


# Step 6
# Using the with keyword

with open("C:\\Users\LOzougwu\Desktop\W3Schools\TestData1.txt", "r") as text3File:
    for line in text3File:
        print(line, end="")

