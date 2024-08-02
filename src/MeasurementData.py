import math 

class MeasurementData:
    # Constructor that creates dictionary for storing the dataframes of attributes
    def __init__(self):
        self.depthDf = None
        self.qtDf = None
        self.suDf = None
        self.icDf = None
        self.parameters = {}
        self.constantType = ""
        self.calcMethod = ""
        self.displacementRatio = 0
        self.constants = {}

    def setParameters(self, parameters, constantType, calcMethod):
        self.parameters = parameters
        self.constantType = constantType
        self.calcMethod = calcMethod
        self.displacmentRatio = 1 - math.pow(((parameters["outerPileDiameter"] - parameters["pileThickness"] * 2) / parameters["outerPileDiameter"]), 2)

    def updateDepth(self, data):
        self.depthDf = data

    def getDepth(self):
        return self.depthDf

    def updateQt(self, data):
        self.qtDf = data

    def updateSu(self, data):
        self.suDf = data

    def updateIc(self, data):
        self.icDf = data
    
    def setConstants(self): 
        if self.constantType == "Compression":
            match self.calcMethod:
                case "ICP-05":
                    self.constants = {'a': 0.1, 'b': 0.2, 'c': 0.4 , 'd': 1 , 'e': 0 , 'u': 0.023 , 'v': math.pow(self.__disp_ratio, 0.25)}

                case "UWA-05":
                    self.constants = {'a': 0, 'b': 0.3, 'c': 0.5, 'd': 1 , 'e': 0 , 'u': 0.003 , 'v': 2}
            
                case "FUGRO-05":
                    self.constants = {'a': 0.05, 'b': 0.45, 'c': 0.90 , 'd': 0 , 'e': 1, 'u': 0.043 , 'v': math.pow(self.__disp_ratio, 0.5)}

                case "NGI-05": 
                    self.constants = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'u': 1.3 , 'v': 0}
        else:
            match self.calcMethod:
                case "ICP-05":
                    self.constants = {'a': 0.1, 'b': 0.2, 'c': 0.4, 'd': 1, 'e': 0 , 'u': 0.016 , 'v': math.pow(self.__disp_ratio, 0.25)}

                case "UWA-05":
                    self.constants = {'a': 0, 'b': 0.3, 'c': 0.5 , 'd': 1 , 'e': 0 , 'u': 0.022 , 'v': 2}
    
                case "FUGRO-05":
                    self.constants = {'a': 0.15, 'b': 0.42, 'c': 0.85 , 'd': 0 , 'e': 0 , 'u': 0.025 , 'v': math.pow(self.__disp_ratio, 0.5)}

                case "NGI-05":
                    self.constants = {'a': 0, 'b': 0, 'c': 0 , 'd': 0 , 'e': 0 , 'u': 1 , 'v': 0}


    
    # Function used for checking if all measurement values have been inputted
    def checkMeasurementValues(self): 
        return self.depthDf and self.icDf and self.qtDf and self.suDf

    # Getter method for dictionary of all dataframes
    def getMeasurementValues(self):
        return self.__measurement_values