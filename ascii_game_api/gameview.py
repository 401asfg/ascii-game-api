from ascii_renderer import Renderable, Screen, Sprite

from ascii_game_api.game import Game


# TODO: test


class GameView(Renderable):
    """
    A renderable view of a game through a screen
    """

    _game: Game
    _hud: Screen

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

    def render(self) -> str:
        """
        :return: A rendering of the hud with the x to x + hud.width - 1 columns 
        and y to y + hud.height - 1 rows of the given game drawn under it; 
        The empty space sprites of the hud don't hide the sprites of the game
        """
        game_screen = self._build_game_screen_from_game()
        self.hud.overlay(game_screen)
        return game_screen.render()

    def _build_game_screen_from_game(self) -> Screen:
        """
        Produces a screen with the x to x + hud.width - 1 columns and y to y + 
        hud.height - 1 rows of the game drawn onto it; if two game objects have 
        the same x and y values, draws the one with the larger depth; if both 
        gameobjects also have the same depth, draws the one with the larger index
        """
        sprite_buffer_depth_value_index = 1
        sprite_buffer: dict[tuple[int, int], tuple[Sprite, int]] = {}

        game_screen_width = self._hud.width
        game_screen_height = self._hud.height
        game_screen = Screen(self._hud.sprite_empty,
                             game_screen_width,
                             game_screen_height)

        def in_view(gameobject):
            x = gameobject.x
            y = gameobject.y

            left = self.x
            top = self.y

            right = left + game_screen_width
            bottom = top + game_screen_height

            return left <= x < right and top <= y < bottom

        def update_sprite_buffer_item(gameobject):
            coordinates = (gameobject.x, gameobject.y)
            sprite = gameobject.sprite
            depth = gameobject.depth

            if coordinates not in sprite_buffer.keys() \
               or sprite_buffer[coordinates][sprite_buffer_depth_value_index] >= depth:
                sprite_buffer[coordinates] = (sprite, depth)

        def build_sprite_buffer_from_game():
            [update_sprite_buffer_item(gameobject)
             for gameobject in self.game
             if in_view(gameobject)]

        build_sprite_buffer_from_game()

        def draw_sprite_buffer_to_game_screen():
            [game_screen.draw(sprite, x, y)
             for (x, y), (sprite, _) in sprite_buffer.items()]

        draw_sprite_buffer_to_game_screen()
        return game_screen

    @property
    def game(self) -> Game:
        return self._game

    @property
    def hud(self) -> Screen:
        return self._hud
