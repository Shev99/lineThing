from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    A = y1 - y0
    B = -1 * (x1 - x0)
    x = x0
    y = y0

    d = (2 * A) + B #simplified formula for distance 
    while x <= x1:
        plot(x,y)
        x++
        if d > 0:
            y++
            d+=2 * B
        x++
        d+=2 * A

    
