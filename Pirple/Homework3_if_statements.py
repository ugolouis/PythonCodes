"""
Assignment on IF statement

"""

def checkEquality(a, b, c):
    if a == b and a == c:
        print(True)
    elif b == c and b == a:
        print(True)
    else:
        print(False)
    return

checkEquality(6, 5, int("5"))
