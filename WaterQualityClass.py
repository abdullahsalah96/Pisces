import urllib.request as urllib
import json

class waterQuality:
    def __init__(self, date, time, pH, temperature, waterQualityLevel):
        self.date = date
        self.time = time
        self.pH = pH
        self.temperature = temperature
        self.waterQualityLevel = waterQualityLevel
        self.url = 'https://ussouthcentral.services.azureml.net/workspaces/9b7b204be697483599b66bbbecd68702/services/0007b08e45444a31a8ecf7b1779af9b0/execute?api-version=2.0&details=true'
        self.api_key = 'FXGBv13k4qgzFdsdjqRk90V+yG1nzcPx9eTwEwMryCI7Cju/dsy/WlpgZjeblBUxM0/m7Rg9jQGED3ZsOKZDQg==' # Replace this with the API key for the web service
        self.headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ self.api_key)}

    def getPrediction(self):
        '''
        a function that returns the prediction list
        returned from the web service
        '''
        data =  {
                "Inputs": {
                        "input1":
                        {
                            "ColumnNames": ["T_degC"],
                            "Values": [ [ str(self.temperature) ]]
                        },        },
                    "GlobalParameters": {
                    }
                }
        body = str.encode(json.dumps(data))
        req = urllib.Request(self.url, body, self.headers)
        response = urllib.urlopen(req)
        result = response.read()
        return result

    def predictWaterSalinity(self):
        '''
        a function that returns the prediction list
        returned from the web service
        '''
        r = self.getPrediction()
        result = r.decode()
        print(result)
        prediction_first_index = result.rfind(",") + 2
        prediction_last_index = prediction_first_index + 8
        return (result[prediction_first_index:prediction_last_index])
