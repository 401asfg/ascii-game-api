from ascii_renderer import Renderable, Screen

from ascii_game_api.game import Game


# TODO: test
# TODO: implement game screen and hud support


class GameView(Renderable):
    """
    A view of a game through a screen
    """

    _game: Game
    _hud: Screen
    _game_screen: Screen

    x: int
    y: int

    def __init__(self, game: Game, hud: Screen, x: int = 0, y: int = 0):
        """
        Initializes the class

        :param game: The game to draw onto the given screen
        :param hud: The graphics rendered on top of the game's view; the view 
        of the game has the same properties as this hud
        :param x: The x coordinate of the left side of the screen in the game
        :param y: The y coordinate of the top side of the screen in the game
        """
        self._game = game
        self._hud = hud
        self.x = x
        self.y = y

        self._game_screen = Screen(self.hud.empty_space_sprite,
                                   self.hud.width,
                                   self.hud.width)

    def render(self) -> str:
        """
        :return: A rendering of the hud with the x to x + hud.width - 1 columns 
        and y to y + hud.height - 1 rows of the given game drawn under it; 
        The empty space sprites of the hud don't hide the sprites of the game
        """
        self._draw_game()
        self.hud.overlay(self._game_screen)
        return self._game_screen.render()

    def _draw_game(self):
        """
        Clears the game_screen and draws the x to x + game_screen.width - 1 columns and y to 
        y + game_screen.height - 1 rows of the game onto the game_screen
        """
        self._game_screen.clear()

        def in_view(game_object):
            x = game_object.x
            y = game_object.y

            left = self.x
            top = self.y
            right = left + self._game_screen.width
            bottom = top + self._game_screen.height

            return left <= x < right and top <= y < bottom

        def draw(game_object):
            self._game_screen.draw(game_object.sprite,
                                   game_object.x,
                                   game_object.y)

        [draw(game_object)
         for game_object in self.game
         if in_view(game_object)]

    @property
    def game(self) -> Game:
        return self._game

    @property
    def hud(self) -> Screen:
        return self._hud
