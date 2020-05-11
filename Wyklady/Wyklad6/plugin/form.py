# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Okno(object):
    def setupUi(self, Okno):
        Okno.setObjectName("Okno")
        Okno.setEnabled(True)
        Okno.resize(519, 492)
        Okno.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Okno.setWindowOpacity(1.0)
        self.buttonBox = QtWidgets.QDialogButtonBox(Okno)
        self.buttonBox.setGeometry(QtCore.QRect(120, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Okno)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 441, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(70, 40, 91, 31))
        self.checkBox.setObjectName("checkBox")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(200, 40, 101, 31))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(60, 80, 47, 13))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Okno)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Okno.accept)
        self.buttonBox.rejected.connect(Okno.reject)
        QtCore.QMetaObject.connectSlotsByName(Okno)

    def retranslateUi(self, Okno):
        _translate = QtCore.QCoreApplication.translate
        Okno.setWindowTitle(_translate("Okno", "NaszPlugin"))
        self.pushButton.setText(_translate("Okno", "Otwórz"))
        self.pushButton_2.setText(_translate("Okno", "Zapisz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Okno", "Tab 1"))
        self.checkBox.setText(_translate("Okno", "KLIK"))
        self.label.setText(_translate("Okno", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Okno", "Tab 2"))
