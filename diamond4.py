import random
from PIL import Image, ImageDraw


def calc_diamond( grid, row, col, size, k):
    scale = k*2*size/len(grid[0])
    grid[row][col] = (grid[row-size][col-size]+grid[row-size][col+size]+grid[row+size][col-size]+grid[row+size][col+size])/4.0 + scale*random.uniform(-1.0, 1.0)

def calc_square( grid, row, col, size, k):
    cap = len(grid[0])
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
   

def diamond( n, jaggedness ):
    grid = [ [0 for i in range(2**n+1)] for j in range(2**n+1)]

    seed_image = Image.open('seed.png')
    seed_level = 5

    size = 2**(n-seed_level)
    sample_scale = 0.1*jaggedness*2*size/len(grid[0])
    for y in range(0, 2**n+1, size):
        for x in range(0, 2**n+1, size):
            sx = int(x/(2.0**n+1)*seed_image.size[0])
            sy = int(y/(2.0**n+1)*seed_image.size[1])
            color = seed_image.getpixel((sx, sy))
            grid[y][x] = (color[0]+color[1]+color[2])/3.0/255.0
            grid[y][x] = min(grid[y][x], max(grid[y][x], 0.0), 1.0) + sample_scale*random.uniform(-1.0,1.0)
            #print("sample({0},{1}) = {2}".format(sx,sy, grid[y][x]))

    #size = 2**n
    while size > 1:
        # diamonds
        for y in range(size/2, 2**n+1, size):
            for x in range(size/2, 2**n+1, size):
                calc_diamond(grid, y, x, size/2, jaggedness)
        # squares
        for y in range(0, 2**n+1, size):
            for x in range(size/2, 2**n+1, size):
                calc_square(grid, y, x, size/2, jaggedness)
        for y in range(size/2, 2**n+1, size):
            for x in range(0, 2**n+1, size):
                calc_square(grid, y, x, size/2, jaggedness)

        size /= 2

    image = Image.new('RGB', (2**n+1, 2**n+1) )
    draw = ImageDraw.Draw(image)
    for y in range(2**n+1):
        for x in range(2**n+1):
            color = int(grid[y][x]*255)
            image.putpixel( (x,y), (color, color, color))

    image.save('heightmap4.png')


diamond(10, 0.5)
