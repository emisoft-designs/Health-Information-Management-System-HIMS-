# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Auth.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Auth(object):
    def setupUi(self, Auth):
        if not Auth.objectName():
            Auth.setObjectName(u"Auth")
        Auth.setWindowModality(Qt.ApplicationModal)
        Auth.resize(804, 844)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Auth.sizePolicy().hasHeightForWidth())
        Auth.setSizePolicy(sizePolicy)
        Auth.setMinimumSize(QSize(800, 800))
        Auth.setMaximumSize(QSize(2440, 1512))
        Auth.setSizeIncrement(QSize(0, 0))
        Auth.setBaseSize(QSize(830, 830))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(7)
        font.setKerning(False)
        Auth.setFont(font)
        Auth.setMouseTracking(True)
        Auth.setTabletTracking(True)
        Auth.setContextMenuPolicy(Qt.CustomContextMenu)
        Auth.setAutoFillBackground(True)
        Auth.setSizeGripEnabled(False)
        Auth.setModal(True)
        self.verticalLayout = QVBoxLayout(Auth)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Auth)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 45))
        self.logo.setMaximumSize(QSize(45, 45))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(5)

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 1, -1)
        self.minButton = QPushButton(self.frame)
        self.minButton.setObjectName(u"minButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.minButton.sizePolicy().hasHeightForWidth())
        self.minButton.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(11)
        font1.setKerning(True)
        self.minButton.setFont(font1)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minButton.setMouseTracking(True)
        self.minButton.setTabletTracking(True)
        self.minButton.setAutoFillBackground(True)
        self.minButton.setStyleSheet(u"")
        self.minButton.setAutoDefault(False)
        self.minButton.setFlat(False)

        self.horizontalLayout_6.addWidget(self.minButton)

        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy2.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy2)
        self.closeButton.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(12)
        font2.setKerning(True)
        self.closeButton.setFont(font2)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(True)
        self.closeButton.setTabletTracking(True)
        self.closeButton.setLayoutDirection(Qt.LeftToRight)
        self.closeButton.setAutoFillBackground(True)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setFlat(False)

        self.horizontalLayout_6.addWidget(self.closeButton)


        self.gridLayout_13.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(405, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_13)


        self.verticalLayout.addWidget(self.frame)

        self.bgLayer = QFrame(Auth)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy3)
        self.bgLayer.setMouseTracking(True)
        self.bgLayer.setTabletTracking(True)
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(2)
        self.gridLayout = QGridLayout(self.bgLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setContentsMargins(9, -1, 9, -1)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.contactauthor = QPushButton(self.bgLayer)
        self.contactauthor.setObjectName(u"contactauthor")
        font3 = QFont()
        font3.setFamily(u"Futura Bk BT")
        font3.setPointSize(6)
        font3.setItalic(True)
        font3.setKerning(True)
        self.contactauthor.setFont(font3)
        self.contactauthor.setFlat(True)

        self.horizontalLayout_5.addWidget(self.contactauthor)

        self.horizontalSpacer_2 = QSpacerItem(305, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.gridLayout_12.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.frame_6 = QFrame(self.bgLayer)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(6)
        self.frame_6.setMidLineWidth(4)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setFrameShape(QFrame.Panel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(11)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.imgView = QLabel(self.frame_8)
        self.imgView.setObjectName(u"imgView")
        self.imgView.setCursor(QCursor(Qt.BlankCursor))
        self.imgView.setFrameShape(QFrame.Box)
        self.imgView.setLineWidth(4)
        self.imgView.setPixmap(QPixmap(u"photos/pic.jpg"))
        self.imgView.setScaledContents(True)

        self.gridLayout_7.addWidget(self.imgView, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_8, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_6, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.stackedWidgets = QStackedWidget(self.bgLayer)
        self.stackedWidgets.setObjectName(u"stackedWidgets")
        sizePolicy4.setHeightForWidth(self.stackedWidgets.sizePolicy().hasHeightForWidth())
        self.stackedWidgets.setSizePolicy(sizePolicy4)
        self.stackedWidgets.setMinimumSize(QSize(0, 0))
        self.stackedWidgets.setMaximumSize(QSize(16777215, 16777215))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.loginForm_2 = QFrame(self.page)
        self.loginForm_2.setObjectName(u"loginForm_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.loginForm_2.sizePolicy().hasHeightForWidth())
        self.loginForm_2.setSizePolicy(sizePolicy6)
        self.loginForm_2.setMaximumSize(QSize(16777215, 295))
        self.loginForm_2.setAutoFillBackground(False)
        self.loginForm_2.setFrameShape(QFrame.Box)
        self.loginForm_2.setFrameShadow(QFrame.Plain)
        self.loginForm_2.setLineWidth(2)
        self.gridLayout_4 = QGridLayout(self.loginForm_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_9 = QFrame(self.loginForm_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setAutoFillBackground(True)
        self.frame_9.setFrameShape(QFrame.Box)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frame_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer = QSpacerItem(93, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Comic Sans MS")
        font4.setPointSize(8)
        font4.setKerning(True)
        self.label_28.setFont(font4)
        self.label_28.setCursor(QCursor(Qt.BlankCursor))

        self.gridLayout_5.addWidget(self.label_28, 1, 1, 1, 1)

        self.label_27 = QLabel(self.frame_9)
        self.label_27.setObjectName(u"label_27")
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(7)
        font5.setKerning(True)
        self.label_27.setFont(font5)

        self.gridLayout_5.addWidget(self.label_27, 4, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.linkReg = QPushButton(self.frame_9)
        self.linkReg.setObjectName(u"linkReg")
        font6 = QFont()
        font6.setFamily(u"Franklin Gothic Medium")
        font6.setPointSize(6)
        font6.setItalic(True)
        font6.setKerning(True)
        self.linkReg.setFont(font6)
        self.linkReg.setCursor(QCursor(Qt.PointingHandCursor))
        self.linkReg.setMouseTracking(True)
        self.linkReg.setTabletTracking(True)
        self.linkReg.setToolTipDuration(3)
        self.linkReg.setLayoutDirection(Qt.LeftToRight)
        self.linkReg.setAutoFillBackground(True)
        self.linkReg.setFlat(True)

        self.horizontalLayout_7.addWidget(self.linkReg)

        self.horizontalSpacer_3 = QSpacerItem(228, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 8, 0, 1, 3)

        self.username = QLineEdit(self.frame_9)
        self.username.setObjectName(u"username")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy7)
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setFont(font5)
        self.username.setAutoFillBackground(False)

        self.gridLayout_5.addWidget(self.username, 3, 1, 1, 2)

        self.password = QLineEdit(self.frame_9)
        self.password.setObjectName(u"password")
        sizePolicy7.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy7)
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setFont(font5)
        self.password.setAutoFillBackground(False)
        self.password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout_5.addWidget(self.password, 4, 1, 1, 2)

        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)

        self.gridLayout_5.addWidget(self.label_26, 3, 0, 1, 1)

        self.loginButton = QCommandLinkButton(self.frame_9)
        self.loginButton.setObjectName(u"loginButton")
        sizePolicy1.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy1)
        self.loginButton.setMaximumSize(QSize(70, 100))
        font7 = QFont()
        font7.setFamily(u"Comic Sans MS")
        font7.setPointSize(7)
        font7.setItalic(True)
        font7.setKerning(True)
        self.loginButton.setFont(font7)
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setAutoDefault(False)
        self.loginButton.setDefault(False)

        self.gridLayout_5.addWidget(self.loginButton, 5, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_9, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.loginForm_2, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.stackedWidgets.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.regForm = QFrame(self.page_2)
        self.regForm.setObjectName(u"regForm")
        self.regForm.setEnabled(True)
        self.regForm.setMaximumSize(QSize(16777215, 16777215))
        self.regForm.setAutoFillBackground(True)
        self.regForm.setStyleSheet(u"background-color: rgb(179, 176, 87);\n"
"color: rgb(2, 2, 2);")
        self.regForm.setFrameShape(QFrame.StyledPanel)
        self.regForm.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.regForm)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_5 = QFrame(self.regForm)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy8)
        self.frame_5.setMaximumSize(QSize(16777215, 120))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")
        font8 = QFont()
        font8.setPointSize(6)
        self.label_24.setFont(font8)

        self.horizontalLayout_4.addWidget(self.label_24)

        self.authID = QLineEdit(self.frame_5)
        self.authID.setObjectName(u"authID")
        self.authID.setAutoFillBackground(False)
        self.authID.setStyleSheet(u"color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.authID)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.gridLayout_10.addLayout(self.formLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.regCancel = QPushButton(self.frame_5)
        self.regCancel.setObjectName(u"regCancel")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.regCancel.sizePolicy().hasHeightForWidth())
        self.regCancel.setSizePolicy(sizePolicy9)
        self.regCancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.regCancel.setStyleSheet(u"border-color: rgb(8, 8, 8);")

        self.horizontalLayout.addWidget(self.regCancel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.regButton = QPushButton(self.frame_5)
        self.regButton.setObjectName(u"regButton")
        sizePolicy9.setHeightForWidth(self.regButton.sizePolicy().hasHeightForWidth())
        self.regButton.setSizePolicy(sizePolicy9)
        self.regButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.regButton.setAutoFillBackground(False)
        self.regButton.setStyleSheet(u"border-color: rgb(8, 8, 8);")
        self.regButton.setFlat(False)

        self.horizontalLayout.addWidget(self.regButton)


        self.gridLayout_10.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_5, 4, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.regForm)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 150))
        font9 = QFont()
        font9.setBold(True)
        font9.setWeight(75)
        self.groupBox_4.setFont(font9)
        self.groupBox_4.setAutoFillBackground(True)
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font8)

        self.gridLayout_9.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font8)

        self.gridLayout_9.addWidget(self.label_23, 1, 0, 1, 1)

        self.regUserid = QLineEdit(self.groupBox_4)
        self.regUserid.setObjectName(u"regUserid")
        self.regUserid.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.regUserid, 0, 1, 1, 1)

        self.regPaswd = QLineEdit(self.groupBox_4)
        self.regPaswd.setObjectName(u"regPaswd")
        self.regPaswd.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.regPaswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_9.addWidget(self.regPaswd, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_4, 3, 0, 1, 1)

        self.label_25 = QLabel(self.regForm)
        self.label_25.setObjectName(u"label_25")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy10)
        self.label_25.setMaximumSize(QSize(300, 40))
        self.label_25.setFont(font9)

        self.gridLayout_8.addWidget(self.label_25, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.regForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(40)
        sizePolicy11.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy11)
        self.groupBox_3.setMaximumSize(QSize(16777215, 356))
        self.groupBox_3.setFont(font9)
        self.gridLayout_11 = QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font8)

        self.gridLayout_11.addWidget(self.label_16, 7, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font8)

        self.gridLayout_11.addWidget(self.label_18, 6, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font8)

        self.gridLayout_11.addWidget(self.label_12, 0, 0, 1, 1)

        self.surname = QLineEdit(self.groupBox_3)
        self.surname.setObjectName(u"surname")
        self.surname.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.surname, 1, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font8)

        self.gridLayout_11.addWidget(self.label_15, 4, 0, 1, 1)

        self.gender = QLineEdit(self.groupBox_3)
        self.gender.setObjectName(u"gender")
        self.gender.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.gender, 2, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font8)

        self.gridLayout_11.addWidget(self.label_14, 3, 0, 1, 1)

        self.rank = QLineEdit(self.groupBox_3)
        self.rank.setObjectName(u"rank")
        self.rank.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.rank, 7, 1, 1, 1)

        self.firstName = QLineEdit(self.groupBox_3)
        self.firstName.setObjectName(u"firstName")
        self.firstName.setStyleSheet(u"color: rgb(8, 8, 8);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.firstName, 0, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font8)

        self.gridLayout_11.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)

        self.gridLayout_11.addWidget(self.label_13, 1, 0, 1, 1)

        self.jobTitle = QLineEdit(self.groupBox_3)
        self.jobTitle.setObjectName(u"jobTitle")
        self.jobTitle.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.jobTitle, 3, 1, 1, 1)

        self.dept = QLineEdit(self.groupBox_3)
        self.dept.setObjectName(u"dept")
        self.dept.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.dept, 4, 1, 1, 1)

        self.employeeID = QLineEdit(self.groupBox_3)
        self.employeeID.setObjectName(u"employeeID")
        self.employeeID.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.employeeID, 6, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.lineEdit, 8, 1, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font8)

        self.gridLayout_11.addWidget(self.label, 8, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.regForm)

        self.stackedWidgets.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidgets, 0, 2, 1, 1)

        self.line = QFrame(self.bgLayer)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.bgLayer)


        self.retranslateUi(Auth)

        self.stackedWidgets.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Auth)
    # setupUi

    def retranslateUi(self, Auth):
        Auth.setWindowTitle(QCoreApplication.translate("Auth", u"Start", None))
        self.logo.setText("")
        self.label_29.setText(QCoreApplication.translate("Auth", u"Welcome", None))
        self.minButton.setText(QCoreApplication.translate("Auth", u"__", None))
        self.closeButton.setText(QCoreApplication.translate("Auth", u"X", None))
        self.contactauthor.setText(QCoreApplication.translate("Auth", u"Contact Author", None))
        self.imgView.setText("")
        self.label_28.setText(QCoreApplication.translate("Auth", u"Login", None))
        self.label_27.setText(QCoreApplication.translate("Auth", u"Password:", None))
