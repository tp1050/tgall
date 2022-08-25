
from flask import render_template, redirect,url_for
from flask import request
from pathlib import Path

from flask import session
from app import app
from flask import send_file
import random



@app.route('/')
def home():
    if "image_paths_dict" not in session:
        from classes.koon import get_pic_paths1
        image_paths = get_pic_paths1(app.config['QR_LIB'], app.config["IMAGE_EXTS"],format='dic')


        session['image_paths_dict']=image_paths
        d=session['image_paths_dict'].keys()
        return render_template('index.html', paths=d,val=image_paths.values())
    else:
        d=session["image_paths_dict"].keys()
        return render_template('index.html', paths=d,val=session['image_paths_dict'].values())


@app.route('/refresh')
def refresh():
    if "image_paths_dict" in session:
        session.pop("image_paths_dict")
    return "refresh"


@app.route('/cdn/<path:filepath>')
def download_file(filepath):

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
    from flask import send_file
    ip = 'Unknown Visitor'
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    from classes.qr_cls import dool_qr
    file_name=dool_qr(data=ip,path=app.config['QR_LIB']).save()
    pic_path=str(Path(app.instance_path,app.config['QR_LIB'],file_name))
    gg=session['image_paths_dict']
    gg[str(random.random())]=pic_path
    session['image_paths_dict']=gg
    return redirect(url_for('home'))
    # return pic_path
    # return render_template("index.html",paths=session['image_paths_dict'].keys(),val=session['image_paths_dict'].values())
    # return send_file(file_name, as_attachment =False)
