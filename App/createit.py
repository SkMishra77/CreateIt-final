# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateIt(object):
    def setupUi(self, CreateIt):
        if not CreateIt.objectName():
            CreateIt.setObjectName(u"CreateIt")
        CreateIt.resize(700, 500)
        CreateIt.setMinimumSize(QSize(700, 500))
        CreateIt.setMaximumSize(QSize(700, 500))
        self.centralwidget = QWidget(CreateIt)
        self.centralwidget.setObjectName(u"centralwidget")
        self.central_frame = QFrame(self.centralwidget)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setGeometry(QRect(-1, -1, 700, 500))
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.red_frame = QFrame(self.central_frame)
        self.red_frame.setObjectName(u"red_frame")
        self.red_frame.setGeometry(QRect(0, 0, 300, 500))
        self.red_frame.setStyleSheet(u"background-color: rgb(129, 9, 9);")
        self.red_frame.setFrameShape(QFrame.StyledPanel)
        self.red_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.red_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 90, 180, 209))
        self.red_Layout = QVBoxLayout(self.layoutWidget)
        self.red_Layout.setObjectName(u"red_Layout")
        self.red_Layout.setContentsMargins(0, 0, 0, 0)
        self.welcome_label = QLabel(self.layoutWidget)
        self.welcome_label.setObjectName(u"welcome_label")
        font = QFont()
        font.setFamily(u"Rosemary")
        font.setPointSize(36)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.red_Layout.addWidget(self.welcome_label)

        self.by = QLabel(self.layoutWidget)
        self.by.setObjectName(u"by")
        self.by.setFont(font)
        self.by.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.by.setAlignment(Qt.AlignCenter)

        self.red_Layout.addWidget(self.by)

        self.createit = QLabel(self.layoutWidget)
        self.createit.setObjectName(u"createit")
        self.createit.setFont(font)
        self.createit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.red_Layout.addWidget(self.createit)

        self.code_label = QLabel(self.red_frame)
        self.code_label.setObjectName(u"code_label")
        self.code_label.setGeometry(QRect(20, 440, 266, 16))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(10)
        self.code_label.setFont(font1)
        self.code_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.sanat_label = QLabel(self.red_frame)
        self.sanat_label.setObjectName(u"sanat_label")
        self.sanat_label.setGeometry(QRect(50, 460, 175, 16))
        self.sanat_label.setFont(font1)
        self.sanat_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.sanat_label.setAlignment(Qt.AlignCenter)
        self.gray_frame = QFrame(self.central_frame)
        self.gray_frame.setObjectName(u"gray_frame")
        self.gray_frame.setGeometry(QRect(299, -1, 450, 500))
        self.gray_frame.setStyleSheet(u"background-color: rgb(214, 214, 214);\n"
"\n"
"")
        self.gray_frame.setFrameShape(QFrame.StyledPanel)
        self.gray_frame.setFrameShadow(QFrame.Raised)
        self.enter_detail_label = QLabel(self.gray_frame)
        self.enter_detail_label.setObjectName(u"enter_detail_label")
        self.enter_detail_label.setGeometry(QRect(10, 10, 141, 31))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(14)
        self.enter_detail_label.setFont(font2)
        self.create_btn = QPushButton(self.gray_frame)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setGeometry(QRect(10, 420, 151, 41))
        self.create_btn.setStyleSheet(u"font: 12pt \"Consolas\";\n"
"background-color: rgb(170, 170, 170);\n"
"")
        self.layoutWidget1 = QWidget(self.gray_frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 50, 358, 51))
        self.folder_layout = QVBoxLayout(self.layoutWidget1)
        self.folder_layout.setObjectName(u"folder_layout")
        self.folder_layout.setContentsMargins(0, 0, 0, 0)
        self.select_path_label = QLabel(self.layoutWidget1)
        self.select_path_label.setObjectName(u"select_path_label")
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(12)
        self.select_path_label.setFont(font3)

        self.folder_layout.addWidget(self.select_path_label)

        self.u_folder_layout = QFormLayout()
        self.u_folder_layout.setObjectName(u"u_folder_layout")
        self.input_path = QLineEdit(self.layoutWidget1)
        self.input_path.setObjectName(u"input_path")
        self.input_path.setMinimumSize(QSize(320, 0))
        self.input_path.setMaximumSize(QSize(320, 16777215))
        self.input_path.setFont(font1)
        self.input_path.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")

        self.u_folder_layout.setWidget(0, QFormLayout.LabelRole, self.input_path)

        self.browse = QToolButton(self.layoutWidget1)
        self.browse.setObjectName(u"browse")
        self.browse.setStyleSheet(u"background-color: rgb(170, 170, 170);")

        self.u_folder_layout.setWidget(0, QFormLayout.FieldRole, self.browse)


        self.folder_layout.addLayout(self.u_folder_layout)

        self.layoutWidget2 = QWidget(self.gray_frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 130, 254, 98))
        self.programming_layout = QVBoxLayout(self.layoutWidget2)
        self.programming_layout.setObjectName(u"programming_layout")
        self.programming_layout.setContentsMargins(0, 0, 0, 0)
        self.programming_label = QLabel(self.layoutWidget2)
        self.programming_label.setObjectName(u"programming_label")
        self.programming_label.setFont(font3)

        self.programming_layout.addWidget(self.programming_label)

        self.lang_layout = QFormLayout()
        self.lang_layout.setObjectName(u"lang_layout")
        self.cplus = QRadioButton(self.layoutWidget2)
        self.cplus.setObjectName(u"cplus")
        self.cplus.setFont(font1)

        self.lang_layout.setWidget(0, QFormLayout.LabelRole, self.cplus)

        self.java = QRadioButton(self.layoutWidget2)
        self.java.setObjectName(u"java")
        self.java.setFont(font1)

        self.lang_layout.setWidget(1, QFormLayout.LabelRole, self.java)

        self.python = QRadioButton(self.layoutWidget2)
        self.python.setObjectName(u"python")
        self.python.setFont(font1)

        self.lang_layout.setWidget(2, QFormLayout.LabelRole, self.python)


        self.programming_layout.addLayout(self.lang_layout)

        self.layoutWidget3 = QWidget(self.gray_frame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 250, 328, 23))
        self.time_delta_layout = QFormLayout(self.layoutWidget3)
        self.time_delta_layout.setObjectName(u"time_delta_layout")
        self.time_delta_layout.setContentsMargins(0, 0, 0, 0)
        self.time_label = QLabel(self.layoutWidget3)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(170, 16))
        self.time_label.setFont(font3)
        self.time_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.time_delta_layout.setWidget(0, QFormLayout.LabelRole, self.time_label)

        self.time_delta_input = QLineEdit(self.layoutWidget3)
        self.time_delta_input.setObjectName(u"time_delta_input")
        self.time_delta_input.setFont(font1)
        self.time_delta_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.time_delta_layout.setWidget(0, QFormLayout.FieldRole, self.time_delta_input)

        self.layoutWidget4 = QWidget(self.gray_frame)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 300, 304, 29))
        self.file_layout = QFormLayout(self.layoutWidget4)
        self.file_layout.setObjectName(u"file_layout")
        self.file_layout.setContentsMargins(0, 0, 0, 0)
        self.add_file_btn = QPushButton(self.layoutWidget4)
        self.add_file_btn.setObjectName(u"add_file_btn")
        self.add_file_btn.setFont(font3)
        self.add_file_btn.setStyleSheet(u"background-color: rgb(170, 170, 170);")

        self.file_layout.setWidget(0, QFormLayout.FieldRole, self.add_file_btn)

        self.file_label = QLabel(self.layoutWidget4)
        self.file_label.setObjectName(u"file_label")
        self.file_label.setFont(font3)

        self.file_layout.setWidget(0, QFormLayout.LabelRole, self.file_label)

        self.gitPushBtn = QPushButton(self.gray_frame)
        self.gitPushBtn.setObjectName(u"gitPushBtn")
        self.gitPushBtn.setGeometry(QRect(190, 420, 151, 41))
        self.gitPushBtn.setFont(font3)
        self.gitPushBtn.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.label = QLabel(self.gray_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 350, 271, 21))
        self.label.setFont(font3)
        self.MessageInput = QLineEdit(self.gray_frame)
        self.MessageInput.setObjectName(u"MessageInput")
        self.MessageInput.setGeometry(QRect(10, 380, 331, 20))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        self.MessageInput.setFont(font4)
        self.MessageInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        CreateIt.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CreateIt)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 21))
        CreateIt.setMenuBar(self.menubar)

        self.retranslateUi(CreateIt)

        QMetaObject.connectSlotsByName(CreateIt)
    # setupUi

    def retranslateUi(self, CreateIt):
        CreateIt.setWindowTitle(QCoreApplication.translate("CreateIt", u"CreateIt", None))
        self.welcome_label.setText(QCoreApplication.translate("CreateIt", u"Welcome", None))
        self.by.setText(QCoreApplication.translate("CreateIt", u"To", None))
        self.createit.setText(QCoreApplication.translate("CreateIt", u"CreateIt", None))
        self.code_label.setText(QCoreApplication.translate("CreateIt", u"This Code is Developed & Maintained by", None))
        self.sanat_label.setText(QCoreApplication.translate("CreateIt", u"SANAT KUMAR MISHRA | PSIT", None))
        self.enter_detail_label.setText(QCoreApplication.translate("CreateIt", u"Enter Details:", None))
        self.create_btn.setText(QCoreApplication.translate("CreateIt", u"CREATE", None))
        self.select_path_label.setText(QCoreApplication.translate("CreateIt", u"Select Folder Path:", None))
        self.input_path.setText("")
        self.input_path.setPlaceholderText(QCoreApplication.translate("CreateIt", u"S E L E C T   P A T H  ", None))
        self.browse.setText(QCoreApplication.translate("CreateIt", u"...", None))
        self.programming_label.setText(QCoreApplication.translate("CreateIt", u"Select Programming Language:", None))
        self.cplus.setText(QCoreApplication.translate("CreateIt", u"C++", None))
        self.java.setText(QCoreApplication.translate("CreateIt", u"Java", None))
        self.python.setText(QCoreApplication.translate("CreateIt", u"Python", None))
        self.time_label.setText(QCoreApplication.translate("CreateIt", u"Enter Time Delta:", None))
        self.time_delta_input.setPlaceholderText(QCoreApplication.translate("CreateIt", u"0 ", None))
        self.add_file_btn.setText(QCoreApplication.translate("CreateIt", u"Add Files Names", None))
        self.file_label.setText(QCoreApplication.translate("CreateIt", u"Enter File Name :", None))
        self.gitPushBtn.setText(QCoreApplication.translate("CreateIt", u"GIT PUSH", None))
        self.label.setText(QCoreApplication.translate("CreateIt", u"Enter Message for Git Commit :", None))
        self.MessageInput.setPlaceholderText(QCoreApplication.translate("CreateIt", u"Enter Git Message to Push", None))
    # retranslateUi

