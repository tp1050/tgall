# from conf import Flask_Config
from pathlib import Path
# from app import encode
conf_extensions =[] #Flask_Config().IMAGE_EXTS

def get_pic_paths(instance_path = Path.home(),extensions = conf_extensions):
    import glob
    img_list=[]
    # for ext in extensions :
    #     files=glob.glob(f"{instance_path}/*{ext}")
    #
    #     for file in files:
    #         img_list.append(Path(instance_path,file))
    return img_list


# il=get_pic_paths('/home/c/Code/github/tFlask-Image-Gallery/instance/qrs',['.jpg'])
#
# for i in il:
#     print(f"\n{i}={encode(str(i))}")

def lan_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
