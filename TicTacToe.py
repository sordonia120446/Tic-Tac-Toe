class TicTacToe():
	'''Play Tic-tac-toe.  Details of the game are here:  https://en.wikipedia.org/wiki/Tic-tac-toe'''

	def __init__(self):
		self.myBoard = []
		self.size = 3
		self.gameOn = True
		self.player1 = Player()
		self.player2 = Opponent()
		self.emptySpot = '|_|'

		# Set up the 3x3 board
		for row in range(self.size):
			self.myBoard.append([])
			for col in range(self.size):
				self.myBoard[row].append(self.emptySpot)

	def printBoard(self):
		'''Cleverly prints out a text board in terminal.  Ghetto but works.'''
		tempString = ''
		board = self.myBoard

		for row in board:
			for col in row:
				tempString += str(col)
			tempString += '\n'
		print(tempString)
        
	def convertToBoardCoordinates(self,location):
		'''Converts location tuple into a row,col ranging from 0~2.'''
		row = location[0]
		col = location[1]
		return (row - 1,col - 1)

	def move(self):
		print('Input the location with the following format:  row #, col#')
		player_move = input('Which row,col do you want to fill in?  ')
		player_move = self.convertToBoardCoordinates(player_move)
		row = player_move[0]
		col = player_move[1]

		if self.is_valid_location(player_move):
			self.myBoard[row][col] = self.player1.marker
		else:
			return self.move()

		self.end_game(player_move)

	def end_game(self,location):
		'''Determines if the game has ended or not.  If game over, sets gameOn boolean to False.'''
		row = location[0]
		col = location[1]

		# Check horizontal
		cntr = 0
		for y_var in range(self.size):
			if self.myBoard[row][y_var] == self.player1.marker:
				cntr += 1
		if cntr == 3:
			self.gameOn = False
			self.game_over_message()

		# Check vertical
		cntr = 0
		for x_var in range(self.size):
			if self.myBoard[x_var][col] == self.player1.marker:
				cntr += 1
		if cntr == 3:
			self.gameOn = False
			self.game_over_message()

		# Check diagonal
		cntr = 0
		if row == col:
			for index in range(self.size):
				if self.myBoard[index][index] == self.player1.marker:
					cntr += 1
			if cntr == 3:
				self.gameOn = False
				self.game_over_message()

		# Check anti-diagonal
		cntr = 0
		ind2 = self.size - 1
		for index in range(self.size):
			if self.myBoard[index][ind2] == self.player1.marker:
				cntr += 1
			ind2 -= 1
		if cntr == 3:
			self.gameOn = False
			self.game_over_message()

	def game_over_message(self):
		print('Game over!')

	def is_valid_location(self,location):
		'''Determines if tuple location is valid or not.  Location should be converted to Python board coordinates by now.'''
		for dimension in location:
			if dimension < 0 or dimension >= self.size:
				print('That is not going to land on the board knucklehead!')
				return False
		return True

	def play(self):
		'''Loops the game for as long as gameOn is True.'''
		while self.gameOn:
			self.printBoard()
			self.move()
		self.printBoard()

class Player():
	'''Player class.'''

	def __init__(self):
		self.name = input("What's your name?...")
		self.marker = ' X '
		self.winner = False
		print('You will be filling the board with Xs')


class Opponent(Player):
	'''Opponent class.  Intended for AI use.'''
	
	def __init__(self):
		self.name = 'Your Foe'
		self.marker = ' O '



# Driver
tic = TicTacToe()
tic.play()


