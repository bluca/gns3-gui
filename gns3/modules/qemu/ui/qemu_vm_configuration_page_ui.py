# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/modules/qemu/ui/qemu_vm_configuration_page.ui'
#
# Created: Fri Apr 17 10:44:35 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_QemuVMConfigPageWidget(object):

    def setupUi(self, QemuVMConfigPageWidget):
        QemuVMConfigPageWidget.setObjectName("QemuVMConfigPageWidget")
        QemuVMConfigPageWidget.resize(486, 407)
        self.verticalLayout = QtWidgets.QVBoxLayout(QemuVMConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiQemutabWidget = QtWidgets.QTabWidget(QemuVMConfigPageWidget)
        self.uiQemutabWidget.setObjectName("uiQemutabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiQemuListLabel = QtWidgets.QLabel(self.tab)
        self.uiQemuListLabel.setObjectName("uiQemuListLabel")
        self.gridLayout_4.addWidget(self.uiQemuListLabel, 2, 0, 1, 2)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout_4.addWidget(self.uiNameLineEdit, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(263, 94, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 4, 1, 1, 2)
        self.uiQemuListComboBox = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQemuListComboBox.sizePolicy().hasHeightForWidth())
        self.uiQemuListComboBox.setSizePolicy(sizePolicy)
        self.uiQemuListComboBox.setObjectName("uiQemuListComboBox")
        self.gridLayout_4.addWidget(self.uiQemuListComboBox, 2, 2, 1, 1)
        self.uiConsolePortSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiConsolePortSpinBox.setMaximum(65535)
        self.uiConsolePortSpinBox.setObjectName("uiConsolePortSpinBox")
        self.gridLayout_4.addWidget(self.uiConsolePortSpinBox, 3, 2, 1, 1)
        self.uiConsolePortLabel = QtWidgets.QLabel(self.tab)
        self.uiConsolePortLabel.setObjectName("uiConsolePortLabel")
        self.gridLayout_4.addWidget(self.uiConsolePortLabel, 3, 0, 1, 2)
        self.uiNameLabel = QtWidgets.QLabel(self.tab)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout_4.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiRamLabel = QtWidgets.QLabel(self.tab)
        self.uiRamLabel.setObjectName("uiRamLabel")
        self.gridLayout_4.addWidget(self.uiRamLabel, 1, 0, 1, 1)
        self.uiRamSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiRamSpinBox.setMinimum(32)
        self.uiRamSpinBox.setMaximum(65535)
        self.uiRamSpinBox.setProperty("value", 256)
        self.uiRamSpinBox.setObjectName("uiRamSpinBox")
        self.gridLayout_4.addWidget(self.uiRamSpinBox, 1, 2, 1, 1)
        self.uiQemutabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.uiHdaDiskImageLabel = QtWidgets.QLabel(self.tab_3)
        self.uiHdaDiskImageLabel.setObjectName("uiHdaDiskImageLabel")
        self.gridLayout_6.addWidget(self.uiHdaDiskImageLabel, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiHdaDiskImageLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.uiHdaDiskImageLineEdit.setObjectName("uiHdaDiskImageLineEdit")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageLineEdit)
        self.uiHdaDiskImageToolButton = QtWidgets.QToolButton(self.tab_3)
        self.uiHdaDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdaDiskImageToolButton.setObjectName("uiHdaDiskImageToolButton")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageToolButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.uiHdbDiskImageLabel = QtWidgets.QLabel(self.tab_3)
        self.uiHdbDiskImageLabel.setObjectName("uiHdbDiskImageLabel")
        self.gridLayout_6.addWidget(self.uiHdbDiskImageLabel, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiHdbDiskImageLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.uiHdbDiskImageLineEdit.setObjectName("uiHdbDiskImageLineEdit")
        self.horizontalLayout_4.addWidget(self.uiHdbDiskImageLineEdit)
        self.uiHdbDiskImageToolButton = QtWidgets.QToolButton(self.tab_3)
        self.uiHdbDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdbDiskImageToolButton.setObjectName("uiHdbDiskImageToolButton")
        self.horizontalLayout_4.addWidget(self.uiHdbDiskImageToolButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.uiHdcDiskImageLabel = QtWidgets.QLabel(self.tab_3)
        self.uiHdcDiskImageLabel.setObjectName("uiHdcDiskImageLabel")
        self.gridLayout_6.addWidget(self.uiHdcDiskImageLabel, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.uiHdcDiskImageLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.uiHdcDiskImageLineEdit.setObjectName("uiHdcDiskImageLineEdit")
        self.horizontalLayout_9.addWidget(self.uiHdcDiskImageLineEdit)
        self.uiHdcDiskImageToolButton = QtWidgets.QToolButton(self.tab_3)
        self.uiHdcDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdcDiskImageToolButton.setObjectName("uiHdcDiskImageToolButton")
        self.horizontalLayout_9.addWidget(self.uiHdcDiskImageToolButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_9, 2, 1, 1, 1)
        self.uiHddDiskImageLabel = QtWidgets.QLabel(self.tab_3)
        self.uiHddDiskImageLabel.setObjectName("uiHddDiskImageLabel")
        self.gridLayout_6.addWidget(self.uiHddDiskImageLabel, 3, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.uiHddDiskImageLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.uiHddDiskImageLineEdit.setObjectName("uiHddDiskImageLineEdit")
        self.horizontalLayout_10.addWidget(self.uiHddDiskImageLineEdit)
        self.uiHddDiskImageToolButton = QtWidgets.QToolButton(self.tab_3)
        self.uiHddDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHddDiskImageToolButton.setObjectName("uiHddDiskImageToolButton")
        self.horizontalLayout_10.addWidget(self.uiHddDiskImageToolButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(438, 257, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 4, 0, 1, 2)
        self.uiQemutabWidget.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiAdaptersLabel = QtWidgets.QLabel(self.tab_7)
        self.uiAdaptersLabel.setObjectName("uiAdaptersLabel")
        self.gridLayout_5.addWidget(self.uiAdaptersLabel, 0, 0, 1, 1)
        self.uiAdaptersSpinBox = QtWidgets.QSpinBox(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdaptersSpinBox.sizePolicy().hasHeightForWidth())
        self.uiAdaptersSpinBox.setSizePolicy(sizePolicy)
        self.uiAdaptersSpinBox.setMinimum(0)
        self.uiAdaptersSpinBox.setMaximum(32)
        self.uiAdaptersSpinBox.setObjectName("uiAdaptersSpinBox")
        self.gridLayout_5.addWidget(self.uiAdaptersSpinBox, 0, 1, 1, 1)
        self.uiAdapterTypesLabel = QtWidgets.QLabel(self.tab_7)
        self.uiAdapterTypesLabel.setObjectName("uiAdapterTypesLabel")
        self.gridLayout_5.addWidget(self.uiAdapterTypesLabel, 1, 0, 1, 1)
        self.uiAdapterTypesComboBox = QtWidgets.QComboBox(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdapterTypesComboBox.sizePolicy().hasHeightForWidth())
        self.uiAdapterTypesComboBox.setSizePolicy(sizePolicy)
        self.uiAdapterTypesComboBox.setObjectName("uiAdapterTypesComboBox")
        self.gridLayout_5.addWidget(self.uiAdapterTypesComboBox, 1, 1, 1, 1)
        self.uiLegacyNetworkingCheckBox = QtWidgets.QCheckBox(self.tab_7)
        self.uiLegacyNetworkingCheckBox.setObjectName("uiLegacyNetworkingCheckBox")
        self.gridLayout_5.addWidget(self.uiLegacyNetworkingCheckBox, 2, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 261, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 3, 1, 1, 1)
        self.uiQemutabWidget.addTab(self.tab_7, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiLinuxBootGroupBox = QtWidgets.QGroupBox(self.tab_2)
        self.uiLinuxBootGroupBox.setObjectName("uiLinuxBootGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiLinuxBootGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiKernelImageLineEdit = QtWidgets.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiKernelImageLineEdit.setObjectName("uiKernelImageLineEdit")
        self.gridLayout_2.addWidget(self.uiKernelImageLineEdit, 1, 1, 1, 1)
        self.uiKernelCommandLineLabel = QtWidgets.QLabel(self.uiLinuxBootGroupBox)
        self.uiKernelCommandLineLabel.setObjectName("uiKernelCommandLineLabel")
        self.gridLayout_2.addWidget(self.uiKernelCommandLineLabel, 2, 0, 1, 1)
        self.uiInitrdLabel = QtWidgets.QLabel(self.uiLinuxBootGroupBox)
        self.uiInitrdLabel.setObjectName("uiInitrdLabel")
        self.gridLayout_2.addWidget(self.uiInitrdLabel, 0, 0, 1, 1)
        self.uiKernelImageLabel = QtWidgets.QLabel(self.uiLinuxBootGroupBox)
        self.uiKernelImageLabel.setObjectName("uiKernelImageLabel")
        self.gridLayout_2.addWidget(self.uiKernelImageLabel, 1, 0, 1, 1)
        self.uiInitrdLineEdit = QtWidgets.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiInitrdLineEdit.setObjectName("uiInitrdLineEdit")
        self.gridLayout_2.addWidget(self.uiInitrdLineEdit, 0, 1, 1, 1)
        self.uiInitrdToolButton = QtWidgets.QToolButton(self.uiLinuxBootGroupBox)
        self.uiInitrdToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiInitrdToolButton.setObjectName("uiInitrdToolButton")
        self.gridLayout_2.addWidget(self.uiInitrdToolButton, 0, 2, 1, 1)
        self.uiKernelImageToolButton = QtWidgets.QToolButton(self.uiLinuxBootGroupBox)
        self.uiKernelImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiKernelImageToolButton.setObjectName("uiKernelImageToolButton")
        self.gridLayout_2.addWidget(self.uiKernelImageToolButton, 1, 2, 1, 1)
        self.uiKernelCommandLineEdit = QtWidgets.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiKernelCommandLineEdit.setObjectName("uiKernelCommandLineEdit")
        self.gridLayout_2.addWidget(self.uiKernelCommandLineEdit, 2, 1, 1, 2)
        self.verticalLayout_2.addWidget(self.uiLinuxBootGroupBox)
        self.uiOptimizationGroupBox = QtWidgets.QGroupBox(self.tab_2)
        self.uiOptimizationGroupBox.setObjectName("uiOptimizationGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiOptimizationGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiActivateCPUThrottlingCheckBox = QtWidgets.QCheckBox(self.uiOptimizationGroupBox)
        self.uiActivateCPUThrottlingCheckBox.setChecked(True)
        self.uiActivateCPUThrottlingCheckBox.setObjectName("uiActivateCPUThrottlingCheckBox")
        self.gridLayout.addWidget(self.uiActivateCPUThrottlingCheckBox, 0, 0, 1, 2)
        self.uiCPUThrottlingLabel = QtWidgets.QLabel(self.uiOptimizationGroupBox)
        self.uiCPUThrottlingLabel.setObjectName("uiCPUThrottlingLabel")
        self.gridLayout.addWidget(self.uiCPUThrottlingLabel, 1, 0, 1, 1)
        self.uiCPUThrottlingSpinBox = QtWidgets.QSpinBox(self.uiOptimizationGroupBox)
        self.uiCPUThrottlingSpinBox.setMinimum(1)
        self.uiCPUThrottlingSpinBox.setMaximum(800)
        self.uiCPUThrottlingSpinBox.setProperty("value", 100)
        self.uiCPUThrottlingSpinBox.setObjectName("uiCPUThrottlingSpinBox")
        self.gridLayout.addWidget(self.uiCPUThrottlingSpinBox, 1, 1, 1, 1)
        self.uiProcessPriorityLabel = QtWidgets.QLabel(self.uiOptimizationGroupBox)
        self.uiProcessPriorityLabel.setObjectName("uiProcessPriorityLabel")
        self.gridLayout.addWidget(self.uiProcessPriorityLabel, 2, 0, 1, 1)
        self.uiProcessPriorityComboBox = QtWidgets.QComboBox(self.uiOptimizationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiProcessPriorityComboBox.sizePolicy().hasHeightForWidth())
        self.uiProcessPriorityComboBox.setSizePolicy(sizePolicy)
        self.uiProcessPriorityComboBox.setObjectName("uiProcessPriorityComboBox")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.gridLayout.addWidget(self.uiProcessPriorityComboBox, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.uiOptimizationGroupBox)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiQemuOptionsLabel = QtWidgets.QLabel(self.groupBox)
        self.uiQemuOptionsLabel.setObjectName("uiQemuOptionsLabel")
        self.gridLayout_3.addWidget(self.uiQemuOptionsLabel, 0, 0, 1, 1)
        self.uiQemuOptionsLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiQemuOptionsLineEdit.setObjectName("uiQemuOptionsLineEdit")
        self.gridLayout_3.addWidget(self.uiQemuOptionsLineEdit, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.uiQemutabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.uiQemutabWidget)

        self.retranslateUi(QemuVMConfigPageWidget)
        self.uiQemutabWidget.setCurrentIndex(0)
        self.uiProcessPriorityComboBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(QemuVMConfigPageWidget)

    def retranslateUi(self, QemuVMConfigPageWidget):
        _translate = QtCore.QCoreApplication.translate
        QemuVMConfigPageWidget.setWindowTitle(_translate("QemuVMConfigPageWidget", "QEMU VM configuration"))
        self.uiQemuListLabel.setText(_translate("QemuVMConfigPageWidget", "Qemu binary:"))
        self.uiConsolePortLabel.setText(_translate("QemuVMConfigPageWidget", "Console port:"))
        self.uiNameLabel.setText(_translate("QemuVMConfigPageWidget", "VM name:"))
        self.uiRamLabel.setText(_translate("QemuVMConfigPageWidget", "RAM:"))
        self.uiRamSpinBox.setSuffix(_translate("QemuVMConfigPageWidget", " MB"))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.tab), _translate("QemuVMConfigPageWidget", "General settings"))
        self.uiHdaDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image (hda):"))
        self.uiHdaDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiHdbDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image (hdb):"))
        self.uiHdbDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiHdcDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image (hdc):"))
        self.uiHdcDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiHddDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image (hdd):"))
        self.uiHddDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.tab_3), _translate("QemuVMConfigPageWidget", "HDD"))
        self.uiAdaptersLabel.setText(_translate("QemuVMConfigPageWidget", "Adapters:"))
        self.uiAdapterTypesLabel.setText(_translate("QemuVMConfigPageWidget", "Type:"))
        self.uiLegacyNetworkingCheckBox.setText(_translate("QemuVMConfigPageWidget", "Use the legacy networking mode"))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.tab_7), _translate("QemuVMConfigPageWidget", "Network"))
        self.uiLinuxBootGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "Linux boot specific settings"))
        self.uiKernelCommandLineLabel.setText(_translate("QemuVMConfigPageWidget", "Kernel command line:"))
        self.uiInitrdLabel.setText(_translate("QemuVMConfigPageWidget", "Initial RAM disk (initrd):"))
        self.uiKernelImageLabel.setText(_translate("QemuVMConfigPageWidget", "Kernel image:"))
        self.uiInitrdToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiKernelImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiOptimizationGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "Optimizations"))
        self.uiActivateCPUThrottlingCheckBox.setText(_translate("QemuVMConfigPageWidget", "Activate CPU throttling"))
        self.uiCPUThrottlingLabel.setText(_translate("QemuVMConfigPageWidget", "Percentage of CPU allowed:"))
        self.uiCPUThrottlingSpinBox.setSuffix(_translate("QemuVMConfigPageWidget", " %"))
        self.uiProcessPriorityLabel.setText(_translate("QemuVMConfigPageWidget", "Process priority:"))
        self.uiProcessPriorityComboBox.setItemText(0, _translate("QemuVMConfigPageWidget", "Realtime"))
        self.uiProcessPriorityComboBox.setItemText(1, _translate("QemuVMConfigPageWidget", "Very high"))
        self.uiProcessPriorityComboBox.setItemText(2, _translate("QemuVMConfigPageWidget", "High"))
        self.uiProcessPriorityComboBox.setItemText(3, _translate("QemuVMConfigPageWidget", "Normal"))
        self.uiProcessPriorityComboBox.setItemText(4, _translate("QemuVMConfigPageWidget", "Low"))
        self.uiProcessPriorityComboBox.setItemText(5, _translate("QemuVMConfigPageWidget", "Very low"))
        self.groupBox.setTitle(_translate("QemuVMConfigPageWidget", "Aditional settings"))
        self.uiQemuOptionsLabel.setText(_translate("QemuVMConfigPageWidget", "Options:"))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.tab_2), _translate("QemuVMConfigPageWidget", "Advanced settings"))
