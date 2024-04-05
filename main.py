from flask import Flask,render_template,request,redirect,url_for
import cv2
import numpy as np
import base64
from edge_detection import canny_edge_detection


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            # Read the image
            img_bytes = file.read()
            # Convert to base64
            encoded_img = base64.b64encode(img_bytes).decode('utf-8')
            #  filter
            filtered_image = canny_edge_detection(encoded_img,50, 100)
            return render_template('index.html', original_image=encoded_img, filtered_image=filtered_image)


if __name__ == '__main__':
    app.run(debug=True)