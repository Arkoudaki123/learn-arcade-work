"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color((135, 206, 250))

# Get ready to draw
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 599, 240, 0, arcade.color.LIGHT_SKY_BLUE)

arcade.draw_lrtb_rectangle_filled(0, 599, 375, 240, arcade.color.WHITE)

arcade.draw_circle_filled(300, 305, 35, arcade.color.YELLOW)

arcade.draw_line(225, 300, 375, 300, arcade.color.YELLOW, 3)
arcade.draw_line(300, 235, 300, 375, arcade.color.YELLOW, 3)
arcade.draw_line(240, 245, 360, 360, arcade.color.YELLOW, 3)
arcade.draw_line(360, 245, 240, 360, arcade.color.YELLOW, 3)

arcade.draw_circle_filled(315, 303, 5, arcade.color.PALE_BROWN)

arcade.draw_circle_filled(283, 303, 5, arcade.color.PALE_BROWN)

arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
