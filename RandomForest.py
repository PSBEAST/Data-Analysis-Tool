from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RF(object):
    def setupUi(self, RF):
        RF.setObjectName("RF")
        RF.setFixedSize(475, 225)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RF.setWindowIcon(icon)
        RF.setStyleSheet("border-image: url(:/images/BackGround.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(RF)
        self.gridLayout.setObjectName("gridLayout")
        self.criterion = QtWidgets.QLabel(RF)
        self.criterion.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.criterion.setScaledContents(True)
        self.criterion.setAlignment(QtCore.Qt.AlignCenter)
        self.criterion.setObjectName("criterion")
        self.gridLayout.addWidget(self.criterion, 0, 1, 1, 2)
        self.max_features = QtWidgets.QLabel(RF)
        self.max_features.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.max_features.setAlignment(QtCore.Qt.AlignCenter)
        self.max_features.setObjectName("max_features")
        self.gridLayout.addWidget(self.max_features, 0, 3, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.criterionlist = QtWidgets.QComboBox(RF)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.criterionlist.setFont(font)
        self.criterionlist.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.criterionlist.setObjectName("criterionlist")
        self.criterionlist.addItem("")
        self.criterionlist.addItem("")
        self.gridLayout.addWidget(self.criterionlist, 1, 1, 1, 2)
        self.max_featureslist = QtWidgets.QComboBox(RF)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max_featureslist.setFont(font)
        self.max_featureslist.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.max_featureslist.setObjectName("max_featureslist")
        self.max_featureslist.addItem("")
        self.max_featureslist.addItem("")
        self.max_featureslist.addItem("")
        self.gridLayout.addWidget(self.max_featureslist, 1, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(105, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)
        self.warm_start = QtWidgets.QLabel(RF)
        self.warm_start.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.warm_start.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.warm_start.setObjectName("warm_start")
        self.gridLayout.addWidget(self.warm_start, 3, 0, 1, 1)
        self.warm_startcheckBox = QtWidgets.QCheckBox(RF)
        self.warm_startcheckBox.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.warm_startcheckBox.setText("")
        self.warm_startcheckBox.setTristate(False)
        self.warm_startcheckBox.setObjectName("warm_startcheckBox")
        self.gridLayout.addWidget(self.warm_startcheckBox, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(31, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 2, 1, 1)
        self.min_samples_split = QtWidgets.QLabel(RF)
        self.min_samples_split.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.min_samples_split.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.min_samples_split.setObjectName("min_samples_split")
        self.gridLayout.addWidget(self.min_samples_split, 3, 3, 1, 2)
        self.min_samples_splitdoubleSpinBox = QtWidgets.QDoubleSpinBox(RF)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.min_samples_splitdoubleSpinBox.setFont(font)
        self.min_samples_splitdoubleSpinBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.min_samples_splitdoubleSpinBox.setMaximum(100.0)
        self.min_samples_splitdoubleSpinBox.setProperty("value", 2.0)
        self.min_samples_splitdoubleSpinBox.setObjectName("min_samples_splitdoubleSpinBox")
        self.gridLayout.addWidget(self.min_samples_splitdoubleSpinBox, 3, 5, 1, 1)
        self.oob_score = QtWidgets.QLabel(RF)
        self.oob_score.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.oob_score.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.oob_score.setObjectName("oob_score")
        self.gridLayout.addWidget(self.oob_score, 4, 0, 1, 1)
        self.oob_scorecheckBox = QtWidgets.QCheckBox(RF)
        self.oob_scorecheckBox.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.oob_scorecheckBox.setText("")
        self.oob_scorecheckBox.setObjectName("oob_scorecheckBox")
        self.gridLayout.addWidget(self.oob_scorecheckBox, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(31, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 2, 1, 1)
        self.max_depth = QtWidgets.QLabel(RF)
        self.max_depth.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.max_depth.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.max_depth.setObjectName("max_depth")
        self.gridLayout.addWidget(self.max_depth, 4, 3, 1, 2)
        self.max_depthspinBox = QtWidgets.QSpinBox(RF)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max_depthspinBox.setFont(font)
        self.max_depthspinBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.max_depthspinBox.setMinimum(0)
        self.max_depthspinBox.setMaximum(100)
        self.max_depthspinBox.setProperty("value", 0)
        self.max_depthspinBox.setObjectName("max_depthspinBox")
        self.gridLayout.addWidget(self.max_depthspinBox, 4, 5, 1, 1)
        self.bootstrap = QtWidgets.QLabel(RF)
        self.bootstrap.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.bootstrap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bootstrap.setObjectName("bootstrap")
        self.gridLayout.addWidget(self.bootstrap, 5, 0, 1, 1)
        self.bootstrapcheckBox = QtWidgets.QCheckBox(RF)
        self.bootstrapcheckBox.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.bootstrapcheckBox.setText("")
        self.bootstrapcheckBox.setChecked(True)
        self.bootstrapcheckBox.setObjectName("bootstrapcheckBox")
        self.gridLayout.addWidget(self.bootstrapcheckBox, 5, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(31, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 5, 2, 1, 1)
        self.n_estimators = QtWidgets.QLabel(RF)
        self.n_estimators.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.n_estimators.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.n_estimators.setObjectName("n_estimators")
        self.gridLayout.addWidget(self.n_estimators, 5, 3, 1, 2)
        self.n_estimatorsspinBox = QtWidgets.QSpinBox(RF)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.n_estimatorsspinBox.setFont(font)
        self.n_estimatorsspinBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.n_estimatorsspinBox.setMaximum(100)
        self.n_estimatorsspinBox.setProperty("value", 100)
        self.n_estimatorsspinBox.setObjectName("n_estimatorsspinBox")
        self.gridLayout.addWidget(self.n_estimatorsspinBox, 5, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 7, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Restore = QtWidgets.QDialogButtonBox(RF)
        self.Restore.setMinimumSize(QtCore.QSize(0, 0))
        self.Restore.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Restore.setOrientation(QtCore.Qt.Horizontal)
        self.Restore.setStandardButtons(QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.Restore.setCenterButtons(True)
        self.Restore.setObjectName("Restore")
        self.horizontalLayout.addWidget(self.Restore)
        self.Cancel = QtWidgets.QDialogButtonBox(RF)
        self.Cancel.setMinimumSize(QtCore.QSize(0, 0))
        self.Cancel.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Cancel.setOrientation(QtCore.Qt.Horizontal)
        self.Cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.Cancel.setCenterButtons(True)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.Apply = QtWidgets.QDialogButtonBox(RF)
        self.Apply.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Apply.setOrientation(QtCore.Qt.Horizontal)
        self.Apply.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.Apply.setCenterButtons(True)
        self.Apply.setObjectName("Apply")
        self.horizontalLayout.addWidget(self.Apply)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 4, 1, 2)

        self.retranslateUi(RF)
        self.Cancel.accepted.connect(RF.accept)
        self.Cancel.rejected.connect(RF.reject)
        QtCore.QMetaObject.connectSlotsByName(RF)
        
        self.Restore.clicked.connect(self.reset)
        self.max_depthspinBox.setValue(1)
        self.min_samples_splitdoubleSpinBox.setValue(1)

    def reset(self):
        self.criterionlist.setCurrentIndex(0)
        self.max_featureslist.setCurrentIndex(0)
        self.min_samples_splitdoubleSpinBox.setValue(2)
        self.max_depthspinBox.setValue(0)
        self.n_estimatorsspinBox.setValue(100)
        self.warm_startcheckBox.setChecked(False)
        self.oob_scorecheckBox.setChecked(False)
        self.bootstrapcheckBox.setChecked(True)

    def retranslateUi(self, RF):
        _translate = QtCore.QCoreApplication.translate
        RF.setWindowTitle(_translate("RF", "Random Forest"))
        self.criterion.setText(_translate("RF", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Criterion</span></p></body></html>"))
        self.max_features.setText(_translate("RF", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Max_Features</span></p></body></html>"))
        self.criterionlist.setItemText(0, _translate("RF", "gini"))
        self.criterionlist.setItemText(1, _translate("RF", "entropy"))
        self.max_featureslist.setItemText(0, _translate("RF", "auto"))
        self.max_featureslist.setItemText(1, _translate("RF", "sqrt"))
        self.max_featureslist.setItemText(2, _translate("RF", "log2"))
        self.warm_start.setText(_translate("RF", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Warm_start</span></p></body></html>"))
        self.min_samples_split.setText(_translate("RF", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Min_samples_split</span></p></body></html>"))
        self.oob_score.setText(_translate("RF", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">OOB_Score</span></p></body></html>"))
        self.max_depth.setText(_translate("RF", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Max_depth</span></p></body></html>"))
        self.bootstrap.setText(_translate("RF", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Bootstrap</span></p></body></html>"))
        self.n_estimators.setText(_translate("RF", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">N_estimators</span></p></body></html>"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    RF = QtWidgets.QDialog()
    ui = Ui_RF()
    ui.setupUi(RF)
    RF.show()
    sys.exit(app.exec_())