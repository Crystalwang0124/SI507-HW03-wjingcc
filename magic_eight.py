#this is the main file for Magic8ball game

import sys
import random


def add_questionsB():
        answers = random.randint(1,20)
            
        if answers == 1:
                print ("It is certain.")
            
        elif answers == 2:
                print ("As I see it, yes.")
            
        elif answers == 3:
                print (" Reply hazy, try again.")
            
        elif answers == 4:
                print ("Don't count on it.")
            
        elif answers == 5:
                print ("It is decidedly so.")
            
        elif answers == 6:
                print ("Most likely. ")
            
        elif answers == 7:
                print ("Ask again later.")
                
        elif answers == 8:
                print ("My reply is no.")
                
        elif answers == 9:
                print ("Without a doubt.")
                
        elif answers == 10:
                print ("Outlook good.")

        elif answers==11:
            print ("Reply hazy, try again")

        elif answers==12:
            print ("Ask again later.")

        elif answers==13:
            print ("Better not tell you now.")

        elif answers==14:
            print ("Cannot predict now.")

        elif answers==15:
            print ("Concentrate and ask again.")

        elif answers==16:
            print ("Don't count on it.")

        elif answers==17:
            print ("My reply is no.")

        elif answers==18:
            print ("My sources say no.")

        elif answers==19:
            print ("Outlook not so good.")

        elif answers==20:
            print ("Very doubtful.")

question = input("What's your question?:")

while True:
	if question == "quit":
		break
	elif question[-1] == "?":
		add_questionsB()
		question = input("What's your next question? quit for exit:")
	elif question[-1] != "?":
		question = input("What's your question and pls end your question with question mark?:")
