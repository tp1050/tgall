
from flask import Flask
from flask import render_template
import os
import binascii
import logging
from pathlib import Path
from conf import Conf1
from helper import tprint
from flask import session
from datetime import datetime

now=datetime.now



app = Flask("Zortom",instance_relative_config = True)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass
app.config.from_object(Conf1())

app.config["loggger_file"] = Path(app.instance_path, 'dool.log' )
app.config["QR_LIB"]=Path(app.instance_path, 'qrs' )
tprint(app.config["QR_LIB"])
logging.basicConfig(filename=app.config["loggger_file"], level=logging.DEBUG, force=True)


def encode(x):
    ret=[]
    if isinstance(x,list):
        for i in x:
            ret.append(encode(i))
    else:
        ret=binascii.hexlify(x.encode('utf-8')).decode()
    return ret

def decode(x):
    # return x
    ret='khiloo.jpg'
    try:
        ret=binascii.unhexlify(x.encode('utf-8')).decode()
    except:
        pass

    return ret


@app.route('/')
def home():
    from koon import get_pic_paths1
    image_paths = encode(get_pic_paths1(app.config['QR_LIB'], app.config["IMAGE_EXTS"]))
    import random
    session['img_path']={}

    for img in image_paths:
        session['img_paths'].update(str(random.random()),img)
    d=session.img_paths.keys()
    return render_template('index.html', paths=d)


@app.route('/cdn/<path:filepath>')
def download_file(filepath):
    from flask import send_file
    print(type(filepath))
    filepath1 = session.img_path[filepath]
    filename = decode(filepath1)
    if Path(app.instance_path, 'qrs', filename).exists():
        return send_file(Path(app.instance_path, 'qrs', filename), as_attachment = False)
    else:
        return send_file(Path(app.instance_path,'qrs/404', 'result.jpg'), as_attachment=False)



if __name__ == "__main__":
    app.run()
