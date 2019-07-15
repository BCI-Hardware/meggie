# coding: utf-8

"""
"""

from meggie.code_meggie.utils.units import get_unit
from meggie.code_meggie.general import fileManager
from meggie.code_meggie.general.preferences import PreferencesHandler
from meggie.code_meggie.general.experiment import Experiment
from meggie.code_meggie.general.experiment import ExperimentHandler
from meggie.ui.general.tabs.mainWindowTabSourceAnalysisMain import MainWindowTabSourceAnalysis
from meggie.ui.general.tabs.mainWindowTabInducedMain import MainWindowTabInduced
from meggie.ui.general.tabs.mainWindowTabEvokedMain import MainWindowTabEvoked
from meggie.ui.general.tabs.mainWindowTabEpochsMain import MainWindowTabEpochs
from meggie.ui.general.tabs.mainWindowTabSpectrumsMain import MainWindowTabSpectrums
from meggie.ui.general.tabs.mainWindowTabPreprocessingMain import MainWindowTabPreprocessing
from meggie.ui.utils.decorators import threaded
from meggie.ui.utils.messaging import messagebox
from meggie.ui.utils.messaging import exc_messagebox
from meggie.ui.general.logDialogMain import LogDialog
from meggie.ui.general.experimentInfoDialogMain import ExperimentInfoDialog
from meggie.ui.general.aboutDialogMain import AboutDialog
from meggie.ui.general.preferencesDialogMain import PreferencesDialog
from meggie.ui.general.infoDialogMain import InfoDialog
from meggie.ui.general.layoutDialogMain import LayoutDialog
from meggie.ui.general.addSubjectDialogMain import AddSubjectDialog
from meggie.ui.general.createExperimentDialogMain import CreateExperimentDialog
from meggie.ui.general.mainWindowUi import Ui_MainWindow
from meggie.ui.icons import mainWindowIcons_rc
import meggie.code_meggie.general.mne_wrapper as mne
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import os
import sys
import warnings
import gc
import logging

import matplotlib
matplotlib.use('Qt5Agg')


