"""
"""

from PyQt5 import QtWidgets

from meggie.ui.source_analysis.lcmvDialogUi import Ui_lcmvDialog  # noqa

from meggie.code_meggie.general.source_analysis import create_lcmv_estimate

from meggie.code_meggie.utils.validators import validate_name

from meggie.ui.utils.messaging import exc_messagebox
from meggie.ui.utils.messaging import messagebox
from meggie.ui.utils.decorators import threaded

import meggie.code_meggie.general.mne_wrapper as mne


class LCMVDialog(QtWidgets.QDialog):
    """
    """

    def __init__(self, parent, fwd_name, inst_type,
                 inst_name, experiment=None, on_close=None):
        QtWidgets.QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_lcmvDialog()
        self.ui.setupUi(self)
        self.on_close = on_close
        self.experiment = experiment
        self.fwd_name = fwd_name
        self.inst_type = inst_type
        self.inst_name = inst_name

        if inst_type == 'raw':
            self.ui.groupBoxTimeParameters.setEnabled(True)
            self.ui.doubleSpinBoxStart.setEnabled(True)
            self.ui.doubleSpinBoxEnd.setEnabled(True)
            raw = self.experiment.active_subject.get_working_file(
                preload=False)
            self.ui.doubleSpinBoxStart.setValue(raw.times[0])
            self.ui.doubleSpinBoxEnd.setValue(raw.times[-1])

        self.ui.lineEditBasedOn.setText(fwd_name)
        self.ui.lineEditData.setText(inst_name)

        # temporarily removed
        # self.populate_labels()

        self.populate_covariances()

    def read_labels(self):
        active_subject = self.experiment.active_subject

        subject = active_subject.mri_subject_name
        subjects_dir = active_subject.source_analysis_directory

        labels = mne.read_labels_from_annot(subject=subject, parc='aparc',
                                            subjects_dir=subjects_dir)
        return labels

    def populate_labels(self):
        labels = self.read_labels()

        self.ui.comboBoxLabel.clear()
        self.ui.comboBoxLabel.addItem('None')
        for label in labels:
            self.ui.comboBoxLabel.addItem(label.name)

        self.ui.comboBoxLabel.setCurrentIndex(0)

    def populate_covariances(self):
        active_subject = self.experiment.active_subject

        covariances = active_subject.get_covfiles()
        self.ui.comboBoxNoiseCovariance.clear()
        self.ui.comboBoxDataCovariance.clear()
        for covariance in covariances:
            self.ui.comboBoxNoiseCovariance.addItem(covariance)
            self.ui.comboBoxDataCovariance.addItem(covariance)
        self.ui.comboBoxNoiseCovariance.setCurrentIndex(0)
        self.ui.comboBoxDataCovariance.setCurrentIndex(0)

    def accept(self):
        """
        """

        # collect parameters
        try:
            stc_name = validate_name(
                str(self.ui.lineEditSourceEstimateName.text()))
        except Exception as exc:
            exc_messagebox(self, exc, exec_=True)
            return

        if not stc_name:
            messagebox(self, "Please give a name for the source estimate",
                       exec_=True)
            return

        if stc_name in self.experiment.active_subject.stcs:
            messagebox(self, "Source estimate with this name already exists",
                       exec_=True)
            return

        fwd_name = self.fwd_name
        inst_name = self.inst_name
        inst_type = self.inst_type

        reg = float(self.ui.doubleSpinBoxReg.value())
        data_covfile = str(self.ui.comboBoxDataCovariance.currentText())
        noise_covfile = str(self.ui.comboBoxNoiseCovariance.currentText())

        start = float(self.ui.doubleSpinBoxStart.value())
        end = float(self.ui.doubleSpinBoxEnd.value())

        if inst_type == 'raw':
            start, end = None, None

        # label = str(self.ui.comboBoxLabel.currentText())
        # if label == 'None':
        #     label = None
        # else:
        #     labels = self.read_labels()
        #     label = [lbl for lbl in labels if lbl.name == label][0]
        label = None

        subject = self.experiment.active_subject

        @threaded
        def lcmv_stc(*args, **kwargs):
            create_lcmv_estimate(*args, **kwargs)

        try:
            update_ui = self.parent.parent.update_ui
            lcmv_stc(self.experiment, stc_name, inst_name, inst_type,
                     data_covfile, noise_covfile, fwd_name, label,
                     reg, start, end, do_meanwhile=update_ui)
        except Exception as exc:
            exc_messagebox(self.parent, exc, exec_=True)

        # call close handler
        if self.on_close:
            self.on_close()

        self.close()
