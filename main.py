
import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
import GUI

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    functionplotter = QtWidgets.QMainWindow()
    ui = GUI.Ui_functionplotter()
    ui.setupUi(functionplotter)
    functionplotter.resize(900, 800)
    functionplotter.show()
    sys.exit(app.exec_())
