import requests
import simplejson as json
import urllib
import cv2
import numpy as np
import cognitive_face as CF
import requests


class authenticateFace():
    def __init__(self):
        KEY = '9fae0e6855d74d83ab4d10b9bf198e9a'  # Replace with a valid Subscription Key here.
        CF.Key.set(KEY)
        self.headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': KEY}
        self.face_api_url = 'https://australiaeast.api.cognitive.microsoft.com/face/v1.0/detect'
        self.base_url = 'https://australiaeast.api.cognitive.microsoft.com/face/v1.0'
        CF.BaseUrl.set(self.base_url)
        self.params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
        'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
        }

    def url_to_image(self, url):
      """
      a helper function that downloads the image, converts it to a NumPy array,
      and then reads it into OpenCV format
      """
      resp = urllib.request.urlopen(url)
      image = np.asarray(bytearray(resp.read()), dtype="uint8")
      image = cv2.imdecode(image, cv2.IMREAD_COLOR)
      return image

    def getFaceInImage(self, url):
        result = getFaceData(url)
        height = result[0]['faceRectangle']['height']
        left = result[0]['faceRectangle']['left']
        top = result[0]['faceRectangle']['top']
        width = result[0]['faceRectangle']['width']
        img = url_to_image(url)
        return img[top:top+height, left:left+width]

    def getFaceData(self, imgPath):
        data = open(imgPath, 'rb')
        response = response = requests.post(self.face_api_url, params=self.params, headers=self.headers, data=data)
        faces = response.json()
        print(faces)
        return faces

    def getFaceID(self, imgPath):
        return self.getFaceData(imgPath)[0]['faceId']

    def verifyPerson(self, faceID1, faceID2):
        """
        returns True if the faces are identical and false otherwise
        """
        return CF.face.verify(faceID1, faceID2)['isIdentical']


f = authenticateFace()
face1 = f.getFaceID("/home/abdullahsalah96/Downloads/me.jpg")
face2 = f.getFaceID("/home/abdullahsalah96/Downloads/me2.jpg")

print("facd1: ", face1)
print("face2: ", face2)

print(f.verifyPerson(face1, face2))
