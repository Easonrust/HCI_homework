#!flask/bin/python
################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------                                                                                                                             
# This file implements the REST layer. It uses flask micro framework for server implementation. Calls from front end reaches 
# here as json and being branched out to each projects. Basic level of validation is also being done in this file. #                                                                                                                                  	       
#-------------------------------------------------------------------------------------------------------------------------------                                                                                                                              
################################################################################################################################
from flask import Flask, jsonify, abort, request, make_response, url_for,redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
import shutil 
import numpy as np
from search import recommend
import tarfile
from datetime import datetime
from scipy import ndimage
from scipy.misc import imsave 
import json

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
from tensorflow.python.platform import gfile
app = Flask(__name__, static_url_path = "")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

#==============================================================================================================================
#                                                                                                                              
#    Loading the extracted feature vectors for image retrieval                                                                 
#                                                                          						        
#                                                                                                                              
#==============================================================================================================================
extracted_features=np.zeros((10000,2048),dtype=np.float32)
with open('saved_features_recom.txt') as f:
    		for i,line in enumerate(f):
        		extracted_features[i,:]=line.split()
print("loaded extracted_features") 


#==============================================================================================================================
#                                                                                                                              
#  This function is used to do the image search/image retrieval
#                                                                                                                              
#==============================================================================================================================
@app.route('/imgUpload', methods=['GET', 'POST'])
#def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_img():
    print("image upload")
    result = 'static/result'
    animals='static/animals'
    baby='static/baby'
    bird='static/bird'
    car='static/car'
    clouds='static/clouds'
    if  gfile.Exists(result):
        shutil.rmtree(result)
    if  gfile.Exists(animals):
        shutil.rmtree(animals)
    if  gfile.Exists(baby):
        shutil.rmtree(baby)
    if  gfile.Exists(bird):
        shutil.rmtree(bird)
    if  gfile.Exists(car):
        shutil.rmtree(car)
    if  gfile.Exists(clouds):
        shutil.rmtree(clouds)
 
    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
           
            print('No selected file')
            return redirect(request.url)
        if file:# and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            recommend(inputloc, extracted_features)
            os.remove(inputloc)
            image_path = "/result"
            image_list =[os.path.join(image_path, file) for file in os.listdir(result)
                              if not file.startswith('.')]
            length=len(image_list)
            images = {
			'image0':image_list[0],
            'image1':image_list[1],	
			'image2':image_list[2],	
			'image3':image_list[3],	
			'image4':image_list[4],	
			'image5':image_list[5],	
			'image6':image_list[6],	
			'image7':image_list[7],	
			'image8':image_list[8],
            'num':length
		      }				
            print(image_list[0])
            return jsonify(images)

@app.route('/animals', methods=['GET', 'POST'])
def animals():
    print("image upload")
    animals = 'static/animals'

 
    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
           
            print('No selected file')
            return redirect(request.url)
        if file:# and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # recommend(inputloc, extracted_features)
            #os.remove(inputloc)
            image_path = "/animals"
 
            image_list =[os.path.join(image_path, file) for file in os.listdir(animals)
                              if not file.startswith('.')]
            length=len(image_list)
            length=str(len(image_list))
            while len(image_list)<9:
                image_list.append("/images/white.jpg")
            images = {
			'image0':image_list[0],
            'image1':image_list[1],	
			'image2':image_list[2],	
			'image3':image_list[3],	
			'image4':image_list[4],	
			'image5':image_list[5],	
			'image6':image_list[6],	
			'image7':image_list[7],	
			'image8':image_list[8],
            'num':length
		      }				
            print(image_list[0])
            print("hello")
            return jsonify(images)

@app.route('/baby', methods=['GET', 'POST'])
def baby():
    print("image upload")
    baby = 'static/baby'

 
    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
           
            print('No selected file')
            return redirect(request.url)
        if file:# and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # recommend(inputloc, extracted_features)
            #os.remove(inputloc)
            image_path = "/baby"
 
            image_list =[os.path.join(image_path, file) for file in os.listdir(baby)
                              if not file.startswith('.')]
            length=len(image_list)
            while len(image_list)<9:
                image_list.append("/images/white.jpg")
            images = {
			'image0':image_list[0],
            'image1':image_list[1],	
			'image2':image_list[2],	
			'image3':image_list[3],	
			'image4':image_list[4],	
			'image5':image_list[5],	
			'image6':image_list[6],	
			'image7':image_list[7],	
			'image8':image_list[8],
            'num':length
		      }				
            print(image_list[0])
            print("hello")
            return jsonify(images)

