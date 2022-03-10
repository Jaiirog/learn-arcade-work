"""
import arcade

def main ():
    arcade.open_window(800, 600, "Dibujo_1")
    arcade.set_background_color(arcade.color.BABY_BLUE)
    arcade.start_render()

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
    arcade.run()

main()
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.BABY_BLUE)
arcade.start_render()

def grass ():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 4, 0, arcade.color.BITTER_LIME)

grass()



left_tree=180
rigth_tree=220

arcade.draw_lrtb_rectangle_filled(left_tree, rigth_tree, 140, 20, arcade.color.BROWN)
arcade.draw_circle_filled(200,150, 40, arcade.color.GREEN)



arcade.finish_render()
arcade.run()
