# Chess Game

### For a game of chess, design:
- a constructor function that will initialize the board
- a method move(x1, y1, x2, y2, color) that returns true if a given move was valid

## Constructor
- Represent the board as a 2D array/list, with dimensions 8x8. (0, 0) will be the bottom left, (7, 7) will be the top right
- Pieces in the array can be integers, positive for white & negative for black
- Map numbers to piece types, e.g.:
-- 0 = Empty
-- 1 = Pawn
-- 2 = Rook
-- 3 = Knight
-- 4 = Bishop
-- 5 = Queen
-- 6 = King
- Manually (hardcode) piece placements other than pawns

```python
SIZE = 8
WHITE = 0
BLACK = 7
board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
	
# pawns
board[1] = [1 for _ in range(SIZE)]
board[6] = [-1 for _ in range(SIZE)]
# rook
board[WHITE][0] = board[WHITE][7] = 2
board[BLACK][0] = board[BLACK][7] = 2
# knight
board[WHITE][1] = board[WHITE][6] = 3
board[BLACK][1] = board[BLACK][7] = 3
# etc.
```

## Move function
* Criteria for a valid move:
	* source and destination are in bounds
	* Piece at source space is a piece belonging to the current player
	* Piece at destination space is either empty or belongs to enemy player (i.e. is not the same player as current)
		* Abstract to function dest_valid(x1, x2, color)
	* Pawns are simplest: destination must be in front (delta depends on color)
	* Knights also simple: either row or col delta must be 2, the other must be 1
	* For pieces that can move many spaces (rook, bishop, queen) ensure that all pieces are empty between source and destination
		* Abstract into 2 methods, plus moves and x moves so that queen may reuse rook & bishop's validators
	* King destinations must be 1 piece away, which means row & col delta must be <= 1
* Structure:
	* get & verify player color
	* test valid destination
	* dispatch to appropriate helper function

```python
def which_color(x1, x2):
	if board[x1][x2] > 0:
		return 'WHITE'
	elif board[x1][x2] < 0:
		return 'BLACK'
	return 'EMTPY'

def same_color(x1, x2, y1, y2):
	return which_color(x1, x2) == which_color(y1, y2)

def dest_valid(x1, x2, source_color): 
	pass



def move(x1, x2, y1, y2, color):
	source_color = which_color(x1, x2)

	# fail fast

```
