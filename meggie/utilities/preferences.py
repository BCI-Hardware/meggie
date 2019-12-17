# coding: utf-8

"""
"""

import os
import logging
import configparser

from meggie.utilities.filemanager import homepath


class PreferencesHandler(object):
    '''
    Class for storing Meggie preferences and setting them into effect.
    '''

    def __init__(self):
        '''Constructor'''
        self.working_directory = ''
        self.freesurfer_home = ''
        self.previous_experiment_name = ''
        self.auto_load_last_open_experiment = False
        self.confirm_quit = False
        self.save_bads = False
        self.read_preferences_from_disk()

    def write_preferences_to_disk(self):
        """
        Writes the preferences to disk, in an easily readable form.
        """
        config = configparser.RawConfigParser()
        config.add_section('MiscOptions')
        config.add_section('Workspace')
        config.add_section('EnvVariables')
        config.add_section('Tabs')

        # Sanity of these values is assumed to be checked by the calling method
        config.set('MiscOptions', 'previousExperimentName',
                   self.previous_experiment_name)
        config.set('Workspace', 'workspaceDir', self.working_directory)
        config.set('EnvVariables', 'FreeSurferHomeDir', self.freesurfer_home)

        if self.auto_load_last_open_experiment:
            config.set('MiscOptions', 'autoReloadPreviousExperiment', 'True')
        else:
            config.set('MiscOptions', 'autoReloadPreviousExperiment', 'False')

        if self.confirm_quit:
            config.set('MiscOptions', 'confirmQuit', 'True')
        else:
            config.set('MiscOptions', 'confirmQuit', 'False')

        if self.save_bads:
            config.set('MiscOptions', 'saveBads', 'True')
        else:
            config.set('MiscOptions', 'saveBads', 'False')

        config.set('Tabs', 'enabledTabs', ','.join(self.enabled_tabs or []))
        config.set('Tabs', 'preset', self.tab_preset)

        # test this!

        with open(os.path.join(homepath(), '.meggieprefs'), 'w') as configfile:
            config.write(configfile)

    def read_preferences_from_disk(self):
        """
        Reads the preferences from disk into class attributes.
        """
        filename = os.path.join(homepath(), '.meggieprefs')
        if os.path.isfile(filename):
            config = configparser.RawConfigParser()
            config.read(filename)

        try:
            self.working_directory = config.get('Workspace', 'workspaceDir')
        except BaseException:
            self.working_directory = ''

        try:
            self.freesurfer_home = config.get(
                'EnvVariables', 'FreeSurferHomeDir')
        except BaseException:
            self.freesurfer_home = ''

        try:
            if config.get('MiscOptions',
                          'autoreloadpreviousexperiment') == 'True':
                self.auto_load_last_open_experiment = True
            else:
                self.auto_load_last_open_experiment = False
        except BaseException:
            self.auto_load_last_open_experiment = False

        try:
            if config.get('MiscOptions', 'confirmQuit') == 'True':
                self.confirm_quit = True
            else:
                self.confirm_quit = False
        except BaseException:
            self.confirm_quit = False

        try:
            self.previous_experiment_name = config.get(
                'MiscOptions', 'previousExperimentName')
        except BaseException:
            self.previous_experiment_name = ''

        try:
            self.enabled_tabs = config.get('Tabs', 'enabledTabs')
            self.enabled_tabs = self.enabled_tabs.split(',')
        except BaseException:
            self.enabled_tabs = ''
        try:
            self.tab_preset = config.get('Tabs', 'preset')
        except BaseException:
            self.tab_preset = ''

    def set_env_variables(self):
        """
        """
        message = ('Setting environment variables...')
        logging.getLogger('ui_logger').info(message)

        # Set environment directly for FreeSurfer.
        if self.freesurfer_home:
            freeSurferBinPath = os.path.join(self.freesurfer_home, 'bin')
            freeSurferTktoolsPath = os.path.join(
                self.freesurfer_home, 'tktools')
            os.environ['FREESURFER_HOME'] = self.freesurfer_home
            os.environ['PATH'] += os.pathsep + freeSurferBinPath
            os.environ['PATH'] += os.pathsep + freeSurferTktoolsPath

        # to make graphical MNE-Python utilities
        # use QT4 backend instead of wx.
        os.environ['ETS_TOOLKIT'] = "qt4"