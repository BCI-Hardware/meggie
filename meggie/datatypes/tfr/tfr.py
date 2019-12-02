# coding: utf-8

"""
"""

import os
import re
import logging

import mne


class TFR(object):
    """
    """

    def __init__(self, name, tfr_directory, params, content=None):
        """
        """
        self._name = name
        self._content = content
        self._tfr_directory = tfr_directory

    def _get_fname(self, tfr_name):
        # for backward compatibility
        if tfr_name == '':
            name = self._name + '-tfr.h5'
        else:
            name = self._name + '-' + tfr_name + '-tfr.h5'

        fname = os.path.join(self._tfr_directory,
                             name)
        return fname

    def save_content(self):
        for tfr_name, tfr in self._content.items():
            fname = self._get_fname(tfr_name)
            tfr.save(fname, overwrite=True)

    def delete_content(self):
        if not self._content:
            return

        for tfr_name, tfr in self._content.items():
            fname = self._get_fname(tfr_name)
            os.remove(fname)

    def _load_content(self):
        self._content = {}
        template = self._name + '-' + r'([a-zA-Z1-9_]+)\-tfr\.h5'
        for fname in os.listdir(self._tfr_directory):
            path = None
            if fname == self._name + '-tfr.h5':
                path = os.path.join(self._tfr_directory, fname)
                key = ''
            else:
                match = re.match(template, fname)
                if match:
                    try:
                        key = str(match.group(1))
                    except Exception as exc:
                        raise Exception("Unknown file name format.")

                    path = os.path.join(self._tfr_directory,
                                        fname)
            if path:
                logging.getLogger('ui_logger').debug(
                    'Reading tfr file: ' + str(path))

                self._content[key] = mne.read_tfrs(path)[0]

    @property
    def content(self):
        if self._content is None:
            self._load_content()
        return self._content

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        self._params = params

    @property
    def name(self):
        return self._name

    @property
    def decim(self):
        return self._params['decim']

    @property
    def n_cycles(self):
        return self._params['n_cycles']

    @property
    def evoked_subtracted(self):
        return self._params['evoked_subtracted']
