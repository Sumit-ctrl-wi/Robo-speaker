import pyttsx3

ramphal=pyttsx3.init()
ramphal.say('hey i am ramphal that will speak to you now ')
while(True):
    x=input("enter what you want to speak:")
    if x=="stop":
        break
    ramphal.say(x)
    ramphal.runAndWait()
