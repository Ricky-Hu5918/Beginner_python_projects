'''how to put strings together'''
# # a few ways to do this
# youtuber = "Kylie Ying"
#
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

# #madlib version 1
# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")
#
# madlib1 = f"Computer programming is so {adj}! it makes me so excited all the time because I love {verb1}. \
# Stay hydrated and {verb2} like you are {famous_person}"
#
# print(madlib1)

#madlib version 2
name = input("Your name: ")
country = input("Country: ")
number1 = input("A number: ")
activity = input("An activity: ")
number2 = input("A number: ")
adj1 = input("Adjective: ")

madlib2 = f"My name is {name}, and I came to {country} for {number1} years. My favorite hobby is {activity}. \
I've been a big fan of {activity} for {number2} years. Doing {activity} is {adj1}. I would highly recommend you to do {activity}."

print(madlib2)

# #using format to output
# noun = 'Python'
# adj = 'beautiful'
# name = 'Kylie'
# word = "I want to learn {} because it is {}. So I subcribe the channel of {}."
# print(word.format(noun, adj, name))

madlib3 = "My name is {name}, and I came to {country} for {number1} years. My favorite hobby is {activity}. \
I've been a big fan of {activity} for {number2} years. Doing {activity} is {adj1}. I would highly recommend you to do {activity}."\
    .format(name=name, country=country, number1=number1, activity=activity, number2=number2, adj1=adj1)

print(madlib3)