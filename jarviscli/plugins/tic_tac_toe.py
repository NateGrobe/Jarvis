from plugin import plugin
from colorama import Fore

board = {'7': '   ', '8': '   ', '9': '   ',
         '4': '   ', '5': '   ', '6': '   ',
         '1': '   ', '2': '   ', '3': '   '}

board_keys = [key for key in board]

@plugin("tic_tac_toe")
class TicTacToe:

    def __call__(self, jarvis, s):
        jarvis.say("Welcome to Tic Tac Toe")
        self.game(jarvis, s)

    def restartBoard(self, board):
        for key in board_keys:
            board[key] = '   '


    def printBoard(self, board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-----------')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-----------')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])


    def checkWinner(self, board, jarvis, turn):
        
        if board['7'] == board['8'] == board['9'] != '   ':
            self.printBoard(board)
            print("\n--- Game Over ---\n")
            print(turn + " won!")
            return True
        
        elif board['4'] == board['5'] == board['6'] != '   ':
            self.printBoard(board)
            print("\n--- Game Over ---\n")
            print(turn + " won!")
            return True
        
        elif board['1'] == board['2'] == board['3'] != '   ':
            self.printBoard(board)
            print("\n--- Game Over ---\n")
            print(turn + " won!")
            return True
        
        elif board['1'] == board['4'] == board['7'] != '   ':
            self.printBoard(board)
            print("\n--- Game Over ---\n")
            print(turn + " won!")
            return True
        
        elif board['2'] == board['5'] == board['8'] != '   ':
            self.printBoard(board)
            print("\n--- Game Over ---\n")
            print(turn + " won!")
            return True
        
        elif board['3'] == board['6'] == board['9'] != '   ':
            self.printBoard(board)
            print("\n--- Game Over ---\n")
            print(turn + " won!")
            return True
        
        elif board['7'] == board['5'] == board['3'] != '   ':
            self.printBoard(board)
            print("\n--- Game Over ---\n")
            print(turn + " won!")
            return True
        
        elif board['1'] == board['5'] == board['9'] != '   ':
            self.printBoard(board)
            print("\n--- Game Over ---\n")
            print(turn + " won!")
            return True
        
        else:
            return False


    
    def game(self, jarvis, s):
        """
        The tic tac toe game for two players
        Positions on the board are placed as follow
        7 | 8 | 9
        -----------
        4 | 5 | 6
        -----------
        1 | 2 | 3
        """

        self.restartBoard(board)
        turn = ' X '
        count = 0

        while count < 10:
            self.printBoard(board)
            s = jarvis.input(turn + "turn. " + "Choose a position!", Fore.BLUE)
            if s not in board_keys:
                jarvis.say(
                    "Incorrect input. Please print any number from 1 to 9 corresponding to the position on the board!", Fore.RED)
                continue

            if board[s] == '   ':
                board[s] = turn
                count += 1
            else:
                jarvis.say(
                    "This position is already filled.\nChoose another position!", Fore.RED)
                continue

            if count >= 5:
                if(self.checkWinner(board, jarvis, turn)):
                    break

            # Check if a draw
            if count == 9:
                self.printBoard(board)
                jarvis.say("\n--- Game Over ---\n", Fore.GREEN)
                jarvis.say("It's a Draw!", Fore.GREEN)
                break

            # Change the turn
            if turn == ' X ':
                turn = ' O '
            else:
                turn = ' X '
