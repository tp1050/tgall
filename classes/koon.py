# from conf import Flask_Config
from pathlib import Path
from helper import tprint



def get_pic_paths(instance_path = Path.home(),extensions =[]):
    tprint(locals())
    import glob
    import classes.conf
    conf_extensions =extensions
    img_list=[]
    for ext in extensions :
        files=glob.glob(f"{instance_path}/{ext}")

        for file in files:
            img_list.append(str(Path(instance_path,file)))
    tprint(img_list)
    return img_list
def get_pic_paths1(instance_path = Path.home(),extensions =[],format="dic"):
    import glob
    import random
    dic={}
    img_list=[]
    for ext in extensions :
        img_list=img_list+glob.glob(f"{instance_path}/{ext}")

    for i in img_list:
        dic[random.random()]=i
    if format=="dic":
        return dic
    else:
        return img_list
# def encode(x):
#     ret=[]
#     if isinstance(x,list):
#         for i in x:
#             ret.append(encode(i))
#     else:
#         ret=binascii.hexlify(x.encode('utf-8')).decode()
#     return ret
#
# def decode(x):
#     # return x
#     print(x)
#     ret='khiloo.jpg'
#     try:
#         ret=binascii.unhexlify(x.encode('utf-8')).decode()
#     except  Exception as e:
#         print(e)
#
#     return ret


# from pathlib import Path
# import random
# from collections import defaultdict
# import pathlib
# class Image_Gallery():
#     gallery=defaultdict("Khers.jpg")
#     def __init__(self,gallery_path=Path.home(),extensions=["*.jpg"],encode=True,encoding="Normal"):
#         self.gallery=self.load_gallery(gallery_path,extensions)
#
#     def load_gallery(self, images : list):
#         d={}
#         for i in images:
#             d.put(i,random.random())
#         return d
#
#     def load_images(self,galllery_path:Path,extensions =[]):
#         import glob
#         img_list=[]
#         for ext in extensions :
#             img_list=img_list+glob.glob(f"{galllery_path}/{ext}")
#         return img_list
#     def put(self,path:pathlib.Path):
#         if self.gallery[path]=="Khers.jpg":
#             self.gallery[path]=random.random()
#
#
#
#
#
# i=Image_Gallery("instance/qrs")
# print(i.gallery)
# il=get_pic_paths('/home/c/Code/github/tFlask-Image-Gallery/instance/qrs',['.jpg'])
#
# for i in il:
#     print(f"\n{i}={encode(str(i))}")

def lan_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
