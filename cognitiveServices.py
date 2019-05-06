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


    def getPrediction(self):
        """
        a function that gets prediction list from Azure service
        """
        data1 = open(self.imgPath, 'rb').read
        conn = http.client.HTTPSConnection(httpAddress)
        conn.request("POST", subscriptionAddress, data1, self.headers)
        response = conn.getresponse()
        data = response.read()
        prediction = data
        conn.close()
        return prediction

    def classify(self, imgPath):
        """
        a function that returns:
            * 1 if the image belongs to the first class
            * 2 if the image belongs to the second class
            * 0 otherwise
        """
        self.imgPath = imgPath
        result = getPrediction().decode()
        first_prob_index = result.find("probability")
        first_class_index = result[first_prob_index:].find(":") + 1 + first_prob_index
        second_prob_index = result.rfind("probability")
        second_class_index = result[second_prob_index:].find(":") + 1 + second_prob_index
        first_class_prediction = result[first_class_index:first_class_index+3]
        if(first_class_prediction > 1):
            first_class_prediction = 0
        second_class_prediction = result[second_class_index:second_class_index+3]
        if(second_class_prediction > 1):
            second_class_prediction = 0
        if(first_class_prediction > second_class_prediction and first_class_prediction != 0):
            return 1
        elif(second_class_prediction > first_class_prediction and second_class_prediction != 0):
            return 2
        else:
            return None
