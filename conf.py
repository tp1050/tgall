from helper import tprint, disp
from koon import lan_ip
class Flask_Config:
    sandogh={}
    def __init__(self,**kwargs):
        self.sandogh.update(kwargs)
    def __str__(self):
        return str(self.sandogh)


class Flask_conf1(Flask_Config):
    def __init__(self):
        super().__init__(instance_relative_config = True, IMAGE_EXTS = [".png", ".jpg", ".jpeg", ".gif", ".tiff"],
        SERVER_NAME=f"{lan_ip()}:8456")
    def sandoghech(self):
        return self.sandogh




f=Flask_conf1()
print(f.sandogh)
print(f)
