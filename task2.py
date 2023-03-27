# Rebekah Gardner-Assignment 5-Task 2-Period 3
#Introduction
print("Welcome to the Social Situation Analyzer System")

#First person's info
print("Person One")
name1 = input("    Enter your name: ")
x1 = int(input("    Enter your x position: "))
y1 = int(input("    Enter your y position: "))
radius1 = int(input("    Enter your personal space radius: "))
print()

#Second person's info
print("Person Two")
name2 = input("     Enter your name: ")
x2 = int(input("     Enter your x position: "))
y2 = int(input("     Enter your y position: "))
radius2 = int(input("     Enter your personal space radius: "))
print()

#Distance formula
distance = 0
distance = distance**((x2 - x1)**2 + (y2 - y1)**2)

#Variables
space = radius1 + radius2
r1 = distance + radius1
r2 = distance + radius2

#If Statements
if distance > space:
    msg = "Social Situation Analysis Results \n     Person Test: Neither " + name1 + " or " + name2 + " are in each other's personal space\n     Space Test: " + name1 + " and " + name2 + "'s personal spaces do not overlap"
elif distance == space:
    msg = "Social Situation Analysis Results \n     Person Test: Neither " + name1 + " or " + name2 + " are in each other's personal space\n     Space Test: " + name1 + " and " + name2 + "'s personal spaces are touching"
elif distance < space:
    msg = "Social Situation Analysis Results \n     Person Test: Neither " + name1 + " or " + name2 + " are in each other's personal space\n     Space Test: " + name1 + " and " + name2 + "'s personal spaces overlap"
elif distance < radius1:
    msg = "Social Situation Analysis Results \n     Person Test: " + name2 + " is inside of " + name1 + "'s personal space\n     Space Test: " + name2 + " and " + name1 + "'s personal space's overlap"
if distance < radius2:
    msg = "Social Situation Analysis Results \n     Person Test: " + name1 + " is inside of " + name2 + "'s personal space\n     Space Test: " + name2 + " and " + name1 + "'s personal space's overlap"
elif r1 < radius2:
    msg = "Social Situation Analysis Results \n     Person Test: " + name1 + " and " + name2 + " are in each other's personal space\n     Space Test: " + name1 + " is entirely inside " + name2 + "'s personal space"
elif r2 < radius1:
    msg = "Social Situation Analysis Results \n     Person Test: " + name1 + " and " + name2 + " are in each other's personal space\n     Space Test: " + name2 + " is entirely inside " + name1 + "'s personal space"

#Conclusion
print(msg)
