### BAD THERAPIST
### HB Project 5 June 2018 - 5 July 2018
### 
### Sometimes therapy works, sometimes it doesn't.  You be the judge
""" * This is part game/part therapy inspired by humor that uses everything learned in Prep"""

import random

therapists = ["Brighticorn", "Unikitty", "Pikachu", "Shawn Mendes"]

# shawn_dict = {"sad": "happy good vibes",
# 			  "happy": "so happy, so very happy for you",
# 			  "angry": "girl, you need to chill out",
# 			  "nervous": "breathe, baby, breathe"}

# pikachu_dict = {"sad": "happy good vibes",
# 			  "happy": "so happy, so very happy for you",
# 			  "angry": "girl, you need to chill out",
# 			  "nervous": "breathe, baby, breathe"}

# unikitty_dict = {"sad": "happy good vibes",
# 			  "happy": "Everything is AWESOME!",
# 			  "angry": "girl, you need to chill out",
# 			  "nervous": "breathe, baby, breathe"}

# brighticorn_dict = {"sad": "happy good vibes",
# 			  "happy": "so happy, so very happy for you",
# 			  "angry": "girl, you need to chill out",
# 			  "nervous": "breathe, baby, breathe"}

unlisted_emotions = {}

on_call = random.choice(therapists)

all_the_dicts = [shawn_dict, pikachu_dict, unikitty_dict, brighticorn_dict]

def use_dict(on_call):
    # use corres. dict depending on on_call
    if on_call == "Shawn Mendes":
        dict = shawn_dict
    elif on_call == "Pikachu":
        dict = pikachu_dict
    elif on_call == "Unikitty":
        dict = unikitty_dict
    else:
        dict = brighticorn_dict
    return dict

### WELCOME TO MY COUCH
# Welcome Message, rules, game play

### THE SESSION BEGINS
### A random therapist is chosen for you
def welcome():
    print("Welcome!")
    print("How are you today?")
    print()
    print("Your randomly selected therapist on duty is: {}.".format(on_call))
    print() 
    print(on_call, "is listening...")

def get_emotion():
    #get emotion
    #match emo_response with what's in dictionary
    #print appropriate response to emotion
    emo_response = input("Please select an emotion: > ")
    return emo_response

def get_response(emotion, use_dict):
    emo_response = input("Please select an emotion: > ")
    if emo_response in use_dict:
        print(on_call, "says: ", use_dict[emo_response])
        #save unlisted emtoion in emotional_dictionary
        unlisted_emotions.[emo_response] = ""
    else:
        print("I'm sorry that's an emotion that doesn't exist in my world.  Please go away.")
        the_end()

def the_end():
    advice_list = ["stay strong", "call a friend", "drink some water", "get a massage"]
    end_advice = random.choice(advice_list)
    print("Until next time please keep this in mind: {}".format(end_advice))
    print("Goodbye")

welcome()
on_call_dict = use_dict(on_call)
emo = get_emotion()
get_response(emo, on_call_dict)


