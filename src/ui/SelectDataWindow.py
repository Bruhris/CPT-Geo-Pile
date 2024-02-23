# Import libraries from PyQt5 to create widgets and windows
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QStyle, QMessageBox, QTableWidgetItem, QWidget
# Import pandas to store data and input files
import pandas as pd

class SelectDataWindow(QDialog):
    def __init__(self, dataframe):
        super().__init__()
        pixmapi = QStyle.SP_MessageBoxInformation
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)
        self.setWindowTitle("Select Data")
        self.df = dataframe
        self.onlyInt = QtGui.QIntValidator()
        self.resize(900,800)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.submitBtn = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitBtn.sizePolicy().hasHeightForWidth())
        self.submitBtn.setText("Submit")
        self.submitBtn.setSizePolicy(sizePolicy)
        self.submitBtn.setObjectName("submitBtn")
        self.gridLayout.addWidget(self.submitBtn, 6, 0, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setText("Cancel")
        self.cancelBtn.setSizePolicy(sizePolicy)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel()
        self.label.setText("Column Number:")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.columnNumLEdit = QtWidgets.QLineEdit()
        self.columnNumLEdit.setValidator(self.onlyInt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columnNumLEdit.sizePolicy().hasHeightForWidth())
        self.columnNumLEdit.setSizePolicy(sizePolicy)
        self.columnNumLEdit.setObjectName("columnNumLEdit")
        self.columnNumLEdit.setValidator(QtGui.QIntValidator(
            bottom=0
        ))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.columnNumLEdit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.formLayout, 5, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Depth")
        self.comboBox.addItem("Qt")
        self.comboBox.addItem("Su")
        self.comboBox.addItem("Ic")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.setLayout(self.gridLayout)

        self.submitBtn.clicked.connect(self.submitData)
        self.cancelBtn.clicked.connect(self.closeWindow)

        self.df.fillna('',inplace = True)
        self.tableWidget.setRowCount(self.df.shape[0])
        self.tableWidget.setColumnCount(self.df.shape[1])

        for row in range(len(self.df.index)):
            for col in range(len(self.df.columns)):
                value = self.df.iloc[row, col]
                if isinstance(value, (float,int)):
                    value = '{0:0.2f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, tableItem)
    
    def submitData(self):
        measurement_name = self.comboBox.currentText()
        # Assign number inputted by user to attribute of class
        try:
            self.col_num = int(self.columnNumLEdit.text())

        # If there is no value inputted, return an error message asking the user to input number
        except ValueError:
            selectionmsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxCritical
            icon = selectionmsg.style().standardIcon(pixmapi)
            selectionmsg.setWindowIcon(icon)
            selectionmsg.setIcon(QMessageBox.Critical)
            selectionmsg.setText("You must input a column number first")
            selectionmsg.setWindowTitle("Error")
            return selectionmsg.exec_() 
        
        # Create an attribute to store the data from the excel file as a dataframe
        try:
            self.fileValues = self.df.iloc[1:, self.col_num-1].tolist()
            self.fileValues = pd.DataFrame(self.fileValues)
        except IndexError: # If the column number is invalid, display error message
            colErrormsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxCritical
            icon = colErrormsg.style().standardIcon(pixmapi)
            colErrormsg.setWindowIcon(icon)
            colErrormsg.setIcon(QMessageBox.Critical)
            colErrormsg.setText("That column number is out of bounds")
            colErrormsg.setWindowTitle("Error")
            return colErrormsg.exec_() 

        # Update the corresponding table to display to user and values for measurement object
        # in MainWindow based on option select from comboBox
        if measurement_name == "Depth":
            self.updateObj(self.fileValues, "Depth")
            self.updateMeasurements(self.fileValues, "Depth")

        elif measurement_name == "Qt":
            self.updateObj(self.fileValues, "Qt")
            self.updateMeasurements(self.fileValues, "Qt")

        elif measurement_name == "Su":
            self.updateObj(self.fileValues, "Su")
            self.updateMeasurements(self.fileValues, "Su")

        elif measurement_name == "Ic":
            self.updateObj(self.fileValues, "Ic")
            self.updateMeasurements(self.fileValues, "Ic")

        # Close the window when finished
        self.closeWindow()

    def closeWindow(self):
        self.close()