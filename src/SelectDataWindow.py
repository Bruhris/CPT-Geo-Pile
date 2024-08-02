from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtGui import QIntValidator
import pandas as pd


class Ui_Dialog(object):
    def setupUi(self, Dialog, data):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1044, 783)
        self.data = data
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 1021, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.data.shape[0])
        self.tableWidget.setColumnCount(self.data.shape[1])
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 630, 172, 73))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.intergerOnly = QIntValidator()
        self.intergerOnly.setRange(0, 999)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(self.intergerOnly)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 729, 1021, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.submitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_3.addWidget(self.submitButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 191, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.measurementComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.measurementComboBox.setObjectName("measurementComboBox")
        self.measurementComboBox.addItem("")
        self.measurementComboBox.addItem("")
        self.measurementComboBox.addItem("")
        self.measurementComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.measurementComboBox)

        self.submitButton.clicked.connect(self.submitData)
        self.cancelButton.clicked.connect(self.closeWindow)

        for row in range(len(self.data.index)):
            for col in range(len(self.data.columns)):
                value = self.data.iloc[row, col]
                if isinstance(value, (float,int)):
                    value = '{0:0.2f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, tableItem)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def submitData(self):
        self.measurement_name = self.measurementComboBox.currentText()
        col_num = int(self.lineEdit.text())
        
        try:
            self.fileValues = self.data.iloc[1:, col_num-1].tolist()
            self.fileValues = pd.DataFrame(self.fileValues)
        # Column number is invalid
        except IndexError as e: 
            print(e)

        self.accept()
    
    def closeWindow(self):
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Column Number:"))
        self.submitButton.setText(_translate("Dialog", "Submit"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Measurement Type:"))
        self.measurementComboBox.setItemText(0, _translate("Dialog", "Depth"))
        self.measurementComboBox.setItemText(1, _translate("Dialog", "Qt"))
        self.measurementComboBox.setItemText(2, _translate("Dialog", "Su"))
        self.measurementComboBox.setItemText(3, _translate("Dialog", "Ic"))


class SelectWindowDialog(QDialog, Ui_Dialog):
    def __init__(self, data, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self, data)
