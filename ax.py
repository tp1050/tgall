from PIL import Image, ImageFont, ImageDraw

from pathlib import Path

my_image = Image.new('RGB',(300,300))
image_editable = ImageDraw.Draw(my_image)
font = ImageFont.truetype(r'instance/times.ttf', 80)
image_editable.text( (150,150),text="KOSTOPL",font=font,align='center')
my_image.save("result.jpg")