#if QT_CONFIG(tooltip)
        self.linkReg.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.linkReg.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.linkReg.setText(QCoreApplication.translate("Auth", u"Register", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Auth", u"Input Usersname or ID", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Auth", u"Input Password", None))
        self.label_26.setText(QCoreApplication.translate("Auth", u"Username/ID:", None))
        self.loginButton.setText(QCoreApplication.translate("Auth", u"Login", None))
        self.label_24.setText(QCoreApplication.translate("Auth", u"Authorized ID:", None))
        self.authID.setText("")
        self.regCancel.setText(QCoreApplication.translate("Auth", u"Cancel", None))
        self.regButton.setText(QCoreApplication.translate("Auth", u"Register", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Auth", u"Login Details", None))
        self.label_22.setText(QCoreApplication.translate("Auth", u"User ID/Name:*", None))
        self.label_23.setText(QCoreApplication.translate("Auth", u"Password:*", None))
        self.label_25.setText(QCoreApplication.translate("Auth", u"Employee Registration Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Auth", u"Personal Details", None))
        self.label_16.setText(QCoreApplication.translate("Auth", u"Rank:", None))
        self.label_18.setText(QCoreApplication.translate("Auth", u"Employment ID:*", None))
        self.label_12.setText(QCoreApplication.translate("Auth", u"First Name:*", None))
        self.label_15.setText(QCoreApplication.translate("Auth", u"Department:*", None))
        self.label_14.setText(QCoreApplication.translate("Auth", u"Job Title:*", None))
        self.firstName.setText("")
        self.label_17.setText(QCoreApplication.translate("Auth", u"Gender:", None))
        self.label_13.setText(QCoreApplication.translate("Auth", u"Surname:*", None))
        self.label.setText(QCoreApplication.translate("Auth", u"Email:*", None))
    # retranslateUi

