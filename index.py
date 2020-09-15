from flask import Flask
from flask import request
from PIL import Image, ImageDraw
import face_recognition
import numpy as np
import action

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/image', methods=['POST'])
def returnImage():
    # get image from postman
    image = request.files["image"]

    #load image from postman
    im = Image.open(image)

    # detect image
    result = action.detectImage(image)

    content = request.form

    return result


if __name__ == '__main__':
    app.run(debug=True)
