"""
Tic Tac Toe Player
"""


X = "X"
O = "O"
EMPTY = None
TOTAL_UTILITY = 0


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    :param board:
    :return player_name: str, X or O
    """
    if board == initial_state():
        return "X"
    else:
        count_x = 0
        count_o = 0
        for row in board:
            for cell in row:
                if cell == "X":
                    count_x += 1
                elif cell == "O":
                    count_o += 1
                    
        if count_x > count_o:
            return "O"
        else:
            return "X"


def actions(board):
    """
    :param board:
    :return actions: Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making an imaginary move (i, j) on the board.
    """
    i, j = action
    new_board = [row.copy() for row in board]
    if new_board[i][j] != EMPTY:
        raise Exception("Invalid action")
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def utility(board):
    """
    Assuming terminal(board) == True <-> the game is over
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board, depth=0):
    """
    Returns the optimal action for the current player on the board.
    
    Assume the board is not a terminal board in the first iteration of the function
    "X" is max, "O" is min
    depending n the turn, minmax() will asume the role of max() or min(), thus no function like that is necessary
    """
   
        
    if terminal(board):
        TOTAL_UTILITY += utility(board)
        return TOTAL_UTILITY
        
        
    elif player(board) == "X": #max is playing
        
        for action in actions(board):
            
            #1) generate new node and new best_action
            new_node_n = result(board, action)
            
            best_action_utility = -10000
            
            
            action_utility = minimax(new_node_n, depth+1)
            if action_utility > best_action_utility:
                best_action_utility = action_utility
                best_action = action
        
        if depth == 0: 
            return best_action
        else:
            return best_action_utility
            
            
    elif player(board) == "O": #min is playing
        
        for action in actions(board):
            
            #1) generate new node and new best_action tuple.
            new_node_n = result(board, action)
            
            worse_action_utility = 10000
            
            
            action_utility = minimax(new_node_n, depth+1)
            if action_utility < worse_action_utility:
                worse_action_utility = action_utility
                worse_action = action
                worse_action_total_utility = TOTAL_UTILITY
            elif action_utility == worse_action_utility and action_utility:
                worse_action = action
                worse_action_utility = action_utility

       
        if depth == 0: 
            return worse_action
        else:
            return worse_action_utility, worse_action_total_utility
        
        
board = initial_state()
board = result(board, (0, 0))
board = result(board, (0, 1))
board = result(board, minimax(board))
print("hola")