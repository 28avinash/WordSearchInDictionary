import json
import difflib
from difflib import get_close_matches
#library used for text comparison

data=json.load(open("dictionary.json"))

def search(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        YN= input("Are you seraching for {}? Enter Y if Yes or N for No:".format(get_close_matches(word,data.keys())[0]))
        if(YN=="Y"):
            return data[get_close_matches(word,data.keys())[0]]
        elif(YN=="N"):
            return "Sorry,your entered word does'nt exist!"
        else:
            return "I can't process your command .Please enter right command"
    else:
        return "Sorry,your entered word does'nt exist!"



word=input("Enter the word:")
Result=search(word)
if type(Result)==list:
    for item in Result:
        print(item)
else:
    print(Result)