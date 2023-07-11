from random import randint

# Global variables
HIT = []
MISS = []

class Seaship_Battle:
    """
    
    """

    def __init__(self,  board_size, num_ships, username,):
        self.board_size = board_size
        self.num_ships = num_ships
        self.username = username
        self.hits = []
        self.misses = []
        self.ships = self.create_ships()

    def print_board(self):
        """
        
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
                    symb = '-'
                row = row + symb
            print(i, row)


    def playr_turn(self, row, col):
        """
        
        """
        coor = (row, col)
        if coor in self.ships:
            self.hits.append(coor)
            self.ships.remove(coor)
            print('HIT')
            return True
        
        elif coor in self.misses or coor in self.hits:
            print("You've already guessed this coordinate.. try again!")
            return False
        
        else:
            self.misses.append(coor)
            print('MISS')
            return False

        
 
    def create_ships(self):
        """
        Sets random ships to the board
        """
        ships = []
        while len(ships) < self.num_ships:
            ship_row = randint(0, self.board_size - 1)
            ship_col = randint(0, self.board_size - 1)
            ship_coor = (ship_row, ship_col)

            if ship_coor not in ships:
                ships.append(ship_coor)

        return ships
    



def run_game():

    board_size = 7
    num_ships = 3 
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


def get_user_input(self):
    """
        
    """
        
    guess_row = input("Enter a row between 0-6: \n")
    while guess_row not in ['0', '1', '2', '3', '4', '5', '6']:
        print("Input invalid. Please enter a valid row.")
        guess_row = input("Enter a row between 0-6: ")

    guess_col = input("Enter a column between 0-6: \n")
    while guess_col not in ['0', '1', '2', '3', '4', '5', '6']:
        print("Input invalid. Please enter a valid column.")
        guess_col = input("Enter a column between 0-6: \n")

    return int(guess_row), int(guess_col)
    

def main():
    """
    Calling function to run the game
    """

    run_game()


main()