from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DT(object):
    def setupUi(self, DT):
        DT.setObjectName("DT")
        DT.setFixedSize(400, 241)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DT.setWindowIcon(icon)
        DT.setStyleSheet("border-image: url(:/images/BackGround.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(DT)
        self.gridLayout.setObjectName("gridLayout")
        self.criterion = QtWidgets.QLabel(DT)
        self.criterion.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.criterion.setScaledContents(True)
        self.criterion.setAlignment(QtCore.Qt.AlignCenter)
        self.criterion.setObjectName("criterion")
        self.gridLayout.addWidget(self.criterion, 0, 1, 1, 2)
        self.splitter = QtWidgets.QLabel(DT)
        self.splitter.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.splitter.setAlignment(QtCore.Qt.AlignCenter)
        self.splitter.setObjectName("splitter")
        self.gridLayout.addWidget(self.splitter, 0, 4, 1, 2)
        self.max_features = QtWidgets.QLabel(DT)
        self.max_features.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.max_features.setAlignment(QtCore.Qt.AlignCenter)
        self.max_features.setObjectName("max_features")
        self.gridLayout.addWidget(self.max_features, 0, 8, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(19, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.criterionlist = QtWidgets.QComboBox(DT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.criterionlist.setFont(font)
        self.criterionlist.setStyleSheet("border-image: url(:/images/1White.png);")
        self.criterionlist.setObjectName("criterionlist")
        self.criterionlist.addItem("")
        self.criterionlist.addItem("")
        self.gridLayout.addWidget(self.criterionlist, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.splitterlist = QtWidgets.QComboBox(DT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.splitterlist.setFont(font)
        self.splitterlist.setStyleSheet("border-image: url(:/images/1White.png);")
        self.splitterlist.setObjectName("splitterlist")
        self.splitterlist.addItem("")
        self.splitterlist.addItem("")
        self.gridLayout.addWidget(self.splitterlist, 1, 4, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 7, 1, 1)
        self.max_featureslist = QtWidgets.QComboBox(DT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max_featureslist.setFont(font)
        self.max_featureslist.setStyleSheet("border-image: url(:/images/1White.png);")
        self.max_featureslist.setObjectName("max_featureslist")
        self.max_featureslist.addItem("")
        self.max_featureslist.addItem("")
        self.max_featureslist.addItem("")
        self.max_featureslist.addItem("")
        self.gridLayout.addWidget(self.max_featureslist, 1, 8, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(19, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 10, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 2, 2)
        self.min_samples_split = QtWidgets.QLabel(DT)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.min_samples_split.setFont(font)
        self.min_samples_split.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.min_samples_split.setScaledContents(True)
        self.min_samples_split.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.min_samples_split.setObjectName("min_samples_split")
        self.gridLayout.addWidget(self.min_samples_split, 3, 2, 1, 5)
        self.min_samples_splitdoubleSpinBox = QtWidgets.QDoubleSpinBox(DT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.min_samples_splitdoubleSpinBox.setFont(font)
        self.min_samples_splitdoubleSpinBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.min_samples_splitdoubleSpinBox.setMaximum(100.0)
        self.min_samples_splitdoubleSpinBox.setProperty("value", 2.0)
        self.min_samples_splitdoubleSpinBox.setObjectName("min_samples_splitdoubleSpinBox")
        self.gridLayout.addWidget(self.min_samples_splitdoubleSpinBox, 3, 7, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(74, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 9, 1, 2)
        self.max_depth = QtWidgets.QLabel(DT)
        self.max_depth.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.max_depth.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.max_depth.setObjectName("max_depth")
        self.gridLayout.addWidget(self.max_depth, 4, 2, 2, 3)
        spacerItem7 = QtWidgets.QSpacerItem(74, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 9, 2, 2)
        spacerItem8 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 5, 0, 1, 2)
        self.max_depthspinBox = QtWidgets.QSpinBox(DT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max_depthspinBox.setFont(font)
        self.max_depthspinBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.max_depthspinBox.setMinimum(0)
        self.max_depthspinBox.setMaximum(100)
        self.max_depthspinBox.setProperty("value", 0)
        self.max_depthspinBox.setObjectName("max_depthspinBox")
        self.gridLayout.addWidget(self.max_depthspinBox, 5, 7, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 6, 0, 1, 2)
        self.min_samples_leaf = QtWidgets.QLabel(DT)
        self.min_samples_leaf.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.min_samples_leaf.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.min_samples_leaf.setObjectName("min_samples_leaf")
        self.gridLayout.addWidget(self.min_samples_leaf, 6, 2, 1, 4)
        self.min_samples_leafspinBox = QtWidgets.QSpinBox(DT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.min_samples_leafspinBox.setFont(font)
        self.min_samples_leafspinBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.min_samples_leafspinBox.setMaximum(100)
        self.min_samples_leafspinBox.setProperty("value", 1)
        self.min_samples_leafspinBox.setObjectName("min_samples_leafspinBox")
        self.gridLayout.addWidget(self.min_samples_leafspinBox, 6, 7, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(74, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 6, 9, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 7, 5, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 8, 0, 1, 6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Restore = QtWidgets.QDialogButtonBox(DT)
        self.Restore.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Restore.setOrientation(QtCore.Qt.Horizontal)
        self.Restore.setStandardButtons(QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.Restore.setCenterButtons(True)
        self.Restore.setObjectName("Restore")
        self.horizontalLayout.addWidget(self.Restore)
        self.Cancel = QtWidgets.QDialogButtonBox(DT)
        self.Cancel.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Cancel.setOrientation(QtCore.Qt.Horizontal)
        self.Cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.Cancel.setCenterButtons(True)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.Apply = QtWidgets.QDialogButtonBox(DT)
        self.Apply.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Apply.setOrientation(QtCore.Qt.Horizontal)
        self.Apply.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.Apply.setCenterButtons(True)
        self.Apply.setObjectName("Apply")
        self.horizontalLayout.addWidget(self.Apply)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 6, 1, 5)

        self.retranslateUi(DT)
        self.Cancel.accepted.connect(DT.accept)
        self.Cancel.rejected.connect(DT.reject)
        QtCore.QMetaObject.connectSlotsByName(DT)

        self.Restore.clicked.connect(self.reset)
        self.max_depthspinBox.setValue(1)
        self.min_samples_splitdoubleSpinBox.setValue(1)
        self.max_featureslist.removeItem(0)

    def reset(self):
        self.criterionlist.setCurrentIndex(0)
        self.splitterlist.setCurrentIndex(0)
        self.max_featureslist.setCurrentIndex(0)
        self.min_samples_splitdoubleSpinBox.setValue(2)
        self.max_depthspinBox.setValue(0)
        self.min_samples_leafspinBox.setValue(1)

    def retranslateUi(self, DT):
        _translate = QtCore.QCoreApplication.translate
        DT.setWindowTitle(_translate("DT", "Decision Tree"))
        self.criterion.setText(_translate("DT", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Criterion</span></p></body></html>"))
        self.splitter.setText(_translate("DT", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Splitter</span></p></body></html>"))
        self.max_features.setText(_translate("DT", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Max_Features</span></p></body></html>"))
        self.criterionlist.setItemText(0, _translate("DT", "gini"))
        self.criterionlist.setItemText(1, _translate("DT", "entropy"))
        self.splitterlist.setItemText(0, _translate("DT", "best"))
        self.splitterlist.setItemText(1, _translate("DT", "random"))
        self.max_featureslist.setItemText(0, _translate("DT", "None"))
        self.max_featureslist.setItemText(1, _translate("DT", "auto"))
        self.max_featureslist.setItemText(2, _translate("DT", "sqrt"))
        self.max_featureslist.setItemText(3, _translate("DT", "log2"))
        self.min_samples_split.setText(_translate("DT", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Min_samples_split</span></p></body></html>"))
        self.max_depth.setText(_translate("DT", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Max_depth</span></p></body></html>"))
        self.min_samples_leaf.setText(_translate("DT", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Min_samples_leaf</span></p></body></html>"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    DT = QtWidgets.QDialog()
    ui = Ui_DT()
    ui.setupUi(DT)
    DT.show()
    sys.exit(app.exec_())