class MainWindow(QtWidgets.QMainWindow):
    """
    Class containing the logic for the MainWindow
    """

    def __init__(self, application):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.experiment = None

        self.setup_loggers()

        # Direct output to console
        if 'debug' not in sys.argv:
            self.ui.actionDirectToConsole.triggered.connect(self.directOutput)
            self.directOutput()

        # For storing and handling program wide prefences.
        self.preferencesHandler = PreferencesHandler()
        self.preferencesHandler.set_env_variables()

        # For handling initialization and switching of experiments.
        self.experimentHandler = ExperimentHandler(self)

        self.tabs = []
        import pkg_resources, json
        config_path = pkg_resources.resource_filename(
            'meggie', 'configuration.json')
        with open(config_path, 'r') as f:
            tab_config = json.load(f)

        def construct_tab(tab_spec):

            class DynamicTab(QtWidgets.QDialog):
                def __init__(self, parent):
                    QtWidgets.QDialog.__init__(self)
                    self.parent = parent
                    self.name = tab_spec["name"]

                    # first create basic layout

                    self.gridLayoutContainer = QtWidgets.QGridLayout(self)

                    self.gridLayoutRoot = QtWidgets.QGridLayout()
                    self.gridLayoutContainer.addLayout(self.gridLayoutRoot, 0, 0, 1, 1)

                    if tab_spec.get('outputs'):
                        self.groupBoxOutputs = QtWidgets.QGroupBox(self)
                        self.groupBoxOutputs.setTitle('Outputs')
                        self.gridLayoutOutputs = QtWidgets.QGridLayout(self.groupBoxOutputs)

                    if tab_spec.get('actions'):
                        self.groupBoxActions = QtWidgets.QGroupBox(self)
                        self.groupBoxActions.setTitle('Actions')
                        self.gridLayoutActions = QtWidgets.QGridLayout(self.groupBoxActions)

                    if tab_spec.get('transforms'):
                        self.groupBoxTransforms = QtWidgets.QGroupBox(self)
                        self.groupBoxTransforms.setTitle('Transforms')
                        self.gridLayoutTransforms = QtWidgets.QGridLayout(self.groupBoxTransforms)
                        
                    if tab_spec.get('inputs'):
                        self.groupBoxInputs = QtWidgets.QGroupBox(self)
                        self.groupBoxInputs.setTitle('Inputs')
                        self.gridLayoutInputs = QtWidgets.QGridLayout(self.groupBoxInputs)


                    # then fill the contents

                    for idx, input_item in enumerate(tab_spec.get('inputs', [])):
                        groupBoxInputElement = QtWidgets.QGroupBox(self.groupBoxInputs)
                        groupBoxInputElement.setTitle(input_item.capitalize())
                        gridLayoutInputElement = QtWidgets.QGridLayout(groupBoxInputElement)
                        listWidgetInputElement = QtWidgets.QListWidget(groupBoxInputElement)

                        gridLayoutInputElement.addWidget(listWidgetInputElement, idx, 0, 1, 1)
                        self.gridLayoutInputs.addWidget(groupBoxInputElement)

                        setattr(self, 'groupBoxInputElement_' + str(idx+1), 
                                groupBoxInputElement)
                        setattr(self, 'gridLayoutInputElement_' + str(idx+1), 
                                gridLayoutInputElement)
                        setattr(self, 'listWidgetInputElement_' + str(idx+1), 
                                listWidgetInputElement)

                    for idx, output_item in enumerate(tab_spec.get('outputs', [])):
                        groupBoxOutputElement = QtWidgets.QGroupBox(self.groupBoxOutputs)
                        groupBoxOutputElement.setTitle(output_item.capitalize())
                        gridLayoutOutputElement = QtWidgets.QGridLayout(groupBoxOutputElement)
                        listWidgetOutputElement = QtWidgets.QListWidget(groupBoxOutputElement)

                        gridLayoutOutputElement.addWidget(listWidgetOutputElement, idx, 0, 1, 1)
                        self.gridLayoutOutputs.addWidget(groupBoxOutputElement)

                        setattr(self, 'groupBoxOutputElement_' + str(idx+1), 
                                groupBoxOutputElement)
                        setattr(self, 'gridLayoutOutputElement_' + str(idx+1), 
                                gridLayoutOutputElement)
                        setattr(self, 'listWidgetOutputElement_' + str(idx+1), 
                                listWidgetOutputElement)

                    for idx, transform_item in enumerate(tab_spec.get('transforms', [])):
                        pushButtonTransformElement = QtWidgets.QPushButton(self.groupBoxTransforms)
                        pushButtonTransformElement.setText(transform_item.capitalize())
                        self.gridLayoutTransforms.addWidget(pushButtonTransformElement, idx, 0, 1, 1)
                        setattr(self, 'pushButtonTransformElement_' + str(idx+1), 
                                pushButtonTransformElement)

                    for idx, action_item in enumerate(tab_spec.get('actions', [])):
                        pushButtonActionElement = QtWidgets.QPushButton(self.groupBoxActions)
                        pushButtonActionElement.setText(action_item.capitalize())
                        self.gridLayoutActions.addWidget(pushButtonActionElement, idx, 0, 1, 1)
                        setattr(self, 'pushButtonActionElement_' + str(idx+1), 
                                pushButtonActionElement)

                    if tab_spec.get('inputs') and not tab_spec.get('transforms'):
                        self.gridLayoutRoot.addWidget(self.groupBoxInputs, 0, 0, 2, 1)
                    elif tab_spec.get('inputs'):
                        self.gridLayoutRoot.addWidget(self.groupBoxInputs, 0, 0, 1, 1)

                    if tab_spec.get('outputs') and not tab_spec.get('actions'):
                        self.gridLayoutRoot.addWidget(self.groupBoxOutputs, 0, 1, 2, 1)
                    elif tab_spec.get('outputs'):
                        self.gridLayoutRoot.addWidget(self.groupBoxOutputs, 0, 1, 1, 1)

                    if tab_spec.get('transforms') and not tab_spec.get('inputs'):
                        self.gridLayoutRoot.addWidget(self.groupBoxTransforms, 0, 0, 2, 1)
                    elif tab_spec.get('transforms'):
                        self.gridLayoutRoot.addWidget(self.groupBoxTransforms, 1, 0, 1, 1)

                    if tab_spec.get('actions') and not tab_spec.get('outputs'):
                        self.gridLayoutRoot.addWidget(self.groupBoxActions, 0, 1, 2, 1)
                    elif tab_spec.get('actions'):
                        self.gridLayoutRoot.addWidget(self.groupBoxActions, 1, 1, 1, 1)

                    spacerItemVertical = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                    self.gridLayoutContainer.addItem(spacerItemVertical, 1, 0, 1, 1)
                    spacerItemHorizontal = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                    self.gridLayoutContainer.addItem(spacerItemHorizontal, 0, 1, 1, 1)


                def initialize_ui(self):
                    pass

            DynamicTab.__name__ = 'MainWindowTab' + tab_spec['id'].capitalize()

            tab = DynamicTab(self)

            return tab

        for tab_spec in tab_config['tabs']:
            tab = construct_tab(tab_spec)
            self.tabs.append(tab)

        # Create the tab contents
        # self.mainWindowTabPreprocessing = MainWindowTabPreprocessing(self)
        # self.mainWindowTabSpectrums = MainWindowTabSpectrums(self)
        # self.mainWindowTabEpochs = MainWindowTabEpochs(self)
        # self.mainWindowTabEvoked = MainWindowTabEvoked(self)
        # self.mainWindowTabSourceAnalysis = MainWindowTabSourceAnalysis(self)
        # self.mainWindowTabInduced = MainWindowTabInduced(self)

        # Creates a label on status bar to show current working file message.
        self.statusLabel = QtWidgets.QLabel()
        self.ui.statusbar.addWidget(self.statusLabel)

        # If the user has chosen to open the previous experiment automatically.
        if self.preferencesHandler.auto_load_last_open_experiment:
            exp = None

            try:
                exp = self.experimentHandler.open_existing_experiment(
                    self.preferencesHandler)
            except Exception as e:
                exc_messagebox(self, e)

            if exp:
                self.experiment = exp
                self.initialize_ui()
            else:
                self.preferencesHandler.previous_experiment_name = ''
                self.preferencesHandler.write_preferences_to_disk()

    def on_actionQuit_triggered(self, checked=None):
        """Closes the program, possibly after a confirmation by the user."""
        if checked is None:
            return

        if self.preferencesHandler.confirm_quit:
            reply = QtWidgets.QMessageBox.question(self, 'Close Meggie',
                                                   'Are you sure you want to quit Meggie?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.close()
        else:
            self.close()

    def on_actionCreate_experiment_triggered(self, checked=None):
        """Create a new CreateExperimentDialog and show it"""
        if checked is None:
            return

        if self.preferencesHandler.working_directory != '':
            self.dialog = CreateExperimentDialog(self)
            self.dialog.experimentCreated.connect(self.setExperiment)
            self.dialog.show()
        else:
            self.check_workspace()
            if self.preferencesHandler.working_directory != '':
                self.dialog = CreateExperimentDialog(self)
                self.dialog.experimentCreated.connect(self.setExperiment)
                self.dialog.show()

    def on_actionOpen_experiment_triggered(self, checked=None):
        """ Open an existing _experiment. """

        if checked is None:
            return

        if self.experiment is not None:
            directory = self.experiment.workspace
        else:
            directory = ''

        path = QtCore.QDir.toNativeSeparators(
            str(QtWidgets.QFileDialog.getExistingDirectory(self,
                                                           "Select experiment directory", directory)))

        if path == '':
            return

        logging.getLogger('ui_logger').info('Opening experiment ' + path)

        try:
            exp = self.experimentHandler.open_existing_experiment(
                self.preferencesHandler, path=path)
            self.experiment = exp
            self.initialize_ui()
        except Exception as e:
            exc_messagebox(self, e)

        # Saves at least the previous experiment name
        self.preferencesHandler.write_preferences_to_disk()

    def on_pushButtonAddSubjects_clicked(self, checked=None):
        """Open subject dialog."""

        if checked is None:
            return

        # Check that we have an experiment that we can add a subject to
        if self.experiment is None:
            msg = ('No active experiment to add a subject to. Load an '
                   'experiment or make a new one, then try again.')
            messagebox(self, msg)
            return

        self.subject_dialog = AddSubjectDialog(self)
        self.subject_dialog.exec_()

    def on_pushButtonRemoveSubject_clicked(self, checked=None):
        """Delete the selected subject item and the files related to it."""
        if checked is None:
            return

        selIndexes = self.ui.listWidgetSubjects.selectedIndexes()

        if selIndexes == []:
            return

        message = 'Permanently remove the selected subjects and the related files?'
        reply = QtWidgets.QMessageBox.question(self, 'Delete selected subjects',
                                               message, QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        failures = []
        if reply == QtWidgets.QMessageBox.Yes:
            for index in selIndexes:
                subject_name = index.data()

                try:
                    self.experiment.remove_subject(subject_name, self)
                except Exception:
                    failures.append(subject_name)

        if failures:
            msg = ''.join(['Could not remove the contents of the subject ',
                           'folder for following subjects: ',
                           '\n'.join(failures)])
            messagebox(self, msg)

        self.experiment.save_experiment_settings()
        self.initialize_ui()

    def closeEvent(self, event):
        """Redefine window close event to allow confirming on quit."""

        if self.preferencesHandler.confirm_quit:
            reply = QtWidgets.QMessageBox.question(self, 'Close Meggie',
                                                   'Are you sure you want to '
                                                   'quit?', QtWidgets.QMessageBox.Yes |
                                                   QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def on_actionSet_workspace_triggered(self, checked=None):
        """
        Open the preferences dialog the for specific purpose of initial setting
        of workspace.
        """
        if checked is None:
            return

        self.check_workspace()

    def on_actionShow_log_triggered(self, checked=None):
        if checked is None:
            return

        if self.experiment is None:
            message = 'Please open an experiment first.'
            messagebox(self, message)
            return

        self.log_dialog = LogDialog(self)
        self.log_dialog.show()

    def on_actionPreferences_triggered(self, checked=None):
        """Open the preferences-dialog."""
        if checked is None:
            return

        self.dialogPreferences = PreferencesDialog(self)
        self.dialogPreferences.show()

    def on_actionAbout_triggered(self, checked=None):
        """Open the About-dialog."""
        if checked is None:
            return

        self.dialogAbout = AboutDialog()
        self.dialogAbout.show()

    def on_actionShowExperimentInfo_triggered(self, checked=None):
        """Open the experiment info dialog """
        if checked is None:
            return
        if self.experiment is None:
            messagebox(self, 'You do not currently have an experiment activated.')  # noqa
            return

        self.expInfoDialog = ExperimentInfoDialog(self)
        self.expInfoDialog.show()

    def on_actionHide_Show_subject_list_and_info_triggered(self, checked=None):
        if checked is None:
            return
        if self.ui.dockWidgetSubjects.isVisible():
            self.ui.dockWidgetSubjects.hide()
        else:
            self.ui.dockWidgetSubjects.show()

    def on_pushButtonLayout_clicked(self, checked=None):
        if checked is None:
            return

        if not self.experiment:
            return

        self.layoutDialog = LayoutDialog(self)
        self.layoutDialog.show()

    def on_pushButtonActivateSubject_clicked(self, checked=None):
        """
        Activates a subject.
        """
        if checked is None:
            return

        if self.ui.listWidgetSubjects.selectedIndexes() == []:
            return

        selIndexes = self.ui.listWidgetSubjects.selectedIndexes()

        if len(selIndexes) > 1:
            return

        subject_name = selIndexes[0].data()

        if self.experiment.active_subject:
            if subject_name == self.experiment.active_subject.subject_name:
                return

        previous_subject = self.experiment.active_subject
        try:
            @threaded
            def activate(subject_name):
                self.experiment.activate_subject(subject_name)
            activate(subject_name, do_meanwhile=self.update_ui)

        except Exception as e:
            self.experiment.active_subject = None
            exc_messagebox(self, "Couldn't activate the subject.")
            if previous_subject:
                message = "Couldn't activate the subject, resuming to previous one."
                logging.getLogger('ui_logger').info(message)
                self.experiment.activate_subject(previous_subject.subject_name)

        self.initialize_ui()

    def get_epochs(self, epoch_name):
        experiment = self.experiment
        if not experiment:
            return

        active_subject = experiment.active_subject
        if not active_subject:
            return

        return active_subject.epochs.get(epoch_name)

    def update_ui(self):
        """
        Method for repainting the ui.
        Used for keeping the ui responsive when threading.
        """
        QApplication.processEvents()

    @QtCore.pyqtSlot(Experiment)
    def setExperiment(self, newExperiment):
        """Temporary setter for experiment."""
        self.experiment = newExperiment
        gc.collect()

        self.initialize_ui()

    def initialize_ui(self):
        """
        """

        self.update_tabs()

        self.setup_loggers()

        self.ui.listWidgetSubjects.clear()
        self.ui.textBrowserEvents.clear()
        self.ui.labelDateValue.clear()
        self.ui.labelLengthValue.clear()
        self.ui.labelEEGValue.clear()
        self.ui.labelGradMEGValue.clear()
        self.ui.labelHighValue.clear()
        self.ui.labelLowValue.clear()
        self.ui.labelMagMEGValue.clear()
        self.ui.labelSamplesValue.clear()
        self.ui.labelSubjectValue.clear()

        self.setWindowTitle('Meggie - ' + self.experiment.experiment_name)

        self.populate_subject_list()

        active_subject = self.experiment.active_subject

        if active_subject is None:
            self.statusLabel.setText('Add or activate subjects before '
                                     'continuing.')
            return

        raw = active_subject.get_working_file()

        name = active_subject.working_file_name
        status = "Current working file: " + name

        self.statusLabel.setText(status)

        # This updates the 'Subject info' section below the subject list.
        try:
            InfoDialog(raw, self.ui, False)
            self.populate_raw_tab_event_list()
        except Exception as err:
            exc_messagebox(self, err)
            return

    def populate_subject_list(self):
        """ """
        active_subject_name = None
        if self.experiment and self.experiment.active_subject:
            active_subject_name = self.experiment.active_subject.subject_name

        for subject_name in sorted(self.experiment.subjects.keys()):
            item = QtWidgets.QListWidgetItem()
            item.setText(subject_name)
            if subject_name == active_subject_name:
                font = item.font()
                font.setBold(True)
                item.setFont(font)
            self.ui.listWidgetSubjects.addItem(item)

    def populate_raw_tab_event_list(self):
        """
        Fill the raw tab event list with info about event IDs and
        amount of events with those IDs.
        """
        events = self.experiment.active_subject.create_event_set()

        if events is None:
            return

        events_string = ''
        for key, value in events.items():
            events_string += 'Trigger %s, %s events\n' % (str(key), str(value))

        self.ui.textBrowserEvents.setText(events_string)

    def update_tabs(self):
        """ method for initializing the tabs. """

        current_tab = self.ui.tabWidget.currentIndex()
        while self.ui.tabWidget.count() > 0:
            self.ui.tabWidget.removeTab(0)

        for tab_idx, tab in enumerate(self.tabs):
            self.ui.tabWidget.insertTab(
                tab_idx+1, tab, tab.name)

        # self.ui.tabWidget.insertTab(
        #     1, self.mainWindowTabPreprocessing, "Preprocessing")
        # self.ui.tabWidget.insertTab(
        #     2, self.mainWindowTabSpectrums, "Spectrums")
        # self.ui.tabWidget.insertTab(3, self.mainWindowTabEpochs, "Epoching")
        # self.ui.tabWidget.insertTab(
        #     4, self.mainWindowTabEvoked, "Evoked responses")
        # self.ui.tabWidget.insertTab(
        #     5, self.mainWindowTabInduced, "Induced responses")
        # self.ui.tabWidget.insertTab(
        #     6, self.mainWindowTabSourceAnalysis, "Source Analysis")

        self.ui.tabWidget.setCurrentIndex(current_tab)

        # self.mainWindowTabSourceAnalysis.update_tabs()
        # self.mainWindowTabSourceAnalysis.initialize_ui()

        for tab in self.tabs:
            tab.initialize_ui()

        # self.mainWindowTabPreprocessing.initialize_ui()
        # self.mainWindowTabSpectrums.initialize_ui()
        # self.mainWindowTabEpochs.initialize_ui()
        # self.mainWindowTabEvoked.initialize_ui()
        # self.mainWindowTabInduced.initialize_ui()

    def directOutput(self):
        """
        Method for directing stdout to the console and back.
        """
        if self.ui.actionDirectToConsole.isChecked():
            stdout_stream = EmittingStream(
                textWritten=self.normalOutputWritten)
            stdout_stream.orig_stream = sys.__stdout__
            stderr_stream = EmittingStream(textWritten=self.errorOutputWritten)
            stderr_stream.orig_stream = sys.__stderr__

            sys.stdout = stdout_stream
            sys.stderr = stderr_stream
        else:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

    def check_workspace(self):
        """
        Open the preferences dialog, in this case for choosing the workspace.
        """
        preferencesDialog = PreferencesDialog(self)
        preferencesDialog.exec_()

    def __del__(self):
        """
        Restores stdout at the end.
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def normalOutputWritten(self, text):
        """
        Appends text to 'console' at the bottom of the dialog.
        Used for redirecting stdout.
        Parameters:
        text - Text to write to the console.
        """
        cursor = self.ui.textEditConsole.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.textEditConsole.setTextCursor(cursor)
        self.ui.textEditConsole.ensureCursorVisible()

    def errorOutputWritten(self, text):
        """
        Appends text to 'console' at the bottom of the dialog.
        Used for redirecting stderr.
        Parameters:
        text - Text to write to the console.
        """
        cursor = self.ui.textEditConsole.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.textEditConsole.setTextCursor(cursor)
        self.ui.textEditConsole.ensureCursorVisible()

    def setup_loggers(self):

        # hide warnings-module warnings,
        # most of these are still contained
        # in mne-level logging
        warnings.simplefilter('ignore')

        logging.getLogger().setLevel(logging.DEBUG)

        # logger for mne wrapper functions
        mne_wrapper_logger = logging.getLogger('mne_wrapper_logger')
        formatter = logging.Formatter('MNE call: %(asctime)s %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')

        mne_wrapper_logger.handlers = []

        # setup file handler
        if self.experiment:
            logfile = os.path.join(
                self.experiment.workspace,
                self.experiment.experiment_name,
                'meggie.log')
            file_handler = logging.FileHandler(logfile)
            file_handler.setLevel('DEBUG')
            file_handler.setFormatter(formatter)
            mne_wrapper_logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel('INFO')
        mne_wrapper_logger.addHandler(stream_handler)

        # logger for ui output
        ui_logger = logging.getLogger('ui_logger')
        formatter = logging.Formatter('Meggie: %(asctime)s %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')

        ui_logger.handlers = []

        # setup file handler
        if self.experiment:
            logfile = os.path.join(
                self.experiment.workspace,
                self.experiment.experiment_name,
                'meggie.log')
            file_handler = logging.FileHandler(logfile)
            file_handler.setLevel('DEBUG')
            file_handler.setFormatter(formatter)
            ui_logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel('INFO')
        ui_logger.addHandler(stream_handler)

        # logger for real mne
        mne_logger = logging.getLogger('mne')
        formatter = logging.Formatter('MNE: %(asctime)s %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')

        mne_logger.handlers = []

        # setup file handler
        if self.experiment:
            logfile = os.path.join(
                self.experiment.workspace,
                self.experiment.experiment_name,
                'meggie.log')
            file_handler = logging.FileHandler(logfile)
            file_handler.setLevel('DEBUG')
            file_handler.setFormatter(formatter)
            mne_logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel('ERROR')
        mne_logger.addHandler(stream_handler)

        # TODO: trait logger ..


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass

    def fileno(self):
        return self.orig_stream.fileno()


def main():

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(app)

    window.showMaximized()

    sys.exit(app.exec_())