@app.route('/bird', methods=['GET', 'POST'])
def bird():
    print("image upload")
    bird = 'static/bird'

 
    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
           
            print('No selected file')
            return redirect(request.url)
        if file:# and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # recommend(inputloc, extracted_features)
            #os.remove(inputloc)
            image_path = "/bird"
 
            image_list =[os.path.join(image_path, file) for file in os.listdir(bird)
                              if not file.startswith('.')]
            length=len(image_list)
            while len(image_list)<9:
                image_list.append("/images/white.jpg")
            images = {
			'image0':image_list[0],
            'image1':image_list[1],	
			'image2':image_list[2],	
			'image3':image_list[3],	
			'image4':image_list[4],	
			'image5':image_list[5],	
			'image6':image_list[6],	
			'image7':image_list[7],	
			'image8':image_list[8],
            'num':length
		      }				
            print(image_list[0])
            print("hello")
            return jsonify(images)

@app.route('/car', methods=['GET', 'POST'])
def car():
    print("image upload")
    car = 'static/car'

 
    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
           
            print('No selected file')
            return redirect(request.url)
        if file:# and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # recommend(inputloc, extracted_features)
            #os.remove(inputloc)
            image_path = "/car"
 
            image_list =[os.path.join(image_path, file) for file in os.listdir(car)
                              if not file.startswith('.')]
            length=len(image_list)
            while len(image_list)<9:
                image_list.append("/images/white.jpg")
            images = {
			'image0':image_list[0],
            'image1':image_list[1],	
			'image2':image_list[2],	
			'image3':image_list[3],	
			'image4':image_list[4],	
			'image5':image_list[5],	
			'image6':image_list[6],	
			'image7':image_list[7],	
			'image8':image_list[8],
            'num':length
		      }				
            print(image_list[0])
            print("hello")
            return jsonify(images)

@app.route('/clouds', methods=['GET', 'POST'])
def clouds():
    print("image upload")
    clouds = 'static/clouds'

 
    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
           
            print('No selected file')
            return redirect(request.url)
        if file:# and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # recommend(inputloc, extracted_features)
            #os.remove(inputloc)
            image_path = "/clouds"
 
            image_list =[os.path.join(image_path, file) for file in os.listdir(clouds)
                              if not file.startswith('.')]
            length=len(image_list)
            while len(image_list)<9:
                image_list.append("/images/white.jpg")
            images = {
			'image0':image_list[0],
            'image1':image_list[1],	
			'image2':image_list[2],	
			'image3':image_list[3],	
			'image4':image_list[4],	
			'image5':image_list[5],	
			'image6':image_list[6],	
			'image7':image_list[7],	
			'image8':image_list[8],
            'num':length
		      }				
           
            return jsonify(images)
@app.route('/favourite', methods=['GET', 'POST'])
def favourite():
    print("image upload")
    favourite = 'static/favourite'

 
    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
           
            print('No selected file')
            return redirect(request.url)
        if file:# and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # recommend(inputloc, extracted_features)
            #os.remove(inputloc)
            image_path = "/favourite"
 
            image_list =[os.path.join(image_path, file) for file in os.listdir(favourite)
                              if not file.startswith('.')]
            length=len(image_list)
            while len(image_list)<9:
                image_list.append("/images/white.jpg")
            images = {
			'image0':image_list[0],
            'image1':image_list[1],	
			'image2':image_list[2],	
			'image3':image_list[3],	
			'image4':image_list[4],	
			'image5':image_list[5],	
			'image6':image_list[6],	
			'image7':image_list[7],	
			'image8':image_list[8],
            'num':length
		      }				
           
            return jsonify(images)
