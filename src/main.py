# CPT Geo Pile Program (main.py)

# Import libraries from PyQt5 to create widgets and windows
from PyQt5 import QtWidgets
from ui.MainWindow import Ui_MainWindow 


if __name__ == "__main__": # Execute code only if file was run directly
    import sys
    # Must create an applications object to run PyQt5 applications with sys arguments
    app = QtWidgets.QApplication(sys.argv)
    # Create object of QMainWindow to structure GUI
    MainWindow = QtWidgets.QMainWindow()
    # Create GUI
    ui = Ui_MainWindow()
    # Type of widget the GUI is created in
    ui.setupUi(MainWindow)
    # Runs application
    MainWindow.show()
    # Terminates app when closed
    sys.exit(app.exec_())
