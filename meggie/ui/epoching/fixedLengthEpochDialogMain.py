'''
Created on 10.9.2015

@author: Jaakko Leppakangas
'''
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialogButtonBox

from mne import make_fixed_length_events

from meggie.code_meggie.general.caller import Caller
from meggie.ui.epoching.fixedLengthEpochsDialogUi import Ui_FixedLengthEpochDialog

class FixedLengthEpochDialog(QtGui.QDialog):
    """
    Class containing the logic for FixedLengthEpochDialog. It is used for
    creating fixed length events.
    """
    #fixed_events_ready = QtCore.pyqtSignal(list, str)
    caller = Caller.Instance()

    def __init__(self, parent):
        """Initialize the event selection dialog.

        Keyword arguments:

        parent -- Set the parent of this dialog
        """
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_FixedLengthEpochDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText('Add events')
        #self.caller = Caller.Instance()
        self.raw = self.caller.experiment.active_subject.working_file
        tmax = int(self.raw.times[-1])
        self.ui.spinBoxStart.setMaximum(tmax)
        self.ui.spinBoxEnd.setMaximum(tmax)
        self.ui.spinBoxEnd.setValue(tmax)

    def accept(self, *args, **kwargs):
        event_params = {
            'tmin': self.ui.spinBoxStart.value(),
            'tmax': self.ui.spinBoxEnd.value(),
            'interval': self.ui.doubleSpinBoxInterval.value(),
            'event_id': self.ui.spinBoxId.value(),
            'event_name': str(self.ui.lineEditName.text())
        }
        events = make_fixed_length_events(
            self.caller.experiment.active_subject.working_file,
            event_params['event_id'], event_params['tmin'],
            event_params['tmax'], event_params['interval']
        )
        if len(events) > 0:
            self.parent.batching_widget.data[self.caller.experiment.active_subject.subject_name]['fixed_length_events'].append(event_params)
            self.parent.update_events()
        return QtGui.QDialog.accept(self, *args, **kwargs)
