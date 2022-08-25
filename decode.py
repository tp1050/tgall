# Import Library
import cv2
import numpy


def decode_qr(img:numpy.ndarray):
    """
    takes input from cv2.imread
    """

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    m=detector.detect(img)
    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(img)
    # if there is a QR code
    # print the data
    if vertices_array is not None:
        return data
    else:
        raise Exception()



def save_img_from_url(pic_url,s):
    import requests
    with open('pic1.jpg', 'wb') as handle:
        response = s.get(pic_url, stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
        handle.write(block)

import requests
s=requests.session()
from netnoche import loadURL
from bs4 import BeautifulSoup as bs
l=loadURL("http://7270.dool.dool:8989",session=s,format="soup")
imgs=l.find_all('img')
for i in imgs:
    print(i)
save_img_from_url("http://7270.dool.dool:8989/cdn/0.3497161147862804",s)

# Name of the QR Code Image file
filename = "dool.jpg"
image = cv2.imread(filename)
print(type(image))
print(decode_qr(image))
# read the QRCODE image
