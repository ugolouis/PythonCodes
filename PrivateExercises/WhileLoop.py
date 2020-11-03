# while loop

"""
# while statement is below
while (condition):
    action1
    actiom2
    action3
"""
i = 0
while ( i < 10):
    #print(i)
    i += 1

destination= 5000
startheight = 0
velocity = 50
time = 0

while (destination > startheight):
    destination = destination -  velocity
    time += 1

print(time)


