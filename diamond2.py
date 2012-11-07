import random
from PIL import Image, ImageDraw

def ds (grid, tr, tc, br, bc, k):
    # tr - top row, tc - top column, etc...
    size = br - tr
    # should be the same as bc - tc
    if size == 1:
        return

    # scale = some constant times the size of current square divided by size of grid
    scale = k*size/len(grid[0])

    grid[tr+size/2][tc+size/2] = \
        (grid[tr][tc]+grid[tr][bc]+grid[bc][tr]+grid[bc][br])/4.0# \
        #+ scale*random.uniform(0.0, 1.0)

    grid[tr][tc+size/2] = (grid[tr][tc]+grid[tr][bc])/2.0# + scale*random.uniform(0.0, 1.0)
    grid[br][tc+size/2] = (grid[br][tc]+grid[br][bc])/2.0# + scale*random.uniform(0.0, 1.0)
    grid[tr+size/2][tc] = (grid[tr][tc]+grid[br][tc])/2.0# + scale*random.uniform(0.0, 1.0)
    grid[tr+size/2][bc] = (grid[tr][bc]+grid[br][bc])/2.0# + scale*random.uniform(0.0, 1.0)

    ds(grid, tr, tc, tr+size/2, tc+size/2, k)
    ds(grid, tr, tc+size/2, tr+size/2, bc, k)
    ds(grid, tr+size/2, tc, br, tc+size/2, k)
    ds(grid, tr+size/2, tc+size/2, br, bc, k)


def diamond( n ):
    grid = [ [0.5 for i in range(2**n+1)] for j in range(2**n+1)]

    grid[0][0] = random.uniform(0.0, 1.0)
    grid[0][-1] = random.uniform(0.0, 1.0)
    grid[-1][0] = random.uniform(0.0, 1.0)
    grid[-1][-1] = random.uniform(0.0, 1.0)

    ds(grid, 0, 0, 2**n, 2**n, 0.1)

    image = Image.new('RGB', (2**n+1, 2**n+1) )
    draw = ImageDraw.Draw(image)
    for y in range(2**n+1):
        for x in range(2**n+1):
            color = int(grid[y][x]*255)
            image.putpixel( (x,y), (color, color, color))

    image.save('heightmap2.png')

diamond(8)
