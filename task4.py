# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 340)
        MainWindow.setStyleSheet("background-color: \"#ffe7ef\"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 40, 281, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.product_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.product_button.setStyleSheet("background-color: #ffffff")
        self.product_button.setObjectName("product_button")
        self.horizontalLayout_2.addWidget(self.product_button)
        self.product_field = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.product_field.setStyleSheet("background-color: #ffffff")
        self.product_field.setObjectName("product_field")
        self.horizontalLayout_2.addWidget(self.product_field)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.increase_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.increase_button.setStyleSheet("background-color: #ffffff")
        self.increase_button.setObjectName("increase_button")
        self.horizontalLayout.addWidget(self.increase_button)
        self.change_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.change_button.setStyleSheet("background-color: #ffffff")
        self.change_button.setObjectName("change_button")
        self.horizontalLayout.addWidget(self.change_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.price_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.price_button.setStyleSheet("background-color: #ffffff")
        self.price_button.setObjectName("price_button")
        self.horizontalLayout_3.addWidget(self.price_button)
        self.price_field = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.price_field.setStyleSheet("background-color: #ffffff")
        self.price_field.setObjectName("price_field")
        self.horizontalLayout_3.addWidget(self.price_field)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.product_button.setText(_translate("MainWindow", "Product"))
        self.increase_button.setText(_translate("MainWindow", "Increase"))
        self.change_button.setText(_translate("MainWindow", "Change"))
        self.price_button.setText(_translate("MainWindow", "Price"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
