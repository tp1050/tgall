# Import Library
import cv2


def decode_qr(img):

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    m=detector.detect(image)
    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    # if there is a QR code
    # print the data
    if vertices_array is not None:
        return data
    else:
        raise Exception()


# Name of the QR Code Image file
filename = "dool.jpg"
image = cv2.imread(filename)
print(decode_qr(image))
# read the QRCODE image
