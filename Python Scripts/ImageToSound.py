from PIL import Image
import time
import ast

start_time = time.time()

#load Image and it´s pixls
img = Image.open(r'Image\Mac Miller - Self Cate.png')
pix = img.load()

x = -1
y = 0

with open(r'D:\VS\Python\NFT\mp3\Mac Miller - Self Care.mp3', 'wb') as file:
    #go through each pixel
    for i in range(2152 * 2152):
        if i < ((y+1)*2152):
            x+=1
        else:
            y+=1
            x=0
        #represent each pixel as a byte | 1Pixel = 3 RGB Colors = 3 Bytes
        byte_string = bytes.fromhex('%02x%02x%02x' % pix[x, y])
        #write each pixel as byte expression into the mp3 file
        file.write(byte_string)

print("Seconds: %s" %(time.time()-start_time))