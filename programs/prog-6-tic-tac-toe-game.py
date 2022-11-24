import os
import time

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def displayBoard(board):
	print(f"       |       |       ")
	print(f"   {board[7]}   |   {board[8]}   |   {board[9]}   ")
	print(f"_______|_______|_______")
	print(f"       |       |       ")
	print(f"   {board[4]}   |   {board[5]}   |   {board[6]}   ")
	print(f"_______|_______|_______")
	print(f"       |       |       ")
	print(f"   {board[1]}   |   {board[2]}   |   {board[3]}   ")
	print(f"       |       |       ") 

def isWinner(board,mark):
	if(board[1] == mark and board[2] == mark and board[3] == mark) or \
	  (board[4] == mark and board[5] == mark and board[6] == mark) or \
	  (board[7] == mark and board[8] == mark and board[9] == mark) or \
	  (board[1] == mark and board[4] == mark and board[7] == mark) or \
	  (board[2] == mark and board[5] == mark and board[8] == mark) or \
	  (board[3] == mark and board[6] == mark and board[9] == mark) or \
	  (board[1] == mark and board[5] == mark and board[9] == mark) or \
	  (board[3] == mark and board[5] == mark and board[7] == mark):
	  return True
	return False

def isBoardFull(board):
	if ' ' in board:
		return False
	return True

def validInput(board,player,mark):
	while True:
		choice = int(input(f"{player} enter choice : "))
		if board[choice] == ' ':
			board[choice] = mark
			return
		print("Wrong Choice!!")

def playerInput(board,player,mark,gameOver):
	validInput(board,player,mark)

	if isWinner(board,mark):
		os.system("cls")
		displayBoard(board)
		print(f"{player} won the game!!")
		gameOver[0] = True


playerX = input("Player X Enter your name : ")
playerO = input("Player O Enter your name : ")
playerXChance = True
gameOver = [False]

while not gameOver[0]:
	os.system("cls")
	displayBoard(board)
	if playerXChance:
		playerInput(board,playerX,'X',gameOver)
		playerXChance = not playerXChance
	else:
		playerInput(board,playerO,'O',gameOver)
		playerXChance = not playerXChance

	if isBoardFull(board) and not gameOver[0]:
		os.system("cls")
		displayBoard(board)
		print("Draw!!")
		gameOver[0] = True






