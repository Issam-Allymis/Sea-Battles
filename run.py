from random import randint

# Global variables
HIT = []
MISS = []

class Seaship_Battle:
    """
    Class representing the Sea Battles game.
    """

    def __init__(self,  board_size, num_ships, username,):
        """
        Initializes a Seaship_Battle object.

        Attributes:
            board_size (int): The size of the game board.
            num_ships (int): The number of ships in the game.
            username (str): The name of the player.
            hits (list): A list of hit coordinates.
            misses (list): A list of missed coordinates.
            ships (list): A list of ship coordinates.
        """
        self.board_size = board_size
        self.num_ships = num_ships
        self.username = username
        self.hits = []
        self.misses = []
        self.ships = self.create_ships()

    def print_board(self):
        """
        Prints the game board.
        """
        print('**********')
        print(f"{self.username}\n ")
        print('**********')
        for i in range(self.board_size):
            row = ' '
            for j in range(self.board_size):
                coor = (i, j)
                symb = ' . '
                if coor in self.hits:
                    symb = 'X'
                elif coor in self.misses:
                    symb = 'O'
                row = row + symb
            print(i, row)


    def playr_turn(self, row, col):
        """
        Processes a player's turn.

        row (int): The guessed row coordinate.
        col (int): The guessed column coordinate.

        returns bool: True if it's a hit, False if it's a miss or already guessed.
        """
        coor = (row, col)
        if coor in self.ships:
            self.hits.append(coor)
            self.ships.remove(coor)
            print('HIT')
            return True
        
        if coor in self.misses or coor in self.hits:
            print("You've already guessed this coordinate.. try again!")
            return False
        
        self.misses.append(coor)
        print('MISS')
        return False

        
 
    def create_ships(self):
        """
        Sets random ships to the board
        returns a list of ship coordinates.
        """
        ships = []
        while len(ships) < self.num_ships:
            ship_row = randint(0, self.board_size - 1)
            ship_col = randint(0, self.board_size - 1)
            ship_coor = (ship_row, ship_col)

            if ship_coor not in ships:
                ships.append(ship_coor)

        return ships
    
def get_user_input():
    """
    Gets user input for row and column.
    Returns a tuple containing the guessed row and column as integers.
    """
    while True:
        guess_row = input("Enter a row between 0-6: \n")
        guess_col = input("Enter a column between 0-6: \n")

        if guess_row in ['0', '1', '2', '3', '4', '5', '6'] and guess_col in ['0', '1', '2', '3', '4', '5', '6']:
            return int(guess_row), int(guess_col)

        print("Input invalid. Please enter valid row and column.")



def run_game():
    """
    Runs the Sea Battles game.
    """

    board_size = 7
    num_ships = 6 
    print('*-*' * 15)
    print('Welcome to Sea Battles!  \n')
    print(f'Board size: {board_size}. Total number of ships: {num_ships}')
    print('How to win: Sink all your oponent\'s ships. \n')
    print('HIT')
    print('MISS \n')


    print('Rules: ')
    print('- Player starts with guessing the row and column.')
    print('- The guess should be between 0 - 6')
    print('- The top left corner would be row: 0, col: 0.')
    print('- You will have ten turns before the game ends.')
    print('X = Hit, O = Miss')
    print('- Once all ships are hit the game will end!')
    print('*-*' * 15)
    username = input('Please enter your name before commencing the game: \n')

    player_game = Seaship_Battle(board_size, num_ships, username)

    turns = 0
    max_turns = 10

    while turns < max_turns and len(player_game.ships) > 0:
        player_game.print_board()
        row, col = get_user_input()
        player_game.playr_turn(row, col)

        if len(player_game.ships) == 0:
            print('Congratualtions! you have destroyed all of the ships!')
    
        elif turns == max_turns:
            break
        turns += 1
        print(f'Amount Turn. {turns} ')

    print('Game Over!')
    return username



    

def main():
    """
    Calling function to run the game
    """

    run_game()


main()