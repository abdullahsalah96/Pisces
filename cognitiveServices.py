import http.client, urllib.request, urllib.parse, urllib.error, base64

class Server:
    def __init__(self, httpAddress, subscriptionAddress, predictionKey, contentType, predictionKeyTwo):
        self.httpAddress = httpAddress
        self.subscriptionAddress  = subscriptionAddress
        self.headers = {
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
        """
        a function that gets prediction list from Azure service
        """
        data1 = open(imgPath, 'rb').read()
        conn = http.client.HTTPSConnection(self.httpAddress)
        conn.request("POST", self.subscriptionAddress, data1, self.headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
