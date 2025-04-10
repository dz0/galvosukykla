from turtle import *
from math import *
import random


reset()
speed(0)



def polygon(n, a=100):
    for i in range(n):
        forward(a); left(360.0/n)

def decorate(cmd, xpensize=None, xcolor=None, dofill=False):
    if dofill: fill(True)
    if xpensize: bckup_pensize = pensize(); pensize(xpensize)
    if xcolor: bckup_coolor = color(); color(xcolor)

    print "cmd:", cmd
    exec(cmd)  # main thing

    if xcolor: color(*bckup_coolor)
    if xpensize: pensize(bckup_pensize)
    if dofill: fill(False)
    
        

def calc_sutff(n, r):
    angle = (90-180.0/n)/180.0*pi
    a_half = r * cos(angle)
    h = r * sin(angle)
    return a_half, h
        
def calc_a(n, r):
    a_half, h = calc_sutff(n, r)
    return  a_half * 2
    
def find_starting_point_from_centre( n, r, cx=0, cy=0):
    a_half, h = calc_sutff(n, r)
    print "starting point", (cx-a_half, cy-h)
    up()
    goto(cx-a_half, cy-h)
    down()
    return (cx-a_half, cy-h)
    


#~ x0, y0 = -200, 0
#~ a0 = 200
#~ r0 = 100 * sin(45/360.0*pi)
#~ cx, cy = x0+a0/2, y0+a0/2

r0 = 100
a0=calc_a(4, r0)



### Variations ###
variations_rows = [ (0, 1, 2), (2, 1, 0), (1, 2, 0) ]
variations_cols = [ (2, 1, 0), (1, 2, 0), (0, 1, 2) ]
variations_3 = [  (1, 2, 0), (2, 1, 0),(0, 1, 2) ]

for variation in [variations_rows, variations_cols, variations_3]:
    random.shuffle(variation)



#~ cells = [ (row, col)
            #~ for row in range(3)
            #~ for col in range(3)
        #~ ]
#~ print "cells", cells        
#~ random.shuffle(cells)
cells = []
for (rows,cols,third) in zip (variations_rows, variations_cols, variations_3):
     cells.extend( zip(rows, cols, third) )
     
print "cells suffled", cells


for row in range(3):
    for col in range(3):

        cell_size = a0+20
        cy = cell_size - row * cell_size
        cx = -cell_size +col * cell_size

        up(); goto(cx, cy)
        

        #~ find_starting_point_from_centre(4, r0, cx, cy)
        #~ polygon(4, calc_a(4, r0))

        var_row, var_col, var3 = cells.pop()  # get mixed features 
        print "== left cells", cells

        n = var_col+4; r=r0/(var3+1); find_starting_point_from_centre(n, r, cx, cy)
        decorate("polygon(%s, %s)" % (n, calc_a(n, r)), xcolor="blue", xpensize=1+var_row*5)

 
hideturtle()
exitonclick()

