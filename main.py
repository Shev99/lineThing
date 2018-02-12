from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0,0,500,450,screen,color)
draw_line(250,250,400,500,screen,color)
draw_line(250,250,250,500,screen,color)
draw_line(450,500,250,250,screen,color)

display(screen)
save_extension(screen, 'img.png')
