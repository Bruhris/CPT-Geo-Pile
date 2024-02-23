# CPT Geo Pile Program (main.py)

from PyQt5.QtWidgets import  QStyle, QMessageBox

import mysql.connector as mdb


class Database:
    def __init__(self): # Assign values for connecting to database
        self.host = "localhost"
        self.user = "root"
        self.passwd = "passwrd"
        self.databasename = "sys"

    def connect(self):
        # Try to create connection to database and if connected, will display message alerting user
        try:
            # Connect to database using values set for connecting to database
            self.db = mdb.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.databasename)
            self.cur = self.db.cursor() # Create cursor to manage database

            connectmsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxInformation
            icon = connectmsg.style().standardIcon(pixmapi)
            connectmsg.setWindowIcon(icon)
            connectmsg.setIcon(QMessageBox.Information)
            connectmsg.setText("You connected to the database")
            connectmsg.setWindowTitle("Connected")
            connectmsg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            connectmsg.exec_()
            return True
        
            # If connection fails, display error message to user
        except mdb.Error as e:
            disconnectmsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxWarning
            icon = disconnectmsg.style().standardIcon(pixmapi)
            disconnectmsg.setWindowIcon(icon)
            disconnectmsg.setIcon(QMessageBox.Warning)
            disconnectmsg.setText("You failed to connect to the database")
            disconnectmsg.setWindowTitle("No Connection")
            disconnectmsg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            disconnectmsg.exec_()
            return False

    def disconnect(self): # Close the connection with the database
        self.db.close()
    
    def checkTable(self, tablenames): # Check to see if there are already tables using the CPT code within database
        # Initialize string containing query for database
        find_table = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '%s'"
        self.cur.execute(find_table % (tablenames[0],)) # Execute command to find table
        self.tableResult = self.cur.fetchone() # Check to see if table is found
        if self.tableResult == (1,): # If the table is found, ask the user if they want to replace the table or not
            tablemsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxQuestion
            icon = tablemsg.style().standardIcon(pixmapi)
            tablemsg.setWindowIcon(icon)
            tablemsg.setIcon(QMessageBox.Question)
            tablemsg.setText("There is already a table with that name")
            tablemsg.setInformativeText("Do you want to replace the tables information with the new data?")
            tablemsg.setWindowTitle("Error")
            tablemsg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            value = tablemsg.exec_()

            if value == QMessageBox.Cancel: # If the user presses cancel option, end function
                return False
            for i in tablenames:
                self.cur.execute("DROP TABLE IF EXISTS `%s`" % (i,))
        
        return True

    def createMeasurementTable(self, tablename, dataDictionary):
        # Initialize string containing query to create table in database
        createTableCmd = '''CREATE TABLE `%s`(
                    depth FLOAT,
                    qt FLOAT,   
                    ic FLOAT,
                    su FLOAT)
                    '''
        # Execute command using cursor
        self.cur.execute(createTableCmd % (tablename,))

        # Input all measurement values using nested for loop into table using corresponding columns
        for row in range(len(dataDictionary['depth'].index)):
            dvalue = float(dataDictionary['depth'].iloc[row, 0])
            qtvalue = float(dataDictionary['qt'].iloc[row, 0])
            suvalue = float(dataDictionary['su'].iloc[row, 0])
            icvalue = float(dataDictionary['ic'].iloc[row, 0])
            insert_values = 'INSERT INTO `%s` (%s,  %s, %s, %s) VALUES (%s, %s, %s, %s)'
            # Execute command
            self.cur.execute(insert_values % (tablename, 'depth', 'qt', 'su', 'ic', dvalue, qtvalue, suvalue, icvalue))

        # Commit the changes to the database
        self.db.commit()
    
    def createParameterTable(self, tablename, dataDictionary):
        # Initialize string containing query to create table in database
        createTableCmd = '''CREATE TABLE `%s`(
                            a FLOAT,
                            b FLOAT,
                            c FLOAT,
                            d FLOAT,
                            e FLOAT,
                            u FLOAT,
                            v FLOAT, 
                            calc_method TINYTEXT,
                            const_method TINYTEXT,
                            outer_pile_diam FLOAT,
                            min_pile_len FLOAT,
                            interval_length FLOAT,
                            no_interval INT,
                            pile_thickness FLOAT,
                            friction_angle FLOAT,
                            gwt FLOAT,
                            unit_weight FLOAT
                            )
                            '''

        # Execute command using cursor
        self.cur.execute(createTableCmd % (tablename,))

        value = dataDictionary['values']
        constants = dataDictionary['constants']

        # Input all measurement values into table with corresponding column
        insert_values = '''INSERT INTO `%s` (a, b, c, d, e, u, v, calc_method, const_method, outer_pile_diam, min_pile_len, 
                    interval_length, no_interval, pile_thickness, friction_angle, gwt, unit_weight) VALUES (%s, %s, %s, 
                    %s, %s, %s, %s, "`%s`", "%s", %s, %s, %s, %s, %s, %s, %s, %s)'''
        # Execute command
        self.cur.execute(insert_values % (tablename, constants.get('a'), constants.get('b'), constants.get('c'), constants.get('d'), 
        constants.get('e'), constants.get('u'), constants.get('v'), value.get('calc_method'), value.get('const_type'), value.get('outer_diam'), 
        value.get('min_len'), value.get('interval_len'), value.get('no_interval'), value.get("pile_thickness"), value.get("friction_angle"), 
        value.get('gwt'), value.get('unit_weight')))

        # Commit the changes to the database
        self.db.commit()

    def createCalculationTable(self, tablename, dataDictionary):
        # Initialize string containing query to create table in database
        createTableCmd = '''CREATE TABLE `%s`(
                    length FLOAT,
                    shaft_resistance INT,
                    base_resistance INT,
                    total_resistance INT
                    )
                    '''
        # Execute command using cursor
        self.cur.execute(createTableCmd % (tablename,))
        
        # Input all measurement values into table with corresponding column using for loop
        for row in range(len(dataDictionary['total_resistance'].index)):
            svalue = float(dataDictionary['shaft_resistance'].iloc[row, 1])
            bvalue = float(dataDictionary['base_resistance'].iloc[row, 1])
            tvalue = float(dataDictionary['total_resistance'].iloc[row, 1])
            length = float(dataDictionary['total_resistance'].iloc[row, 0])
            insert_values = 'INSERT INTO `%s` (%s,  %s, %s, %s) VALUES (%s, %s, %s, %s)'
            # Execute command
            self.cur.execute(insert_values % (tablename, 'shaft_resistance', 'base_resistance', 
            'total_resistance', 'length', svalue, bvalue, tvalue, length))

        # Commit the changes to the database
        self.db.commit()