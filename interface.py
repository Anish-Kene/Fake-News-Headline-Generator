#1- Import the radom module
import random

#2- Create Subjects
subjects= [
    "Shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbaim Cat",
    "Prime Minister Modi",
    "Auto Rickshaw Driver From Delhi"
]

actions = [
    "Launches",
    "Cancles",
    "dance with",
    "declears war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local train",
    "a plate of Saamosa",
    "Inside parliament",
    "at ganga ghat",
    "During IPL Match",
    "At India Gate"
]

#3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    Headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n" + Headline)

    user_input = input("\nDo you want another headline ? (yes/no)").strip().lower
    if user_input == "no":
        break
    

#print goodbye message
    print("\n Thanks for using the Fake News Headline Generator. Have a fun day")
    
