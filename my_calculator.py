# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(590, 308)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(590, 308))
        Form.setMaximumSize(QtCore.QSize(627, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("background: rgb(63, 63, 63)")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(560, 95))
        self.lcdNumber.setMaximumSize(QtCore.QSize(560, 95))
        self.lcdNumber.setStyleSheet("color: rgb(85, 255, 0); background-color: rgb(16, 16, 16);")
        self.lcdNumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhPreferNumbers)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(12)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 0);\n"
                                    "")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_n6 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n6.setFont(font)
        self.pushButton_n6.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n6.setObjectName("pushButton_n6")
        self.gridLayout.addWidget(self.pushButton_n6, 1, 0, 1, 1)
        self.pushButton_n9 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n9.setFont(font)
        self.pushButton_n9.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n9.setObjectName("pushButton_n9")
        self.gridLayout.addWidget(self.pushButton_n9, 0, 0, 1, 1)
        self.pushButton_n3 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n3.setFont(font)
        self.pushButton_n3.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);;")
        self.pushButton_n3.setObjectName("pushButton_n3")
        self.gridLayout.addWidget(self.pushButton_n3, 2, 0, 1, 1)
        self.pushButton_n8 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n8.setFont(font)
        self.pushButton_n8.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n8.setObjectName("pushButton_n8")
        self.gridLayout.addWidget(self.pushButton_n8, 0, 1, 1, 1)
        self.pushButton_n2 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n2.setFont(font)
        self.pushButton_n2.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n2.setObjectName("pushButton_n2")
        self.gridLayout.addWidget(self.pushButton_n2, 2, 1, 1, 1)
        self.pushButton_n5 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n5.setFont(font)
        self.pushButton_n5.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n5.setObjectName("pushButton_n5")
        self.gridLayout.addWidget(self.pushButton_n5, 1, 1, 1, 1)
        self.pushButton_n7 = QtWidgets.QPushButton(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_n7.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n7.setFont(font)
        self.pushButton_n7.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n7.setObjectName("pushButton_n7")
        self.gridLayout.addWidget(self.pushButton_n7, 0, 2, 1, 1)
        self.pushButton_n4 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n4.setFont(font)
        self.pushButton_n4.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n4.setObjectName("pushButton_n4")
        self.gridLayout.addWidget(self.pushButton_n4, 1, 2, 1, 1)
        self.pushButton_n1 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n1.setFont(font)
        self.pushButton_n1.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n1.setObjectName("pushButton_n1")
        self.gridLayout.addWidget(self.pushButton_n1, 2, 2, 1, 1)
        self.pushButton_n0 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n0.setFont(font)
        self.pushButton_n0.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_n0.setObjectName("pushButton_n0")
        self.gridLayout.addWidget(self.pushButton_n0, 3, 0, 1, 2)
        self.pushButton_comma = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_comma.setFont(font)
        self.pushButton_comma.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                            "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_comma.setObjectName("pushButton_comma")
        self.gridLayout.addWidget(self.pushButton_comma, 3, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_2.addWidget(self.pushButton_20, 0, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 3, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 4, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 1, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 3, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 4, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 0, 1, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                         "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_2.addWidget(self.pushButton_21, 1, 2, 1, 1)
        self.pushButton_divide = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                             " border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout_2.addWidget(self.pushButton_divide, 0, 3, 1, 1)
        self.pushButton_subtract = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_subtract.setFont(font)
        self.pushButton_subtract.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                               "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_subtract.setObjectName("pushButton_subtract")
        self.gridLayout_2.addWidget(self.pushButton_subtract, 4, 3, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                          "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);;")
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_2.addWidget(self.pushButton_add, 3, 3, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setStyleSheet(" border-style: outset;; border-width: 1px; border-radius: 4px;\n"
                                               "border-color: rgb(0, 255, 0); background-color: rgb(16, 16, 16);")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout_2.addWidget(self.pushButton_multiply, 1, 3, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("background-color: rgb(255, 0, 0); border-style: outset;; border-width: "
                                            "1px; border-radius: 4px; border-color: rgb(0, 255, 0);")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout_2.addWidget(self.pushButton_clear, 0, 0, 2, 1)
        self.pushButton_result = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_result.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_result.setFont(font)
        self.pushButton_result.setStyleSheet("background-color: rgb(255, 255, 127);color: rgb(0, 0, 0); border-style:"
                                             "outset;; border-width: 1px; border-radius: 4px;"
                                             "border-color: rgb(0, 255, 0);")
        self.pushButton_result.setObjectName("pushButton_result")
        self.gridLayout_2.addWidget(self.pushButton_result, 3, 2, 2, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Ввод"))
        self.pushButton_n6.setText(_translate("Form", "6"))
        self.pushButton_n9.setText(_translate("Form", "9"))
        self.pushButton_n3.setText(_translate("Form", "3"))
        self.pushButton_n8.setText(_translate("Form", "8"))
        self.pushButton_n2.setText(_translate("Form", "2"))
        self.pushButton_n5.setText(_translate("Form", "5"))
        self.pushButton_n7.setText(_translate("Form", "7"))
        self.pushButton_n4.setText(_translate("Form", "4"))
        self.pushButton_n1.setText(_translate("Form", "1"))
        self.pushButton_n0.setText(_translate("Form", "0"))
        self.pushButton_comma.setText(_translate("Form", ","))
        self.groupBox_2.setTitle(_translate("Form", "Операции"))
        self.pushButton_20.setText(_translate("Form", "M-"))
        self.pushButton_14.setText(_translate("Form", "sgrt"))
        self.pushButton_15.setText(_translate("Form", "PB"))
        self.pushButton_17.setText(_translate("Form", "M+"))
        self.pushButton_18.setText(_translate("Form", "degree"))
        self.pushButton_19.setText(_translate("Form", "PB"))
        self.pushButton_16.setText(_translate("Form", "M"))
        self.pushButton_21.setText(_translate("Form", "%"))
        self.pushButton_divide.setText(_translate("Form", "/"))
        self.pushButton_subtract.setText(_translate("Form", "-"))
        self.pushButton_add.setText(_translate("Form", "+"))
        self.pushButton_multiply.setText(_translate("Form", "*"))
        self.pushButton_clear.setText(_translate("Form", "AC"))
        self.pushButton_result.setText(_translate("Form", "="))
