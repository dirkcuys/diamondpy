# Recursive implementation of the diamond square algorith
#
# Author: Dirk Uys
# License: BSD

import random
from PIL import Image, ImageDraw


def calc_diamond( grid, row, col, size, k):
    scale = k*2*size/len(grid[0])
    grid[row][col] = (grid[row-size][col-size]+grid[row-size][col+size]+grid[row+size][col-size]+grid[row+size][col+size])/4.0 + scale*random.uniform(-1.0, 1.0)


def calc_square( grid, row, col, size, k):
    cap = len(grid[0])
    # scale = some constant times the size of current square divided by size of grid
    scale = k*2*size/len(grid[0])
    ave = 0
    cnt = 0
    if row-size >= 0:
        ave += grid[row-size][col]
        cnt += 1
    if col-size >= 0:
        ave += grid[row][col-size]
        cnt += 1
    if col+size < cap:
        ave += grid[row][col+size]
        cnt += 1
    if row+size < cap:
        ave += grid[row+size][col]
        cnt += 1
    grid[row][col] = ave/cnt + scale*random.uniform(-1.0, 1.0)


def ds (grid, tr, tc, br, bc, k):
    # tr - top row, tc - top column, etc...
    size = br - tr
    # should be the same as bc - tc
    if size == 1:
        return

    calc_diamond(grid, tr+size/2, tc+size/2, size/2, k)

    calc_square(grid, tr, tc+size/2, size/2, k)
    calc_square(grid, br, tc+size/2, size/2, k)
    calc_square(grid, tr+size/2, tc, size/2, k)
    calc_square(grid, tr+size/2, bc, size/2, k)

    ds(grid, tr, tc, tr+size/2, tc+size/2, k)
    ds(grid, tr, tc+size/2, tr+size/2, bc, k)
    ds(grid, tr+size/2, tc, br, tc+size/2, k)
    ds(grid, tr+size/2, tc+size/2, br, bc, k)


def diamond( n ):
    grid = [ [0 for i in range(2**n+1)] for j in range(2**n+1)]

    # initialize grid
    grid[0][0] = random.uniform(0.0, 1.0)
    grid[0][-1] = random.uniform(0.0, 1.0)
    grid[-1][0] = random.uniform(0.0, 1.0)
    grid[-1][-1] = random.uniform(0.0, 1.0)

    ds(grid, 0, 0, 2**n, 2**n, 0.5)

    image = Image.new('RGB', (2**n+1, 2**n+1) )
    draw = ImageDraw.Draw(image)
    for y in range(2**n+1):
        for x in range(2**n+1):
            color = int(grid[y][x]*255)
            image.putpixel( (x,y), (color, color, color))

    image.save('heightmap2.1.png')

diamond(10)
