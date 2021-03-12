#
# - Rectangle Board MxN
# - Bone - random coordinate inside MxN, 1 bone at a time shown on board.
# - Dog - start at 0,0
# - Dog - Using arrow keys, Dog can move 1 by 1 step on the board to reach Bone
# - Getting the bone +1 score
#
#
# Score 0/10
from board import Board
from player import BoardPlayer
from treasure import Treasure

from ui.ui import Dog, Bone


class Game:

    def __init__(self):
        self.board = Board(number_of_rows=5, number_of_columns=5, game=self)

        self.board.player = BoardPlayer(x=0, y=0, player_type=Dog(), board=self.board)
        self.board.treasure = Treasure(treasure_type=Bone())
        self.score = 0

    def start_game(self):
        self.board.init_board()

    def update_score(self):
        self.score += 1
        print('Score Updated:::', self.score)


g = Game()
g.start_game()

print("============")
g.board.visualize_board()
print('User standing at', g.board.player.x, g.board.player.y)
print('Using controller', f"'{g.board.player.controller}'")

while True:
    direction = input("Enter the direction you want to move...[w,a,s,d]   ")
    if direction == 'w':
        g.board.player.controller.move_up()
    if direction == 's':
        g.board.player.controller.move_down()
    if direction == 'a':
        g.board.player.controller.move_left()
    if direction == 'd':
        g.board.player.controller.move_right()
    print('User standing at', g.board.player.x, g.board.player.y)


