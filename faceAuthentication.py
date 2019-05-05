########### Python 2.7 #############
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
  resp = urllib.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype="uint8")
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  # return the image
  return image


# height = result[0]['faceRectangle']['height']
# left = result[0]['faceRectangle']['left']
# top = result[0]['faceRectangle']['top']
# width = result[0]['faceRectangle']['width']
# cv2.imshow("im", img[top:top+height, left:left+width])

url1 = 'https://pixel.nymag.com/imgs/fashion/daily/2017/05/08/08-brad-pitt.w700.h700.jpg'
result = CF.face.detect(url1)
img = url_to_image(url1)
cv2.imshow("1", img)
height = result[0]['faceRectangle']['height']
left = result[0]['faceRectangle']['left']
top = result[0]['faceRectangle']['top']
width = result[0]['faceRectangle']['width']
cv2.imshow("im", img[top:top+height, left:left+width])

res = CF.face.detect(url1)
print(res)

test_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg/220px-Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg'
img = url_to_image(test_url)
cv2.imshow("2", img)
test_result = CF.face.detect(test_url)
test_faceId = test_result[0]['faceId']

r = CF.face.verify(res[0]['faceId'], test_faceId)
print(r)

cv2.waitKey(0)

####################################

# ########### Python 3.2 #############
# import http.client, urllib.request, urllib.parse, urllib.error, base64
#
# headers = {
#     # Request headers
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': '{subscription key}',
# }
#
# params = urllib.parse.urlencode({
#     # Request parameters
#     'returnFaceId': 'true',
#     'returnFaceLandmarks': 'false',
#     'returnFaceAttributes': '{string}',
#     'recognitionModel': 'recognition_01',
#     'returnRecognitionModel': 'false',
# })
#
# try:
#     conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
#     conn.request("POST", "/face/v1.0/detect?%s" % params, "{body}", headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))
#
# ####################################
