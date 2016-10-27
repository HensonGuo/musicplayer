#encoding=utf-8
__author__ = 'Administrator'

from PyQt4.phonon import *


class SongAudio(object):

    def __init__(self):
        super(SongAudio, self).__init__()
         #create media
        self.__media_obj = Phonon.MediaObject(None)
        self.__media_obj.setTickInterval(100)
        self.__audio_output = Phonon.AudioOutput(Phonon.MusicCategory)
         # connect mediaObject with audioOutput
        Phonon.createPath(self.__media_obj, self.__audio_output)

    def set_url(self, url):
        self.__media_obj.setCurrentSource(Phonon.MediaSource(url.decode('utf-8')))

    def play(self):
        self.__media_obj.play()

    def pause(self):
        self.__media_obj.pause()

    def stop(self):
        self.__media_obj.stop()

    @property
    def media_obj(self):
        return self.__media_obj

    @property
    def audio_output(self):
        return self.__audio_output
