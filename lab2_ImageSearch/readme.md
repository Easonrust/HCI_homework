# Lab 2 Information Retrieval

## Requirements for Image Search Task

A search framework help to coordinate design practices and satisfy the needs of all users, and it often contain five stages:

1. *Formulation*
2. *Initiation of action*
3. *Review of results*
4. *Refinement*
5. *Use*

Five stages can be repeated until users' needs are met. If users' are unsatisfied with the results, they should be able to have additional options and change their queries easily.

## Design for Image Search Task

As for Image Search Task, I  make the following designs for  five stages:

1. **An input box to upload an image(Formulation)**. Users can click on the input box or the *select files* button to choose an image from computers for uploading.
2. **Preview of the query image on the searching window(Formulation)**. Users can preview the query image in the searching window.
3. **Search button(Initiation)**. After users uploading an image, they can click on the *search* button to search similar images.
4.    **Overview of the results(Review)**. Users can see the total number of results.
5. **Review of the results(Review**. After users clicking on the *search* button, they can see 9 images that are similar to the query image.
6. **Classify Results(Refinement)**. Users can choose search parameters(e.g. *animals*) and click on search again. Then they can see images with certain tags of the results. I provide 7 parameters, which are *all**, *animals*, *baby*, * bird*, *car*, *clouds* and *favourite*.
7. **Favourite list(Use)**. Users can click on the *like!* button on the left of every result to add the result to *Favourite list*. Also, Users can choose *favourite* parameter and click on the *search* button again to view favourite list. When users see the *Favourite* list, they can click on *dislike* to delete the image from the list but they also need to click on *search* button to refresh.

## Core Code

### Classify Results

```python
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
```

### Favourite List

```javascript
function likeimg0(){
        
        var address=document.getElementById("img0").src;
        dic={img0_address:address,};
        send_data = JSON.stringify(dic);
        $.ajax({
            url: 'like0',
            type: 'Post',
            data: send_data,
            datatype:"json",
                success: function (data) {  //成功得到返回数据后回调的函数
                    console.log(data);
                }
            })
    }
    function dislikeimg0(){
        
        var address=document.getElementById("img0").src;
        dic={img0_address:address,};
        send_data = JSON.stringify(dic);
        $.ajax({
            url: 'dislike0',
            type: 'Post',
            data: send_data,
            datatype:"json",
                success: function (data) {  //成功得到返回数据后回调的函数
                    console.log(data);
                }
            })
    }
```

```python
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
```



## Design for Ui

### Overview

![Ui](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\Ui.png)

## Test the Features

### Basic Search

#### Input

![input_1](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\input_1.png)

#### Output

![output_1](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\output_1.png)

### Search with Tags

#### Input

![input_2](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\input_2.png)

#### Output

![output_2](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\output_2.png)

### Favourite List

#### Input

![input_3](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\input_3.png)

#### Output

![output_3](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\output_3.png)

### Delete Images from List

#### Input

![input_4](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\input_4.png)

#### Output

![output_4](C:\Users\yangl\Desktop\交互设计\lab2-image retrieval\lab2-image retrieval\server\output_4.png)

## How to Run My code

1. You should first run **server/image_vectorizer.py**. This will generate two files.
2. Then you should run **server/rest-server.py**, be careful with you ***path***.

## Programming Environment

Python 3.7+Ajax+Javascript+JQuery+HTML
