# Import the turtle graphics library
import turtle
import colorsys
# Set up the turtle graphics window size
turtle.setup(800, 800)
# Setting the drawing speed (1 is slow)
turtle.speed(1)
# Setting the number of animation frames
turtle.tracer(10)
# Setting the width of the turtle's pen
turtle.width(2)
# Setting the background color
turtle.bgcolor("black")
# Loop to draw the pattern
for i in range(25):
    for j in range(15):
        # Set the turtle's color based on the hue and saturation
        turtle.color(colorsys.hsv_to_rgb(j/15, i/25, 1))
        turtle.right(90)  # Turn right by 90 degrees
        turtle.circle(200 - i * 4, 90)  # Draw a quarter circle
        turtle.left(90)  # Turn left by 90 degrees
        turtle.circle(200 - i * 4, 90)  # Draw another quarter circle
        turtle.right(180)  # Turn around by 180 degrees
        turtle.circle(50, 24)  # Draw a small arc

turtle.hideturtle()  # Hide the turtle cursor
turtle.done()  # Finish the drawing
