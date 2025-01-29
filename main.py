from time import *
import random as r


def mistake(partest, user):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != user[i]:
                error += 1
        except:
            error += 1
    return error


def speed_time(start, end, userinput):
    total_time = end - start
    time_round = round(total_time, 2)
    speed = len(userinput) / time_round
    return round(speed, 2)


test = [
    "Python is a programming language", "He will get his money worth.",
    "He is a great kid.",
]

test1 = r.choice(test)
print("Typing speed calculator ")
print(test1)
print()
print()
time_1 = time()
test_input = input("Enter :")

time_2 = time()

print("Speed: ",speed_time(time_1, time_2, test_input), "WPM")

print("Errors: ", mistake(test1.split(), test_input.split()))