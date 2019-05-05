import requests
import simplejson as json
import urllib
import cv2
import numpy as np
import cognitive_face as CF


KEY = '9fae0e6855d74d83ab4d10b9bf198e9a'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://australiaeast.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


def url_to_image(url):
  """
  a helper function that downloads the image, converts it to a NumPy array,
  and then reads it into OpenCV format
  """
  resp = urllib.request.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype="uint8")
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  return image

def getFaceInImage(url):
    result = getFaceData(url)
    height = result[0]['faceRectangle']['height']
    left = result[0]['faceRectangle']['left']
    top = result[0]['faceRectangle']['top']
    width = result[0]['faceRectangle']['width']
    img = url_to_image(url)
    return img[top:top+height, left:left+width]

def getFaceData(url):
    return CF.face.detect(url)

def getFaceID(url):
    return getFaceData(url)[0]['faceId']

def authenticateFace(faceID1, faceID2):
    """
    returns True if the faces are identical and false otherwise
    """
    return CF.face.verify(faceID1, faceID2)['isIdentical']

url1 = 'https://pixel.nymag.com/imgs/fashion/daily/2017/05/08/08-brad-pitt.w700.h700.jpg'
result = getFaceID(url1)
img = url_to_image(url1)
cv2.imshow('img', img)
i = getFaceInImage(url1)


res = getFaceData(url1)
print(res)
id = getFaceID(url1)
print(id)

test_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg/220px-Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg'
img = url_to_image(test_url)
cv2.imshow("2", img)
# test_result = CF.face.detect(test_url)
test_faceId = getFaceID(test_url)

with open("/home/abdullahsalah96/Downloads/me.jpg", 'rb') as f:
  data = f.read()

print(data)
# r = requests.post("https://host.url.com/upload/img.png", data=data)
# url = "https://host.url.com/upload/img.png"
# cv2.imshow('5', url_to_image(url))

r = authenticateFace(res[0]['faceId'], test_faceId)
print(r)
cv2.waitKey(0)
