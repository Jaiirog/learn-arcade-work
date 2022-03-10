"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

"""
# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# --- Draw the barn ---

# Barn cement base
arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BISQUE)

# Bottom half
arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)

# Left-bottom window
arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)

# Right-bottom window
arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)

# Barn door
arcade.draw_rectangle_filled(190, 230, 100, 100, arcade.color.BLACK_BEAN)

# Rail above the door
arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.BONE)

# Draw second level of barn
arcade.draw_polygon_filled([[20, 350],
                            [100, 470],
                            [280, 470],
                            [360, 340]],
                            arcade.color.BROWN)

# Draw loft of barn
arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BROWN)

# Left-top window
arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.BLACK)

# Right-top window
arcade.draw_rectangle_filled(250, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(250, 440, 20, 30, arcade.color.BLACK)

# Draw 2nd level door
arcade.draw_rectangle_outline(190, 310, 30, 60, arcade.color.BONE, 5)

# --- Draw the tractor ---

# Draw the engine
arcade.draw_rectangle_filled(600, 120, 140, 70, arcade.color.GRAY)
arcade.draw_rectangle_filled(590, 105, 90, 40, arcade.color.BLACK)

# Draw the smoke stack
arcade.draw_rectangle_filled(580, 175, 10, 40, arcade.color.BLACK)

# Back wheel
arcade.draw_circle_filled(490, 110, 50, arcade.color.BLACK)
arcade.draw_circle_filled(490, 110, 45, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(490, 110, 35, arcade.color.OLD_LACE)
arcade.draw_circle_filled(490, 110, 10, arcade.color.RED)

# Front wheel
arcade.draw_circle_filled(650, 90, 30, arcade.color.BLACK)
arcade.draw_circle_filled(650, 90, 25, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(650, 90, 18, arcade.color.OLD_LACE)
arcade.draw_circle_filled(650, 90, 5, arcade.color.RED)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

"""






import arcade

arcade.open_window(800,600,"Dibujo_1")

arcade.set_background_color(arcade.color.BABY_BLUE)

arcade.start_render()

#Road

arcade.draw_lrtb_rectangle_filled(0, 800, 200,0, arcade.color.DIM_GRAY)
arcade.draw_lrtb_rectangle_filled(9,49,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(89,129,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(169,209,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(249,289,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(329,369,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(409,449,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(489,529,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(569,609,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(649,689,110,100, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(729,769,110,100, arcade.color.BONE)

#Draw Sun

arcade.draw_circle_filled(740, 540, 40, arcade.color.GOLD)

#Eyes
arcade.draw_circle_filled(725,555,7, arcade.color.BLACK)
arcade.draw_circle_filled(750,555,7, arcade.color.BLACK)
#Smile
arcade.draw_arc_outline(740, 530, 20, 10,
                       arcade.color.BLACK,
                       190, 350, 10)

texture=arcade.load_texture("coche_azul.png")
texture2=arcade.load_texture("coche_azul_alreves.png")
arcade.draw_texture_rectangle(170, 180,texture.width -  1400, texture.height-787, texture, 0)
arcade.draw_texture_rectangle(630, 70,texture2.width - 1400, texture2.height-787, texture2, 0)


arcade.finish_render()
arcade.run()

