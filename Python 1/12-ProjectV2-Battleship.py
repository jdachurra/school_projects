"""
COMP.CS.100 Programming 1

Battleship game Project

StudentId: 151487475
name:      Jose Daniel Achurra Santos
email:     jose.achurrasantos@tuni.fi

The program is implemented as follows:

    There are 3 classes, with the follwoing hierarchy: 
        Board -> Tiles -> Ship.
        
    The Board's main attribute is a 10x10 matrix (list of list) of Tiles objects, 
      where each Tile can be (or not) linked to a Ship object.
      The classes are connected in a way that the parent class communicates
      with the child class, but the other way around is not preferred.
    
    When the program starts, an object Board is initialized with the given input file.
        For each tile of the board, a Tile object is created, 
        and for each ship in the input file, a Ship object is created.
    
    The output of the board that the user sees, 
    is basically a "print" of a string attribute that
    every Tile object have.
    
    The Tile objects (and the Ship too) are not connected to each other in any way, 
        instead, their "connected" behaviour is handled by the Board.
    


"""

COORDINATE_STR_LIST = ["A","B","C","D","E","F","G","H","I","J",
                       "a","b","c","d","e","f","g","h","i","j"]
COORDINATE_INT_LIST = ["0","1","2","3","4","5","6","7","8","9"]


def coordinate_to_index(coordinate_string, is_ship_init = False):
    """
    Given a string with format char-int, e.g. "A0", 
    returns a tuple with its corresponding board index.
    returns ("Error", "Error") if the input is invalid
    
    :param coordinate_string: str, coordinate string
    :param is_ship_init: bool, if the function is called from Ship__init__
    :return: tuple, (int, int) or ("Error", "Error")
    
    """
    if (
        len(coordinate_string) != 2
        or coordinate_string[0] not in COORDINATE_STR_LIST
        or coordinate_string[1] not in COORDINATE_INT_LIST
        ):
        
        if is_ship_init:
            #Exception 2
            print("Error in ship coordinates!")

        return ("Error", "Error")
    
    j = ord(coordinate_string[0].upper()) - 65
    i = int(coordinate_string[1])
    return (i,j)



class Tiles:
    """
    Tile entity. Can be linked to a Ship object, 
        and it can send commands to it.
        
    The tile can be in 4 states:
        - " " : empty
        - "*" : shot, no ship
        - "X" : shot, ship
        - "A" : ship A (e.g.)
        
    @private
    __tile_status: str, the status of the tile
    __linked_ship: Ship, the ship linked to the tile
    
    @public
    link_ship: void, links a ship to the tile
    get_linked_ship: Ship, returns the linked ship
    get_tile_status: str, returns the tile status
    shoot_this: void, changes the tile status to shot
    sink_this_tile: void, changes the tile status to the ship symbol
    
    """
    
    def __init__(self):
        self.__tile_status = " "
        self.__linked_ship = None
        
    
    def __del__(self):
        pass
    
    def __str__(self):
        return self.__tile_status
    
    
    def link_ship(self, ship_obj):
        """
        Links a Ship object to the Tile object.
        
        :param ship_obj: Ship, the ship object
        :return: None
        """
        self.__linked_ship = ship_obj
        
        return
    
    
    #Getters
    def get_linked_ship(self):
        """
        Getter for the linked ship
        :return: Ship, the linked ship
        """
        return self.__linked_ship
    
    def get_tile_status(self):
        """
        Getter for the tile status
        :return: str, the tile status
        """
        return self.__tile_status
    
    def shoot_this(self):
        """
        This is called by the method shoot_action in the Board object.
        It changes the status of the tile. 
        NB: All sanity checks are done before in the Board object.
        
        :return: None
        """
        if self.__linked_ship == None:
            self.__tile_status = "*"
        else:
            self.__tile_status = "X"
            self.__linked_ship.hit()
            
        return

    
    
    def sink_this_tile(self):
        """
        This is called by the method shoot_action in 
            the Board object, only if the ship is sunk.
        
        :return: None    
        """
        self.__tile_status = self.__linked_ship.get_symbol()
        return


    #private variables
    __tile_status = ""
    __linked_ship = None
    




