from display import *

def oct(x0,y0,x1,y1):
    if (x0 == x1):
        return 0
    else:
        m = (float(y1) - y0)/(x1 - x0)
    
    if (m==0):
        return 0
    elif ((m > 0) & (m <= 1)):
        return 1
    elif (m > 1):
        return 2
    elif ((m < -1)):
        return 4
    else:
        return 3
    
def testUndefinedLine(x0,x1):
    if (x0 == x1):
        return True


def draw_line( x0, y0, x1, y1, screen, color ):
    A = y1 - y0
    B = -1 * (x1 - x0)
    x = x0
    y = y0
    m = oct(x,y,x1,y1)
    
    if (testUndefinedLine(x,x1)):         #vertical line
        while (y <= y1):
            plot (screen, color, x, y)
            y += 1
    elif (m==0):                          #horizontal line
        while (x <= x1):
            plot (screen, color, x, y)
            x += 1
    elif (m == 1):                        #quad 1
        d = (2 * A) + B #simplified formula for distance 
        while x <= x1:
            plot(screen,color,x,y)
            if d > 0:
                y+=1
                d+=2 * B
            x+=1
            d+=2 * A
    elif (m == 2):                         #quad 2
        d =(2 * B) + A #formula reversed for quad 2
        while y <= y1:
            plot (screen,color,x,y)
            if d < 0:
                x += 1
                d+=2 * A
            y+=1
            d+=2 * B
    elif (m == 3):                         #quad3
        d = A - 2 * B
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B
    elif (m == 4):                         #quad4
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
