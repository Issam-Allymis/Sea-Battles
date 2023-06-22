from random import randint



class Seaship_Battle:
    """
    
    """

    def __init__(self,  board_size, num_ships, username,):
        self.board_size = board_size
        self.num_ships = num_ships
        self.username = username
      
    

    def print_board(self):
        """
        
        """
        print('**********')
        print(f"{self.username} : {turns}\n ")
        print(" 0 1 2 3 4 5")



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
    
    
