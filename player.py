from controller import KeyboardController


class Player:

    def __init__(self, player_type):
        self.player_type = player_type


class BoardPlayer(Player):

    def __init__(self, x, y, player_type, board):
        self.x = x
        self.y = y
        self.controller = KeyboardController(player_instance=self)
        self.board = board
        super(BoardPlayer, self).__init__(player_type)

    def move_x(self, x):
        if self.board.is_valid_move_x(x):
            self.board.move_x_and_occupy_square(player=self, x=x)
            self.x = x
            self.board.check_if_found_treasure(player=self)
        else:
            print(f'Cannot move to x = {x} location. Out of bounds!')

    def move_y(self, y):
        if self.board.is_valid_move_y(y):
            self.board.move_y_and_occupy_square(player=self, y=y)
            self.y = y
            self.board.check_if_found_treasure(player=self)
        else:
            print(f'Cannot move to y = {y} location. Out of bounds!')

