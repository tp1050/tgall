# # from netnoche import is_valid_ipv4_address
# # from helper import tprint
# # import socket
# # from socket import error
# #
# #
# #
# # a = ['80.210.57.222']
# # print('----------------------------------------')
# # print(is_valid_ipv4_address(a))
# # import socket
# #
# #
# # def ip_check(ipAddress):
# #     for i in ipAddress:
# #         try :
# #             binaryIP    = socket.inet_pton(socket.AF_INET, ipAddress)
# #             return True
# #         except:
# #             return False
# #
# # from netnoche import *
# from netnoche import loadURL
#
# h=loadURL('http://192.168.5.2:8456/',format='soup')
from flask import Flask
from flask import session
from conf import Conf1
app = Flask("Bacon")
app.config.from_object(Conf1())



@app.route('/')
def index():
    session['data']=921284053349526
    return f"<html><h1>{session['data']}</html></h1>"

@app.route('/test')
def test():

    return f"<html><h1>{session.get('data')+999}</html></h1>"

from flask import Flask, render_template, request, redirect,url_for, flash, make_response, session

@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return "Total visits: {}".format(session.get('visits'))

@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None) # delete visits
    return 'Visits deleted'




app.run()
