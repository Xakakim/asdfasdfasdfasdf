from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(239, 172)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Api = QtWidgets.QLineEdit(self.centralwidget)
        self.Api.setGeometry(QtCore.QRect(20, 30, 120, 20))
        self.Api.setObjectName("Api")
        self.Phone = QtWidgets.QLineEdit(self.centralwidget)
        self.Phone.setGeometry(QtCore.QRect(20, 80, 120, 20))
        self.Phone.setObjectName("Phone")
        self.Hash = QtWidgets.QLineEdit(self.centralwidget)
        self.Hash.setGeometry(QtCore.QRect(20, 130, 196, 20))
        self.Hash.setObjectName("Hash")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(147, 27, 70, 100))
        self.Login.setObjectName("Login")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 15, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 65, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 115, 56, 12))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Login.clicked.connect(MainWindow.loginChk) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Api"))
        self.label_2.setText(_translate("MainWindow", "(+82)Phone"))
        self.label_3.setText(_translate("MainWindow", "Hash"))