@app.route('/like0', methods=['POST'])
def like_img0():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img0_add=json_re['img0_address']
    img0_add=img0_add[29:]
    img0_result_add="static/result/"+img0_add
    img0_fav_add="static/favourite/"+img0_add
    shutil.copyfile(img0_result_add,img0_fav_add)
    print("hello")
    print(img0_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/like1', methods=['POST'])
def like_img1():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img1_add=json_re['img1_address']
    img1_add=img1_add[29:]
    img1_result_add="static/result/"+img1_add
    img1_fav_add="static/favourite/"+img1_add
    shutil.copyfile(img1_result_add,img1_fav_add)
    print("hello")
    print(img1_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/like2', methods=['POST'])
def like_img2():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img2_add=json_re['img2_address']
    img2_add=img2_add[29:]
    img2_result_add="static/result/"+img2_add
    img2_fav_add="static/favourite/"+img2_add
    shutil.copyfile(img2_result_add,img2_fav_add)
    print("hello")
    print(img2_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/like3', methods=['POST'])
def like_img3():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img3_add=json_re['img3_address']
    img3_add=img3_add[29:]
    img3_result_add="static/result/"+img3_add
    img3_fav_add="static/favourite/"+img3_add
    shutil.copyfile(img3_result_add,img3_fav_add)
    print("hello")
    print(img3_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/like4', methods=['POST'])
def like_img4():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img4_add=json_re['img4_address']
    img4_add=img4_add[29:]
    img4_result_add="static/result/"+img4_add
    img4_fav_add="static/favourite/"+img4_add
    shutil.copyfile(img4_result_add,img4_fav_add)
    print("hello")
    print(img4_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/like5', methods=['POST'])
def like_img5():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img5_add=json_re['img5_address']
    img5_add=img5_add[29:]
    img5_result_add="static/result/"+img5_add
    img5_fav_add="static/favourite/"+img5_add
    shutil.copyfile(img5_result_add,img5_fav_add)
    print("hello")
    print(img5_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/like6', methods=['POST'])
def like_img6():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img6_add=json_re['img6_address']
    img6_add=img6_add[29:]
    img6_result_add="static/result/"+img6_add
    img6_fav_add="static/favourite/"+img6_add
    shutil.copyfile(img6_result_add,img6_fav_add)
    print("hello")
    print(img6_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/like7', methods=['POST'])
def like_img7():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img7_add=json_re['img7_address']
    img7_add=img7_add[29:]
    img7_result_add="static/result/"+img7_add
    img7_fav_add="static/favourite/"+img7_add
    shutil.copyfile(img7_result_add,img7_fav_add)
    print("hello")
    print(img7_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/like8', methods=['POST'])
def like_img8():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img8_add=json_re['img8_address']
    img8_add=img8_add[29:]
    img8_result_add="static/result/"+img8_add
    img8_fav_add="static/favourite/"+img8_add
    shutil.copyfile(img8_result_add,img8_fav_add)
    print("hello")
    print(img8_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike0', methods=['POST'])
def dislike_img0():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img0_add=json_re['img0_address']
    img0_add=img0_add[32:]
    img0_fav_add="static/favourite/"+img0_add
    os.remove(img0_fav_add)
    print("hello")
    print(img0_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike1', methods=['POST'])
def dislike_img1():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img1_add=json_re['img1_address']
    img1_add=img1_add[32:]
    img1_fav_add="static/favourite/"+img1_add
    os.remove(img1_fav_add)
    print("hello")
    print(img1_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike2', methods=['POST'])
def dislike_img2():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img2_add=json_re['img2_address']
    img2_add=img2_add[32:]
    img2_fav_add="static/favourite/"+img2_add
    os.remove(img2_fav_add)
    print("hello")
    print(img2_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike3', methods=['POST'])
def dislike_img3():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img3_add=json_re['img3_address']
    img3_add=img3_add[32:]
    img3_fav_add="static/favourite/"+img3_add
    os.remove(img3_fav_add)
    print("hello")
    print(img3_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike4', methods=['POST'])
def dislike_img4():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img4_add=json_re['img4_address']
    img4_add=img4_add[32:]
    img4_fav_add="static/favourite/"+img4_add
    os.remove(img4_fav_add)
    print("hello")
    print(img4_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike5', methods=['POST'])
def dislike_img5():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img5_add=json_re['img5_address']
    img5_add=img5_add[32:]
    img5_fav_add="static/favourite/"+img5_add
    os.remove(img5_fav_add)
    print("hello")
    print(img5_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike6', methods=['POST'])
def dislike_img6():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img6_add=json_re['img6_address']
    img6_add=img6_add[32:]
    img6_fav_add="static/favourite/"+img6_add
    os.remove(img6_fav_add)
    print("hello")
    print(img6_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike7', methods=['POST'])
def dislike_img7():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img7_add=json_re['img7_address']
    img7_add=img7_add[32:]
    img7_fav_add="static/favourite/"+img7_add
    os.remove(img7_fav_add)
    print("hello")
    print(img7_add)
    ID={'id':1}
    return jsonify(ID)

@app.route('/dislike8', methods=['POST'])
def dislike_img8():
    recv_data = request.get_data()
    json_re = json.loads(recv_data)
    img8_add=json_re['img8_address']
    img8_add=img8_add[32:]
    img8_fav_add="static/favourite/"+img8_add
    os.remove(img8_fav_add)
    print("hello")
    print(img8_add)
    ID={'id':1}
    return jsonify(ID)
#==============================================================================================================================
#                                                                                                                              
#                                           Main function                                                        	            #						     									       
#  				                                                                                                
#==============================================================================================================================
@app.route("/")
def main():
    
    return render_template("main.html")   
if __name__ == '__main__':
    app.run(debug = True, host = "localhost")
