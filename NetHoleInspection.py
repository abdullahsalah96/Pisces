from cognitiveServices import Server


class NetHoleDetection(Server):
    def __init__(self):
        self.httpAddress = 'australiaeast.api.cognitive.microsoft.com'
        self.subAddress = "/customvision/v3.0/Prediction/0081ddad-4c13-4705-ac6b-819068f863f8/classify/iterations/Fishnet_Holes_Detection/image"
        self.predKey = 'bd5db334ffa249f1bd8ca2d43ccf5da3'
        self.contentType = 'application/octet-stream'
        self.predkey = '/subscriptions/16e8c7d2-4877-4c8f-bb77-ae2931dd33eb/resourceGroups/Test/providers/Microsoft.CognitiveServices/accounts/Test_Prediction'
        super().__init__(self.httpAddress, self.subAddress, self.predKey, self.contentType, self.predkey)

    def predict(self, img):
        """
        a function that returns:
            * 1 if the fishnet doesn't have a hole
            * 2 if the fishnet has a hole
            * 0 otherwise
        """
        pred = self.getPrediction(img).decode()
        print(pred)
        tag_index = pred.find("tagId") + 8
        if(pred[tag_index:tag_index+1] == 'f'):
            return 'No Hole'
        elif(pred[tag_index:tag_index+1] == '4'):
            return 'Hole'
        else:
            return "Can't Determine"
