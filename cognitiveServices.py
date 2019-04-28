import http.client, urllib.request, urllib.parse, urllib.error, base64

class Server:
    def __init__(self, imagePath, httpAddress, subscriptionAddress, predictionKey, contentType, predictionKeyTwo):
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
        try:
            data1 = open(ImagePath, 'rb').read()
            conn = http.client.HTTPSConnection(httpAddress)
            conn.request("POST", subscriptionAddress, data1, headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
