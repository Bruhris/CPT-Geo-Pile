import math

class Parameters:
    def __init__(self, calc_method, const_type, outer_diam, min_len, interval_len,
     no_interval, pile_thickness, friction_angle, gwt, unit_weight):
        # Initalize attributes of class
        self.__calc_method = calc_method
        self.__const_type = const_type
        self.__disp_ratio = 1-((outer_diam-pile_thickness*2)/outer_diam)**2
        # Create a dictionary of values that store all user inputted values 
        # as values and a correspondingly named string as its key
        self.__values = {
            "calc_method" : calc_method,
            "const_type" : const_type,
            "outer_diam" : outer_diam,
            "min_len" : min_len,
            "interval_len" : interval_len,
            "no_interval" : no_interval + 1,
            "pile_thickness" : pile_thickness,
            "friction_angle" : min(math.tan(friction_angle), 0.55),
            "gwt" : gwt,
            "unit_weight" : unit_weight,
            "disp_ratio" : self.__disp_ratio
        }

    # Setter method for the constant values
    def setConst(self): # Assign constants to dictionary with values corresponding to a key name from: a, b, c, d, e, u, v
        if self.__const_type == "Compression": # depending on the constant type and calculation method
            if self.__calc_method == "ICP-05":
                self.__constants = {'a': 0.1, 'b': 0.2, 'c': 0.4 , 'd': 1 , 'e': 0 , 'u': 0.023 , 'v': self.__disp_ratio**0.25}

            elif self.__calc_method == "UWA-05":
                self.__constants = {'a': 0, 'b': 0.3, 'c': 0.5, 'd': 1 , 'e': 0 , 'u': 0.003 , 'v': 2}
            
            elif self.__calc_method == "FUGRO-05":
                self.__constants = {'a': 0.05, 'b': 0.45, 'c': 0.90 , 'd': 0 , 'e': 1, 'u': 0.043 , 'v': self.__disp_ratio**0.5}

            elif self.__calc_method == "NGI-05": 
                self.__constants = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'u': 1.3 , 'v': 0}

        elif self.__const_type == "Tension":
            if self.__calc_method == "ICP-05":
                self.__constants = {'a': 0.1, 'b': 0.2, 'c': 0.4, 'd': 1, 'e': 0 , 'u': 0.016 , 'v': self.__disp_ratio**0.25}

            elif self.__calc_method == "UWA-05":
                self.__constants = {'a': 0, 'b': 0.3, 'c': 0.5 , 'd': 1 , 'e': 0 , 'u': 0.022 , 'v': 2}
 
            elif self.__calc_method == "FUGRO-05":
                self.__constants = {'a': 0.15, 'b': 0.42, 'c': 0.85 , 'd': 0 , 'e': 0 , 'u': 0.025 , 'v': self.__disp_ratio**0.5}

            elif self.__calc_method == "NGI-05":
                self.__constants = {'a': 0, 'b': 0, 'c': 0 , 'd': 0 , 'e': 0 , 'u': 1 , 'v': 0}

    # Getter method for constant values
    def getConstants(self):
        return self.__constants
    # Getter method for the values inputted by user
    def getValues(self):
         return self.__values
    # Getter method for inputted values and constant values
    def getParameters(self):
        self.__parameters = {}
        self.__parameters.update({"constants" : self.__constants})
        self.__parameters.update({"values" : self.__values})
        return self.__parameters