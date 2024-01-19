# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6disc_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import uiResourse_background_demo


class Ui_Form_6(object):
    def setupUi(self, Form_6):
        Form_6.setObjectName("Form_6")
        Form_6.resize(1169, 848)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_6.sizePolicy().hasHeightForWidth())
        Form_6.setSizePolicy(sizePolicy)
        Form_6.setMinimumSize(QtCore.QSize(1169, 848))
        Form_6.setMaximumSize(QtCore.QSize(1169, 848))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_6.setWindowIcon(icon)
        self.background_pic = QtWidgets.QLabel(Form_6)
        self.background_pic.setGeometry(QtCore.QRect(-30, -20, 1221, 881))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_pic.sizePolicy().hasHeightForWidth())
        self.background_pic.setSizePolicy(sizePolicy)
        self.background_pic.setMinimumSize(QtCore.QSize(1221, 881))
        self.background_pic.setMaximumSize(QtCore.QSize(1221, 881))
        self.background_pic.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.background_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.background_pic.setAutoFillBackground(False)
        self.background_pic.setStyleSheet("image: url(:/newPrefix/background_50.png);")
        self.background_pic.setText("")
        self.background_pic.setObjectName("background_pic")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form_6)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(850, 20, 131, 42))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_timer = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_timer.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_timer.setObjectName("horizontalLayout_timer")
        self.timer_icon = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_icon.sizePolicy().hasHeightForWidth())
        self.timer_icon.setSizePolicy(sizePolicy)
        self.timer_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.timer_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.timer_icon.setStyleSheet("border-image: url(:/newPrefix/timer.png);")
        self.timer_icon.setText("")
        self.timer_icon.setObjectName("timer_icon")
        self.horizontalLayout_timer.addWidget(self.timer_icon)
        self.timer_num = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_num.sizePolicy().hasHeightForWidth())
        self.timer_num.setSizePolicy(sizePolicy)
        self.timer_num.setMinimumSize(QtCore.QSize(40, 40))
        self.timer_num.setMaximumSize(QtCore.QSize(40, 40))
        self.timer_num.setStyleSheet("font: 15pt \"SetoFont\";")
        self.timer_num.setObjectName("timer_num")
        self.horizontalLayout_timer.addWidget(self.timer_num)
        self.pushButton_help = QtWidgets.QPushButton(Form_6)
        self.pushButton_help.setGeometry(QtCore.QRect(1020, 20, 100, 45))
        self.pushButton_help.setMinimumSize(QtCore.QSize(100, 45))
        self.pushButton_help.setMaximumSize(QtCore.QSize(100, 45))
        self.pushButton_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_help.setStyleSheet("font: 10pt \"SetoFont\";\n"
"border-image: url(:/newPrefix/help.png);")
        self.pushButton_help.setText("")
        self.pushButton_help.setObjectName("pushButton_help")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(Form_6)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(30, 90, 1111, 132))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_p12 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_p12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_p12.setObjectName("gridLayout_p12")
        self.pushButton_p12_2 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p12_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p12_2.setSizePolicy(sizePolicy)
        self.pushButton_p12_2.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_2.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p12_2.setText("")
        self.pushButton_p12_2.setObjectName("pushButton_p12_2")
        self.gridLayout_p12.addWidget(self.pushButton_p12_2, 0, 2, 1, 1)
        self.pushButton_p12_1 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p12_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p12_1.setSizePolicy(sizePolicy)
        self.pushButton_p12_1.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_1.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p12_1.setStyleSheet("border-image: url(:/newPrefix/b1r.png);")
        self.pushButton_p12_1.setText("")
        self.pushButton_p12_1.setObjectName("pushButton_p12_1")
        self.gridLayout_p12.addWidget(self.pushButton_p12_1, 0, 1, 1, 1)
        self.label_p12 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_p12.sizePolicy().hasHeightForWidth())
        self.label_p12.setSizePolicy(sizePolicy)
        self.label_p12.setMinimumSize(QtCore.QSize(40, 60))
        self.label_p12.setMaximumSize(QtCore.QSize(40, 60))
        self.label_p12.setStyleSheet("font: 15pt \"SetoFont\";")
        self.label_p12.setObjectName("label_p12")
        self.gridLayout_p12.addWidget(self.label_p12, 0, 0, 1, 1)
        self.pushButton_p12_5 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p12_5.sizePolicy().hasHeightForWidth())
        self.pushButton_p12_5.setSizePolicy(sizePolicy)
        self.pushButton_p12_5.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_5.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p12_5.setText("")
        self.pushButton_p12_5.setObjectName("pushButton_p12_5")
        self.gridLayout_p12.addWidget(self.pushButton_p12_5, 0, 5, 1, 1)
        self.pushButton_p12_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p12_4.sizePolicy().hasHeightForWidth())
        self.pushButton_p12_4.setSizePolicy(sizePolicy)
        self.pushButton_p12_4.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_4.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p12_4.setText("")
        self.pushButton_p12_4.setObjectName("pushButton_p12_4")
        self.gridLayout_p12.addWidget(self.pushButton_p12_4, 0, 4, 1, 1)
        self.pushButton_p12_3 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p12_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p12_3.setSizePolicy(sizePolicy)
        self.pushButton_p12_3.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_3.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p12_3.setText("")
        self.pushButton_p12_3.setObjectName("pushButton_p12_3")
        self.gridLayout_p12.addWidget(self.pushButton_p12_3, 0, 3, 1, 1)
        self.pushButton_p12_6 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p12_6.sizePolicy().hasHeightForWidth())
        self.pushButton_p12_6.setSizePolicy(sizePolicy)
        self.pushButton_p12_6.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_6.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p12_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p12_6.setText("")
        self.pushButton_p12_6.setObjectName("pushButton_p12_6")
        self.gridLayout_p12.addWidget(self.pushButton_p12_6, 0, 6, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(Form_6)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(30, 230, 1111, 132))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_p11 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_p11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_p11.setObjectName("gridLayout_p11")
        self.pushButton_p11_2 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p11_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p11_2.setSizePolicy(sizePolicy)
        self.pushButton_p11_2.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_2.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p11_2.setText("")
        self.pushButton_p11_2.setObjectName("pushButton_p11_2")
        self.gridLayout_p11.addWidget(self.pushButton_p11_2, 0, 2, 1, 1)
        self.pushButton_p11_1 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p11_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p11_1.setSizePolicy(sizePolicy)
        self.pushButton_p11_1.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_1.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p11_1.setText("")
        self.pushButton_p11_1.setObjectName("pushButton_p11_1")
        self.gridLayout_p11.addWidget(self.pushButton_p11_1, 0, 1, 1, 1)
        self.label_p11 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_p11.sizePolicy().hasHeightForWidth())
        self.label_p11.setSizePolicy(sizePolicy)
        self.label_p11.setMinimumSize(QtCore.QSize(40, 60))
        self.label_p11.setMaximumSize(QtCore.QSize(40, 60))
        self.label_p11.setStyleSheet("font: 15pt \"SetoFont\";")
        self.label_p11.setObjectName("label_p11")
        self.gridLayout_p11.addWidget(self.label_p11, 0, 0, 1, 1)
        self.pushButton_p11_5 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p11_5.sizePolicy().hasHeightForWidth())
        self.pushButton_p11_5.setSizePolicy(sizePolicy)
        self.pushButton_p11_5.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_5.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p11_5.setText("")
        self.pushButton_p11_5.setObjectName("pushButton_p11_5")
        self.gridLayout_p11.addWidget(self.pushButton_p11_5, 0, 5, 1, 1)
        self.pushButton_p11_4 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p11_4.sizePolicy().hasHeightForWidth())
        self.pushButton_p11_4.setSizePolicy(sizePolicy)
        self.pushButton_p11_4.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_4.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p11_4.setText("")
        self.pushButton_p11_4.setObjectName("pushButton_p11_4")
        self.gridLayout_p11.addWidget(self.pushButton_p11_4, 0, 4, 1, 1)
        self.pushButton_p11_3 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p11_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p11_3.setSizePolicy(sizePolicy)
        self.pushButton_p11_3.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_3.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p11_3.setText("")
        self.pushButton_p11_3.setObjectName("pushButton_p11_3")
        self.gridLayout_p11.addWidget(self.pushButton_p11_3, 0, 3, 1, 1)
        self.pushButton_p11_6 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p11_6.sizePolicy().hasHeightForWidth())
        self.pushButton_p11_6.setSizePolicy(sizePolicy)
        self.pushButton_p11_6.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_6.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p11_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p11_6.setText("")
        self.pushButton_p11_6.setObjectName("pushButton_p11_6")
        self.gridLayout_p11.addWidget(self.pushButton_p11_6, 0, 6, 1, 1)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Form_6)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(30, 370, 234, 42))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_score_p1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_score_p1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_score_p1.setObjectName("horizontalLayout_score_p1")
        self.label_p1 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_p1.sizePolicy().hasHeightForWidth())
        self.label_p1.setSizePolicy(sizePolicy)
        self.label_p1.setMinimumSize(QtCore.QSize(120, 40))
        self.label_p1.setMaximumSize(QtCore.QSize(120, 40))
        self.label_p1.setStyleSheet("font: 16pt \"SetoFont\";\n"
"color: rgb(106, 83, 131);")
        self.label_p1.setObjectName("label_p1")
        self.horizontalLayout_score_p1.addWidget(self.label_p1)
        self.label_score_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_score_1.sizePolicy().hasHeightForWidth())
        self.label_score_1.setSizePolicy(sizePolicy)
        self.label_score_1.setMinimumSize(QtCore.QSize(90, 40))
        self.label_score_1.setMaximumSize(QtCore.QSize(90, 40))
        self.label_score_1.setStyleSheet("font: 16pt \"SetoFont\";\n"
"color: rgb(106, 83, 131);")
        self.label_score_1.setObjectName("label_score_1")
        self.horizontalLayout_score_p1.addWidget(self.label_score_1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form_6)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 410, 356, 82))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_dice = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_dice.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_dice.setObjectName("horizontalLayout_dice")
        self.label_dice_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_dice_1.setMinimumSize(QtCore.QSize(80, 80))
        self.label_dice_1.setMaximumSize(QtCore.QSize(80, 80))
        self.label_dice_1.setText("")
        self.label_dice_1.setObjectName("label_dice_1")
        self.horizontalLayout_dice.addWidget(self.label_dice_1)
        self.label_dice_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_dice_2.setMinimumSize(QtCore.QSize(80, 80))
        self.label_dice_2.setMaximumSize(QtCore.QSize(80, 80))
        self.label_dice_2.setText("")
        self.label_dice_2.setObjectName("label_dice_2")
        self.horizontalLayout_dice.addWidget(self.label_dice_2)
        self.label_dice_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_dice_3.setMinimumSize(QtCore.QSize(80, 80))
        self.label_dice_3.setMaximumSize(QtCore.QSize(80, 80))
        self.label_dice_3.setText("")
        self.label_dice_3.setObjectName("label_dice_3")
        self.horizontalLayout_dice.addWidget(self.label_dice_3)
        self.pushButton_rollDice = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_rollDice.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton_rollDice.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_rollDice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_rollDice.setStyleSheet("font: 9pt \"SetoFont\";")
        self.pushButton_rollDice.setObjectName("pushButton_rollDice")
        self.horizontalLayout_dice.addWidget(self.pushButton_rollDice)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Form_6)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(920, 490, 219, 42))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_score_p2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_score_p2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_score_p2.setObjectName("horizontalLayout_score_p2")
        self.label_p2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_p2.sizePolicy().hasHeightForWidth())
        self.label_p2.setSizePolicy(sizePolicy)
        self.label_p2.setMinimumSize(QtCore.QSize(120, 40))
        self.label_p2.setMaximumSize(QtCore.QSize(120, 40))
        self.label_p2.setStyleSheet("font: 16pt \"SetoFont\";\n"
"color: rgb(236, 128, 81);")
        self.label_p2.setObjectName("label_p2")
        self.horizontalLayout_score_p2.addWidget(self.label_p2)
        self.label_score_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_score_2.sizePolicy().hasHeightForWidth())
        self.label_score_2.setSizePolicy(sizePolicy)
        self.label_score_2.setMinimumSize(QtCore.QSize(90, 40))
        self.label_score_2.setMaximumSize(QtCore.QSize(90, 40))
        self.label_score_2.setStyleSheet("font: 16pt \"SetoFont\";\n"
"color: rgb(236, 128, 81);")
        self.label_score_2.setObjectName("label_score_2")
        self.horizontalLayout_score_p2.addWidget(self.label_score_2)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(Form_6)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(30, 680, 1111, 132))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_p21 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_p21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_p21.setObjectName("gridLayout_p21")
        self.pushButton_p21_4 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p21_4.sizePolicy().hasHeightForWidth())
        self.pushButton_p21_4.setSizePolicy(sizePolicy)
        self.pushButton_p21_4.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_4.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p21_4.setText("")
        self.pushButton_p21_4.setObjectName("pushButton_p21_4")
        self.gridLayout_p21.addWidget(self.pushButton_p21_4, 0, 4, 1, 1)
        self.pushButton_p21_6 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p21_6.sizePolicy().hasHeightForWidth())
        self.pushButton_p21_6.setSizePolicy(sizePolicy)
        self.pushButton_p21_6.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_6.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p21_6.setText("")
        self.pushButton_p21_6.setObjectName("pushButton_p21_6")
        self.gridLayout_p21.addWidget(self.pushButton_p21_6, 0, 6, 1, 1)
        self.pushButton_p21_3 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p21_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p21_3.setSizePolicy(sizePolicy)
        self.pushButton_p21_3.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_3.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p21_3.setText("")
        self.pushButton_p21_3.setObjectName("pushButton_p21_3")
        self.gridLayout_p21.addWidget(self.pushButton_p21_3, 0, 3, 1, 1)
        self.pushButton_p21_2 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p21_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p21_2.setSizePolicy(sizePolicy)
        self.pushButton_p21_2.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_2.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p21_2.setText("")
        self.pushButton_p21_2.setObjectName("pushButton_p21_2")
        self.gridLayout_p21.addWidget(self.pushButton_p21_2, 0, 2, 1, 1)
        self.label_p21 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_p21.sizePolicy().hasHeightForWidth())
        self.label_p21.setSizePolicy(sizePolicy)
        self.label_p21.setMinimumSize(QtCore.QSize(40, 60))
        self.label_p21.setMaximumSize(QtCore.QSize(40, 60))
        self.label_p21.setStyleSheet("font: 15pt \"SetoFont\";")
        self.label_p21.setObjectName("label_p21")
        self.gridLayout_p21.addWidget(self.label_p21, 0, 0, 1, 1)
        self.pushButton_p21_1 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p21_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p21_1.setSizePolicy(sizePolicy)
        self.pushButton_p21_1.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_1.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p21_1.setText("")
        self.pushButton_p21_1.setObjectName("pushButton_p21_1")
        self.gridLayout_p21.addWidget(self.pushButton_p21_1, 0, 1, 1, 1)
        self.pushButton_p21_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p21_5.sizePolicy().hasHeightForWidth())
        self.pushButton_p21_5.setSizePolicy(sizePolicy)
        self.pushButton_p21_5.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_5.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p21_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p21_5.setText("")
        self.pushButton_p21_5.setObjectName("pushButton_p21_5")
        self.gridLayout_p21.addWidget(self.pushButton_p21_5, 0, 5, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(Form_6)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(30, 540, 1111, 132))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_p22 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_p22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_p22.setObjectName("gridLayout_p22")
        self.pushButton_p22_4 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p22_4.sizePolicy().hasHeightForWidth())
        self.pushButton_p22_4.setSizePolicy(sizePolicy)
        self.pushButton_p22_4.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_4.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p22_4.setText("")
        self.pushButton_p22_4.setObjectName("pushButton_p22_4")
        self.gridLayout_p22.addWidget(self.pushButton_p22_4, 0, 4, 1, 1)
        self.pushButton_p22_5 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p22_5.sizePolicy().hasHeightForWidth())
        self.pushButton_p22_5.setSizePolicy(sizePolicy)
        self.pushButton_p22_5.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_5.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p22_5.setText("")
        self.pushButton_p22_5.setObjectName("pushButton_p22_5")
        self.gridLayout_p22.addWidget(self.pushButton_p22_5, 0, 5, 1, 1)
        self.pushButton_p22_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p22_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p22_3.setSizePolicy(sizePolicy)
        self.pushButton_p22_3.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_3.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p22_3.setText("")
        self.pushButton_p22_3.setObjectName("pushButton_p22_3")
        self.gridLayout_p22.addWidget(self.pushButton_p22_3, 0, 3, 1, 1)
        self.pushButton_p22_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p22_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p22_2.setSizePolicy(sizePolicy)
        self.pushButton_p22_2.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_2.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p22_2.setText("")
        self.pushButton_p22_2.setObjectName("pushButton_p22_2")
        self.gridLayout_p22.addWidget(self.pushButton_p22_2, 0, 2, 1, 1)
        self.label_p22 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_p22.sizePolicy().hasHeightForWidth())
        self.label_p22.setSizePolicy(sizePolicy)
        self.label_p22.setMinimumSize(QtCore.QSize(40, 60))
        self.label_p22.setMaximumSize(QtCore.QSize(40, 60))
        self.label_p22.setStyleSheet("font: 15pt \"SetoFont\";")
        self.label_p22.setObjectName("label_p22")
        self.gridLayout_p22.addWidget(self.label_p22, 0, 0, 1, 1)
        self.pushButton_p22_1 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p22_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p22_1.setSizePolicy(sizePolicy)
        self.pushButton_p22_1.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_1.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p22_1.setText("")
        self.pushButton_p22_1.setObjectName("pushButton_p22_1")
        self.gridLayout_p22.addWidget(self.pushButton_p22_1, 0, 1, 1, 1)
        self.pushButton_p22_6 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p22_6.sizePolicy().hasHeightForWidth())
        self.pushButton_p22_6.setSizePolicy(sizePolicy)
        self.pushButton_p22_6.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_6.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_p22_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p22_6.setText("")
        self.pushButton_p22_6.setObjectName("pushButton_p22_6")
        self.gridLayout_p22.addWidget(self.pushButton_p22_6, 0, 6, 1, 1)
        self.pushButton_quit = QtWidgets.QPushButton(Form_6)
        self.pushButton_quit.setGeometry(QtCore.QRect(40, 20, 90, 40))
        self.pushButton_quit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_quit.setStyleSheet("border-image:url(:/newPrefix/quit.png)")
        self.pushButton_quit.setText("")
        self.pushButton_quit.setObjectName("pushButton_quit")

        self.retranslateUi(Form_6)
        QtCore.QMetaObject.connectSlotsByName(Form_6)

    def retranslateUi(self, Form_6):
        _translate = QtCore.QCoreApplication.translate
        Form_6.setWindowTitle(_translate("Form_6", "PERUKE"))
        self.timer_num.setText(_translate("Form_6", "<html><head/><body><p><br/></p></body></html>"))
        self.label_p12.setText(_translate("Form_6", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#6a5383;\">2</span><span style=\" font-size:12pt; font-weight:600; color:#6a5383; vertical-align:super;\">nd</span></p></body></html>"))
        self.label_p11.setText(_translate("Form_6", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#6a5383;\">1</span><span style=\" font-size:12pt; font-weight:600; color:#6a5383; vertical-align:super;\">st</span></p></body></html>"))
        self.label_p1.setText(_translate("Form_6", "<html><head/><body><p><span style=\" font-weight:600; color:#6a5383;\">Player1:</span></p></body></html>"))
        self.label_score_1.setText(_translate("Form_6", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_rollDice.setText(_translate("Form_6", "ROLL"))
        self.label_p2.setText(_translate("Form_6", "<html><head/><body><p><span style=\" font-weight:600; color:#ec8051;\">Player2:</span></p></body></html>"))
        self.label_score_2.setText(_translate("Form_6", "<html><head/><body><p><br/></p></body></html>"))
        self.label_p21.setText(_translate("Form_6", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ec8051;\">1</span><span style=\" font-size:12pt; font-weight:600; color:#ec8051; vertical-align:super;\">st</span></p></body></html>"))
        self.label_p22.setText(_translate("Form_6", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ec8051;\">2</span><span style=\" font-size:12pt; font-weight:600; color:#ec8051; vertical-align:super;\">nd</span></p></body></html>"))
