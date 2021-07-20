import pymongo, time
import numpy as np 

client = pymongo.MongoClient("url")
mycollection = mycollection = client['db']['collection']

# test query time

## query all the mfalff data in the collection

start_time = time.time()
docs = mycollection.find({},{"Images.mfalff":1}) 

## switch json array to numpy array, method_1
## Execution time: 1.3s - 1.5s
imgs = [ ]
for doc in docs: 
    img = doc["Images"]["mfalff"]
    imgs.append(img) 
imgs = np.array(imgs)

print("Shape of the images: {}".format(imgs.shape))
print(f"Execution time: {(time.time()-start_time)} secs")


start_time2 = time.time()
docs = mycollection.find({},{"Images.mfalff":1}) 

## switch json array to numpy array, method_2
## Execution time: 1.3s - 1.4s
imgs2 = list()
for doc in docs: 
    img = np.array(doc["Images"]["mfalff"]) 
    img = img[None, ...] 
    imgs2.append(img) 
imgs2 = np.concatenate(imgs2, axis = 0)
print("Shape of the images: {}".format(imgs2.shape))
print(f"Execution time: {(time.time()-start_time2)} secs")



# Summary report 
## Both execution time are idetical, since they are all O(n)
## but the 2nd method is generally 0.1s faster than 1st method 
## Therefore both methods are fine, depends on yourself
## -- Kaiyi, 20/07/2021