class Ship:
    """
    Ship object. Each ship contains specific proper coordinates 
        that refer to the main board. The ship can be in 2 states 
        depending on the amount of hitpoints left (either sunk or not).
    
    @private
    __coor_list: list, list of tuples with the coordinates of the ship
    __name: str, the name of the ship
    __symbol: str, the symbol of the ship
    __hitpoints: int, the amount of hitpoints left
    __is_sunk: bool, if the ship is sunk
    
    @public
    hit: void, decreases the hitpoints of the ship
    get_coordinate_list: list, returns the coordinate list
    get_name: str, returns the name of the ship
    get_symbol: str, returns the symbol of the ship
    get_hitpoints: int, returns the hitpoints of the ship
    get_is_sunk: bool, returns if the ship is sunk
    __str__: str, returns the name of the ship
    
    """
    
    def __init__(self, ship_data_list):
        self.__coor_list = []
        
        temp_iterator = 0
        for data_string in ship_data_list:
            if temp_iterator == 0:
                self.__name = data_string
                self.__symbol = data_string[0].upper()
            else:
                self.__coor_list.append(coordinate_to_index(data_string, True))
                if self.__coor_list[-1] == ("Error", "Error"):
                    raise ValueError
                
            temp_iterator += 1
        
        self.__hitpoints = len(self.__coor_list)
        self.__is_sunk = False
        
        
    def __del__(self):
        pass


    def hit(self):
        """
        Reduce the hitpoints of the ship by 1.
        This is called by the method shoot_action in the Board object, 
            only when a ship is hit.
            
        :return: None
        """
        self.__hitpoints -= 1
        if self.__hitpoints == 0:
            self.__is_sunk = True
        return

    
    #Special methods
    def __str__(self):
        return self.__name
    
    
    #Getters
    def get_coordinate_list(self):
        """
        Getter for the coordinate list
        :return: list, the coordinate list
        """
        return self.__coor_list
    
    def get_name(self):
        """
        Getter for the name of the ship
        :return: str, the name of the ship
        """
        return self.__name
    
    def get_symbol(self):
        """
        Getter for the ship's symbol
        :return: str, the ship's symbol
        """
        return self.__symbol


    def get_hitpoints(self):
        """
        Getter for the hitpoints of the ship 
            (the amount of Tiles it is connected with)
        :return: int, the name of the ship
        """
        return self.__hitpoints

    def get_is_sunk(self):
        """
        Getter for the sunk status of the ship
        :return: bool, True if the ship is sunk
        """
        return self.__is_sunk
    
    
    #Private Variables
    __coor_list = []
    __name = ""
    __symbol = ""
    __hitpoints = 0
    __is_sunk = False
    
    


    
