"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Robert Belk.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
ricky = rg.SimpleTurtle()
bobby = rg.SimpleTurtle()
ricky.pen = rg.Pen('yellow',5)
bobby.pen = rg.Pen('Teal',5)
ricky.speed = 15
bobby.speed = 15
size = 100
for k in range(10):
    ricky.draw_square(size)
    ricky.pen_up()
    ricky.right(45)
    ricky.forward(10)
    ricky.left(45)
    ricky.pen_down()
    size = size - 10
    bobby.draw_circle(size)
    bobby.pen_up()
    bobby.right(10)
    bobby.forward(10)
    bobby.left(10)
    bobby.pen_down()
    size = size - 10

window.close_on_mouse_click()
