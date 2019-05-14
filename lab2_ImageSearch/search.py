################################################################################################################################
# This function implements the image search/retrieval .
# inputs: Input location of uploaded image, extracted vectors
# 
################################################################################################################################
import random
import tensorflow as tf
import numpy as np
import os
import scipy.io
import time
from datetime import datetime
from scipy import ndimage
from scipy.misc import imsave 
from scipy.spatial.distance import cosine
#import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import pickle 
from PIL import Image
import gc
import os
from tempfile import TemporaryFile
from tensorflow.python.platform import gfile
BOTTLENECK_TENSOR_NAME = 'pool_3/_reshape:0'
BOTTLENECK_TENSOR_SIZE = 2048
MODEL_INPUT_WIDTH = 299
MODEL_INPUT_HEIGHT = 299
MODEL_INPUT_DEPTH = 3
JPEG_DATA_TENSOR_NAME = 'DecodeJpeg/contents:0'
RESIZED_INPUT_TENSOR_NAME = 'ResizeBilinear:0'
MAX_NUM_IMAGES_PER_CLASS = 2 ** 27 - 1  # ~134M

#show_neighbors(random.randint(0, len(extracted_features)), indices, neighbor_list)

def get_top_k_similar(image_data, pred, pred_final, k):
        print("total data",len(pred))
        print(image_data.shape)
        #for i in pred:
        #print(i.shape)
                #break
        if not gfile.Exists('static/result'):
          os.mkdir('static/result')
        if not gfile.Exists('static/animals'):
          os.mkdir('static/animals')
        if not gfile.Exists('static/baby'):
          os.mkdir('static/baby')
        if not gfile.Exists('static/bird'):
          os.mkdir('static/bird')
        if not gfile.Exists('static/car'):
          os.mkdir('static/car')
        if not gfile.Exists('static/clouds'):
          os.mkdir('static/clouds')
        
    # cosine calculates the cosine distance, not similiarity. Hence no need to reverse list
        top_k_ind = np.argsort([cosine(image_data, pred_row) \
                            for ith_row, pred_row in enumerate(pred)])[:k]
        print(top_k_ind)
        
        for i, neighbor in enumerate(top_k_ind):
            image = ndimage.imread(pred_final[neighbor])
            #timestr = datetime.now().strftime("%Y%m%d%H%M%S")
            #name= timestr+"."+str(i)
            name = pred_final[neighbor]
            tokens = name.split("\\")
            img_name = tokens[-1]
            num=name[19:-4]

            #find animals
            f=open('database/tags/animals.txt')
            animals_tag=f.read()
            animals_tag=animals_tag.split('\n')
            i=0
            while animals_tag[i] !=animals_tag[-1]:
              if animals_tag[i]==num:
                name='static/animals/'+img_name
                imsave(name,image)
                find=1
                break
              i+=1
            #find baby
            f=open('database/tags/baby.txt')
            baby_tag=f.read()
            baby_tag=baby_tag.split('\n')
            i=0
            while baby_tag[i] !=baby_tag[-1]:
              if baby_tag[i]==num:
                name='static/baby/'+img_name
                imsave(name,image)
                find=1
                break
              i+=1

            #find bird
            f=open('database/tags/bird.txt')
            bird_tag=f.read()
            bird_tag=bird_tag.split('\n')
            i=0
            while bird_tag[i] !=bird_tag[-1]:
              if bird_tag[i]==num:
                name='static/bird/'+img_name
                imsave(name,image)
                find=1
                break
              i+=1
            
            #find car
            f=open('database/tags/car.txt')
            car_tag=f.read()
            car_tag=car_tag.split('\n')
            i=0
            while car_tag[i] !=car_tag[-1]:
              if car_tag[i]==num:
                name='static/car/'+img_name
                imsave(name,image)
                find=1
                break
              i+=1

            #find clouds
            f=open('database/tags/clouds.txt')
            clouds_tag=f.read()
            clouds_tag=clouds_tag.split('\n')
            i=0
            while clouds_tag[i] !=clouds_tag[-1]:
              if clouds_tag[i]==num:
                name='static/clouds/'+img_name
                imsave(name,image)
                find=1
                break
              i+=1            

            
            print(img_name)
            name = 'static/result/'+img_name
            imsave(name, image)

                
def create_inception_graph():
  """"Creates a graph from saved GraphDef file and returns a Graph object.

  Returns:
    Graph holding the trained Inception network, and various tensors we'll be
    manipulating.
  """
  with tf.Session() as sess:
    model_filename = os.path.join(
        'imagenet', 'classify_image_graph_def.pb')
    with gfile.FastGFile(model_filename, 'rb') as f:
      graph_def = tf.GraphDef()
      graph_def.ParseFromString(f.read())
      bottleneck_tensor, jpeg_data_tensor, resized_input_tensor = (
          tf.import_graph_def(graph_def, name='', return_elements=[
              BOTTLENECK_TENSOR_NAME, JPEG_DATA_TENSOR_NAME,
              RESIZED_INPUT_TENSOR_NAME]))
  return sess.graph, bottleneck_tensor, jpeg_data_tensor, resized_input_tensor

def run_bottleneck_on_image(sess, image_data, image_data_tensor,
                            bottleneck_tensor):
 
    bottleneck_values = sess.run(
            bottleneck_tensor,
            {image_data_tensor: image_data})
    bottleneck_values = np.squeeze(bottleneck_values)
    return bottleneck_values

def recommend(imagePath, extracted_features):
        tf.reset_default_graph()

        config = tf.ConfigProto(
            device_count = {'GPU': 0}
        )

        sess = tf.Session(config=config)
        graph, bottleneck_tensor, jpeg_data_tensor, resized_image_tensor = (create_inception_graph())
        image_data = gfile.FastGFile(imagePath, 'rb').read()
        features = run_bottleneck_on_image(sess, image_data, jpeg_data_tensor, bottleneck_tensor)	

        with open('neighbor_list_recom.pickle','rb') as f:
                    neighbor_list = pickle.load(f)
        print("loaded images")
        get_top_k_similar(features, extracted_features, neighbor_list, k=9)

