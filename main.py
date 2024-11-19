import cairo
import math

# Set up canvas
width, height = 260, 260
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Background
context.set_source_rgb(1, 1, 1)  # White background
context.rectangle(0, 0, width, height)
context.fill()

# Lawn with green fill
context.set_source_rgb(0, 0.5, 0)  # Green color
context.move_to(70, 158)
context.line_to(40, 170)
context.line_to(140, 200)
context.line_to(240, 150)
context.line_to(190, 135)
context.close_path()
context.fill()  # Fill the main lawn area

context.move_to(40, 170)
context.line_to(40, 180)
context.line_to(140, 210)
context.line_to(240, 160)
context.line_to(240, 150)
context.close_path()
context.fill()  # Fill the secondary lawn area

context.move_to(140, 200)
context.line_to(140, 210)
context.close_path()
context.fill()  # Fill the connecting segment of the lawn

# Outlines for the lawn
context.set_source_rgb(0, 0, 0)  # Black color for the outlines
context.set_line_width(0.8)  # Ensure the outlines are visible
context.move_to(70, 158)
context.line_to(40, 170)
context.line_to(140, 200)
context.line_to(240, 150)
context.line_to(190, 135)
context.close_path()
context.stroke()

context.move_to(40, 170)
context.line_to(40, 180)
context.line_to(140, 210)
context.line_to(240, 160)
context.line_to(240, 150)
context.close_path()
context.stroke()

context.move_to(140, 200)
context.line_to(140, 210)
context.close_path()
context.stroke()


# Walls
# Left wall
context.set_source_rgb(1, 0.98, 0.8)  # Cream color
context.move_to(120, 180)
context.line_to(120, 95)
context.line_to(70, 80)
context.line_to(70, 165)
context.close_path()
context.fill()

# Side wall with cream color
context.set_source_rgb(1, 0.98, 0.8)  # Cream color
context.move_to(120, 180)
context.line_to(120, 100)
context.line_to(190, 65)
context.line_to(190, 145)
context.close_path()
context.fill()  # Fill with cream color

# Side wall additional structure (inner lines)
context.set_source_rgb(0, 0, 0)  # Black for the inner lines
context.move_to(155, 150)
context.line_to(175, 140)
context.line_to(185, 145)
context.line_to(165, 155)
context.close_path()
context.stroke()


# Wall outlines
context.set_source_rgb(0, 0, 0)
context.set_line_width(0.8)
context.stroke()

# Windows
# Bottom right window
context.move_to(110, 160)
context.line_to(110, 140)
context.line_to(97, 135)
context.line_to(97, 155)
context.close_path()

# Bottom left window
context.move_to(93, 155)
context.line_to(93, 135)
context.line_to(80, 130)
context.line_to(80, 150)
context.close_path()

# Top right window
context.move_to(110, 128)
context.line_to(110, 110)
context.line_to(97, 105)
context.line_to(97, 123)
context.close_path()

# Top left window
context.move_to(93, 105)
context.line_to(80, 100)
context.line_to(80, 119)
context.line_to(93, 123)
context.close_path()
context.stroke()

# Roof
# Back roof
context.set_source_rgb(0.2, 0.2, 0.2)  # Dark grey color
context.move_to(60, 85)
context.line_to(145, 45)
context.line_to(175, 35)
context.line_to(90, 75)
context.close_path()
context.fill()

# Front roof
context.set_source_rgb(0.2, 0.2, 0.2)  # Dark grey color
context.move_to(175, 35)
context.line_to(200, 52.5)
context.line_to(115, 95)
context.line_to(90, 75)
context.line_to(175, 35)
context.close_path()
context.fill()

# Chimney
context.move_to(160, 45)
context.line_to(160, 60)
context.line_to(165, 60)
context.line_to(165, 47.5)
context.close_path()
context.move_to(165, 47.5)
context.line_to(165, 60)
context.line_to(172.5, 55)
context.line_to(172.5, 45)
context.close_path()
context.move_to(160, 45)
context.line_to(165, 47.5)
context.line_to(172.5, 55)
context.line_to(170, 37.5)
context.line_to(160, 45)
context.close_path()
context.set_line_width(0.8)
context.set_source_rgb(0, 0, 0)
context.stroke()

# Side wall
context.move_to(120, 180)
context.line_to(120, 100)
context.line_to(190, 65)
context.line_to(190, 145)
context.move_to(155, 150)
context.line_to(175, 140)
context.line_to(185, 145)
context.line_to(165, 155)
context.close_path()

# Front details
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

# Side windows
# Left side window
context.move_to(130, 130)
context.line_to(130, 110)
context.line_to(138, 98)
context.line_to(138, 120)
context.close_path()

# Right side window
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
print("Drawing saved as 2D_House_Colored.png")
