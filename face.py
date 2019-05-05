import requests
import simplejson as json
import urllib
import cv2
import numpy as np
import cognitive_face as CF

class authenticateFace():
    self.KEY = '9fae0e6855d74d83ab4d10b9bf198e9a'  # Replace with a valid Subscription Key here.
    CF.Key.set(self.KEY)
    self.BASE_URL = 'https://australiaeast.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(self.BASE_URL)

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

    def getFaceData(self, url):
        return CF.face.detect(url)

    def getFaceID(self, url):
        return getFaceData(url)[0]['faceId']

    def authenticateFace(faceID1, faceID2):
        """
        returns True if the faces are identical and false otherwise
        """
        return CF.face.verify(faceID1, faceID2)['isIdentical']
