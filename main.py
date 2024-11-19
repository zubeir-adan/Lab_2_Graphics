import cairo
import math

# Create the surface and context
width, height = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)
context.set_source_rgb(1, 1, 1)  # White color
context.rectangle(0, 0, width, height)  # Cover the entire surface
context.fill()

# Lawn color (RGB)
lawn_color = (0.3, 0.8, 0.3)  # Green

# Ground structure
context.set_source_rgb(*lawn_color)  # Set lawn color
context.move_to(70, 158)
context.line_to(40, 170)
context.line_to(140, 200)
context.line_to(240, 150)
context.line_to(190, 135)

context.move_to(40, 170)
context.line_to(40, 180)
context.line_to(140, 210)
context.line_to(240, 160)
context.line_to(240, 150)

context.move_to(140, 200)
context.line_to(140, 210)

context.set_source_rgb(0, 0, 0)
context.set_line_width(0.8)
context.stroke()

# Wall structure
context.move_to(120, 180)
context.line_to(120, 95)
context.line_to(70, 80)
context.line_to(70, 165)
context.close_path()

context.move_to(120, 175)
context.line_to(70, 160)
context.line_to(70, 165)
context.line_to(120, 180)
context.close_path()

context.set_source_rgb(0, 0, 0)
context.set_line_width(0.8)
context.stroke()

# Adding Windows
context.move_to(110, 160)
context.line_to(110, 140)
context.line_to(97, 135)
context.line_to(97, 155)
context.close_path()

context.move_to(93, 155)
context.line_to(93, 135)
context.line_to(80, 130)
context.line_to(80, 150)
context.close_path()

context.move_to(110, 128)
context.line_to(110, 110)
context.line_to(97, 105)
context.line_to(97, 123)
context.close_path()

context.move_to(93, 105)
context.line_to(80, 100)
context.line_to(80, 119)
context.line_to(93, 123)
context.close_path()

context.stroke()

# Draw the back roof (angled for 3D effect)
context.move_to(60, 85)
context.line_to(145, 45)
context.line_to(175, 35)
context.line_to(90, 75)
context.close_path()

# Draw the front roof (angled for 3D effect)
context.move_to(175, 35)
context.line_to(200, 52.5)
context.line_to(115, 95)
context.line_to(90, 75)
context.line_to(175, 35)
context.close_path()

# Chimney (Front part)
context.move_to(160, 45)
context.line_to(160, 60)
context.line_to(165, 60)
context.line_to(165, 47.5)
context.close_path()

# Chimney (Lateral part)
context.move_to(165, 47.5)
context.line_to(165, 60)
context.line_to(172.5, 55)
context.line_to(172.5, 45)
context.close_path()

# Chimney (Top part)
context.move_to(160, 45)
context.line_to(165, 47.5)
context.line_to(172.5, 55)
context.line_to(170, 37.5)
context.line_to(160, 45)
context.close_path()

context.set_line_width(0.8)
context.set_source_rgb(0, 0, 0)
context.stroke()

# More structure lines for the front side of the house
context.move_to(120, 180)
context.line_to(120, 100)
context.line_to(190, 65)
context.line_to(190, 145)

context.move_to(155, 150)
context.line_to(175, 140)
context.line_to(185, 145)
context.line_to(165, 155)
context.close_path()

context.move_to(155, 150)
context.line_to(155, 165)
context.line_to(180, 170)
context.line_to(200, 160)
context.line_to(200, 155)
context.line_to(185, 150)
context.line_to(165, 160)
context.line_to(180, 165)
context.line_to(180, 170)
context.move_to(180, 165)
context.line_to(200, 155)
context.move_to(165, 160)
context.line_to(165, 155)
context.move_to(185, 150)
context.line_to(185, 145)

context.move_to(120, 180)
context.line_to(155, 160)
context.move_to(190, 145)
context.line_to(185, 147)

context.move_to(155, 150)
context.line_to(155, 110)
context.line_to(175, 100)
context.line_to(175, 140)

context.move_to(157, 110)
context.line_to(157, 145)
context.line_to(165, 141)
context.line_to(165, 106)

context.move_to(130, 130)
context.line_to(130, 110)
context.line_to(138, 98)
context.line_to(138, 120)
context.close_path()

context.move_to(142, 98)
context.line_to(150, 90)
context.line_to(150, 110)
context.line_to(142, 120)
context.close_path()

context.set_source_rgb(0, 0, 0)
context.set_line_width(0.8)
context.stroke()

# Save the drawing
surface.write_to_png("house.png")
print("Drawing saved as Updated_House.png")


