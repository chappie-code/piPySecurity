
from PIL import Image
im1 = Image.open("manipulate/img001.jpg")
im2 = Image.open("manipulate/img002.jpg")

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
    newData.append(tuple(new_pixel))
    



im.putdata(newData)
im.save("manipulate/compare_img001.jpg")

