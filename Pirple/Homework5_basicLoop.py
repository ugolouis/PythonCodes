# Homework Assignment#5: Basic Loops

countFizz = []
countBuzz = []
countFizzBuzz = []
countPrime = []

for i in range(1,101): # limit 101 so we can include 100
    if i%3 == 0:
        print("Fizz")
        countFizz.append(i) # append to a list so we can count elements therein
        if i%5 ==0:
            print("FizzBuzz")
            countFizzBuzz.append(i) # append to a list so we can count elements therein
    elif i%5 == 0:
        print("Buzz")
        countBuzz.append(i) # append to a list so we can count elements therein


# extra marks
# check for prime (divisble only by itself and 1; that is not a multple of any number)

for prime in range(1, 101):
    if prime > 2: # 2 is the even prime number
        for i in range(2, prime):
            if prime%i == 0:
                break
        else:
            print(prime,": prime number")
            countPrime.append(prime) # append to a list so we can count elements therein

# Print out the count of members in the list 
print(len(countFizz))
print(len(countBuzz))
print(len(countFizzBuzz))
print(len(countPrime))