class Board:
    
    """
    The main board object. Contains a 10x10 matrix of Tiles objects, 
    and a list of Ship objects. It can send commands to the Tiles objects.
    
    @private
    __main_board: list, 10x10 matrix of Tiles objects
    __ships_obj_list: list, list of Ship objects
    __error_signal: bool, if an error has ocurred
    __sunk_ships: int, the amount of ships that have been sunk
    
    @public
    print_board: void, prints the board
    shoot_action: void, shoots a tile and updates the board
    is_all_sunk: bool, returns if all ships have been sunk
    get_error_signal: bool, returns the error signal
    
    """
    
    def __init__(self, filename):
        
        #The board is a 10x10 list of lists, containing Tiles objects
        self.__main_board = [[Tiles() for i in range(10)] for j in range(10)]
        
        self.__ships_obj_list = []
        self.__error_signal = False
        
        self.__sunk_ships = 0
        self.__load_board(filename, self.__main_board, self.__ships_obj_list)
        
        
    def __del__(self):
        pass
    
    def print_board(self):
        """
        The board is printed is printed as follows:
        - Prints extra text
        - Prints the main board (Tile objects status)
        - Prints extra text
        
        :return: None
        """
        
        print()
        print("  A B C D E F G H I J")
        
        for i in range(10):
            print(i, end=" ")
            for j in range(10):
                print(str(self.__main_board[i][j]), end=" ")
            print(i, end="\n")
            
        print("  A B C D E F G H I J")
        print()
            
        
    def __load_board(self, filename, main_board, ships_obj_list):
        """
        Loads the board from the input file.
        The method reads the file, creates the Ship objects,
        and links them to the Tile objects.
        
        :param filename: str, the name of the file
        :param main_board: list, the main board
        :param ships_obj_list: list, the list of Ship objects
        :return: None
        """
        try:
            with open(filename) as file:
                for line in file:
                    #Initialize the ship object and add it to the ships list
                    ships_obj_list.append( Ship( line.strip().split(";") ) )
                    
                    #connect the ship to the tile, by calling the proper Tile's method
                    self.__add_ship_to_tiles(ships_obj_list[-1], main_board)
                    
        
        except ValueError:
            self.__error_signal = True
        except:
            #Exception 1 (in Plussa)
            print("File can not be read!")
            self.__error_signal = True

            
        return
    
    def __add_ship_to_tiles(self, ship_obj, main_board):
        """
        Add the Ship object to every Tile object that the ship is in.
        First, the method checks if the ship is overlapping with another ship.
        
        :param ship_obj: Ship, the ship object
        :param main_board: list, the main board
        :return: None
        """
        
        #assumes the ship have at least 1 coordinate
        for coor in ship_obj.get_coordinate_list():
            if main_board[coor[0]][coor[1]].get_linked_ship() != None:
                #Exception 3
                print("There are overlapping ships in the input file!")
                self.__error_signal = True
            else:
                #Call the Tile's method to link the ship
                main_board[coor[0]][coor[1]].link_ship(ship_obj)
        return
    
    
    
    def shoot_action(self, coordinate_tuple):
        """
        This is called when the user shoots a tile.
        It checks if the coordinate is valid,
        and if the tile has not been shot before.
        After this, send the command to the Tile object, 
        and then check if a ship have been sunk.
        
        :param coordinate_tuple: tuple, (int, int) with the coordinate
        :return: None    
        """
        
        i = coordinate_tuple[0]
        j = coordinate_tuple[1]
        if self.__main_board[i][j].get_tile_status() != " ": 
            print("Location has already been shot at!")
            return
        
        #The coordinate is valid
        self.__main_board[i][j].shoot_this()
        
        #Check if the boat have been sunk
        if self.__main_board[i][j].get_linked_ship() != None:
            if self.__main_board[i][j].get_linked_ship().get_is_sunk():
                
                self.__sunk_ships += 1
                print("You sank a " + str(self.__main_board[i][j].get_linked_ship()) + "!")
                for coor in self.__main_board[i][j].get_linked_ship().get_coordinate_list():
                    self.__main_board[coor[0]][coor[1]].sink_this_tile()
                    

        

    
    def is_all_sunk(self):
        """
        Returns if all ships have been sunk
        :return: bool, if all ships have been sunk
        """
        return self.__sunk_ships == len(self.__ships_obj_list)
    
    #Getters
    def get_error_signal(self):
        """
        Getter for the error signal
        :return: bool, the error signal
        """
        return self.__error_signal
    

    #Private
    __main_board = []
    __ships_obj_list = []
    __sunk_ships = 0
    __error_signal = False
    
    
def play_game(board_obj):
    """
    Plays the game until all ships are sunk or the user quits.
    An input error will not cause the game to stop.
    
    :param board_obj: Board, the board object
    :return: None
    """
    while True:
        
        board_obj.print_board()
        
        if board_obj.is_all_sunk():
            print("Congratulations! You sank all enemy ships.")
            return
        
        print("Enter place to shoot (q to quit): ", end="")
        
        command_ = input()
        
        #Exception 6
        if command_ == "q" or command_ == "Q":
            print("Aborting game!")
            return
        
        coordinate_tuple_ = coordinate_to_index(command_)
        
        #Exception 4
        if coordinate_tuple_[0] == "Error" or coordinate_tuple_[1] == "Error":
            print("Invalid command!")
            continue
        
        #here, the coordinate is already valid. 
        #Check if it have been shot, update the tile, update if a ship have been sunk
        board_obj.shoot_action(coordinate_tuple_)
        
        
        
    

    
def main():
    """
    Main function. 
    Initialize the board and then plays the game
    
    :return: None
    """
    
    file_name = input("Enter file name: ")
    
    #Initialize board
    game_board = Board(file_name)
    
    #Play the game
    if not game_board.get_error_signal():
        play_game(game_board)
        
    #Game ends here



if __name__ == "__main__":
    main()