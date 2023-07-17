import Validation
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QMessageBox
from PySide2 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def create_font(point_size, is_bold, is_italic, font_weight):
    font = QtGui.QFont()
    font.setFamily("MS Reference Sans Serif")
    font.setPointSize(point_size)
    font.setBold(is_bold)
    font.setItalic(is_italic)
    font.setWeight(font_weight)
    return font


class Ui_functionplotter(object):

    def setupUi(self, functionplotter):
        functionplotter.setObjectName("functionplotter")
        self.centralwidget = QtWidgets.QWidget(functionplotter)
        self.centralwidget.setObjectName("centralwidget")

        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(create_font(19, True, True, 75))
        self.label.setObjectName("label")
        self.layout.addWidget(self.label, alignment=QtCore.Qt.AlignHCenter)

        # Function input
        hbox_function = QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(create_font(11, False, False, 50))
        self.label_2.setObjectName("label_2")
        hbox_function.addWidget(self.label_2)
        self.function = QtWidgets.QLineEdit(self.centralwidget)
        self.function.setFont(create_font(11, False, False, 0))
        self.function.setObjectName("function")
        self.function.setFixedWidth(500)
        hbox_function.addWidget(self.function)
        hbox_function.addStretch(1)
        self.layout.addLayout(hbox_function)

        hbox_minX = QtWidgets.QHBoxLayout()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFont(create_font(11, False, False, 50))
        self.label_3.setObjectName("label_3")
        hbox_minX.addWidget(self.label_3)
        self.minX = QtWidgets.QLineEdit(self.centralwidget)
        self.minX.setFont(create_font(11, False, False, 0))
        self.minX.setObjectName("minX")
        self.minX.setFixedWidth(100)
        hbox_minX.addWidget(self.minX)
        hbox_minX.addStretch(1)
        self.layout.addLayout(hbox_minX)

        # MaxX input
        hbox_maxX = QtWidgets.QHBoxLayout()
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFont(create_font(11, False, False, 50))
        self.label_4.setObjectName("label_4")
        hbox_maxX.addWidget(self.label_4)
        self.maxX = QtWidgets.QLineEdit(self.centralwidget)
        self.maxX.setFont(create_font(11, False, False, 0))
        self.maxX.setObjectName("maxX")
        self.maxX.setFixedWidth(100)
        hbox_maxX.addWidget(self.maxX)
        hbox_maxX.addStretch(1)
        self.layout.addLayout(hbox_maxX)

        # Push button to plot
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setFont(create_font(10, False, False, 0))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.draw)
        self.layout.addWidget(self.pushButton, alignment=QtCore.Qt.AlignHCenter)

        # Label 5 and Label 6
        hbox_labels = QtWidgets.QHBoxLayout()
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setFont(create_font(11, False, False, 0))
        self.label_5.setObjectName("label_5")
        hbox_labels.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setFont(create_font(11, False, False, 0))
        self.label_7.setObjectName("label_7")
        self.layout.addWidget(self.label_7)
        hbox_labels.addWidget(self.label_7)
        self.layout.addLayout(hbox_labels)

        functionplotter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(functionplotter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 26))
        self.menubar.setObjectName("menubar")
        functionplotter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(functionplotter)
        self.statusbar.setObjectName("statusbar")
        functionplotter.setStatusBar(self.statusbar)
        self.retranslateUi(functionplotter)
        QtCore.QMetaObject.connectSlotsByName(functionplotter)
        functionplotter.setObjectName("functionplotter")
        self.centralwidget = QtWidgets.QWidget(functionplotter)
        self.centralwidget.setObjectName("centralwidget")

        self.canvas = FigureCanvas(plt.figure())
        self.layout.addWidget(self.canvas)

        plt.style.use("seaborn-dark")
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.grid()

    def retranslateUi(self, functionplotter):
        _translate = QtCore.QCoreApplication.translate
        functionplotter.setWindowTitle(_translate("functionplotter", "MainWindow"))
        self.label.setText(_translate("functionplotter", "Function Plotter "))
        self.label_2.setText(_translate("functionplotter", "Enter a Function :"))
        self.label_3.setText(_translate("functionplotter", "Enter The Minimim Value of  x :"))
        self.label_4.setText(_translate("functionplotter", "Enter The Maximim Value of  x :"))
        self.pushButton.setText(_translate("functionplotter", "plot"))
        self.label_5.setText(_translate("functionplotter", "Enter a Function Like: 5*x^3+2*x"))
        self.label_7.setText(_translate("functionplotter", "The Supported Operators: + - / * ^"))

    def PopUpMessage(self, error_message):  # function to print the error
        msg = QMessageBox()
        msg.setWindowTitle("error")
        msg.setText(error_message)
        x = msg.exec_()

    def draw(self):  # the function that draw the function
        function = self.function.text()
        minX = self.minX.text()
        maxX = self.maxX.text()
        answer = Validation.validInputs(function, minX, maxX)  # check if the input is valid
        if answer != "true":  # if the input not valid we should print the error
            self.PopUpMessage(answer)
            return
        function = self.function.text()
        function=Validation.replace_implicit_multiplication(function)

        # if we reached here so the input is valid
        minX = int(self.minX.text())
        maxX = int(self.maxX.text())
        listX = []
        listY = []
        for i in range(minX, maxX+1):
            tmp = function.replace("x", '(' + str(i) + ')')  # if we have x^2 and x is negative
            tmp = tmp.replace("^", "**")
            tmp = tmp.replace(' ', '')
            x = eval(tmp)
            listX.append(i)
            listY.append(x)
        # print(listX)
        # print(listY)
        plt.clf()
        plt.style.use("seaborn-dark")
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.grid()
        plt.plot(listX, listY, color="black")
        self.canvas.draw()