# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Wizard for IOU devices.
"""

import os
import sys

from gns3.qt import QtGui, QtCore
from gns3.node import Node
from gns3.servers import Servers
from gns3.utils.get_resource import get_resource
from gns3.utils.get_default_base_config import get_default_base_config
from gns3.device_wizard import DeviceWizard

from ..ui.iou_device_wizard_ui import Ui_IOUDeviceWizard
from .. import IOU


class IOUDeviceWizard(DeviceWizard, Ui_IOUDeviceWizard):

    """
    Wizard to create an IOU device.

    :param parent: parent widget
    """

    def __init__(self, iou_devices, parent):

        super().__init__(parent)
        self.setPixmap(QtGui.QWizard.LogoPixmap, QtGui.QPixmap(":/symbols/multilayer_switch.normal.svg"))

        self.uiTypeComboBox.currentIndexChanged[str].connect(self._typeChangedSlot)

        if sys.platform.startswith("win") or sys.platform.startswith("darwin"):
            # Cannot use IOU locally on Windows and Mac
            self.uiLocalRadioButton.setEnabled(False)

        # Available types
        self.uiTypeComboBox.addItems(["L2 image", "L3 image"])

        # Mandatory fields
        self.uiNameImageWizardPage.registerField("name*", self.uiNameLineEdit)
        self.uiNameImageWizardPage.registerField("image*", self.uiIOUImageLineEdit)

        self._iou_devices = iou_devices

        if IOU.instance().settings()["use_local_server"]:
            # skip the server page if we use the local server
            self.uiLocalRadioButton.setEnabled(True)
            self.setStartId(1)

        self.uiIOUImageLineEdit.textChanged.connect(self._imageLineEditTextChangedSlot)

        # location of the base config templates
        self._base_iou_l2_config_template = get_resource(os.path.join("configs", "iou_l2_base_initial-config.txt"))
        self._base_iou_l3_config_template = get_resource(os.path.join("configs", "iou_l3_base_initial-config.txt"))

        from ..pages.iou_device_preferences_page import IOUDevicePreferencesPage
        self.addImageSelector(self.uiExistingImageRadioButton, self.uiIOUImageListComboBox, self.uiIOUImageLineEdit, self.uiIOUImageToolButton, IOUDevicePreferencesPage.getIOUImage)

    def _imageLineEditTextChangedSlot(self, text):
        """
        Set image type depending of user choice
        """

        if "l2" in text:
            self.uiTypeComboBox.setCurrentIndex(0)  # L2 image
        elif "l3" in text:
            self.uiTypeComboBox.setCurrentIndex(1)  # L3 image

    def _typeChangedSlot(self, image_type):
        """
        When the type of IOU device is changed.

        :param image_type: type of image (L2 or L3)
        """

        if image_type == "L2 image":
            #  L2 image
            self.setPixmap(QtGui.QWizard.LogoPixmap, QtGui.QPixmap(":/symbols/multilayer_switch.normal.svg"))
        else:
            #  L3 image
            self.setPixmap(QtGui.QWizard.LogoPixmap, QtGui.QPixmap(":/symbols/router.normal.svg"))

    def initializePage(self, page_id):

        super().initializePage(page_id)
        if self.page(page_id) == self.uiServerWizardPage:
            self.uiRemoteServersComboBox.clear()
            for server in Servers.instance().remoteServers().values():
                self.uiRemoteServersComboBox.addItem("{}:{}".format(server.host, server.port), server)
        if self.page(page_id) == self.uiNameImageWizardPage:
            if not self.uiLocalRadioButton.isChecked():
                QtGui.QMessageBox.warning(self, "IOU image", "You have chosen to use a remote server, please provide the path to an IOU image located on this server!")
            self.loadImagesList("/iou/vms")

    def validateCurrentPage(self):
        """
        Validates the server.
        """

        if super().validateCurrentPage() is False:
            return False

        if self.currentPage() == self.uiNameImageWizardPage:
            name = self.uiNameLineEdit.text()
            for iou_device in self._iou_devices.values():
                if iou_device["name"] == name:
                    QtGui.QMessageBox.critical(self, "Name", "{} is already used, please choose another name".format(name))
                    return False
        if self.currentPage() == self.uiServerWizardPage:
            if self.uiRemoteRadioButton.isChecked():
                if not Servers.instance().remoteServers():
                    QtGui.QMessageBox.critical(self, "Remote server", "There is no remote server registered in IOS on UNIX preferences")
                    return False
                self._server = self.uiRemoteServersComboBox.itemData(self.uiRemoteServersComboBox.currentIndex())
            else:
                self._server = Servers.instance().localServer()
        return True

    def getSettings(self):
        """
        Returns the settings set in this Wizard.

        :return: settings dict
        """

        path = self.uiIOUImageLineEdit.text()

        initial_config = ""
        if self.uiTypeComboBox.currentText() == "L2 image":
            # set the default L2 base initial-config
            default_base_config = get_default_base_config(self._base_iou_l2_config_template)
            if default_base_config:
                initial_config = default_base_config
            default_symbol = ":/symbols/multilayer_switch.normal.svg"
            hover_symbol = ":/symbols/multilayer_switch.selected.svg"
            category = Node.switches
            ethernet_adapters = 4
            serial_adapters = 0
        else:
            # set the default L3 base initial-config
            default_base_config = get_default_base_config(self._base_iou_l3_config_template)
            if default_base_config:
                initial_config = default_base_config
            default_symbol = ":/symbols/router.normal.svg"
            hover_symbol = ":/symbols/router.selected.svg"
            category = Node.routers
            ethernet_adapters = 2
            serial_adapters = 2

        if self.uiLocalRadioButton.isChecked():
            server = "local"
        elif self.uiRemoteRadioButton.isChecked():
            if self.uiLoadBalanceCheckBox.isChecked():
                server = next(iter(Servers.instance()))
                server = "{}:{}".format(server.host, server.port)
            else:
                server = self.uiRemoteServersComboBox.currentText()
        else:  # Cloud is selected
            server = "cloud"

        settings = {
            "name": self.uiNameLineEdit.text(),
            "path": path,
            "image": os.path.basename(path),
            "initial_config": initial_config,
            "ethernet_adapters": ethernet_adapters,
            "serial_adapters": serial_adapters,
            "default_symbol": default_symbol,
            "category": category,
            "hover_symbol": hover_symbol,
            "server": server,
        }

        return settings
