import random
from PIL import Image, ImageDraw


def ds( grid, row, col, size, k ):
    
    scale = k*size/len(grid[0])

    grid[row+size/2][col+size/2] = (grid[row][col]+grid[row][col+size]+grid[row+size][col]+grid[row+size][col+size])/4.0 + scale*random.uniform(-1.0, 1.0)


    grid[row][col+size/2] = (grid[row][col]+grid[row][col+size])/2.0 + scale*random.uniform(-1.0, 1.0)
    grid[row+size][col+size/2] = (grid[row+size][col]+grid[row+size][col+size])/2.0 + scale*random.uniform(-1.0, 1.0)
    grid[row+size/2][col] = (grid[row][col]+grid[row+size][col])/2.0 + scale*random.uniform(-1.0, 1.0)
    grid[row+size/2][col+size] = (grid[row][col+size]+grid[row+size][col+size])/2.0 + scale*random.uniform(-1.0, 1.0)
    

def diamond( n , k ):
    grid = [ [random.uniform(0.0, 1.0) for i in range(2**n+1)] for j in range(2**n+1)]

    grid[0][0] = random.uniform(0.0, 1.0)
    grid[0][-1] = random.uniform(0.0, 1.0)
    grid[-1][0] = random.uniform(0.0, 1.0)
    grid[-1][-1] = random.uniform(0.0, 1.0)

    size = 2**n
    while size > 1:
        y = 0
        while y < 2**n:
            x = 0
            while x < 2**n:
                ds(grid, y, x, size, k)
                x += size
            y+= size
        size /= 2

    image = Image.new('RGB', (2**n+1, 2**n+1) )
    draw = ImageDraw.Draw(image)
    for y in range(2**n+1):
        for x in range(2**n+1):
            color = int(grid[y][x]*255)
            image.putpixel( (x,y), (color, color, color))

    image.save('heightmap.png')


diamond(9, 0.5)
