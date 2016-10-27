#encoding=utf-8
__author__ = 'Administrator'

import os, re
from utils import util


class SongIrc(object):

    def __init__(self):
        super(SongIrc, self).__init__()
        self.__blocks = {}

    def set_url(self, url):
        self.clear()
        if not os.path.exists(url):
            return
        with open(url, 'r') as f:
            irc_list = f.readlines()
        for line_irc in irc_list:
            arr = re.findall('\\[\\d{2}:\\d{2}\\.\\d{2}\\]', line_irc)
            arr_len = len(arr)
            if arr_len <= 0:
                continue
            for i in range(arr_len):
                arr_value = arr[i]
                key_with_signal = arr_value
                key = util.msz_str_2_time(key_with_signal[1:len(key_with_signal) - 1])
                block = line_irc[len(key_with_signal) * arr_len:len(line_irc)]
                self.__blocks[key] = block

    def get_block(self, time):
        if time in self.__blocks:
            return self.__blocks[time]
        else:
            #向前查找
            finded = False
            while not finded:
                time -= 1
                if time < 0:
                    return None
                if time in self.__blocks:
                    finded = True
                    return self.__blocks[time]

    def clear(self):
        self.__blocks = {}