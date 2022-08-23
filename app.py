
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


from flask.ext.login import LoginManager
login_manager = LoginManager()

app = Flask("Zortom",instance_relative_config = True)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

c=Conf1(LOGGER_FILE= str(Path(app.instance_path, 'dool.log' )),QR_LIB=str(Path(app.instance_path, 'qrs' )))
app.config.from_object(c)

logging.basicConfig(filename=app.config['LOGGER_FILE'], level=logging.DEBUG,force=True)
logging.info(app.config)
login_manager.init_app(app)

from routes import *

if __name__ == "__main__":
    app.run()
