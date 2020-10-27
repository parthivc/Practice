


class Piece:

    def __init__(self, color, value):
        self.color = color  # True is white, False is black
        self.taken = False
        self.value = value

class King(Piece):

    def __init__(self, color):
        super().__init__(color, float('inf'))
        self.canCastle = True
    
class Queen(Piece):

    def __init__(self, color):
        super().__init__(color, 9)

class Rook(Piece):

    def __init__(self, color):
        super().__init__(color, 5)
        self.canCastle = True    

class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color, 3)

class Knight(Piece):

    def __init__(self, color):
        super().__init__(color, 3)

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color, 1)
        self.enpassant = 0  # A certain move number

class Player:

    def __init__(self, color):
        self.color = color

    def move(self, board):
        # Prompt user for input
        # Validate that move is allowed
        # Update the board object accordingly
        # Calculate what move just happened
        # Return that notation to the Board class for notation
        return "Nxb2"

    def canMove(self, startX, startY, endX, endY):
        # Verify that:
            # A piece exists at that location
            # It is a piece of the current player's color
            # Both locations are valid
            # It can move to the specified location as per the rules of the piece (e.g. Knight)
            # That no piece of the same color exists
            # That it isn't putting the king into check
            # For enpassant, if move numbers match
            # For castling, if rook and king haven't moved and all path squares aren't under attack
        return startX and startY

class Board():
    
    def __init__(self, p1, p2):
        self.board = [[None for x in range(8)] for y in range(8)]
        self.resetBoard()  # Resets the board
        self.gameState = "active"
        self.playerMove = True  # True is p1 (white), False is p2 (black)
        self.moveCount = 1  # Increments after each black move
        self.moveHistory = []
        self.p1 = p1
        self.p2 = p2

    def resetBoard(self):
        for y in range(8):
            if y == 0 or y == 7:
                self.board[0][y] = Rook(True)
                self.board[7][7 - y] = Rook(False)
            elif y == 1 or y == 6:
                self.board[0][y] = Knight(True)
                self.board[7][7 - y] = Knight(False)
            elif y == 2 or y == 5:
                self.board[0][y] = Bishop(True)
                self.board[7][7 - y] = Bishop(False)
            elif y == 3: 
                self.board[0][y] = Queen(True)
                self.board[7][7 - y] = Queen(False)
            else: 
                self.board[0][y] = King(True)
                self.board[7][7 - y] = King(False)
            self.board[1][y] = Pawn(True)
            self.board[6][y] = Pawn(False)
            for x in range(2, 6):
                self.board[x][y] = None

    def evaluateGameState(self):
        states = ["Active", "White Won", "Black Won", "Draw", "Stalemate", "Draw by 3-Fold Repetition", "White Wins by Resignation", "Black Wins by Resignation"]
        # Would return a state at this point after the appropriate logic had been computed
        return states[0]

    def makeMove(self):
        move = None
        if self.playerMove:
            move = self.p1.move(self.board)
        else:
            move = self.p2.move(self.board)
        self.moveHistory.append(move)
        state = self.evaluateGameState()
        if state == "Active":
            self.playerMove = not self.playerMove
            if self.playerMove:
                self.moveCount += 1

    def underAttack(self, x, y):
        # Checks if the current piece is under attack and check all available pieces
        return False


def main():
    print("\nHello World\n")


if __name__ == "__main__":
    main()
