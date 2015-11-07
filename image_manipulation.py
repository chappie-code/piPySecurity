
from PIL import Image
im = Image.open("images/img001.jpg")
im.convert("RGB")
pixel_values = im.getdata()

newData = []
count = 0


    

for pixel in pixel_values:
    new_pixel = []
    for colour in pixel:
        if colour > (255/2):
            colour = 255
        else:
            colour = 0
        
        new_pixel.append(colour)
    #r,g,b = pixel
    #r = g = b = (r+g+b /3)
    #pixel = r,g,b
    newData.append(tuple(new_pixel))
    



im.putdata(newData)
im.save("images/bw_img001.jpg")

