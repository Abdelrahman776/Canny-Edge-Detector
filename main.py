from flask import Flask,render_template,request,redirect,url_for
import os
from edge_detection import canny_edge_detection
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/', methods=['POST'])
# def upload_and_process():
#     if 'og' not in request.files:
#         return "No file part"

#     og = request.files['og']

#     if og.filename == '':
#         return "No selected file"

#     processed_image_path = "path/to/processed/image.jpg"

#     # Display the processed image or any message in the template
#     return render_template('index.html', ogname=og.filename)


if __name__ == '__main__':
    app.run(debug=True)