# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/ui/idlepc_dialog.ui'
#
# Created: Fri Apr 17 10:44:30 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_IdlePCDialog(object):

    def setupUi(self, IdlePCDialog):
        IdlePCDialog.setObjectName("IdlePCDialog")
        IdlePCDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(IdlePCDialog)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLabel = QtWidgets.QLabel(IdlePCDialog)
        self.uiLabel.setObjectName("uiLabel")
        self.gridLayout.addWidget(self.uiLabel, 0, 0, 1, 1)
        self.uiComboBox = QtWidgets.QComboBox(IdlePCDialog)
        self.uiComboBox.setObjectName("uiComboBox")
        self.gridLayout.addWidget(self.uiComboBox, 1, 0, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(IdlePCDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply | QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Help | QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 2, 0, 1, 1)

        self.retranslateUi(IdlePCDialog)
        self.uiButtonBox.accepted.connect(IdlePCDialog.accept)
        self.uiButtonBox.rejected.connect(IdlePCDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IdlePCDialog)

    def retranslateUi(self, IdlePCDialog):
        _translate = QtCore.QCoreApplication.translate
        IdlePCDialog.setWindowTitle(_translate("IdlePCDialog", "Idle-PC values"))
        self.uiLabel.setText(_translate("IdlePCDialog", "Potentially better Idle-PC values are marked with \'*\'"))
