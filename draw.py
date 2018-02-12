from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    A = y1 - y0
    B = -1 * (x1 - x0)
    x = x0
    y = y0

    d = (2 * A) + B #simplified formula for distance 
    while x <= x1:
        plot(screen,color,x,y)
        if d > 0:
            y+=1
            d+=2 * B
        x+=1
        d+=2 * A

    
