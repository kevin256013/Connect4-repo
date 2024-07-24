class Connect4():

    def __init__(self):
        # Initialize the game board and other necessary attributes.
        self.board = [['_' for i in range(7)] for row in range(6)]
        self.current_player = None

    def display_board(self):
        # Print the current state of the board.
        for row in self.board:
            print(' | '.join(row))
        print()
          
    def make_move(self,player,column):
        # Allow a player to make a move in a specified column
        pass
    def check_winnner(self):
        # Check if there's a winner after a move.
        pass
    def is_full(self):
        # Check if the board is full (i.e., no more valid moves)
        pass
    def reset_board(self):
        # Reset the board for a new game
        pass
        
    
class Player():

    def __init__(self,name, age):
        # Initialize the player's name, age, score, and ID.
        self.name = name
        self.age = age
        self.score = 0
        self.player_id = 0

    def __repr__(self):
        # Provide a string representation of the player.
        return f"Hello {self.name} are you ready to play Connect 4!!! "
    
    def set_player_1(self):
        # Set the player as Player 1
        return f"You are player {self.player_id + 1}"
        
    def set_player_2(self):
        # Set the player as Player 2.
        return f"You are player {self.player_id + 2}"
    def get_move(self):
        # Get the player's move.
        pass
    def update_score():
        # Update the player's score.
        pass
    def is_winner():
        # Determine if the player is the winner.
        pass
    



Danny = Player("Danny", 18)
player1 = Danny.set_player_1()
print(Danny)
print(player1)

Kevin = Player("Kevin", 24)
player2 = Kevin.set_player_2()
print(Kevin)
print(player2)


game_board = Connect4()
game_board.display_board()






