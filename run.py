from random import randint



class Seaship_Battle:
    """
    
    """

    def __init__(self,  board_size, num_ships, username,):
        self.board_size = board_size
        self.num_ships = num_ships
        self.username = username
        self.hits = []
        self.misses = []
    

    def print_board(self):
        """
        
        """
        print('**********')
        print(f"{self.username} : {turns}\n ")
        print('**********')
        for i in range(self.board_size):
            row = ' '
            for j in range(self.board_size):
                coor = (i, j)
                symb = ' . '
                if coor in self.hits:
                    symb = 'X'
                elif coor in self.misses:'3 '
                symb = '-'
                row = row + symb
            print(x, row)



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
    
    
    def get_user_input(self):
        """
        
        """
        try:
            guess_row = input("Enter a row between 0-6: \n")
            while guess_row not in ['0', '1', '2', '3', '4', '5', '6']:
                print("Input invalid. Please enter a valid row.")
                guess_row = input("Enter a row between 0-6: ")

            guess_col = input("Enter a column between 0-6: \n")
            while guess_col not in ['0', '1', '2', '3', '4', '5', '6']:
                print("Input invalid. Please enter a valid column.")
                guess_col = input("Enter a column between 0-6: \n")

            return int(guess_row), int(guess_col) 







game = Seaship_Battle(board_size=7, num_ships=3, username="Player1")
Ships = game.create_ships()