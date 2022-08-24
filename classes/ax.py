from PIL import Image, ImageFont, ImageDraw

from pathlib import Path


def create_image(h,w,text):
    from PIL import Image, ImageFont, ImageDraw
    my_image = Image.new('RGB',(h,w))
    image_editable = ImageDraw.Draw(my_image)
    font = ImageFont.truetype(r'instance/times.ttf', 80)
    image_editable.text( (0,0),text=text,(255,255,255),font=font,align='center')
    return my_image

    my_image.save("result.jpg")
