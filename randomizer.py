from sys import argv
import sys


from random import choice
from living_things import *


i=0

foo = ['a', 'b', 'c', 'd', 'e']
goo = ['f', 'g', 'h', 'h', 'i']
hoo = ['j', 'k', 'l', 'm', 'n']


while i < 30:
	i = i + 1
#	print ("[",)
	print (choice(mammals)) ,
	print (choice(invet_marine)) ,
	print (choice(reptials)) ,
	print ("-----")