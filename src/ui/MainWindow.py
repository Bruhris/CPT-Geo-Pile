import os
# Import libraries from PyQt5 to create widgets and windows
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QStyle, QMessageBox, QTableWidgetItem, QWidget
from PyQt5.QtCore import Qt
# Import library from pyqtgraph to plot data and create graphs
from pyqtgraph import PlotWidget
import pyqtgraph as pg
# Import pandas to store data and input files
import pandas as pd


from Resistance import BaseResistance, ShaftResistance
from MeasurementData import MeasurementData
from Database import Database
from Parameters import Parameters
from ui.SelectDataWindow import SelectDataWindow

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        self.measurementObj = MeasurementData()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.centralLayout.setObjectName("tablayout1")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        # Tab 1
        self.tab1.setObjectName("tab1")
        self.backgroundLayout = QtWidgets.QGridLayout(self.tab1)
        self.backgroundLayout.setObjectName("gridLayout_4")
        self.measurementLayouts = QtWidgets.QGridLayout()
        self.measurementLayouts.setObjectName("gridLayout_2")
        self.qtTable = QtWidgets.QTableWidget(self.tab1)
        self.qtTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtTable.sizePolicy().hasHeightForWidth())
        self.qtTable.setSizePolicy(sizePolicy)
        self.qtTable.setObjectName("qtTable")
        self.qtTable.setColumnCount(0)
        self.qtTable.setRowCount(0)
        self.measurementLayouts.addWidget(self.qtTable, 3, 1, 1, 1)
        self.depthLabel = QtWidgets.QLabel(self.tab1)
        self.depthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.depthLabel.setObjectName("depthLabel")
        self.measurementLayouts.addWidget(self.depthLabel, 2, 0, 1, 1)
        self.qtLabel = QtWidgets.QLabel(self.tab1)
        self.qtLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.qtLabel.setObjectName("qtLabel")
        self.measurementLayouts.addWidget(self.qtLabel, 2, 1, 1, 1)
        self.suTable = QtWidgets.QTableWidget(self.tab1)
        self.suTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suTable.sizePolicy().hasHeightForWidth())
        self.suTable.setSizePolicy(sizePolicy)
        self.suTable.setObjectName("suTable")
        self.suTable.setColumnCount(0)
        self.suTable.setRowCount(0)
        self.measurementLayouts.addWidget(self.suTable, 5, 0, 1, 1)
        self.icTable = QtWidgets.QTableWidget(self.tab1)
        self.icTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icTable.sizePolicy().hasHeightForWidth())
        self.icTable.setSizePolicy(sizePolicy)
        self.icTable.setObjectName("icTable")
        self.icTable.setColumnCount(0)
        self.icTable.setRowCount(0)
        self.measurementLayouts.addWidget(self.icTable, 5, 1, 1, 1)
        self.icLabel = QtWidgets.QLabel(self.tab1)
        self.icLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.icLabel.setObjectName("icLabel")
        self.measurementLayouts.addWidget(self.icLabel, 4, 1, 1, 1)
        self.depthTable = QtWidgets.QTableWidget(self.tab1)
        self.depthTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depthTable.sizePolicy().hasHeightForWidth())
        self.depthTable.setSizePolicy(sizePolicy)
        self.depthTable.setObjectName("depthTable")
        self.depthTable.setColumnCount(0)
        self.depthTable.setRowCount(0)
        self.measurementLayouts.addWidget(self.depthTable, 3, 0, 1, 1)
        self.suLabel = QtWidgets.QLabel(self.tab1)
        self.suLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.suLabel.setObjectName("suLabel")
        self.measurementLayouts.addWidget(self.suLabel, 4, 0, 1, 1)
        self.backgroundLayout.addLayout(self.measurementLayouts, 2, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(25, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.backgroundLayout.addItem(spacerItem, 2, 3, 1, 2)
        self.selectMeasurementsBtn = QtWidgets.QPushButton(self.tab1)
        self.selectMeasurementsBtn.setObjectName("selectMeasurementsBtn")
        self.backgroundLayout.addWidget(self.selectMeasurementsBtn, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(25, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.backgroundLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.worksheet_num = QtWidgets.QSpinBox(self.tab1)
        self.worksheet_num.setMinimum(1)
        self.worksheet_num.setValue(1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.worksheet_num.sizePolicy().hasHeightForWidth())
        self.worksheet_num.setSizePolicy(sizePolicy)
        self.worksheet_num.setObjectName("worksheet_num")
        self.gridLayout.addWidget(self.worksheet_num, 1, 1, 1, 1)
        self.measurementFileTable = QtWidgets.QTableWidget(self.tab1)
        self.measurementFileTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.measurementFileTable.setObjectName("measurementFileTable")
        self.measurementFileTable.setColumnCount(0)
        self.measurementFileTable.setRowCount(0)
        self.gridLayout.addWidget(self.measurementFileTable, 7, 0, 1, 3)
        self.worksheetNumber = QtWidgets.QLabel(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.worksheetNumber.sizePolicy().hasHeightForWidth())
        self.worksheetNumber.setSizePolicy(sizePolicy)
        self.worksheetNumber.setObjectName("worksheetNumber")
        self.gridLayout.addWidget(self.worksheetNumber, 1, 0, 1, 1)
        self.selectFileBtn = QtWidgets.QPushButton(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectFileBtn.sizePolicy().hasHeightForWidth())
        self.selectFileBtn.setSizePolicy(sizePolicy)
        self.selectFileBtn.setObjectName("selectFileBtn")
        self.gridLayout.addWidget(self.selectFileBtn, 0, 0, 1, 1)
        self.filePathLabel = QtWidgets.QLabel(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathLabel.sizePolicy().hasHeightForWidth())
        self.filePathLabel.setSizePolicy(sizePolicy)
        self.filePathLabel.setObjectName("filePathLabel")
        self.gridLayout.addWidget(self.filePathLabel, 2, 0, 1, 3)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.backgroundLayout.addLayout(self.gridLayout, 0, 1, 3, 1)
        self.tabWidget.addTab(self.tab1, "")

        # Tab 2
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 1, 1, 1)
        self.resistanceTable = QtWidgets.QTableWidget(self.tab2)
        self.resistanceTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.resistanceTable.setObjectName("resistanceTable")
        self.resistanceTable.setColumnCount(4)
        self.resistanceTable.setRowCount(0)
        self.resistanceTable.setHorizontalHeaderLabels(['Length [m]', 'Shaft Resistance [kN]', 'Base Resistance [kN]', 'Total Resistance [kN]'])
        self.hresistanceHeader = self.resistanceTable.horizontalHeader()
        self.hresistanceHeader.setSectionResizeMode(1)
        self.vresistanceHeader = self.resistanceTable.verticalHeader()
        self.vresistanceHeader.setSectionResizeMode(1)
        self.vresistanceHeader.hide()
        self.gridLayout_3.addWidget(self.resistanceTable, 2, 2, 4, 5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.calcMethods = QtWidgets.QComboBox(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcMethods.sizePolicy().hasHeightForWidth())
        self.calcMethods.setSizePolicy(sizePolicy)
        self.calcMethods.setObjectName("comboBox")
        self.calcMethods.addItem("")
        self.calcMethods.addItem("")
        self.calcMethods.addItem("")
        self.calcMethods.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.calcMethods)
        self.compressionRBtn = QtWidgets.QRadioButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compressionRBtn.sizePolicy().hasHeightForWidth())
        self.compressionRBtn.setSizePolicy(sizePolicy)
        self.compressionRBtn.setObjectName("compressionRBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.compressionRBtn)
        self.tensionRBtn = QtWidgets.QRadioButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tensionRBtn.sizePolicy().hasHeightForWidth())
        self.tensionRBtn.setSizePolicy(sizePolicy)
        self.tensionRBtn.setObjectName("tensionRBtn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tensionRBtn)
        self.outerPileDiam_label = QtWidgets.QLabel(self.tab2)
        self.outerPileDiam_label.setObjectName("outerPileDiam_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.outerPileDiam_label)
        self.outer_diameterLineEdit = QtWidgets.QLineEdit(self.tab2)
        # Set the validator of line edit so that it only accepts number double data types as input
        self.outer_diameterLineEdit.setValidator(QtGui.QDoubleValidator(
                bottom=0.0, # Set minimum value of input
                top = 1000,
                decimals=3, # Set the maximum number of decimal places in input
                notation=QtGui.QDoubleValidator.StandardNotation # Set valid notation of input
            ))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outer_diameterLineEdit.sizePolicy().hasHeightForWidth())
        self.outer_diameterLineEdit.setSizePolicy(sizePolicy)
        self.outer_diameterLineEdit.setObjectName("outer_diameterLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.outer_diameterLineEdit)
        self.minPileLen_label = QtWidgets.QLabel(self.tab2)
        self.minPileLen_label.setObjectName("minPileLen_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.minPileLen_label)
        self.minPileLen_LEdit = QtWidgets.QLineEdit(self.tab2)
        self.minPileLen_LEdit.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minPileLen_LEdit.sizePolicy().hasHeightForWidth())
        self.minPileLen_LEdit.setSizePolicy(sizePolicy)
        self.minPileLen_LEdit.setObjectName("minPileLen_LEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.minPileLen_LEdit)
        self.interval_label = QtWidgets.QLabel(self.tab2)
        self.interval_label.setObjectName("interval_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.interval_label)
        self.interval_LEdit = QtWidgets.QLineEdit(self.tab2)
        self.interval_LEdit.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,  
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interval_LEdit.sizePolicy().hasHeightForWidth())
        self.interval_LEdit.setSizePolicy(sizePolicy)
        self.interval_LEdit.setObjectName("interval_LEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.interval_LEdit)
        self.nointerval_label = QtWidgets.QLabel(self.tab2)
        self.nointerval_label.setObjectName("nointerval_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.nointerval_label)
        self.nointerval_LEdit = QtWidgets.QLineEdit(self.tab2)
        self.nointerval_LEdit.setValidator(QtGui.QIntValidator(
                bottom=0,
                top = 1000
            ))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nointerval_LEdit.sizePolicy().hasHeightForWidth())
        self.nointerval_LEdit.setSizePolicy(sizePolicy)
        self.nointerval_LEdit.setObjectName("nointerval_LEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.nointerval_LEdit)
        self.pileThickness_label = QtWidgets.QLabel(self.tab2)
        self.pileThickness_label.setObjectName("pileThickness_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.pileThickness_label)
        self.pileThickness_LEdit = QtWidgets.QLineEdit(self.tab2)
        self.pileThickness_LEdit.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=4,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pileThickness_LEdit.sizePolicy().hasHeightForWidth())
        self.pileThickness_LEdit.setSizePolicy(sizePolicy)
        self.pileThickness_LEdit.setObjectName("pileThickness_LEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pileThickness_LEdit)
        self.frictionAngle_label = QtWidgets.QLabel(self.tab2)
        self.frictionAngle_label.setObjectName("frictionAngle_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.frictionAngle_label)
        self.frictionAngle_LEdit = QtWidgets.QLineEdit(self.tab2)
        self.frictionAngle_LEdit.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frictionAngle_LEdit.sizePolicy().hasHeightForWidth())
        self.frictionAngle_LEdit.setSizePolicy(sizePolicy)
        self.frictionAngle_LEdit.setObjectName("frictionAngle_LEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.frictionAngle_LEdit)
        self.gwt_label = QtWidgets.QLabel(self.tab2)
        self.gwt_label.setObjectName("gwt_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.gwt_label)
        self.gwt_LEdit = QtWidgets.QLineEdit(self.tab2)
        self.gwt_LEdit.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gwt_LEdit.sizePolicy().hasHeightForWidth())
        self.gwt_LEdit.setSizePolicy(sizePolicy)
        self.gwt_LEdit.setObjectName("gwt_LEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.gwt_LEdit)
        self.unitWeight_label = QtWidgets.QLabel(self.tab2)
        self.unitWeight_label.setObjectName("unitWeight_label")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.unitWeight_label)
        self.unitWeight_LEdit = QtWidgets.QLineEdit(self.tab2)
        self.unitWeight_LEdit.setValidator(QtGui.QDoubleValidator(
                bottom=0.0,
                top = 1000,
                decimals=1,
                notation=QtGui.QDoubleValidator.StandardNotation
            ))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unitWeight_LEdit.sizePolicy().hasHeightForWidth())
        self.unitWeight_LEdit.setSizePolicy(sizePolicy)
        self.unitWeight_LEdit.setObjectName("unitWeight_LEdit")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.unitWeight_LEdit)
        self.updateParametersBtn = QtWidgets.QPushButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.updateParametersBtn.sizePolicy().hasHeightForWidth())
        self.updateParametersBtn.setSizePolicy(sizePolicy)
        self.updateParametersBtn.setObjectName("updateParametersBtn")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.updateParametersBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 6, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.calcBaseBtn = QtWidgets.QPushButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcBaseBtn.sizePolicy().hasHeightForWidth())
        self.calcBaseBtn.setSizePolicy(sizePolicy)
        self.calcBaseBtn.setObjectName("calcBaseBtn")
        self.gridLayout_5.addWidget(self.calcBaseBtn, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 1, 1, 1, 1)
        self.constantsTable = QtWidgets.QTableWidget(self.tab2)
        self.constantsTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.constantsTable.sizePolicy().hasHeightForWidth())
        self.constantsTable.setSizePolicy(sizePolicy)
        self.constantsTable.setMaximumSize(QtCore.QSize(1000, 1000))
        self.constantsTable.setObjectName("constantsTable")
        self.constantsTable.setColumnCount(7)
        self.constantsTable.setRowCount(1)
        self.constantsTable.setHorizontalHeaderLabels(['a', 'b', 'c', 'd', 'e', 'u', 'v'])
        self.header = self.constantsTable.horizontalHeader()
        self.vheader = self.constantsTable.verticalHeader()
        self.vheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.vheader.hide()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(1)
        self.gridLayout_5.addWidget(self.constantsTable, 0, 0, 3, 1)
        self.calcShaftBtn = QtWidgets.QPushButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcShaftBtn.sizePolicy().hasHeightForWidth())
        self.calcShaftBtn.setSizePolicy(sizePolicy)
        self.calcShaftBtn.setObjectName("calcShaftBtn")
        self.gridLayout_5.addWidget(self.calcShaftBtn, 0, 2, 1, 1)
        self.calcTotalBtn = QtWidgets.QPushButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcTotalBtn.sizePolicy().hasHeightForWidth())
        self.calcTotalBtn.setSizePolicy(sizePolicy)
        self.calcTotalBtn.setObjectName("calcTotalBtn")
        self.gridLayout_5.addWidget(self.calcTotalBtn, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 2, 1, 5)
        self.tabWidget.addTab(self.tab2, "")
        # Tab 3
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.graphOptions = QtWidgets.QComboBox(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphOptions.sizePolicy().hasHeightForWidth())
        self.graphOptions.setSizePolicy(sizePolicy)
        self.graphOptions.setObjectName("graphOptions")
        self.graphOptions.addItem("")
        self.graphOptions.addItem("")
        self.graphOptions.addItem("")
        self.graphOptions.addItem("")
        self.graphOptions.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.graphOptions)
        self.displayGraphBtn = QtWidgets.QPushButton(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayGraphBtn.sizePolicy().hasHeightForWidth())
        self.displayGraphBtn.setSizePolicy(sizePolicy)
        self.displayGraphBtn.setObjectName("displayGraphBtn")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.displayGraphBtn)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.cptCode_label = QtWidgets.QLabel(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cptCode_label.sizePolicy().hasHeightForWidth())
        self.cptCode_label.setSizePolicy(sizePolicy)
        self.cptCode_label.setObjectName("cptCode_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cptCode_label)
        self.cptCode_LEdit = QtWidgets.QLineEdit(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cptCode_LEdit.sizePolicy().hasHeightForWidth())
        self.cptCode_LEdit.setSizePolicy(sizePolicy)
        self.cptCode_LEdit.setObjectName("cptCode_LEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cptCode_LEdit)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem7)
        self.updateDatabaseBtn = QtWidgets.QPushButton(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateDatabaseBtn.sizePolicy().hasHeightForWidth())
        self.updateDatabaseBtn.setSizePolicy(sizePolicy)
        self.updateDatabaseBtn.setObjectName("updateDatabaseBtn")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.updateDatabaseBtn)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        self.horizontalLayout_2.addLayout(self.formLayout_2)

        self.graph = PlotWidget(self.tab3)
        self.graph.setBackground('w')
        self.graph.getPlotItem().hideAxis('bottom')
        self.graph.getPlotItem().showAxis('top')
        self.graph.getAxis('left').setPen('b')
        self.graph.getAxis('left').setTextPen('b')
        self.graph.getAxis('top').setPen('b')
        self.graph.getAxis('top').setTextPen('b')
        self.graph.getAxis('bottom').setPen('b')
        self.graph.getAxis('bottom').setTextPen('b')
        self.graph.getViewBox().invertY(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy)
        self.graph.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.graph.setObjectName("graph")


        self.horizontalLayout_2.addWidget(self.graph)
        self.tabWidget.addTab(self.tab3, "")
        self.centralLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.selectFileBtn.clicked.connect(self.openFile)
        self.selectMeasurementsBtn.clicked.connect(self.openWindow)
        self.updateParametersBtn.clicked.connect(self.updateParameters)
        self.calcShaftBtn.clicked.connect(self.updateShaftResistance)
        self.calcBaseBtn.clicked.connect(self.updateBaseResistance)
        self.calcTotalBtn.clicked.connect(self.updateTotalResistance)
        self.displayGraphBtn.clicked.connect(self.displayGraph)
        self.updateDatabaseBtn.clicked.connect(self.connectDatabase)
        

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    


    
    def connectDatabase(self):
        # If the user has not inputted anything, return an error message asking them to input something
        if self.cptCode_LEdit.text() == '':
            emptyCodemsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxCritical
            icon = emptyCodemsg.style().standardIcon(pixmapi)
            emptyCodemsg.setWindowIcon(icon)
            emptyCodemsg.setIcon(QMessageBox.Critical)
            emptyCodemsg.setText("You have not inputted a CPT code")
            emptyCodemsg.setWindowTitle("Error")
            return emptyCodemsg.exec_()

        # Create a name for the tables based off of the text inputted by the user
        measurement_tablename = "CPT"+self.cptCode_LEdit.text()+"_Measurement"
        parameters_tablename = "CPT"+self.cptCode_LEdit.text()+"_Parameter"
        calculations_tablename = "CPT"+self.cptCode_LEdit.text()+"_Calculation"

        # Create list of names contained in strings
        tablenames = [measurement_tablename, parameters_tablename, calculations_tablename]

        # If the user properly connects to the database, display success message
        self.database = Database()
        connection_stat = self.database.connect()
        if connection_stat == False:
            return
        if self.database.checkTable(tablenames) == False: # If the user does not want to replace the table, end function
            return

        # If the program is missing objects containing data for storing, return error message
        if (hasattr(self, "measurementObj") == False or hasattr(self, "parametersObj") == False or hasattr(self, "shaftResistanceObj") == False or 
        hasattr(self, "baseResistanceobj") == False or hasattr(self, "totalResistanceDataframe") == False):
            missingDbdmsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxCritical
            icon = missingDbdmsg.style().standardIcon(pixmapi)
            missingDbdmsg.setWindowIcon(icon)
            missingDbdmsg.setIcon(QMessageBox.Critical)
            missingDbdmsg.setText("You are missing data required for updating database")
            missingDbdmsg.setWindowTitle("Error")
            return missingDbdmsg.exec_()

        if(self.measurementObj.checkMeasurementValues() == True): # Check if all measurement values have been inputted
            # Create measurement table in database
            self.database.createMeasurementTable(measurement_tablename, self.measurementObj.getMeasurementValues())
            
        else: # Display error message if the user is missing data from measurement values
            missingDbdmsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxCritical
            icon = missingDbdmsg.style().standardIcon(pixmapi)
            missingDbdmsg.setWindowIcon(icon)
            missingDbdmsg.setIcon(QMessageBox.Critical)
            missingDbdmsg.setText("You are missing data required for updating database")
            missingDbdmsg.setWindowTitle("Error")
            return missingDbdmsg.exec_()

        # Create parameter and calculation table in data base using data
        self.database.createParameterTable(parameters_tablename, self.parametersObj.getParameters())
        self.database.createCalculationTable(calculations_tablename, {'shaft_resistance' : self.shaftResistanceObj.getResistance(),
        'base_resistance' : self.baseResistanceobj.getResistance(), 'total_resistance' : self.totalResistanceDataframe})
            
    
    def displayGraph(self):
        # Create a HTML style dictionary for the axis labels of the graph
        styles = {'font-family': 'Arial', 'color':'#12419E', 'font-size':'16px'}
        # Initialize variable containing combo box text for the type of graph user wants to display
        graph_option = self.graphOptions.currentText()
        # Check to see if data required to create plot is missing
        try:
            # Depending on the option selected in combo box, 
            # show corresponding graph using calculated and inputted data
            if graph_option == "Qt vs Depth":
                # Clear the graph in case previous graph was displayed
                self.graph.clear()
                # Set the x_range and y_range of graph as the dataframe values
                # from corresponding graph option converted into a list
                x_range = self.measurementObj.getQt()[0].values.tolist()
                y_range = self.measurementObj.getDepth()[0].values.tolist()
                # Set the axis labels to appropriate values
                self.graph.setLabel('left', 'Depth [m]', **styles)
                self.graph.setLabel('top', 'CPT Resistance [MPa]', **styles)
                # Initalize pen with custom RGB color for the drawing the line of the graph
                pen = pg.mkPen(color='#271CB8')
                # Plot the graph using data and pen
                self.graph.plot(x_range, y_range, pen=pen)

            elif graph_option == "Su vs Depth":
                    self.graph.clear()

                    x_range = self.measurementObj.getDepth()[0].values.tolist()
                    y_range = self.measurementObj.getSu()[0].values.tolist()

                    self.graph.setLabel('left', 'Depth [m]', **styles)
                    self.graph.setLabel('top', 'Su [kPa]', **styles)

                    pen = pg.mkPen(color="#EE741A")
                    self.graph.plot(x_range, y_range, pen=pen)

            elif graph_option == "Base Resistance vs Depth":
                self.graph.clear()

                x_range = self.baseResistanceDataframe[1].values.tolist()
                y_range = self.baseResistanceDataframe[0].values.tolist()

                self.graph.setLabel('left', 'Depth (m)', **styles)
                self.graph.setLabel('top', 'Base Resistance [kN]', **styles)

                pen = pg.mkPen(color='#1A24EE')
                self.graph.plot(x_range, y_range, pen=pen)

            elif graph_option == "Shaft Resistance vs Depth":
                self.graph.clear()

                x_range = self.shaftResistanceDataframe[1].values.tolist()
                y_range = self.shaftResistanceDataframe[0].values.tolist()

                self.graph.setLabel('left', 'Depth (m)', **styles)
                self.graph.setLabel('top', 'Shaft Resistance [kN]', **styles)

                pen = pg.mkPen(color="#1A24EE")
                self.graph.plot(x_range, y_range, pen=pen)
                
            elif graph_option == "Total Resistance vs Depth":
                self.graph.clear()

                x_range = self.totalResistanceDataframe[1].values.tolist()
                y_range = self.totalResistanceDataframe[0].values.tolist()

                self.graph.setLabel('left', 'Depth (m)', **styles)
                self.graph.setLabel('top', 'Total Resistance [kN]', **styles)

                pen = pg.mkPen(color='#1A24EE')
                self.graph.plot(x_range, y_range, pen=pen)
        # If data is missing, display error message
        except AttributeError:
            self.errorBox("You are missing measurements/resistances for graphing")

    
    def openFile(self):
        # Input file using QFileDialog to open users file directory to select a .XLS file
        self.file = QFileDialog.getOpenFileName(self, 'Open file', os.getenv('HOME'), 'XLS File (*.xls)')

        # Convert file into pandas Excel file and save the worksheet number inputted by user
        try:
            all_data = pd.ExcelFile(self.file[0])
            work_sheet = all_data.sheet_names[self.worksheet_num.value()-1]
        except FileNotFoundError: # If user closes file dialog, end function
            return
        except ValueError: # If the file is corrupted/invalid, return error message
            fileErrormsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxCritical
            icon = fileErrormsg.style().standardIcon(pixmapi)
            fileErrormsg.setWindowIcon(icon)
            fileErrormsg.setIcon(QMessageBox.Critical)
            fileErrormsg.setText("There was a problem with the file you submitted. Please try again.")
            fileErrormsg.setWindowTitle("Error")
            return fileErrormsg.exec_()
        except IndexError: # If worksheet is out of bounds, return error message
            fileErrormsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxCritical
            icon = fileErrormsg.style().standardIcon(pixmapi)
            fileErrormsg.setWindowIcon(icon)
            fileErrormsg.setIcon(QMessageBox.Critical)
            fileErrormsg.setText("That worksheet number is out of bounds. Please try again.")
            fileErrormsg.setWindowTitle("Error")
            return fileErrormsg.exec_()

        # Read excel file and save it to a dataframe in MainWindow
        self.df = pd.read_excel(all_data, work_sheet, index_col = 0)
        
        # Create table using dataframe and nested for loop to input values into table
        self.measurementFileTable.setRowCount(self.df.shape[0])
        self.measurementFileTable.setColumnCount(self.df.shape[1])

        for row in range(len(self.df.index)):
            for col in range(len(self.df.columns)):
                value = self.df.iloc[row, col]
                tableItem = QTableWidgetItem(str(value))
                self.measurementFileTable.setItem(row, col, tableItem)

        # Display the path of the file submitted on label
        self.filePathLabel.setText(f"File: {self.file[0]}")
    
    def openWindow(self):
        # Create second window as object of SelectDataWindow and 
        # execute the window using parameters from MainWindow
        try:
            dataWindow = SelectDataWindow(self.df)
            dataWindow.exec_()
            
        # If the window is missing information from MainWindow, display error message
        except AttributeError:
            self.errorBox("You must submit a data file")
        
    def updateTable(self, dataframe, tablename):
        # Replaces any NaN values if there are any in dataframe
        dataframe.fillna('',inplace = True)
        # Changes table structure to dataframe structure
        tablename.setRowCount(dataframe.shape[0])
        tablename.setColumnCount(1)
        # For every row and column in dataframe, fill an item in the 
        # table with the value at that index in the dataframe
        for row in range(len(dataframe.index)):
            for col in range(len(dataframe.columns)):
                value = dataframe.iloc[row, col]
                # If the value is a float or integer, reformat value 
                # to 2 decimal places and set item as string
                if isinstance(value, (float,int)):
                    value = '{0:0.2f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                tablename.setItem(row, col, tableItem)
    
    def updateMeasurements(self, dataframe, type):
        # Depending on type of data recieved from second window,
        # update corresponding measurement tables with data 
        if type == "Depth":
            self.updateTable(dataframe, self.depthTable)
        # Change headers to resize to fit table widget size 
            hheader = self.depthTable.horizontalHeader()
            hheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        elif type == "Qt":
            self.updateTable(dataframe, self.qtTable)

            hheader = self.qtTable.horizontalHeader()
            hheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        elif type == "Su":
            self.updateTable(dataframe, self.suTable)

            hheader = self.suTable.horizontalHeader()
            hheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        elif type == "Ic":
            self.updateTable(dataframe, self.icTable)

            hheader = self.icTable.horizontalHeader()
            hheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def updateObj(self, values, type): 
        # Measurement value updated defined using a string
        if type == "Depth":
            # Update object variables with dataframe from
            # second window
            self.measurementObj.updateDepth(values)
        elif type == "Qt":
            self.measurementObj.updateQt(values)
        elif type == "Su":
            self.measurementObj.updateSu(values)
        elif type == "Ic":
            self.measurementObj.updateIc(values)

    
    def updateParameters(self):
        # Assign the values inputted by user to variables which will be used as attributes for Parameters object
        try:
            calc_method = self.calcMethods.currentText()
            if self.compressionRBtn.isChecked() == True:
                const_type = "Compression"
            elif self.tensionRBtn.isChecked() == True:
                const_type = "Tension"
            else:
                raise ValueError # If no value is inputted raise and error to send message to user
            
            #Convert all values from string to float
            outer_pile_diameter = float(self.outer_diameterLineEdit.text())
            minimum_pile_length = float(self.minPileLen_LEdit.text())
            interval_length = float(self.interval_LEdit.text())
            no_intervals = int(self.nointerval_LEdit.text())
            pile_thickness = float(self.pileThickness_LEdit.text())
            friction_angle = float(self.frictionAngle_LEdit.text())
            ground_water_table = float(self.gwt_LEdit.text())
            unit_weight = float(self.unitWeight_LEdit.text())

            # Error checks for limits on parameters for valid calculations
            if ((minimum_pile_length + (interval_length*no_intervals) > self.measurementObj.getDepth().iloc[-1, 0]) or
            (round(minimum_pile_length + (interval_length*no_intervals) + (4 * outer_pile_diameter)) > self.measurementObj.getDepth().iloc[-1, 0]) or
            (pile_thickness >= outer_pile_diameter) or
            (friction_angle <= 0 or friction_angle > 360)):
                raise ValueError

        # If one of the inputs is not filled in, display an error message asking the user fill the missing boxes in
        except ValueError:
            missingInputmsg = QMessageBox()
            pixmapi = QStyle.SP_MessageBoxCritical
            icon = missingInputmsg.style().standardIcon(pixmapi)
            missingInputmsg.setWindowIcon(icon)
            missingInputmsg.setIcon(QtWidgets.QMessageBox.Critical)
            missingInputmsg.setText("There was an issue with the pararmeters inputted. Please try again.")
            missingInputmsg.setWindowTitle("Error")
            return missingInputmsg.exec_()

        except AttributeError:
            self.errorBox("You have not inputted a measurement file. Please try again.")
            
        # Create list of all inputs
        inputs = [calc_method, const_type, outer_pile_diameter, minimum_pile_length, interval_length, 
        no_intervals, pile_thickness, friction_angle, ground_water_table, unit_weight]
        # Create instance of Parameters Class and use the values inputted by user as attributes for object
        self.parametersObj = Parameters(*inputs)
        # Create a list of constants using method from object and store object in dataframe within MainWindow
        self.parametersObj.setConst()
        self.constList = pd.DataFrame(list(self.parametersObj.getConstants().items()))
        
        # Display dataframe of constants on a table with custom labels
        self.constList.fillna('',inplace = True)

        for row in range(len(self.constList.index)):
            value = self.constList.iloc[row, 1]
            if isinstance(value, (float,int)):
                value = '{0:0.3f}'.format(value)
            tableItem = QTableWidgetItem(str(value))
            tableItem.setTextAlignment(Qt.AlignCenter)
            self.constantsTable.setItem(0, row, tableItem)
    
    def updateBaseResistance(self):
        # Create BaseResistance object with Parameters object and MeasurementData object as parameters
        try:
            self.baseResistanceobj = BaseResistance(self.parametersObj, self.measurementObj)
        # If instantiation is missing objects, return an error message saying that the user is missing data
        except AttributeError:
            self.errorBox("You are missing required data to calculate base resistance.")
            return
        
        # Calculate the base resistance and retrieve dataframe, which will also be shown on table widget
        self.baseResistanceobj.calcBaseRes()
        self.baseResistanceDataframe = self.baseResistanceobj.getResistance()
        self.baseResistanceDataframe.fillna('',inplace = True)
        self.resistanceTable.setRowCount(self.baseResistanceDataframe.shape[0])

        # Place values from dataframe into table widget based off of position in dataframe
        for row in range(len(self.baseResistanceDataframe.index)):
                for col in range(len(self.baseResistanceDataframe.columns)):
                    baseValue = self.baseResistanceDataframe.iloc[row, col]
                    if isinstance(baseValue,(float,int)):
                        baseValue = '{0:0.2f}'.format(baseValue)
                    baseItem = QTableWidgetItem(baseValue)
                    if col == 1:
                        self.resistanceTable.setItem(row, 2, baseItem)
                    else:
                        self.resistanceTable.setItem(row, col, baseItem)
        
    def updateShaftResistance(self):
        # Create ShaftResistance object with Parameters object and MeasurementData object as parameters
        try:
            self.shaftResistanceObj = ShaftResistance(self.parametersObj, self.measurementObj)
        # If instantiation is missing objects, return an error message saying that the user is missing data
        except AttributeError:
            self.errorBox("You are missing required data to calculate shaft resistance.")
            return

        # Calculate the shaft resistance and retrieve dataframe, which will then be shown on the table widget
        self.shaftResistanceObj.calcShaftRes()
        self.shaftResistanceDataframe = self.shaftResistanceObj.getResistance()
        self.shaftResistanceDataframe.fillna('',inplace = True)
        self.resistanceTable.setRowCount(self.shaftResistanceDataframe.shape[0])

        # Place values from dataframe into table widget based off of position in dataframe
        for row in range(len(self.shaftResistanceDataframe.index)):
                for col in range(len(self.shaftResistanceDataframe.columns)):
                    shaftValue = self.shaftResistanceDataframe.iloc[row, col]
                    if isinstance(shaftValue,(float,int)): # Round resistance value to 2 decimal places
                        shaftValue = '{0:0.2f}'.format(shaftValue)
                    shaftItem = QTableWidgetItem(shaftValue)
                    self.resistanceTable.setItem(row, col, shaftItem)

    def updateTotalResistance(self):
        # Create a list that will store the length and total resistance as a list
        totalResistanceList = []
        # For every row in the table widget, take the length and the sum of the base and shaft resistance values
        for row in range(self.resistanceTable.rowCount()):
            try:
                shaft = float(self.resistanceTable.item(row, 1).text())
                base = float(self.resistanceTable.item(row, 2).text())
                length = float(self.resistanceTable.item(row, 0).text())
            except AttributeError: # If items cannot be converted into a float and added, display error message
                self.errorBox("You are missing required data to calculate total resistance")
            
            totalRes = shaft+base
            # Add to a list and append that list to the totalResistance List
            total = [length, totalRes]
            totalResistanceList.append(total)
            if isinstance(totalRes,(float,int)): # Round resistance value to 2 decimal places
                    totalRes = '{0:0.2f}'.format(totalRes)
            totalItem = QTableWidgetItem(totalRes)
            # Add the total resistance value at that length to the resistance table in corresponding column and row
            self.resistanceTable.setItem(row, 3, totalItem)
        # Convert the list of list of lengths and total resistances into a dataframe for later use
        self.totalResistanceDataframe = pd.DataFrame(totalResistanceList)
    
    def errorBox(self, errorMessage):
        msgBox = QMessageBox()
        pixmapi = QStyle.SP_MessageBoxCritical
        icon = msgBox.style().standardIcon(pixmapi)
        msgBox.setWindowIcon(icon)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(errorMessage)
        msgBox.setWindowTitle("Error")
        msgBox.exec_()
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPT Geo Pile"))
        self.depthLabel.setText(_translate("MainWindow", "Depth [m]"))
        self.qtLabel.setText(_translate("MainWindow", "Qt [MPa]"))
        self.icLabel.setText(_translate("MainWindow", "Ic"))
        self.suLabel.setText(_translate("MainWindow", "Su [kPa]"))
        self.selectMeasurementsBtn.setText(_translate("MainWindow", "Select Measurements"))
        self.worksheetNumber.setText(_translate("MainWindow", "Worksheet Number:"))
        self.selectFileBtn.setText(_translate("MainWindow", "Select File"))
        self.filePathLabel.setText(_translate("MainWindow", "File Path:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Measurements"))
        self.calcMethods.setItemText(0, _translate("MainWindow", "ICP-05"))
        self.calcMethods.setItemText(1, _translate("MainWindow", "UWA-05"))
        self.calcMethods.setItemText(2, _translate("MainWindow", "FUGRO-05"))
        self.calcMethods.setItemText(3, _translate("MainWindow", "NGI-05"))
        self.compressionRBtn.setText(_translate("MainWindow", "Compression"))
        self.tensionRBtn.setText(_translate("MainWindow", "Tension"))
        self.outerPileDiam_label.setText(_translate("MainWindow", "Outer Pile Diameter:"))
        self.minPileLen_label.setText(_translate("MainWindow", "Minimum Pile Length [m]:"))
        self.interval_label.setText(_translate("MainWindow", "Interval Length [m]:"))
        self.nointerval_label.setText(_translate("MainWindow", "Number of Intervals: "))
        self.pileThickness_label.setText(_translate("MainWindow", "Pile Thickness [m]: "))
        self.frictionAngle_label.setText(_translate("MainWindow", "δcv Value (degrees): "))
        self.gwt_label.setText(_translate("MainWindow", "GWT [m]:"))
        self.unitWeight_label.setText(_translate("MainWindow", "Unit Weight: "))
        self.updateParametersBtn.setText(_translate("MainWindow", "Update Parameters"))
        self.calcShaftBtn.setText(_translate("MainWindow", "Calculate Shaft Resistance"))
        self.calcTotalBtn.setText(_translate("MainWindow", "Calculate Total Resistance"))
        self.calcBaseBtn.setText(_translate("MainWindow", "Calculate Base Resistance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Calculations"))
        self.cptCode_label.setText(_translate("MainWindow", "Enter CPT Code:"))
        self.updateDatabaseBtn.setText(_translate("MainWindow", "Update Database"))
        self.displayGraphBtn.setText(_translate("MainWindow", "Display Graph"))
        self.graphOptions.setItemText(0, _translate("MainWindow", "Qt vs Depth"))
        self.graphOptions.setItemText(1, _translate("MainWindow", "Su vs Depth"))
        self.graphOptions.setItemText(3, _translate("MainWindow", "Shaft Resistance vs Depth"))
        self.graphOptions.setItemText(2, _translate("MainWindow", "Base Resistance vs Depth"))
        self.graphOptions.setItemText(4, _translate("MainWindow", "Total Resistance vs Depth"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Data"))