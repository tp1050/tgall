import qrcode
import time
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw



def create_image(w,h,text):
    from PIL import Image, ImageFont, ImageDraw
    my_image = Image.new('RGB',(h,w))
    image_editable = ImageDraw.Draw(my_image)
    font = ImageFont.truetype(r'instance/times.ttf',10)
    image_editable.text( (1,1),text=text,font=font)
    return my_image
def concat_text(img_src,data):
    w,h=img_src.size
    im2=create_image(w, int(h/6), data)
    im3=Image.new('RGB',(w,(h+int(h/6))))
    im3.paste(img_src,(0,0))
    im3.paste(im2,(0,h))
    return im3




class dool_qr:
    def __init__(self,data="DOOL",img=None,path=None):
        self.path=path
        self.data=data
        qr=qrcode.QRCode()
        qr.add_data(data)
        qr.make(fit=True)
        self.img_raw=qr.make_image(fill_color='red',back_color='white')
        self.file_name=str(time.time_ns())+str(data)+".jpg"
    def save(self):
        self.img=concat_text(self.img_raw, self.file_name)
        self.img.save(Path(self.path,self.file_name))
        return Path(self.path,self.file_name)
    def qr(self):
        return self.img
