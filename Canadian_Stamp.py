from ast import Str
import math
import string
#1.	Assume a Canadian postal stamp is 85 cents. Using the division and the modulo operator, 
#write a small program that reads an amount of money (in cents). 
#Use the operators to calculate (then output):
#How many Canadian stamps you can buy with that amount.
#How many one-cent stamps you can buy with the remaining money. 

money = input ("How much money (in cents) do you have? ")
able = float (money) / 85
print ("You can buy ". int (able), " of 0.85 cents stamps")
able2 = int (money) % 85
print ("And you can buy ",able2, " of 1 cent stamps with your remaining money") 


