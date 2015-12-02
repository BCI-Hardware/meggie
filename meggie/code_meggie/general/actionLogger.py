"""
Created on 26.11.2015

@author: Janne Pesonen
"""
import os
import logging

#from meggie.code_meggie.general.caller import Caller

    #logger = logging.getLogger('mne')
    #mne.utils.set_log_file('reallogs.log', '%(message)', None)  
    #mne.utils.set_log_level('INFO')
    
    # TODO: new logging system for Meggie
    #logger = logging.getLogger('meggie')  # one selection here used across mne-python
    #logger.propagate = False  # don't propagate (in case of multiple imports)
    #logging.basicConfig(filename='reallogs.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)
    #logging.info('Config file in path: ' + mne.get_config_path())




class ActionLogger(object):
    """
    classdocs
    """


    def __init__(self):
        """
        Constructor
        """
        #copied stuff from MNE-Python utils.py
        self._logger = logging.getLogger('meggie')  # one selection here used across Meggie
        self._logger.propagate = False  # don't propagate (in case of multiple imports)
        self._actionCounter = 1;
        #self.initialize_logger()
        
    @property
    def logger(self):
        """
        Returns the logger.
        """
        return self._logger
        
    def initialize_logger(self):
        """Initializes the logger and adds a handler to it that handles writing and formatting
        the logs to a file.
        
        Keyword arguments
        path -    path to save the log file
        """
        #TODO: try JSON or YAML
        #TODO: If you use FileHandler for writing logs, the size of log file will grow with time.
        #Someday, it will occupy all of your disk. In order to avoid that situation, you should
        #use RotatingFileHandler instead of FileHandler in production environment.
        handler = logging.FileHandler('meggie_log.log')
        handler.setLevel(logging.INFO)
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)
        
    def log_dict(self, function_name, params, msg):
        """
        """
        self._logger.info('>>>')
        self._logger.info(function_name)
        self._logger.info(msg)
        self._logger.info('>>>')
        #self._logger.info('>' + str(self._actionCounter))
        if params != None:
            for key, value in params.items():
                self._logger.info(str(key) + ',' + str(value))
        self._actionCounter += 1
        
    def log_list(self, function_name, params, msg):
        self._logger.info('>>>')
        self._logger.info(function_name)
        self._logger.info(msg)
        self._logger.info('>>>')
        #self._logger.info('>' + str(self._actionCounter))
        for param in params:
            self._logger.info(str(param))
        self._actionCounter += 1
    
    def log_success(self, function_name, params):
        msg = 'SUCCESS'
        if isinstance(params, dict):
            self.log_dict(function_name, params, msg)
        else:
            self.log_list(function_name, params, msg)
        
    def log_error(self, function_name, params, error):
        msg = 'FAILURE: ' + error
        if isinstance(params, dict):
            self.log_dict(function_name, params, msg)
        else:
            self.log_list(function_name, params, msg)
        
    def log_warning(self, function_name, params, warning):
        msg = 'WARNING: ' + warning
        if isinstance(params, dict):
            self.log_dict(function_name, params, msg)
        else:
            self.log_list(function_name, params, msg)
        
    def log_message(self, msg):
        self._logger.info('#')
        #self._logger.info('>' + str(self._actionCounter))
        self._logger.info(msg)
        self._logger.info('#')
        #self._actionCounter += 1
        
    def log_subject_activation(self, subject_name):
        self._logger.info('----------------------------------------------------------------------------------------------------')
        #self._logger.info('Activated subject: ')
        self._logger.info(subject_name)
        
        
        