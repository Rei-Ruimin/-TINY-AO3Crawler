# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(246, 249)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/download.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 7pt \"Verdana\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.info_btn = QtWidgets.QPushButton(Form)
        self.info_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.info_btn.setMaximumSize(QtCore.QSize(15, 15))
        self.info_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(85, 0, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    font: 7pt \"Verdana\";\n"
"    border-style:none;\n"
"    padding:3px;\n"
"    min-height:10px;\n"
"    min-width:10px;\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(68, 0, 206);\n"
"}")
        self.info_btn.setObjectName("info_btn")
        self.horizontalLayout.addWidget(self.info_btn, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.search_key_le = QtWidgets.QLineEdit(Form)
        self.search_key_le.setMinimumSize(QtCore.QSize(140, 0))
        self.search_key_le.setMaximumSize(QtCore.QSize(140, 16777215))
        self.search_key_le.setStyleSheet("QLineEdit {\n"
"    font: 7pt \"Verdana\";\n"
"    border: 0.5px solid rgb(196, 196, 196);\n"
"    border-radius: 8px;\n"
"    height: 17px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border-color:rgb(146, 209, 244);\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    background-color: rgb(231, 231, 231);\n"
"}")
        self.search_key_le.setText("")
        self.search_key_le.setPlaceholderText("")
        self.search_key_le.setObjectName("search_key_le")
        self.verticalLayout_2.addWidget(self.search_key_le, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(15, 0))
        self.label_2.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_2.setStyleSheet("font: 7pt \"Verdana\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("font: 7pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.search_p_url_le = QtWidgets.QLineEdit(Form)
        self.search_p_url_le.setEnabled(True)
        self.search_p_url_le.setMinimumSize(QtCore.QSize(140, 0))
        self.search_p_url_le.setMaximumSize(QtCore.QSize(140, 16777215))
        self.search_p_url_le.setStyleSheet("QLineEdit {\n"
"    font: 7pt \"Verdana\";\n"
"    border: 0.5px solid rgb(196, 196, 196);\n"
"    border-radius: 8px;\n"
"    height: 17px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border-color:rgb(146, 209, 244);\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    background-color: rgb(231, 231, 231);\n"
"}")
        self.search_p_url_le.setText("")
        self.search_p_url_le.setReadOnly(False)
        self.search_p_url_le.setObjectName("search_p_url_le")
        self.verticalLayout_3.addWidget(self.search_p_url_le, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_dir_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_dir_btn.sizePolicy().hasHeightForWidth())
        self.save_dir_btn.setSizePolicy(sizePolicy)
        self.save_dir_btn.setMinimumSize(QtCore.QSize(126, 18))
        self.save_dir_btn.setMaximumSize(QtCore.QSize(110, 16777215))
        self.save_dir_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(85, 0, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    font: 7pt \"Verdana\";\n"
"    border-style:none;\n"
"    padding:3px;\n"
"    min-height:12px;\n"
"    min-width:120px;\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(68, 0, 206);\n"
"}")
        self.save_dir_btn.setObjectName("save_dir_btn")
        self.verticalLayout.addWidget(self.save_dir_btn, 0, QtCore.Qt.AlignHCenter)
        self.save_dir_le = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_dir_le.sizePolicy().hasHeightForWidth())
        self.save_dir_le.setSizePolicy(sizePolicy)
        self.save_dir_le.setMinimumSize(QtCore.QSize(160, 0))
        self.save_dir_le.setMaximumSize(QtCore.QSize(140, 16777215))
        self.save_dir_le.setStyleSheet("QLineEdit {\n"
"    font: 7pt \"Verdana\";\n"
"    color: gray;\n"
"    border: 0.5px solid rgb(196, 196, 196);\n"
"    border-radius: 0px;\n"
"    height: 15px;\n"
"    border-color: white white lightgray white\n"
"}")
        self.save_dir_le.setReadOnly(True)
        self.save_dir_le.setObjectName("save_dir_le")
        self.verticalLayout.addWidget(self.save_dir_le, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.ok_btn = QtWidgets.QPushButton(Form)
        self.ok_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(85, 0, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    font: 7pt \"Verdana\";\n"
"    border-style:none;\n"
"    padding:3px;\n"
"    min-height:20px;\n"
"    min-width:40px;\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(68, 0, 206);\n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout_4.addWidget(self.ok_btn, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)

        self.retranslateUi(Form)
        self.info_btn.clicked.connect(Form.info_btn_c)
        self.save_dir_btn.clicked.connect(Form.save_dir_btn_c)
        self.ok_btn.clicked.connect(Form.ok_btn_c)
        self.search_key_le.textChanged['QString'].connect(Form.search_key_le_changed)
        self.search_p_url_le.textChanged['QString'].connect(Form.search_p_url_le_changed)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AO3 Crawler"))
        self.label.setText(_translate("Form", "Search Keyword"))
        self.info_btn.setText(_translate("Form", "?"))
        self.label_2.setText(_translate("Form", "OR"))
        self.label_3.setText(_translate("Form", "URL of Search Page"))
        self.save_dir_btn.setText(_translate("Form", "Choose Save Directory"))
        self.save_dir_le.setText(_translate("Form", "the chosen directory will be here"))
        self.ok_btn.setText(_translate("Form", "OK"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
