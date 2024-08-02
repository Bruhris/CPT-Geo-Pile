import os
import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QWidget
from pyqtgraph import PlotWidget

from Resistance import ShaftResistance, BaseResistance
from MeasurementData import MeasurementData
from SelectDataWindow import SelectWindowDialog


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 787)
        
        # self.shaftResistance = ShaftResistance()
        # self.baseResistance = BaseResistance()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.measurements_tab = QtWidgets.QWidget()
        self.measurements_tab.setObjectName("measurements_tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.measurements_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 381, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openFileButton.setObjectName("openFileButton")
        self.verticalLayout.addWidget(self.openFileButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.worksheetLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.worksheetLabel.setObjectName("worksheetLabel")
        self.horizontalLayout.addWidget(self.worksheetLabel)
        self.worksheetNumberSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.worksheetNumberSpinBox.setObjectName("worksheetNumberSpinBox")
        self.horizontalLayout.addWidget(self.worksheetNumberSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.filePathLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.filePathLabel.setObjectName("filePathLabel")
        self.verticalLayout.addWidget(self.filePathLabel)
        self.measurementFileTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.measurementFileTableWidget.setObjectName("measurementFileTableWidget")
        self.measurementFileTableWidget.setColumnCount(0)
        self.measurementFileTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.measurementFileTableWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.measurements_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(440, 15, 551, 691))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.measurementSelectionButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.measurementSelectionButton.setObjectName("measurementSelectionButton")
        self.verticalLayout_2.addWidget(self.measurementSelectionButton)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.depthLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.depthLabel.setObjectName("depthLabel")
        self.gridLayout_2.addWidget(self.depthLabel, 0, 0, 1, 1)
        self.QtLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.QtLabel.setObjectName("QtLabel")
        self.gridLayout_2.addWidget(self.QtLabel, 0, 1, 1, 1)
        self.SuLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.SuLabel.setObjectName("SuLabel")
        self.gridLayout_2.addWidget(self.SuLabel, 2, 0, 1, 1)
        self.IcLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.IcLabel.setObjectName("IcLabel")
        self.gridLayout_2.addWidget(self.IcLabel, 2, 1, 1, 1)
        self.depthTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.depthTableWidget.setObjectName("depthTableWidget")
        self.depthTableWidget.setColumnCount(0)
        self.depthTableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.depthTableWidget, 1, 0, 1, 1)
        self.QtTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.QtTableWidget.setObjectName("QtTableWidget")
        self.QtTableWidget.setColumnCount(0)
        self.QtTableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.QtTableWidget, 1, 1, 1, 1)
        self.SuTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.SuTableWidget.setObjectName("SuTableWidget")
        self.SuTableWidget.setColumnCount(0)
        self.SuTableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.SuTableWidget, 3, 0, 1, 1)
        self.IcTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.IcTableWidget.setObjectName("IcTableWidget")
        self.IcTableWidget.setColumnCount(0)
        self.IcTableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.IcTableWidget, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        icon = QtGui.QIcon.fromTheme("folder")
        self.tabWidget.addTab(self.measurements_tab, icon, "")
        self.calculations_tab = QtWidgets.QWidget()
        self.calculations_tab.setObjectName("calculations_tab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.calculations_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 301, 691))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.calculationMethodComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.calculationMethodComboBox.setObjectName("calculationMethodComboBox")
        self.calculationMethodComboBox.addItem("")
        self.calculationMethodComboBox.addItem("")
        self.calculationMethodComboBox.addItem("")
        self.calculationMethodComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.calculationMethodComboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.constantTypeComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.constantTypeComboBox.setObjectName("constantTypeComboBox")
        self.constantTypeComboBox.addItem("")
        self.constantTypeComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.constantTypeComboBox)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.OPDInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.OPDInput.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=3,
                notation=QtGui.QDoubleValidator.StandardNotation))
        self.OPDInput.setObjectName("OPDInput")
        self.gridLayout_3.addWidget(self.OPDInput, 1, 1, 1, 1)
        self.GWTLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.GWTLabel.setObjectName("GWTLabel")
        self.gridLayout_3.addWidget(self.GWTLabel, 13, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 14, 0, 1, 1)
        self.ocvInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.ocvInput.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 360,
                decimals=1,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        self.ocvInput.setObjectName("ocvInput")
        self.gridLayout_3.addWidget(self.ocvInput, 11, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 6, 0, 1, 1)
        self.PTInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.PTInput.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=4,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        self.PTInput.setObjectName("PTInput")
        self.gridLayout_3.addWidget(self.PTInput, 9, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 12, 0, 1, 1)
        self.unitWeightInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.unitWeightInput.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        self.unitWeightInput.setObjectName("unitWeightInput")
        self.gridLayout_3.addWidget(self.unitWeightInput, 15, 1, 1, 1)
        self.OPDLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.OPDLabel.setObjectName("OPDLabel")
        self.gridLayout_3.addWidget(self.OPDLabel, 1, 0, 1, 1)
        self.updateParamsButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.updateParamsButton.setObjectName("updateParamsButton")
        self.gridLayout_3.addWidget(self.updateParamsButton, 17, 0, 1, 1)
        self.MPLInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.MPLInput.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        self.MPLInput.setObjectName("MPLInput")
        self.gridLayout_3.addWidget(self.MPLInput, 3, 1, 1, 1)
        self.unitWeightLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.unitWeightLabel.setObjectName("unitWeightLabel")
        self.gridLayout_3.addWidget(self.unitWeightLabel, 15, 0, 1, 1)
        self.ocvLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.ocvLabel.setObjectName("ocvLabel")
        self.gridLayout_3.addWidget(self.ocvLabel, 11, 0, 1, 1)
        self.noIntervalInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.noIntervalInput.setValidator(QtGui.QIntValidator(
                bottom=0,
                top = 1000
            ))
        self.noIntervalInput.setObjectName("noIntervalInput")
        self.gridLayout_3.addWidget(self.noIntervalInput, 7, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 10, 0, 1, 1)
        self.intervalLenInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.intervalLenInput.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,  
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        self.intervalLenInput.setObjectName("intervalLenInput")
        self.gridLayout_3.addWidget(self.intervalLenInput, 5, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 8, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 1)
        self.intervalLenLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.intervalLenLabel.setObjectName("intervalLenLabel")
        self.gridLayout_3.addWidget(self.intervalLenLabel, 5, 0, 1, 1)
        self.noIntervalLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.noIntervalLabel.setObjectName("noIntervalLabel")
        self.gridLayout_3.addWidget(self.noIntervalLabel, 7, 0, 1, 1)
        self.GWTInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.GWTInput.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        self.GWTInput.setObjectName("GWTInput")
        self.gridLayout_3.addWidget(self.GWTInput, 13, 1, 1, 1)
        self.PTLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.PTLabel.setObjectName("PTLabel")
        self.gridLayout_3.addWidget(self.PTLabel, 9, 0, 1, 1)
        self.MPLLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.MPLLabel.setObjectName("MPLLabel")
        self.gridLayout_3.addWidget(self.MPLLabel, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 16, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.calculations_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(340, 20, 651, 201))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.constantsTableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.constantsTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.constantsTableWidget.sizePolicy().hasHeightForWidth())
        self.constantsTableWidget.setSizePolicy(sizePolicy)
        self.constantsTableWidget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.constantsTableWidget.setObjectName("constantsTable")
        self.constantsTableWidget.setColumnCount(7)
        self.constantsTableWidget.setRowCount(1)
        self.constantsTableWidget.setHorizontalHeaderLabels(['a', 'b', 'c', 'd', 'e', 'u', 'v'])
        self.header = self.constantsTableWidget.horizontalHeader()
        self.vheader = self.constantsTableWidget.verticalHeader()
        self.vheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.vheader.hide()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(1)
        self.horizontalLayout_2.addWidget(self.constantsTableWidget)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.calcSRButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.calcSRButton.setObjectName("calcSRButton")
        self.verticalLayout_5.addWidget(self.calcSRButton)
        self.calcBRButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.calcBRButton.setObjectName("calcBRButton")
        self.verticalLayout_5.addWidget(self.calcBRButton)
        self.calcTRButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.calcTRButton.setObjectName("calcTRButton")
        self.verticalLayout_5.addWidget(self.calcTRButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.calcTableWidget = QtWidgets.QTableWidget(self.calculations_tab)
        self.calcTableWidget.setGeometry(QtCore.QRect(340, 260, 651, 441))
        self.calcTableWidget.setObjectName("calcTableWidget")
        self.calcTableWidget.setColumnCount(0)
        self.calcTableWidget.setRowCount(0)
        icon = QtGui.QIcon.fromTheme("accessories-calculator")
        self.tabWidget.addTab(self.calculations_tab, icon, "")
        self.visualization_tab = QtWidgets.QWidget()
        self.visualization_tab.setObjectName("visualization_tab")
        self.graphDisplay = PlotWidget(self.visualization_tab)
        self.graphDisplay.setGeometry(QtCore.QRect(410, 30, 561, 661))
        self.graphDisplay.setObjectName("graphDisplay")

        self.graphDisplay.setBackground('w')
        self.graphDisplay.getPlotItem().hideAxis('bottom')
        self.graphDisplay.getPlotItem().showAxis('top')
        self.graphDisplay.getAxis('left').setPen('b')
        self.graphDisplay.getAxis('left').setTextPen('b')
        self.graphDisplay.getAxis('top').setPen('b')
        self.graphDisplay.getAxis('top').setTextPen('b')
        self.graphDisplay.getAxis('bottom').setPen('b')
        self.graphDisplay.getAxis('bottom').setTextPen('b')
        self.graphDisplay.getViewBox().invertY(True)

        self.graphOptionsComboBox = QtWidgets.QComboBox(self.visualization_tab)
        self.graphOptionsComboBox.setGeometry(QtCore.QRect(20, 30, 162, 22))
        self.graphOptionsComboBox.setObjectName("graphOptionsComboBox")
        self.graphOptionsComboBox.addItem("")
        self.graphOptionsComboBox.addItem("")
        self.graphOptionsComboBox.addItem("")
        self.graphOptionsComboBox.addItem("")
        self.graphOptionsComboBox.addItem("")
        icon = QtGui.QIcon.fromTheme("utilities-system-monitor")
        self.tabWidget.addTab(self.visualization_tab, icon, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.measurements = MeasurementData()

        self.openFileButton.clicked.connect(self.openFile)
        self.measurementSelectionButton.clicked.connect(self.openSelectDataWindow)
        self.updateParamsButton.clicked.connect(self.updateParameters)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def openFile(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file', os.getenv('HOME'), 'XLS File (*.xls)')

        if (not all(self.file)):
            return
        
        try:
            self.data = pd.read_excel(self.file[0], sheet_name=self.worksheetNumberSpinBox.value())

            self.measurementFileTableWidget.setRowCount(self.data.shape[0])
            self.measurementFileTableWidget.setColumnCount(self.data.shape[1])

            for row in range(len(self.data.index)):
                for col in range(len(self.data.columns)):
                    value = self.data.iloc[row, col]
                    tableItem = QTableWidgetItem(str(value))
                    tableItem.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.measurementFileTableWidget.setItem(row, col, tableItem)
                    
            self.filePathLabel.setText(f"File: {self.file[0]}")
        except ValueError or IndexError:
            print("There was an error")
    
    def openSelectDataWindow(self):
        try:
            dataWindow = SelectWindowDialog(self.data, self)
            
            if(dataWindow.exec_()):
                self.updateMeasurements(dataWindow.fileValues, dataWindow.measurement_name)

        except AttributeError as err:
            print(err)
        
    
    def updateMeasurements(self, data, type):
        match type:
            case "Depth":
                self.updateTable(data, self.depthTableWidget)
                self.measurements.updateDepth(data)
            case "Qt":
                self.updateTable(data, self.QtTableWidget)
                self.measurements.updateQt(data)
            case "Su":
                self.updateTable(data, self.SuTableWidget)
                self.measurements.updateSu(data)
            case "Ic":
                self.updateTable(data, self.IcTableWidget)
                self.measurements.updateIc(data)
            case _:
                print("There was an error")


    def updateTable(self, dataframe, tableWidget):
        dataframe.fillna('',inplace = True)

        tableWidget.setRowCount(dataframe.shape[0])
        tableWidget.setColumnCount(1)

        for row in range(len(dataframe.index)):
            value = dataframe.iloc[row, 0]
            if isinstance(value, (float,int)):
                value = '{0:0.2f}'.format(value)
            tableItem = QTableWidgetItem(str(value))
            tableWidget.setItem(row, 0, tableItem)
        
        hheader = tableWidget.horizontalHeader()
        hheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    
    def updateParameters(self):
        parameters = {}
        
        outerPileDiameter = float(self.OPDInput.text())
        minimumPileLength = float(self.MPLInput.text())
        intervalLength = float(self.intervalLenInput.text())
        noIntervals = int(self.noIntervalInput.text())
        pileThickness = float(self.PTInput.text())
        frictionAngle = float(self.ocvInput.text())
        groundWaterTable = float(self.GWTInput.text())
        unitWeight = float(self.unitWeightInput.text())
        
        calculationMethod = self.calculationMethodComboBox.currentText() 
        constantType = self.constantTypeComboBox.currentText()


        if ((minimumPileLength + (intervalLength * noIntervals) > self.measurements.getDepth().iloc[-1, 0]) or
            (round(minimumPileLength + (intervalLength * noIntervals) + (4 * outerPileDiameter)) > self.measurements.getDepth().iloc[-1, 0]) or
            (pileThickness >= outerPileDiameter)):
                raise ValueError
        
        parameters.update({"outerPileDiameter" : outerPileDiameter})
        parameters.update({"minimumPileLength" : minimumPileLength})
        parameters.update({"intervalLength" : intervalLength})
        parameters.update({"noIntervals" : noIntervals})
        parameters.update({"pileThickness" : pileThickness})
        parameters.update({"frictionAngle" : frictionAngle})
        parameters.update({"groundWaterTable" : groundWaterTable})
        parameters.update({"unitWeight" : unitWeight})
        
        self.measurements.setParameters(parameters, constantType, calculationMethod)

        return




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openFileButton.setText(_translate("MainWindow", "Select Measurement File"))
        self.worksheetLabel.setText(_translate("MainWindow", "Worksheet Number"))
        self.filePathLabel.setText(_translate("MainWindow", "File Path: "))
        self.measurementSelectionButton.setText(_translate("MainWindow", "Select Measurements"))
        self.depthLabel.setText(_translate("MainWindow", "Depth (m)"))
        self.QtLabel.setText(_translate("MainWindow", "Qt (MPa)"))
        self.SuLabel.setText(_translate("MainWindow", "Su (kPa)"))
        self.IcLabel.setText(_translate("MainWindow", "Ic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measurements_tab), _translate("MainWindow", "Measurements"))
        self.calculationMethodComboBox.setItemText(0, _translate("MainWindow", "ICP-05"))
        self.calculationMethodComboBox.setItemText(1, _translate("MainWindow", "UWA-05"))
        self.calculationMethodComboBox.setItemText(2, _translate("MainWindow", "FURGO-05"))
        self.calculationMethodComboBox.setItemText(3, _translate("MainWindow", "NGI-05"))
        self.constantTypeComboBox.setItemText(0, _translate("MainWindow", "Compression"))
        self.constantTypeComboBox.setItemText(1, _translate("MainWindow", "Tension"))
        self.unitWeightLabel.setText(_translate("MainWindow", "Unit Weight:"))
        self.noIntervalLabel.setText(_translate("MainWindow", "Number of Intervals:"))
        self.MPLLabel.setText(_translate("MainWindow", "Minimum Pile Length (m):"))
        self.GWTLabel.setText(_translate("MainWindow", "GWT (m):"))
        self.intervalLenLabel.setText(_translate("MainWindow", "Interval Length (m):"))
        self.OPDLabel.setText(_translate("MainWindow", "Outer Pile Diameter:"))
        self.PTLabel.setText(_translate("MainWindow", "Pile Thickness (m):"))
        self.ocvLabel.setText(_translate("MainWindow", "ocv Value (degrees):"))
        self.updateParamsButton.setText(_translate("MainWindow", "Update Parameters"))
        self.calcSRButton.setText(_translate("MainWindow", "Shaft Resistance"))
        self.calcBRButton.setText(_translate("MainWindow", "Base Resistance"))
        self.calcTRButton.setText(_translate("MainWindow", "Total Resistance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calculations_tab), _translate("MainWindow", "Calculations"))
        self.graphOptionsComboBox.setItemText(0, _translate("MainWindow", "Qt vs. Depth"))
        self.graphOptionsComboBox.setItemText(1, _translate("MainWindow", "Su vs. Depth"))
        self.graphOptionsComboBox.setItemText(2, _translate("MainWindow", "Base Resistance vs. Depth"))
        self.graphOptionsComboBox.setItemText(3, _translate("MainWindow", "Shaft Resistance vs. Depth"))
        self.graphOptionsComboBox.setItemText(4, _translate("MainWindow", "Total Resistance vs. Depth"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visualization_tab), _translate("MainWindow", "Visualization"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
