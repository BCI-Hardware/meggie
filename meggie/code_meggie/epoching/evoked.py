'''
Created on 20.2.2014

@author: jaolpeso
'''

import os

from PyQt4.QtCore import QObject

import mne

from meggie.code_meggie.general.fileManager import load_evoked

class Evoked(QObject):
    """
    Class for creating and handling evokeds
    """

    def __init__(self, name, subject, mne_evokeds):
        """
        Constructor
        
        Keyword arguments:
        raw    -- raw evoked file
        name   -- name of the raw evoked file
        events -- list of events in raw file
        """
        QObject.__init__(self)
        self._name = name
        self._mne_evokeds = mne_evokeds
        self._path = os.path.join(subject.evokeds_directory, name)
        
#     @property
#     def raw(self):
#         """
#         Returns the raw .fif of the evoked.
#         """
#         if isinstance(self._raw, mne.Evoked):
#             return self._raw
#         else:
#             raw = self.load_working_file()
#             return raw
#         
#     @raw.setter
#     def raw(self, raw):
#         """
#         Sets the raw data for the evoked collection.
#          
#         Keyword arguments:
#         raw    -- the raw .fif of the collection
#         """
#         self._raw = raw        

    @property
    def mne_evokeds(self):
        """
        """
        if None in self._mne_evokeds.values():
            # load everything
            evokeds = load_evoked(self._path)
            for key in self._mne_evokeds:
                for evoked in evokeds:
                    if key == evoked.comment:
                        self._mne_evokeds[key] = evoked
                        break
            if None in self._mne_evokeds.keys():
                raise ValueError('Event name ' + key + 
                                 ' missing from Evoked FIF file.')
        return self._mne_evokeds

    @property
    def name(self):
        """
        Returns the name of the raw file.
        """
        return self._name
    
    @name.setter
    def name(self, name):
        """
        Sets the name for the raw
        
        Keyword arguments:
        name    -- name of the evoked fif file without suffix
        """
        self._name = name
        
#     def load_working_file(self):
#         if self._raw is None:
#             self._raw = load_evoked(self._path)
#         return self._raw

