# this the main file for Magic8ball game

def question_from_user():
	print("What is your question?")
	question = input()
	
import sys
import random

def add_questionsB():
        answers = random.randint(1,10)
            
        if question == "":
                sys.exit()
            
        elif answers == 1:
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
