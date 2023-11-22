import unittest
import logic

from cli import TicTacToeGame, HumanPlayer, BotPlayer


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_game_init(self):
        player1_symbol = 'X'
        player2_symbol = 'O'

        player1 = HumanPlayer(player1_symbol)
        player2 = BotPlayer(player2_symbol)
        game = TicTacToeGame(player1, player2)
        # Test that there are two players
        self.assertEqual(len(game.players), 2)
    
    def test_player_symbol_assign(self):
        player1_symbol = 'X'
        player2_symbol = 'O'

        player1 = HumanPlayer(player1_symbol)
        player2 = BotPlayer(player2_symbol)
        game = TicTacToeGame(player1, player2)
        self.assertEqual(game.players[0].symbol, 'X')
        self.assertEqual(game.players[1].symbol, 'O')
        
    def test_player_switch(self):
        player1_symbol = 'X'
        player2_symbol = 'O'

        player1 = HumanPlayer(player1_symbol)
        player2 = BotPlayer(player2_symbol)
        game = TicTacToeGame(player1, player2)
        self.assertEqual(game.current_player_index, 0)
        game.switch_player()
        self.assertEqual(game.current_player_index, 1)
        game.switch_player()
        self.assertEqual(game.current_player_index, 0)
        
    def test_winning_board(self):
        player1_symbol = 'X'
        player2_symbol = 'O'

        player1 = HumanPlayer(player1_symbol)
        player2 = BotPlayer(player2_symbol)
        game = TicTacToeGame(player1, player2)
        game.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(game.board), 'X')
        
    def test_draw(self):
        player1_symbol = 'X'
        player2_symbol = 'O'

        player1 = HumanPlayer(player1_symbol)
        player2 = BotPlayer(player2_symbol)
        game = TicTacToeGame(player1, player2)
        game.board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(game.board), None)
        
    def test_invalid_move(self):
        player1_symbol = 'X'
        player2_symbol = 'O'

        player1 = HumanPlayer(player1_symbol)
        player2 = BotPlayer(player2_symbol)
        game = TicTacToeGame(player1, player2)
        game.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        current_board = [[v for v in row] for row in game.board]
        self.assertEqual(game.board[0][0], 'X')
        game.play_round()
        self.assertEqual(game.board, current_board)
        
    def test_winner_identified(self):
        player1_symbol = 'X'
        player2_symbol = 'O'

        player1 = HumanPlayer(player1_symbol)
        player2 = BotPlayer(player2_symbol)
        game = TicTacToeGame(player1, player2)
        game.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(game.board), 'X')
        


if __name__ == '__main__':
    unittest.main()
