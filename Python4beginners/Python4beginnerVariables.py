# Chapter2

# execises1
v_targetNumber = 10025
v_a= 7
v_b = 10025 / 7
v_c = round(7 * v_b)
print (v_c)

v_e = v_targetNumber * 7
v_f = round(v_e / 7)
print(v_f)

v_g = (7 - 2) * 2005
print (v_g)

v_i = v_targetNumber - 7
v_j = 7 + v_i
print(v_j)

### number 2
var_a = (18 + 21 + 19 + 52 + 6 + 33 + 15 + 46 + 72 + 25 ) / 10

print ( var_a)

# numner 3 

y = 10
c = 7
a = 10 - 151
b = 7 * (144 + 10)
x = y + (a * b / c)

print("x is: " + str(x))

# number 4
feb_days = 365 - (31 + 14)
datediff = ((2000 - 1968) * 365.25) + feb_days
#ageJonny = feb_days + datediff
print ( "--------- Question 4 answer ----------------")
print(datediff)

""" 
--- excercise 5
--- Question on car speed
"""

# defining variables
totaltime = 60 
time1 = 5
time2 = 1
speed1 = 20
deceleration = 5
speed2 = speed1 - deceleration
# calculations
duration1 = (totaltime / (time1 + time2)) * time1
# print("duration1 is: " + str(duration1))
duration2 = (totaltime / (time1 + time2)) * time2
#print("duration2 is: " + str(duration2))
distance1 = (speed1 / totaltime) * duration1
distance2 = (speed2 / totaltime) * duration2
totalDistance = distance1 + distance2
# print results
print ("------ Question 5 answer  --------------------")
print("total distance: " + str(totalDistance))


