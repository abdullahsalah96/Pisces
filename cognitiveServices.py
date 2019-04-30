import http.client, urllib.request, urllib.parse, urllib.error, base64

class Server:
    def __init__(self, httpAddress, subscriptionAddress, predictionKey, contentType, predictionKeyTwo):
        headers = {
            # Request headers
            'Prediction-Key': predictionKey,
            'Content-Type': contentType,
            'Prediction-key': predictionKeyTwo,
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'application': '{string}',
        })


    def getPrediction(self, imgPath):
        data1 = open(imgPath, 'rb').read    
        conn = http.client.HTTPSConnection(httpAddress)
        conn.request("POST", subscriptionAddress, data1, self.headers)
        response = conn.getresponse()
        data = response.read()
        prediction = data
        conn.close()
        return prediction
