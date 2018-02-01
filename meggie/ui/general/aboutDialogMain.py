# coding: utf-8

"""
Created on Apr 29, 2013

@author: Janne Pesonen
Contains the PreferencesDialog-class used in setting the preferences for
the application.
"""

from PyQt4 import QtCore, QtGui
from meggie.ui.general.aboutDialogUi import Ui_Dialog


class AboutDialog(QtGui.QDialog):
    """
    Dialog to set the preferences for the application. Only allows choosing the
    calibration file for the experiment.
    """

    def __init__(self):
        """
        Constructor
        """
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        
    def on_pushButtonClose_clicked(self, checked=None):
        if checked is None: return
        self.close()
