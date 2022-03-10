""" Lab 7 - User Control """
"""
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
     Our Custom Window Class

    def __init__(self):
         Initializer

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.start_render()

        #Draw

        arcade.set_background_color(arcade.color.BABY_BLUE)

        # Road

        arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.DIM_GRAY)
        arcade.draw_lrtb_rectangle_filled(9, 49, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(89, 129, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(169, 209, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(249, 289, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(329, 369, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(409, 449, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(489, 529, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(569, 609, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(649, 689, 110, 100, arcade.color.BONE)
        arcade.draw_lrtb_rectangle_filled(729, 769, 110, 100, arcade.color.BONE)

        # Draw Sun

        arcade.draw_circle_filled(740, 540, 40, arcade.color.GOLD)

        # Eyes
        arcade.draw_circle_filled(725, 555, 7, arcade.color.BLACK)
        arcade.draw_circle_filled(750, 555, 7, arcade.color.BLACK)
        # Smile
        arcade.draw_arc_outline(740, 530, 20, 10,
                                arcade.color.BLACK,
                                190, 350, 10)

        texture = arcade.load_texture("coche_azul.png")
        texture2 = arcade.load_texture("coche_azul_alreves.png")
        arcade.draw_texture_rectangle(170, 180, texture.width - 1400, texture.height - 787, texture, 0)
        arcade.draw_texture_rectangle(630, 70, texture2.width - 1400, texture2.height - 787, texture2, 0)

        arcade.finish_render()



def main():
    window = MyGame()
    arcade.run()


main()

"""

'''


import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()

def on_mouse_press(self, x, y, button, modifiers):
    """ Called when the user presses a mouse button. """

    if button == arcade.MOUSE_BUTTON_LEFT:
        print("Left mouse button pressed at", x, y)
    elif button == arcade.MOUSE_BUTTON_RIGHT:
        print("Right mouse button pressed at", x, y)

'''
'''
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
texture = arcade.load_texture("coche_azul.png")

class Texture:
    def __init__(self, position_x, position_y, change_x, change_y, ):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        """ Draw the texture with the instance variables we have. """
        arcade.draw_texture_rectangle(170, 180, texture.width - 1400, texture.height - 787, texture, 0)

    def update(self):
        # Move the texture
        self.position_y += self.change_y
        self.position_x += self.change_x


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball

        arcade.draw_texture_rectangle(170, 180, texture.width - 1400, texture.height - 787, texture, 0)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.testure.draw()

    def update(self, delta_time):
        self.texture.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.texture.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.texture.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.texture.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.texture.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.texture.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.texture.change_y = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()
'''


import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

car = arcade.load_texture('coche_azul.png')


class Car(arcade.Sprite):
    def update(self, x, y):
        self.position_x = x
        self.position_y = y

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        car = Car("coche_azul.png", 1)

        car.position_x = SCREEN_WIDTH//2
        car.position_y = SCREEN_HEIGHT//2

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.car.update(x, y)


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()