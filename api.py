import cv2
import numpy as np

from flask import Flask, request

from house3d_worker_demo import process_img

app = Flask(__name__)


@app.route("/change_img_color", methods=["POST"])
def convert_img_color():
    # Doc anh gui len tu phia client
    filestr = request.files['image'].read()
    # Do anh duoc gui len co dang du lieu chuoi (string),
    # can duoc chuyen doi sang dang ma tran numpy
    # de tien thao tac ve sau
    npimg = np.fromstring(filestr, np.uint8)
    # Chuyen doi du lieu numpy array ve du lieu ma tran anh chuan
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    process_img(img)

    return "Done"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

