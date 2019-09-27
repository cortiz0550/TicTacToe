import os  #to use clear to clear the screen

#This dictionary holds all the values for the table
theBoard = {'1':' ', '2':' ', '3':' ',
			'4':' ', '5':' ', '6':' ',
			'7':' ', '8':' ', '9':' '}

#This prints the updated board
def printBoard(board):
	print(board['1'] + '|' + board['2'] + '|' + board['3'])
	print('-+-+-')
	print(board['4'] + '|' + board['5'] + '|' + board['6'])
	print('-+-+-')
	print(board['7'] + '|' + board['8'] + '|' + board['9'])

#Deal with input that doesn't work with the program
def checkInput(inp):

	while True:
		space = theBoard.get(inp)

		if space:
			break

		inp = input("Enter a number ")

	while True:
		if theBoard[inp].isspace():
			break

		inp = input("That space has been chosen! Pick another ")

	return inp
	
	

# We need this to check if a player has won the game.
def winGame(board):

	print()

	if((board['1'] == board['2'] == board['3'] and not (board['1'] + board['2'] + board['3']).isspace())
	or (board['4'] == board['5'] == board['6'] and not (board['4'] + board['5'] + board['6']).isspace())
	or (board['7'] == board['8'] == board['9'] and not (board['7'] + board['8'] + board['9']).isspace())
	or (board['1'] == board['4'] == board['7'] and not (board['1'] + board['4'] + board['7']).isspace())
	or (board['2'] == board['5'] == board['8'] and not (board['2'] + board['5'] + board['8']).isspace())
	or (board['3'] == board['6'] == board['9'] and not (board['3'] + board['6'] + board['9']).isspace())
	or (board['1'] == board['5'] == board['9'] and not (board['1'] + board['5'] + board['9']).isspace())
	or (board['3'] == board['5'] == board['7'] and not (board['3'] + board['5'] + board['7']).isspace())):

		return True
	else:
		return False

#The first player is X
turn = 'X'

#This loop will run for the whole game
for i in range(9):

	os.system('clear')

	printBoard(theBoard)
	print('Turn for ' + turn + '. Move on which space?')
	#move = input()

	# check to make sure the input is okay and modify if it isn't.
	check = str(input())
	move = checkInput(check)

	#Replace value at the key indicated.
	theBoard[move] = turn

	win = winGame(theBoard)

	print("bool" + str(win))

	if(win):
		os.system('clear')
		print("Congrats!, Player " + turn + " won!")
		break
	
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'


printBoard(theBoard)
