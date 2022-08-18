import numpy as np

class Connect4:
    def __init__(self, board = None):
        if board is None:
            self.board = np.zeros((6, 7))
            self.history = -np.ones((42, 1))
            self.move_number = 0
        else:
            self.board = board.copy()
            self.move_number = np.sum(np.abs(board))

        if(self.board.shape != (6, 7)):
            raise Exception("board is invalid")
        if(np.sum(self.board) == 0):
            self.player = 1
        elif(np.sum(self.board) == 1):
            self.player = -1
        else:
            raise Exception("board is invalid")

    def check_win(self):
        #horizontal
        for row in range(6):
            for column in range(4):
                if(self.board[row][column] == self.board[row][column+1] == self.board[row][column+2] == self.board[row][column+3] != 0):
                    return True, self.board[row][column]

        #vertical
        for row in range(3):
            for column in range(7):
                if(self.board[row][column] == self.board[row+1][column] == self.board[row+2][column] == self.board[row+3][column] != 0):
                    return True, self.board[row][column]

        #diagonal
        for row in range(3):
            for column in range(4):
                if(self.board[row][column] == self.board[row+1][column+1] == self.board[row+2][column+2] == self.board[row+3][column+3] != 0):
                    return True, self.board[row][column]
                if(self.board[row][6-column] == self.board[row + 1][5-column] == self.board[row + 2][4-column] == self.board[row + 3][3-column] != 0):
                    return True, self.board[row][6-column]

        if(np.count_nonzero(self.board) == 42):
            return True, 0

        return False, 0

    def get_legal_actions(self):
        legalmoves = []
        for i, col in enumerate(self.board.T):
            if (np.count_nonzero(col==0) == 0):
                continue
            else:
                legalmoves.append(i)
        return legalmoves

    def play(self, move):
        if(move not in self.get_legal_actions()):
            return True, -self.player
        for row in range(6):

            if(self.board[row][move] == 0):
                self.board[row][move] = self.player
                self.player = -self.player
                self.history[self.move_number] = move
                self.move_number += 1
                return self.check_win()

            else:
                continue

        return self.check_win()


    def get_board(self):
        white = np.copy(self.board)
        white[white <= 0] = 0
        black = -np.copy(self.board)
        black[black <= 0] = 0
        return white, black



def print_board(game):
        if (type(game) == Connect4):
            temp = np.flipud(game.board)
        elif(type(game) == np.ndarray):
            temp = np.flipud(game)
        else:
            return 1
        print("-----------------------------")
        for row in range(6):
            for column in range(7):
                if(temp[row][column] == 0):
                    print("|  ", end=" ")
                if(temp[row][column] == 1):
                    print("| X", end=" ")
                if(temp[row][column] == -1):
                    print("| O", end=" ")

            print("|")
            print("-----------------------------")



