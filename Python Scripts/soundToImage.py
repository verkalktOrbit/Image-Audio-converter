from math import ceil, sqrt
from turtle import color
from PIL import Image
import time

if __name__ == '__main__':
    start_time = time()
    #read the Bytes of the Audio and convert it into hex expression
    file = open(r'mp3\Mac Miller - Self Care.mp3', 'rb')
    content = file.read()
    hex_data = content.hex()

    #Calculate size of the Image 2 hex Value will make one Color value -> 3 Color Value = 1 RGB -> 1 RGB = 1 Pixel
    width = ceil(sqrt(len(hex_data)//6))
    height = width
    size = height, width

    img = Image.new('RGB', size, color=0)
    pix = img.load()

    x = -1
    y = 0

    for i in range(width*height):
        if i < ((y+1)*img.width):
            x+=1
        else:
            y+=1
            x = 0
        try:
            r = int(hex_data[i*6:i*6+2], 16)
            g = int(hex_data[i*6+2:i*6+4], 16)
            b = int(hex_data[i*6+4:i*6+6], 16)
        except:
            r,g,b = 0,0,0

        pix[x, y] = (r,g,b)

    img.save(r'Image\Mac Miller - Self Care.png')

    print('=============================\nTime: %s seconds\n=============================' %(time.time() - start_time))