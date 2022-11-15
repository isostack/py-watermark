#Import required Image library
from PIL import Image, ImageDraw, ImageFont


class Modify:
    def __init__(self):
        self.font = ImageFont.truetype("arial.ttf", 36)
        self.color = (255, 255, 255)
        self.position = (0, 0)
    def process(self, text, image):
        #Create an Image Object from an Image
        im = Image.open(image)
        width, height = im.size

        draw = ImageDraw.Draw(im)

        font = ImageFont.truetype('arial.ttf', 30)
        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font)
        im.show()

        #Save watermarked image
        im.save('images/watermarked.png')