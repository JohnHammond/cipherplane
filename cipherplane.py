#!/usr/bin/env python

from colorama import *
import collections

'''
We need to know...

1. if there are duplicates in the plaintext
2. if there are duplicates in the ciphertext
3. if there are entries in the plaintext that are in the ciphertext
4. if there are entries in the ciphertext that are in the plaintext
'''

def G(string): return Style.BRIGHT + Fore.GREEN + string + Fore.RESET + Style.NORMAL
def g(string): return  Fore.GREEN + string + Fore.RESET
def B(string): return Style.BRIGHT + Fore.BLUE + string + Fore.RESET + Style.NORMAL
def b(string): return  Fore.BLUE + string + Fore.RESET
def Y(string): return Style.BRIGHT + Fore.YELLOW + string + Fore.RESET + Style.NORMAL
def y(string): return  Fore.YELLOW + string + Fore.RESET
def C(string): return Style.BRIGHT + Fore.CYAN + string + Fore.RESET + Style.NORMAL
def c(string): return  Fore.CYAN + string + Fore.RESET


def get_duplicates( entries ):

	counted_entries = collections.Counter(entries)
	duplicates = { item : count for item, count in counted_entries.items() if count > 1 }

	return duplicates


def print_duplicates(entries):
	duplicates = get_duplicates(entries)
	number_duplicates = len(duplicates.keys())
	if number_duplicates > 0:
		print g("\n[!] There are "+ G(str(number_duplicates)) +" duplicates!")
		index = 1
		for duplicate, count in duplicates.iteritems():
			print y("["+str(index)+"] " ) + Y(str(duplicate)) + y(" duplicated ") + G(str(count)) + y(" times!")
			index += 1
		print "\n"


def get_similarities( a, b ):
	return list(set(a).intersection(set(b)))


def print_similarities( a, b ):

	similarities = get_similarities(a, b)
	number_similarities = len(similarities)
	if number_similarities > 0:
		print g("\n[!] There are ") + G(str(number_similarities)) + g(" same entries in the two sets!")
		index = 1
		for similarity in similarities:
			print y("["+str(index)+"] " ) + Y(str(similarity)) 
			index += 1
		print "\n"



def process( plaintext, ciphertext ):
	print C("Processing plaintext...")
	print_duplicates(plaintext)
	print C("Processing ciphertext...")
	print_duplicates(ciphertext)
	print C("Processing plaintext and ciphertext...")
	print_similarities( plaintext, ciphertext )


plaintext = range(1, 10) + range(1, 4) 
ciphertext = [ x**2 for x in range(1,10) ]

process(plaintext, ciphertext)