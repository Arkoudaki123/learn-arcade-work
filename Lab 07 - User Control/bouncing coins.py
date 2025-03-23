""""
Platformer
"""
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

CHARACTER_SCALING = 1
TITLE_SCALING = 0.5

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.wall_list = None
        self.player_list = None
        self.player_sprite = None

        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        image_source = ":resources:images/animated_characters/robot/robot_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:image/tiles/grassMid.png")
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

    def on_draw(self):

        self.clear()

def main():

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
        main()