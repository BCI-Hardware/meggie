# coding: utf-8

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
Created on Mar 12, 2013

@author: Jaakko Leppakangas
Contains the Events-class that gets events from a raw file.
"""
import mne

class Events(object):
    """
    Class for getting events from the raw file, by type if need be.
    """

    def __init__(self, raw, stim_ch=None, mask=0):
        """
        Constructor    
        Keyword arguments:
        raw           -- A raw object
        stim_ch       -- Name of the stimulus channel
        mask          -- Mask for excluding bits.
        """
        
        # use combination of shortest_event=1 and 
        # min_duration=2/sfreq to avoid spurious events
        # without being caught to exceptions
        self._events = mne.find_events(raw, stim_channel=stim_ch,
            shortest_event=1, min_duration=2.0/raw.info['sfreq'], mask=mask)
        
    @property    
    def events(self):
        """
        Property for events.
        """
        return self._events
    
    def pick(self, event_id):
        """
        Method for picking events with selected id.
        Keyword arguments:
        event_id      -- Id of the event.
        Raises an exception if the events haven't been initialized.
        Returns events matching the event_id.
        """
        if self._events is None:
            raise Exception('No events found.')
        return [x for x in self._events if x[2] == event_id]
        #self._events = mne.pick_events(self._events, include=event_id)
