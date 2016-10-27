__author__ = 'Administrator'

from song_audio import SongAudio
from song_irc import SongIrc
from song_wave import SongWave
from PyQt4.QtCore import QObject
from PyQt4 import QtCore
from songs import SongMgr


class Song(QObject):
    update = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal()
    irc_update = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Song, self).__init__()
        self.__url = ''
        self.__audio = SongAudio()
        self.__irc = SongIrc()
        self.__wave = SongWave()

        self.__audio.media_obj.tick.connect(self.__on_update)
        self.__audio.media_obj.finished.connect(self.__on_finished)

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value
        self.__audio.set_url(value)
        ircurl = SongMgr.get_song_irc(SongMgr, value)
        self.__irc.set_url(QtCore.QString.fromUtf8(ircurl).__str__())

    def play(self):
        self.__audio.play()

    def pause(self):
        self.__audio.pause()

    def stop(self):
        self.__audio.stop()

    def clear(self):
        self.__audio.media_obj.clear()
        self.__irc.clear()

    @property
    def audio(self):
        return self.__audio

    def __on_update(self, time):
        self.update.emit(time)
        irc_block = self.__irc.get_block(time)
        if irc_block:
            self.irc_update.emit(irc_block)

    def __on_finished(self):
        self.finished.emit()



