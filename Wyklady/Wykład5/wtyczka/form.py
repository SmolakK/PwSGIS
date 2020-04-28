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
        Okno.resize(331, 288)
        Okno.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        Okno.setWindowOpacity(1.0)
        self.buttonBox = QtWidgets.QDialogButtonBox(Okno)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Okno)
        self.buttonBox.accepted.connect(Okno.accept)
        self.buttonBox.rejected.connect(Okno.reject)
        QtCore.QMetaObject.connectSlotsByName(Okno)

    def retranslateUi(self, Okno):
        _translate = QtCore.QCoreApplication.translate
        Okno.setWindowTitle(_translate("Okno", "NaszPlugin"))
