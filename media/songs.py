#encoding=utf-8
__author__ = 'g7842'


import os
import logging
from PyQt4 import QtCore


SONGS_FORMARTS = ('mp3', 'wav', 'waf', 'rm', 'midi', 'cd', 'wma', 'ape', 'vqf', 'real', 'module', 'asf')


def songs_formats_2_str(fmt1, fmt2):
    if len(fmt1) <= 3:
        return fmt1.upper() + ' File' + '(*.' + fmt1 + ')' + '\n' + fmt2.upper() + ' File' + '(*.' + fmt2 + ')'
    return fmt1 + '\n' + fmt2.upper() + ' File' + '(*.' + fmt2 + ')'

FILTER_FORMAT_STR = reduce(songs_formats_2_str, SONGS_FORMARTS)

CODEC = 'utf-8'


#歌曲列表
class SongMgr(object):

    def __init__(self, file_url):
        self.__list = []
        self.__list_url = file_url

    def load_list(self):
        while self.__list.__len__() > 0:
            self.__list.pop()
        if os.path.exists(self.__list_url) is not True:
            logging.info('file_url 不存在')
            return
        with open(self.__list_url, 'r') as f:
            for song in f.readlines():
                song = song.strip()
                if song == '':
                    continue
                self.__list.append(song.strip())

    def save_list(self):
        with open(self.__list_url, 'w') as f:
            for song in self.__list:
                f.write(song + '\n')

    def add_song(self, file_url):
        song_formate = file_url.split('.')[-1]
        try:
            SONGS_FORMARTS.index(song_formate.__str__())
        except ValueError:
            return False
        finally:
            pass
        if self.__list.count(file_url) != 0:
            logging(file_url + '歌曲已经存在，不能重复添加')
            return False
        self.__list.append(file_url.__str__().encode(CODEC))
        self.save_list()
        return True

    def del_song(self, index):
        self.__list.remove(self.__list[index])
        self.save_list()

    def get_song(self, index):
        return self.__list[index]

    @property
    def song_count(self):
        return len(self.__list)

    @staticmethod
    def get_song_name(cls, song_url):
        name_with_suffix = os.path.split(song_url)
        return QtCore.QString.fromUtf8(name_with_suffix[1].split('.')[0])

    @staticmethod
    def get_song_irc(cls, song_url):
        name_with_url = QtCore.QString(os.path.splitext(song_url)[0])
        name_with_url = name_with_url.replace('songs', 'irc')
        return QtCore.QString(name_with_url + '.irc')
