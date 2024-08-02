import pandas as pd
import math

class Resistance():
    def __init__(self):
        self.something = ''

    

class ShaftResistance(Resistance):
    def __init__(self, parameters, measurements):
        super().__init__(parameters, measurements)
    
    def calcShaftRes(self):
        intervals = self.values["no_interval"]
        tempPileLength = self.values["min_len"]
        while (intervals > 0):
            initial_len = 0.0
            total_shaft = 0
            while initial_len <= tempPileLength:
                if initial_len < self.values["gwt"]:
                    Po = self.values["unit_weight"] * initial_len
                else:
                    Po = self.values["unit_weight"] * self.values["gwt"] + (initial_len -  self.values["gwt"]) * (self.values["unit_weight"] - 10)
                try:
                    calc1 = self.constants['u'] * self.qt_data.iloc[int(initial_len * 10), 0]

                    calc2 = pow((Po/100), self.constants['a']) * pow((self.values["disp_ratio"]), self.constants['b'])

                    calc3 = max((tempPileLength - initial_len)/self.values["outer_diam"], pow(self.constants['v']), (-(self.constants['c'])))

                    calc4 = pow(self.values["friction_angle"], (-(self.constants['d']))) * min(pow((tempPileLength - initial_len)/self.values["outer_diam"]* (1/self.constants['v']), 1),(-(self.constants['e'])))

                    total_shaft += (calc1 * calc2 * calc3 * calc4) * 1000

                # If there is an error in the calculations, continue running function but don't add anything
                except (ZeroDivisionError, IndexError):
                    continue

                initial_len += 0.1
                initial_len = round(initial_len, 1)

            # Add length and resistance as key-pair values to dictionary and increase tempPileLength by the interval length
            self.resistanceDict.update({tempPileLength: total_shaft})
            # Increase the tempPileLength value by the interval lengths inputted by the user and repeat the loop with the new pile length
            tempPileLength+=self.values["interval_len"]
            intervals -= 1

class BaseResistance(Resistance):
    def __init__(self, parameters, measurements):
        # Run parent class (Resistance class) constructor 
        super().__init__(parameters, measurements)
    
    # For a more detailed description of the algorithm, refer to the appendices
    def calcBaseRes(self): 
        # Initialize variables that will be used in calculations later using measurements and parameters
        min_qt = 0
        # Get variables needed for calculating base resistance
        ffr = min(1, pow(((self.values["outer_diam"] - self.values["pile_thickness"] * 2) / 1.5), 0.2))
        arb = 1 - ffr * ((self.values["outer_diam"] - self.values["pile_thickness"]*2) / pow(self.values["outer_diam"]), 2)
        base_area = math.pi * pow((self.values["outer_diam"] / 2), 2)
        tempPileLen = self.values["min_len"]

        for j in range(self.values["no_interval"]): # For every interval
            min_qc = 0 # Variable used to store the smallest qc value which is calculated at each loop
            counter = 0.7 # Counter variable
            while counter <= 4: 
                # Calculate average qt values between a certain range
                section1 = self.average(tempPileLen, round(tempPileLen+(counter*self.values["outer_diam"]), 1), self.qt_data) 
                # Calculate the minimum qt values between a certain range
                section2, min_qt = self.min_average(round(tempPileLen + (counter*self.values["outer_diam"]), 1), tempPileLen, self.qt_data, min_qt)
                section3, min_qt = self.min_average(tempPileLen, round(tempPileLen - 8 * self.values["outer_diam"], 1), self.qt_data, min_qt)

                # Plug in the values into calculations
                qc = 0.5 * (0.5 * (section1 + section2) + section3)

                if counter == 0.7 or qc < min_qc:  # If this is the first iteration of the loop or the qc value calculated from
                    min_qc = qc                    # the while loop is smaller than min_qc, reassign the value min_qc to qc

                counter += 0.1 # Increment counter value by 0.1
                counter = round(counter, 1)
            # Calculate for base resistance as Qa
            Qb = min_qc * (0.15 + 0.45 * arb)
            Qa = Qb * base_area * 1000
            # Store the length and Qa (Base resistance value) as key-value pairs and increate the value of the 
            # tempPileLen by the interval length specified by the user
            self.resistanceDict.update({tempPileLen : Qa})
            tempPileLen+=self.values["interval_len"] # Increase the value of tempPileLen by the interval value 
                                                     # inputted by user and repeat loop

    def min_average(self, upperlen, lowerlen, qt_data, min_qt):
        minaveragelist = [] # Create a list that will store qt values
        min_qt = qt_data.iloc[int(upperlen*10), 0]
        while upperlen >= lowerlen: # While being between the range of the upper and lower lengths
            try:
                if qt_data.iloc[int(upperlen*10), 0] < min_qt: # If the qt value at the length is 
                    min_qt = qt_data.iloc[int(upperlen*10), 0] # less than the min_qt value, replace the min_qt value with the qt value
            except IndexError: # If the qt values trying to be called is out of bound, keep function running
                pass
            finally:
                minaveragelist.append(min_qt)
                upperlen-=0.1 # Decrement the upperlen by 0.1
                upperlen = round(upperlen, 1)
        if len(minaveragelist) == 0: # Prevents zero division error
            return 0, 0
        # Return the value of the min_qt and the average of the values within the list
        return sum(minaveragelist)/len(minaveragelist), min_qt
    

    def average(self, lowerlen, upperlen, qt_data):
        averagelist = [] # Create list that will store qt values
        while lowerlen <= upperlen: # While being between the range of the lower to upper length
            try:
                averagelist.append(qt_data.iloc[int(lowerlen*10),0]) # Add the value at that length to the list
            except IndexError: # If the qt values trying to be called is out of bound, keep function running
                pass
            finally:
                lowerlen+=0.1
                lowerlen = round(lowerlen, 1) # Increment the value of the lowerlen by 0.1
        if len(averagelist) == 0: # Prevents zero division error
            return 0
        return sum(averagelist)/len(averagelist) # Return the average of the list