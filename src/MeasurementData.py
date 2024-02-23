class MeasurementData:
    # Constructor that creates dictionary for storing the dataframes of attributes
    def __init__(self):
        self.__measurement_values = {}
        
    # Setter method for depth dataframe
    def updateDepth(self, depth_values):
        self.__depth_values = depth_values
        self.__measurement_values.update({"depth" : self.__depth_values})

    # Getter method for depth dataframe
    def getDepth(self):
        return self.__depth_values
        
    # Setter method for qt dataframe
    def updateQt(self, qt_values):
        self.__qt_values = qt_values
        self.__measurement_values.update({"qt" : self.__qt_values})

    # Getter method for qt dataframe
    def getQt(self):
        return self.__qt_values

    # Setter method for su dataframe
    def updateSu(self, su_values):
        self.__su_values = su_values
        self.__measurement_values.update({"su" : self.__su_values})

    # Getter method for su dataframe
    def getSu(self):
        return self.__su_values

    # Setter method for ic dataframe
    def updateIc(self, ic_values):
        self.__ic_values = ic_values
        self.__measurement_values.update({"ic" : self.__ic_values})

    # Getter method for ic dataframe
    def getIc(self):
        return self.__ic_values
    
    # Function used for checking if all measurement values have been inputted
    def checkMeasurementValues(self): 
        if ("qt" in self.__measurement_values and "depth" in self.__measurement_values
        and "su" in self.__measurement_values and "ic" in self.__measurement_values):
            return True
        else:
            return False

    # Getter method for dictionary of all dataframes
    def getMeasurementValues(self):
        return self.__measurement_values