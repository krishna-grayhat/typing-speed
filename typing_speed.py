from time import *
import random as r
import pyfiglet


def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error +1
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)

test =["As the popular Veermata Jijabai Bhosale (VJB) Udyan and Zoo","commonly known as Rani Bagh and Byculla zoo", "clocks 160 years on November 19", "the authorities announced the birth of three new .."]

text = pyfiglet.figlet_format("Typing-Speed")
test1 = r.choice(test)

print(text)
print(test1)
print()
print()
time1 = time()
testinput = input(" Enter : ")
time2 = time()
print('speed : ', speed_time(time1,time2,testinput), "w/sec")
print('Error : ', mistake(test1,testinput))