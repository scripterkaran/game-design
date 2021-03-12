from random import randrange


class Square:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player_occupied = False
        self.treasure_occupied = False
        self.occupied_player = None

    def remove_player(self):
        self.player_occupied = False
        self.occupied_player = None

    def place_player(self, player):
        self.player_occupied = True
        self.occupied_player = player

    def __repr__(self):
        return f"Square({self.x},{self.y}): Has Treasure: {self.treasure_occupied}"


class Board:

    def __init__(self, number_of_rows, number_of_columns, game):

        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.grid = []
        self.make_grid()

        self.treasure = None
        self.player = None
        self.game = game
        self.treasure_x = None
        self.treasure_y = None

    def visualize_board(self):
        for row in self.grid:
            print('row', row)

    def make_grid(self):
        for i in range(self.number_of_rows):
            row = []
            for j in range(self.number_of_columns):
                row.append(Square(i, j))
            self.grid.append(row)

    def is_valid_move_x(self, x):
        return 0 <= x <= self.number_of_rows - 1

    def is_valid_move_y(self, y):
        return 0 <= y <= self.number_of_columns - 1

    def init_board(self):
        self.place_treasure_randomly()

    def place_treasure_randomly(self):
        self.treasure_x = randrange(self.number_of_rows)
        self.treasure_y = randrange(self.number_of_columns)
        self.grid[self.treasure_x][self.treasure_y].treasure_occupied = True
        print('Placing Treasure at', self.treasure_x, self.treasure_y)

    def remove_treasure(self):
        self.grid[self.treasure_x][self.treasure_y].treasure_occupied = False

    def remove_player_from_current_square(self, player):
        old_square = self.grid[player.x][player.y]
        old_square.remove_player()

    def move_x_and_occupy_square(self, player, x):
        """
        Emitted from Player class, after valid move check
        Removes the player from current square block and move to next square block
        """
        self.remove_player_from_current_square(player)
        new_square = self.grid[x][player.y]
        new_square.place_player(player)

    def move_y_and_occupy_square(self, player, y):
        """
        Emitted from Player class, after valid move check
        Removes the player from current square block and move to next square block
        """
        self.remove_player_from_current_square(player)

        new_square = self.grid[player.x][y]
        new_square.place_player(player)

    def check_if_found_treasure(self, player):
        if self.grid[player.x][player.y].treasure_occupied:
            self.game.update_score()
            self.remove_treasure()
            self.place_treasure_randomly()
