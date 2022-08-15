from conf import Flask_Config
from pathlib import Path

ext = Flask_Config().IMAGE_EXTS

def get_pic_paths(instance_path = Path.home(),exts = ext):
    import glob
    img_list=[]
    for ext1 in ext :
        for file in glob.glob(f"*{ext1}"))):
            img_list.append(path(instance_path,file)
    return img_list
