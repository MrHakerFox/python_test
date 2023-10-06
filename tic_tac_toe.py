# Global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
	print("Крестики-нолики, блин.\n")

def ask_yes_no(question):
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response

def ask_number(question, low, hight):
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

def pieces():
	go_first = ask_yes_no("Хочешь оставить за собой первый ход?")
	if go_first == 'y':
		print("\nИграйте крестиками.")
		human = X computer = O
	else:
		print("\nБуду начинать Я.")
		computer = X human = O
	return computer, human

def new_board():
	board = []
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board

def display_board():
	print("\n\t", board[0], "|", board[1], "|", board[2])
	print("\t", "--------")
	print("\n\t", board[3], "|", board[4], "|", board[5])
	print("\t", "--------")
	print("\n\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
	moves = []
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square);
	return moves

def winner(board):
	WAYS_TO_WIN = (
		(0, 1, 2),
		(3,4, 5),
		(6, 7, 8),
		(0,3, 6),
		(1, 4, 7),
		(2, 5, 8),
		(0, 4, 8),
		(2, 4, 6)
		);
	for row in WAYS_TO_WIN:
		if board[fow[0]]==board[row[1]]==board[row[2]]!= EMPTY:
			winner = board[row[0]]
			return winner
		if EMPTY not in board:
			return TIE
		return None








