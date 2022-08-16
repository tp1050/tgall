
from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
import os
import glob
import sys
import binascii
import argparse
import logging
from pathlib import Path
from conf import Flask_conf1




app = Flask("Zortom")
app.config.update(Flask_conf1().sandoghech())

app.config["loggger_file"] = Path(app.instance_path, 'dool.log' )
app.config["QR_LIB"]=Path(app.instance_path, '/qrs' )
logging.basicConfig(filename=app.config["loggger_file"], level=logging.DEBUG, force=True)


def encode(x):
    # return x
    return binascii.hexlify(x.encode('utf-8')).decode()

def decode(x):
    # return x
    return binascii.unhexlify(x.encode('utf-8')).decode()


@app.route('/')
def home():
    from koon import get_pic_paths
    root_dir = app.config['QR_LIB']
    image_paths = get_pic_paths(root_dir, app.config["IMAGE_EXTS"])
    # for root,dirs,files in os.walk(root_dir):
    #     for file in files:
    #         if any(file.endswith(ext) for ext in app.config['IMAGE_EXTS']):
                # image_paths.append(encode(os.path.join(root,file)))
    return render_template('index.html', paths=image_paths)


@app.route('/cdn/<path:filepath>')
def download_file(filepath):
    dir,filename = os.path.split(decode(filepath))
    return send_from_directory(dir, filename, as_attachment=False)


if __name__=="__main__":
    app.run()
    # parser = argparse.ArgumentParser('Usage: %prog [options]')
    # parser.add_argument('root_dir', help='Gallery root directory path')
    # parser.add_argument('-l', '--listen', dest='host', default='127.0.0.1', \
    #                                 help='address to listen on [127.0.0.1]')
    # parser.add_argument('-p', '--port', metavar='PORT', dest='port', type=int, \
    #                             default=5000, help='port to listen on [5000]')
    # args = parser.parse_args()
    # app.config['ROOT_DIR'] = args.root_dir
    # app.run(host=args.host, port=args.port, debug=True)
