# coding: latin1

#Copyright (c) <2013>, <Kari Aliranta, Jaakko Lepp�kangas, Janne Pesonen and Atte Rautio>
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met: 
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer. 
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution. 
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The views and conclusions contained in the software and documentation are those
#of the authors and should not be interpreted as representing official policies, 
#either expressed or implied, of the FreeBSD Project.

"""
@author: Kari Aliranta, Jaakko Leppakangas
Contains the CreateExperimentDialog-class that holds the logic for
CreateExperimentDialog-window.
"""

from fileManager import FileManager
from infoDialogMain import InfoDialog
import messageBox

from experiment import Experiment
from workspace import Workspace

from infoDialogUi import Ui_infoDialog
from createExperimentDialogUi import Ui_CreateExperimentDialog

from PyQt4 import QtCore, QtGui 

import os, sys
import StringIO
import pickle
import time
import ConfigParser

class CreateExperimentDialog(QtGui.QDialog):
    """
    Class containing the logic for CreateExperimentDialog. It is used for 
    setting up a new experiment for analyzing MEG data.
    """
    fname = ''
    
    def __init__(self, parent):
        QtGui.QDialog.__init__(self)
        self.fname = ''
        
        # Reference to main dialog window
        self.parent = parent
        
        # Refers to class in file CreateProjecDialog
        self.ui = Ui_CreateExperimentDialog() 
        self.ui.setupUi(self)
        #self.ui.showFileInfoButton.setEnabled(False)
        
        #self.ui.FilePathLineEdit.textChanged.connect(self.file_path_changed)
                
    def accept(self):
        """Create the new experiment.
        """
        self.parent.hide_workspace_option()
        self._initialize_experiment()
        
    def file_path_changed(self):
        """A slot for enabling or disabling show file info button.
        """
        if self.ui.FilePathLineEdit.text() == '':
            self.ui.showFileInfoButton.setEnabled(False)
            
        else: self.ui.showFileInfoButton.setEnabled(True)
        
                
    def on_browseButton_clicked(self, checked=None):
        """
        Opens a browse dialog to select the raw data.
        """
        # Standard workaround for file dialog opening twice
        if checked is None: return
        
        self.fname = str(QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                           '/home/'))
      
        
        if self.fname != '':        
            self.ui.FilePathLineEdit.setText(self.fname)        
        
    def on_showFileInfoButton_clicked(self, checked = None):
        """
        Opens the infoDialog for the raw file selected.
        """
        try:
            f = FileManager()
            self.raw = f.open_raw(self.fname, pre_load = False)
            self.ui.showFileInfoButton.setEnabled(True)
            
        except IOError as e:
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText(str(e))
            self.messageBox.show()
            return
        
        except OSError as e:
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText(str(e))
            self.messageBox.show()
            return
        
        except ValueError as e:
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText(str(e))
            self.messageBox.show()
            return
            
        info = Ui_infoDialog()
        self.infoDialog = InfoDialog(self.raw, info, True)
        self.infoDialog.show()

        QtGui.QApplication.processEvents() 
        
    def _initialize_experiment(self):
        """
        Initializes the experiment object with the given data.
        """
        if self.ui.lineEditExperimentName.text() == '':
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText('Give experiment a name.')
            self.messageBox.show()
            return          
   
        try:
            self.workspace = Workspace()
            self.experiment = Experiment()
            self.experiment.author = self.ui.lineEditAuthor.text()
            self.experiment.experiment_name = self.ui.\
            lineEditExperimentName.text()
            self.experiment.description = (self.ui.textEditDescription.
                                           toPlainText())
            self.experiment.subject_paths = []

        except AttributeError:
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText('Cannot assign attribute' + 
                                                   ' to experiment.')
            self.messageBox.show()
        try:
            self.experiment.workspace = self.workspace.working_directory
            print self.experiment.workspace
        except Exception, err:
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText(str(err))
            self.messageBox.show()
            return
        
        QtGui.QApplication.processEvents()
                
        # Give control of the experiment to the main window of the application
        self.parent.experiment = self.experiment
        
        self.parent.ui.labelExperimentName.setText(self.experiment.
                                                   experiment_name)
        
        self.parent.ui.labelAuthorName.setText(self.experiment.author)
        self.parent.ui.textBrowserExperimentDescription.setText(self.
                                                                experiment.
                                                                description)
        try:
            self.experiment.save_experiment_settings()
        except Exception, err:
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText(str(err))
            self.messageBox.show()
            return
            
        self.close()
        self.parent.add_tabs()
        self.parent._initialize_ui() 
          
class OutLog:
    def __init__(self, edit, out=None, color=None):
        
        #(edit, out=None, color=None) -> can write stdout, stderr to a
        #QTextEdit.
        #edit = QTextEdit
        #out = alternate stream ( can be the original sys.stdout )
        #color = alternate color (i.e. color stderr a different color)
        
        self.edit = edit
        self.out = None
        self.color = color

    def write(self, m):
        if self.color:
            tc = self.edit.textColor()
            self.edit.setTextColor(self.color)

        self.edit.moveCursor(QtGui.QTextCursor.End)
        self.edit.insertPlainText(m)

        if self.color:
            self.edit.setTextColor(tc)

        if self.out:
            self.out.write(m)
            