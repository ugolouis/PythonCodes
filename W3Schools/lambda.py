
# lambda
# anonymous function
# can take multiple arguments but can only have one expression
# lambda arguments: expression

x = lambda a: (a + 10)

print(x(10))

b = lambda a, b, c: a * b * c

#print (b(10, 2, 5))

z = 100

def myfunc(n):
    return lambda z: z * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Regex 
# Sequence of characters that form a search pattern
#

import re

txt = "This is spain in Europe"

x = re.search("^This.*spain*", txt) # search the first letter "This" and last letter "spain"

if x:
    print("Yes! We have a match")
else:
    print("No match")

y = re.findall("eu", txt)
print(y)

