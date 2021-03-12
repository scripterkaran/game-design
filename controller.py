class MovementControllerInterface:
    """ abstracts the directional inputs """

    def move_up(self):
        self.set_y(self.player_instance.y - 1)

    def move_down(self):
        self.set_y(self.player_instance.y + 1)

    def move_right(self):
        self.set_x(self.player_instance.x + 1)

    def move_left(self):
        self.set_x(self.player_instance.x - 1)

    def set_x(self, x):
        self.player_instance.move_x(x)

    def set_y(self, y):
        self.player_instance.move_y(y)


class HardwareControllerBase(object):

    def __init__(self, player_instance):
        self.player_instance = player_instance

    def __repr__(self):
        return self.__class__.__name__


class KeyboardController(HardwareControllerBase, MovementControllerInterface):
    pass


class DPadController(HardwareControllerBase, MovementControllerInterface):
    pass


class SwipeController(HardwareControllerBase, MovementControllerInterface):
    pass
