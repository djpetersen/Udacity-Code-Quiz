# IPND Stage 2 Final Project
# David Petersen djpetersen@gmail.com

# Statements
# note: text taken from 
# https://en.wikipedia.org/wiki/Python_(programming_language)

import sys
import time

# Global variables, starting with our 3 text examples which form levels
easy = ('A ___1___ is created with the def keyword. You specify the inputs'
	' a ___1___ takes by adding ___2___ separated by commas between the ' 
	'parentheses.  ___1___s by default return ___3___ if you do not specify '
	'the value to return. ___2___ can be standard data types such as string, '
	'number, dictionary, tuple, and ___4___ or can be more complicated such '
	'as objects and lambda functions.')

medium = ('The ___1___ statement, which conditionally executes a block of '
	'code, along with else and ___2___ . The for statement, which iterates '
	'over an iterable object, capturing each element to a local variable for'
	' use by the attached block. The ___3___ statement, which executes a '
	'block of code as long as its ___4___ is true.')

hard = ('Python makes a distinction between lists and tuples. Lists are '
	'written as [1, 2, 3], are ___1___ , and cannot be used as the keys of '
	'dictionaries (dictionary keys must be immutable in Python). Tuples are '
	'written as (1, 2, 3), are ___2___ and thus can be used as the keys of '
	'dictionaries, provided all elements of the tuple are immutable. The '
	'___3___ around the tuple are optional in some contexts. Tuples can '
	'appear on the left side of an equal sign; hence a statement like x, '
	'y = y, x can be used to swap two ___4___.')

examples = [easy,medium,hard]

difficultyLevel = ['easy', 'medium', 'hard']

key = [['function','arguments','none','lists'],
	['if','elif','while','condition'],
	['mutable','immutable','parentheses','variables']]

blanks = ['___1___','___2___','___3___','___4___']


# Function definitions
def instructions():
	''' Print game instructions. Returns last line of instructions.'''
	print '\n'
	print ('Welcome to Fill-in-the-Blanks. Your goal is to successfully'
		' complete')
	print ('each of the blanks in sequence. Do not make too many incorrect '
		'answers,')
	print 'or you will lose the game!' + '\n'
	return 'Good Luck!' + '\n'

def userInput(title):
	''' function to accept user input, standardize to lower case, allow quit. 
	Accepts a question to print, and returns the user input in lower case '''
	answer = (raw_input(title)).lower()
	if answer == 'q':
		sys.exit()
	return answer

def fillText(example, blank, key):
	''' fillText: Tokenize a piece of text (example), and then for each token 
	in the sequence lookup item you want to replace that was passed in (here 
	"blank"), replace it if it matches "key" otherwise keep the original item. 
	Then string all tokens (with any replaced items) back together and return 
	that string (replaced).'''
	replaced = []
	tokens = example.split()
	for item in tokens:
		if blank in example:
			item = item.replace(blank,key)
			replaced.append(item)
		else:
			replaced.append(item)
	replaced = " ".join(replaced)
	return replaced

def evaluate(text,blanks,key,level,counter):
	'''function compares user input to answer key, and if match is made, 
	it calls the fill text function to replace key value with correct answer. 
	Otherwise monitors number of tries, bombs user when limitAttempts reached. 
	Returns counter, edited text, and True if user made match, false if user  
	could not correctly complete'''
	limitAttempts = 0 # when tries hits this number, will exit the game
	tries = 5 # how many incorrect answers are you allowed before you lose 
	while tries > limitAttempts: #setup a while loop to control num of tries
		guess = (userInput('Please guess the value of ' + 
			str(blanks[counter]) + ':  '))
		if guess == key[level][counter].lower(): # compare user input to key
			print '\n' + 'Correct!' #print correct if correct
			text = fillText(text, blanks[counter], key[level][counter]) 
			counter +=1	# move on to the next blank
			return counter, True, text
		else: # reduce num of tries by one, loop to top of while for guess
			tries = tries - 1
			print ('\n' + 'Incorrect. You have ' + str(tries) + ' tries left.'
				+ '\n')
			if tries == limitAttempts: # exit function, return success = false
				return counter, False, text

def levelPlay(text,blanks,key,level):
	'''Level play - from levelSelect, gets a piece of text, identification
	of what represents blanks, the answer key and the level selected (for 
	printing out to the user). This function loops the user through blanks, 
	allowing them guesses, and evaluating the answers against a key. Returns 
	a value of "True" if the user successfully completes all questions, 
	or "False" if the user fails after 5 tries'''
	counter = 0
	for item in blanks: # loop over all the items in blanks to be filled in
		print(('\n'*1) + 'Level ' + str(level+1) + ': ' + 'The current ' 
			'paragraph reads as such: ' + '\n'*2 + text + '\n') 
		counter, passfail, text = evaluate(text,blanks,key,level,counter) 
		if passfail == False: # if user fails, report back to levelSelect game
			return False
	return True # if user passes whole loop, return success = True

def levelSelect():
	'''levelSelect function: handles both the selection of level via a call 
	to userInput function (and ability to quit), error handling if user  
	submits an answer not in our list of options, and then once it receives 
	a satisfactory input, it calls the levelPlay function above to return a 
	success value of True or False. If success == True, you get the 
	congratulations message, otherwise you get the losing message of 
	"Thanks for playing!"	'''
	validLevel = False
	while validLevel == False: #emulate udacity's error handling of input
		whatLevel = userInput('Select easy, medium, or hard (or q to quit): ')
		if whatLevel not in difficultyLevel: #if user entry not in list
			print 'That is not an option!' #print error, return to top of loop
		else: #only if user enters a valid level, break loop & proceed to game
			validLevel = True	
	levelNum = difficultyLevel.index(whatLevel) #get position of level in list
	success = levelPlay(examples[levelNum],blanks,key,levelNum) #play it
	if success == True: #returned from levelPlay - if true, you have won game
		complete = '***    Congratulations! You have won the game!    ***'
		return ('\n' + '*'*len(complete) + '\n' + complete + '\n' + 
			'*'*len(complete) + '\n'*3)
	else: #returned from levelPlay - success == False, so you didn't win
		return '\n' + 'Thanks for playing!' + '\n'*3

# Print the instructions and play the game!

instruct = instructions()
print instruct
result = levelSelect()		
print result	