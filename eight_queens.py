# find all the ways to place eight queens on a chess board
# such that none of the queens threaten each other

# recurse through each row of chessboard
# loop through every column of chessboard
# if you can place a queen at a given row column, do it
# can store a chessboard as a list representing columns such that
# list[row] = col -> at this row there is a queen at that col

QUEENS = 8
def place_queens(results, curr_board, row):
	if row == QUEENS:
		results.append(curr_board[:])
		return
	for col in range(QUEENS):
		if valid_placement(row, col, curr_board):
			curr_board[row] = col
			place_queens(results, curr_board, row + 1)


def valid_placement(row, col, curr_board):
	for row2 in range(row):
		col2 = curr_board[row2]
		if col2 == col:
			return False

		col_dist = abs(col2 - col)
		row_dist = row - row2
		if col_dist == row_dist:
			return False
	return True

def print_board(board):
	full = [[None for _ in range(QUEENS)] for _ in range(QUEENS)]
	for r, c in enumerate(board):
		full[r][c] = 'Q'

	for row in full:
		for col in row:
			if col != None:
				print(col, end=' ')
			else:
				print('.', end=' ')
		print()

if __name__ == '__main__':
	results = []
	board = [-1 for _ in range(QUEENS)]
	place_queens(results, board, 0)
	
	for result in results:
		print_board(result)
		print('---')

	print(len(results))