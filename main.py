from flask import Flask,render_template,request,redirect,url_for
import cv2
import numpy as np
from edge_detection import canny_edge_detection


app = Flask(__name__)
image_name=""
@app.route('/',methods=['POST','GET'])
def upload_detect():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            # Read the image name
            image_name = file.filename
            
            # new_path=canny_edge_detection(image_name,50,150) # edge detection manually
            img_new_name = image_name.split(".")[0]+"_processed.png"
            new_path="static/images/"+img_new_name
            
            edge=cv2.Canny(cv2.imread("static/images/"+image_name),100,250)
            cv2.imwrite(new_path,edge)
            
        return render_template('index.html', original_image=image_name,filtered_image=new_path)

if __name__ == '__main__':
    app.run(debug=True)