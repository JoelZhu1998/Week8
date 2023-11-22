import logging
from player import HumanPlayer, BotPlayer
from logic import make_empty_board, get_winner

logging.basicConfig(
    filename='logs/happyjoel_game_log.log',
    level=logging.INFO
)
class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = make_empty_board()
        self.players = [player1, player2]
        self.current_player_index = 0
        self.winner = None

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(" " if self.board[i][j] is None else self.board[i][j], end="")
                if j < 2:
                    print(" | ", end="")
            print()
            if i < 2:
                print("-" * 9)

    def play_round(self):
        player = self.players[self.current_player_index]
        self.print_board()
        print(f"Player {player.symbol}'s turn:")

        move = player.make_move(self.board)

        if move is not None:
            row, col = move
            if self.board[row][col] is None:
                self.board[row][col] = player.symbol
                self.winner = get_winner(self.board)
            else:
                print("Invalid move. That position is already occupied. Try again.")
        else:
            print("Invalid move. No available moves. Try again.")

        self.switch_player()

    def play_game(self):
        while self.winner is None:
            self.play_round()

        self.print_board()

        if self.winner:
            print(f"Player {self.winner} wins!")
            logging.info('You win!')
        else:
            print("It's a draw!")
            logging.info("It's a draw!")

if __name__ == '__main__':
    player1_symbol = 'X'
    player2_symbol = 'O'

    player1 = HumanPlayer(player1_symbol)
    player2 = BotPlayer(player2_symbol)

    game = TicTacToeGame(player1, player2)
    game.play_game()
