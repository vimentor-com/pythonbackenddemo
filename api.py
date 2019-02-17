import cv2
import numpy as np

from flask import Flask, request

from house3d_worker_demo import process_img

app = Flask(__name__)


@app.route("/change_img_color", methods=["POST"])
def convert_img_color():
    # read image file string data
    filestr = request.files['image'].read()
    # convert string data to numpy array
    npimg = np.fromstring(filestr, np.uint8)
    # convert numpy array to image
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    process_img(img)

    return "Done"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

