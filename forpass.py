from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgotPassword(object):
    def setupUi(self, ForgotPassword):
        ForgotPassword.setObjectName("ForgotPassword")
        ForgotPassword.resize(514, 503)
        ForgotPassword.setMinimumSize(QtCore.QSize(514, 503))
        ForgotPassword.setMaximumSize(QtCore.QSize(514, 503))
        font = QtGui.QFont()
        font.setPointSize(10)
        ForgotPassword.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Img/Images/logoicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ForgotPassword.setWindowIcon(icon)
        ForgotPassword.setStyleSheet("background-color: rgb(54, 57, 63);")
        ForgotPassword.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(ForgotPassword)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(28, 348, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.usernamelabel = QtWidgets.QLabel(ForgotPassword)
        self.usernamelabel.setMinimumSize(QtCore.QSize(401, 21))
        self.usernamelabel.setMaximumSize(QtCore.QSize(401, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernamelabel.setFont(font)
        self.usernamelabel.setObjectName("usernamelabel")
        self.verticalLayout.addWidget(self.usernamelabel)
        self.username = QtWidgets.QLineEdit(ForgotPassword)
        self.username.setMinimumSize(QtCore.QSize(411, 41))
        self.username.setMaximumSize(QtCore.QSize(411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);\n"+"border-radius: 6;")
        self.username.setText("")
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SecQuecomboBox = QtWidgets.QComboBox(ForgotPassword)
        self.SecQuecomboBox.setMinimumSize(QtCore.QSize(411, 31))
        self.SecQuecomboBox.setMaximumSize(QtCore.QSize(411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SecQuecomboBox.setFont(font)
        self.SecQuecomboBox.setStyleSheet("")
        self.SecQuecomboBox.setObjectName("SecQuecomboBox")
        self.SecQuecomboBox.addItem("")
        self.SecQuecomboBox.addItem("")
        self.SecQuecomboBox.addItem("")
        self.SecQuecomboBox.addItem("")
        self.SecQuecomboBox.addItem("")
        self.verticalLayout_2.addWidget(self.SecQuecomboBox)
        self.securityQue = QtWidgets.QLineEdit(ForgotPassword)
        self.securityQue.setMinimumSize(QtCore.QSize(411, 41))
        self.securityQue.setMaximumSize(QtCore.QSize(411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.securityQue.setFont(font)
        self.securityQue.setStyleSheet("background-color: rgb(255, 255, 255);\n"+"border-radius: 6;")
        # self.securityQue.setEchoMode(QtWidgets.QLineEdit.Password)
        self.securityQue.setObjectName("securityQue")
        self.verticalLayout_2.addWidget(self.securityQue)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(408, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.passwordlabel = QtWidgets.QLabel(ForgotPassword)
        self.passwordlabel.setMinimumSize(QtCore.QSize(401, 21))
        self.passwordlabel.setMaximumSize(QtCore.QSize(401, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setObjectName("passwordlabel")
        self.verticalLayout_3.addWidget(self.passwordlabel)
        self.password = QtWidgets.QLineEdit(ForgotPassword)
        self.password.setMinimumSize(QtCore.QSize(411, 41))
        self.password.setMaximumSize(QtCore.QSize(411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);\n"+"border-radius: 6;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_3.addWidget(self.password)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.repasswordlabel = QtWidgets.QLabel(ForgotPassword)
        self.repasswordlabel.setMinimumSize(QtCore.QSize(411, 24))
        self.repasswordlabel.setMaximumSize(QtCore.QSize(411, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.repasswordlabel.setFont(font)
        self.repasswordlabel.setObjectName("repasswordlabel")
        self.verticalLayout_4.addWidget(self.repasswordlabel)
        self.repassword = QtWidgets.QLineEdit(ForgotPassword)
        self.repassword.setMinimumSize(QtCore.QSize(411, 41))
        self.repassword.setMaximumSize(QtCore.QSize(411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.repassword.setFont(font)
        self.repassword.setStyleSheet("background-color: rgb(255, 255, 255);\n"+"border-radius: 6;")
        self.repassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repassword.setObjectName("repassword")
        self.verticalLayout_4.addWidget(self.repassword)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(28, 348, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(478, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(328, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.Reset = QtWidgets.QPushButton(ForgotPassword)
        self.Reset.setMinimumSize(QtCore.QSize(93, 28))
        self.Reset.setMaximumSize(QtCore.QSize(93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Reset.setFont(font)
        self.Reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reset.setStyleSheet("background-color: rgb(255, 255, 255);\n"+"border-radius: 6;")
        self.Reset.setObjectName("Reset")
        self.horizontalLayout.addWidget(self.Reset)
        spacerItem5 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(458, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.retranslateUi(ForgotPassword)
        QtCore.QMetaObject.connectSlotsByName(ForgotPassword)

    def retranslateUi(self, ForgotPassword):
        _translate = QtCore.QCoreApplication.translate
        ForgotPassword.setWindowTitle(_translate("ForgotPassword", "Forgot Password?"))
        self.usernamelabel.setText(_translate("ForgotPassword", "Username"))
        self.SecQuecomboBox.setItemText(0, _translate("ForgotPassword", "Security Question?"))
        self.SecQuecomboBox.setItemText(1, _translate("ForgotPassword", "Mother\'s Name"))
        self.SecQuecomboBox.setItemText(2, _translate("ForgotPassword", "First Pet Name"))
        self.SecQuecomboBox.setItemText(3, _translate("ForgotPassword", "First School Name"))
        self.SecQuecomboBox.setItemText(4, _translate("ForgotPassword", "Set Passcode"))
        self.passwordlabel.setText(_translate("ForgotPassword", "Password"))
        self.repasswordlabel.setText(_translate("ForgotPassword", " Re-Password"))
        self.Reset.setText(_translate("ForgotPassword", "Reset"))


import Images_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    ForgotPassword = QtWidgets.QDialog()
    ui = Ui_ForgotPassword()
    ui.setupUi(ForgotPassword)
    ForgotPassword.show()
    sys.exit(app.exec_())
