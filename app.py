
from flask import Flask
from flask import render_template
import os
import binascii
import logging
from pathlib import Path
import pathlib
from conf import Conf1
from helper import tprint
from flask import session
from datetime import datetime
from time import time_ns as ns
now=datetime.now
from flask import request
import qr_cls



app = Flask("Zortom",instance_relative_config = True)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

c=Conf1(LOGGER_FILE= str(Path(app.instance_path, 'dool.log' )),QR_LIB=str(Path(app.instance_path, 'qrs' )))
app.config.from_object(c)

logging.basicConfig(filename=app.config['LOGGER_FILE'], level=logging.DEBUG,force=True)
logging.info(app.config)


@app.route('/')
def home():
    if "image_paths_dict" not in session:
        from koon import get_pic_paths1
        image_paths = get_pic_paths1(app.config['QR_LIB'], app.config["IMAGE_EXTS"],format='dic')
        d=image_paths.keys()
        session['image_paths_dict']=image_paths
        return render_template('index.html', paths=d)
    else:
        d=session["image_paths_dict"].keys()
        return render_template('index.html', paths=d)




@app.route('/cdn/<path:filepath>')
def download_file(filepath):
    from flask import send_file
    if "image_paths_dict" not in session:
        print("session dead!!")
    else:
        filename = session['image_paths_dict'].get(filepath)
    if Path(app.instance_path, 'qrs', filename).exists():
        return send_file(Path(app.instance_path, 'qrs', filename), as_attachment =False)
    else:
        return send_file(Path(app.instance_path,'qrs/404', 'result.jpg'), as_attachment=False)

@app.route('/qrIP', methods=['GET','POST'])
def qrIP():
    ip = 'Unknown Visitor'
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    from qr_cls import dool_qr
    file_name=dool_qr(data=ip,path=app.config['QR_LIB']).save()
    return f"<html>{file_name}</html>"

if __name__ == "__main__":
    app.run()
