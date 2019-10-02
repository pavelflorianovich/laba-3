from graph import canvasSize, run
from graph import penColor, brushColor, penSize
from graph import rectangle, circle, polygon
from math import sin, cos, pi

def fon(): 
    canvasSize(1200, 800)         # drawing size
    penColor(0 , 255 , 0)         # grass
    brushColor(0 , 245, 0)
    rectangle(0, 400, 1200, 800)
    penColor(200 , 230, 255)      # sky
    brushColor(200 , 230, 255)
    rectangle(0, 0, 1200, 400)

def tree(x, y, r, n):             # x, y - coordinates of the upper left corner of a rectangle 
    penColor(0 , 0 , 0)           # with the (70*n; 100*n) dimensios described around the cloud
    brushColor(0 , 0 , 0)         # n - parameter that sets the size of the tree
    rectangle(x + 30 * n, y + 50 * n, x + 40 * n, y + 100 * n) 
    brushColor(0 , 90 , 0)
    circle(x + 35 * n, y + 15 * n, r * n) # r - radius
    circle(x + 15 * n, y + 25 * n, r * n)
    circle(x + 55 * n, y + 25 * n, r * n)
    circle(x + 35 * n, y + 35 * n, r * n)
    circle(x + 20 * n, y + 50 * n, r * n)
    circle(x + 50 * n, y + 50 * n, r * n)
  
def house(x, y, n):               # n - parameter that sets the size of the house
    penColor (0 , 0 , 0)          # x, y - coordinates of the upper left edge of the house 
    brushColor(210 , 200 , 10) 
    rectangle(x , y, x + 200 * n, y + 150 * n)
    brushColor(255 , 100 , 100)
    polygon([(x, y),(x + 200 * n, y),(x + 100 * n, y - 100 * n),(x, y)])
    brushColor(150 , 150 , 255)
    penColor(255 , 100 , 10)
    rectangle(x + 50 * n, y + 50 * n, x + 150 * n, y + 100 * n)

def cloud(x, y, r, n):            # n - parameter that sets the size of the cloud
    penColor(0 , 0 , 0)           # x, y - coordinates of the upper left corner of a rectangle 
    brushColor(255 , 255 , 255)   # with the (50*n; 30*n) dimensios described around the cloud
    circle(x + 10 * n, y + 20 * n, r * n)
    circle(x + 20 * n, y + 20 * n, r * n)                                                                                                                                                                                                                                                                                                                                                                                                                          
    circle(x + 30 * n, y + 20 * n, r * n)
    circle(x + 40 * n, y + 20 * n, r * n)
    circle(x + 18 * n, y + 10 * n, r * n)
    circle(x + 32 * n, y + 10 * n, r * n)

def sun(x_center, y_center, radius, wave_height, definition, N): # N - number of rays
    brushColor("yellow")
    penColor(255 , 100 , 10)
    verts=[]
    t=0
    while t < ( 10 * N * definition + 1 ) :
        z_1 = ( pi / ( N * definition )) * t
        z_2 = ( pi / definition ) * t
        x = x_center + radius * (1 + wave_height * sin( z_2 )) * cos( z_1 )
        y = y_center + radius * (1 + wave_height * sin( z_2 )) * sin( z_1 )
        verts.append(( x, y ))  
        t += 1
    polygon (verts)

   
penSize( 2 )
fon()
sun(120, 110, 75, 0.07, 800, 22)
cloud(250, 70, 15, 4)
cloud(550, 130, 15, 3)
cloud(850, 60, 15, 3.5)
tree(415, 200, 15, 3.5)
tree(1000, 230, 15, 2.2)
house(100, 350, 1.5)
house(700, 350, 1.2)
run()
