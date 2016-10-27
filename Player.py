#encoding=utf-8
__author__ = 'g7842'

import sys
import random
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.phonon import *
from PyQt4 import QtCore
from PyQt4 import QtGui

from ui.mainui import MainUI
from ui.desk_irc_ui import Desk_Irc_UI
from media.songs import SongMgr
from media import songs
from media.song import Song
from utils import util


class Player(QWidget, MainUI):

    def __init__(self, parent=None):
        super(Player, self).__init__()
        self.is_playing = False
        self.is_pause = False
        self.is_shuffle = False
        self.is_loop = False
        self.play_index = 0
        self.init_ui()
        self.init_menu()
        self.init_data()

    def init_menu(self):
        self.pop_menu = QtGui.QMenu(self.header)

        about_action = QAction(QIcon(""), u'关于', self)
        self.pop_menu.addAction(about_action)

        help_action = QAction(QIcon(""), u'帮助', self)
        self.pop_menu.addAction(help_action)

        quit_action = QAction(QIcon(""), u'退出', self)
        self.connect(quit_action, SIGNAL("triggered()"), self.close)
        self.pop_menu.addAction(quit_action)

    def init_ui(self):
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.add_elements(self)
        self.btnclose.setToolTip(QString(u'<font color="#ffffff" size = 4>关闭</font>'))
        self.connect(self.btnclose, SIGNAL('clicked()'), self.close)

        self.btnplay.setToolTip(QString(u'<font color="#ffffff" size = 4>播放</font>'))
        self.connect(self.btnplay, SIGNAL('clicked()'), self.play_or_pause)

        self.btnstop.setToolTip(QString(u'<font color="#ffffff" size = 4>停止</font>'))
        self.connect(self.btnstop, SIGNAL('clicked()'), self.stop)

        self.btnprev.setToolTip(QString(u'<font color="#ffffff" size = 4>播放上一首</font>'))
        self.connect(self.btnprev, SIGNAL('clicked()'), self.play_prev)

        self.btnnext.setToolTip(QString(u'<font color="#ffffff" size = 4>播放下一首</font>'))
        self.connect(self.btnnext, SIGNAL('clicked()'), self.play_next)

        self.btnshuffle.setToolTip(QString(u'<font color="#ffffff" size = 4>随机播放</font>'))
        self.connect(self.btnshuffle, SIGNAL('clicked()'), self.shuffle)

        self.btnloop.setToolTip(QString(u'<font color="#ffffff" size = 4>单曲循环</font>'))
        self.connect(self.btnloop, SIGNAL('clicked()'), self.loop)

        self.btnadd.setToolTip(QString(u'<font color="#ffffff" size = 4>添加歌曲</font>'))
        self.connect(self.btnadd, SIGNAL('clicked()'), self.add)

        self.btndel.setToolTip(QString(u'<font color="#ffffff" size = 4>删除歌曲</font>'))
        self.connect(self.btndel, SIGNAL('clicked()'), self.delete)

        self.desk_irc = Desk_Irc_UI()
        self.desk_irc.show()

        self.list_songs.mouseDoubleClickEvent = self.double_click_2_play

    def init_data(self):
        self.music_mgr = SongMgr('assets/songlist.txt')
        #装载默认歌曲列表
        self.refresh_list()
        #create media
        self.song = Song()
        self.song.update.connect(self.update_time)
        self.song.finished.connect(self.play_finished)
        self.song.irc_update.connect(self.irc_update)
        # 绑定声音控件
        self.volume_slider.setAudioOutput(self.song.audio.audio_output)
        self.volume_slider.setMaximumVolume(1)
        # 绑定播放进度控件
        self.progress_slider.setMediaObject(self.song.audio.media_obj)

    def enterEvent(self, event):
        print('你妹的')


    def refresh_list(self):
        self.music_mgr.load_list()
        self.list_songs.clear()
        for i in range(self.music_mgr.song_count):
            song = self.music_mgr.get_song(i)
            self.list_songs.addItem(SongMgr.get_song_name(SongMgr, song))

    def play_or_pause(self):
        # 设置play按钮状态
        if self.is_playing:
            self.is_playing = False
            self.set_elements_style(self.btnplay, 'btnpause', True)
            self.btnplay.setToolTip(QString(u'<font color="#ffffff" size = 4>点击播放</font>'))
            self.song.pause()
            self.is_pause = True
        else:
            self.is_playing = True
            self.set_elements_style(self.btnplay, 'btnplay', True)
            self.btnplay.setToolTip(QString(u'<font color="#ffffff" size = 4>点击暂停</font>'))

            if self.is_pause:
                self.song.play()
            else:
                items = self.list_songs.selectedItems()
                if len(items) > 0:
                    item = self.list_songs.selectedItems()[0]
                    self.play_index = self.listSongs.row(item)
                self.play_by_index(self.play_index)

    def play_by_index(self, index):
        url = self.music_mgr.get_song(index)
        self.song.url = url
        self.song.play()
        self.is_playing = True
        song_name = SongMgr.get_song_name(SongMgr, self.music_mgr.get_song(index))
        self.song_name.setText(song_name)
        self.song_irc.setText('')
        self.set_elements_style(self.btnplay, 'btnplay', True)
        self.btnplay.setToolTip(QString(u'<font color="#ffffff" size = 4>点击暂停</font>'))

    def shuffle(self, toggle=True):
        if self.is_shuffle or not toggle:
            self.is_shuffle = False
            self.set_elements_style(self.btnshuffle, 'btnshuffle', True)
        else:
            self.is_shuffle = True
            self.set_elements_style(self.btnshuffle, 'btnshuffle::selection', True)
            self.loop(False)

    def play_by_shuffle(self):
        index = random.randint(0, self.music_mgr.song_count - 1)
        self.play_by_index(index)

    def loop(self, toggle=True):
        if self.is_loop or not toggle:
            self.is_loop = False
            self.set_elements_style(self.btnloop, 'btnloop', True)
        else:
            self.is_loop = True
            self.set_elements_style(self.btnloop, 'btnloop::selection', True)
            self.shuffle(False)

    def play_by_loop(self):
        self.play_by_index(self.play_index)

    def double_click_2_play(self, e):
        if len(self.list_songs.selectedItems()) == 0:
            return
        self.play_index = self.list_songs.row(self.list_songs.selectedItems()[0])
        self.play_by_index(self.play_index)

    def play_next(self):
        self.play_index += 1
        if self.play_index >= self.music_mgr.song_count:
            self.play_index = 0
        self.play_by_index(self.play_index)
        self.list_songs.setCurrentRow(self.play_index)

    def play_prev(self):
        self.play_index -= 1
        if self.play_index < 0:
            self.play_index = self.music_mgr.song_count - 1
        self.play_by_index(self.play_index)
        self.music_mgr.setCurrentRow(self.play_index)

    def stop(self):
        self.song.stop()
        self.set_elements_style(self.btnplay, 'btnpause', True)
        self.consume_time.setText(util.time_2_ms_str(0))

    def play_finished(self):
        if self.is_loop:
            self.play_by_loop()
            return
        if self.is_shuffle:
            self.play_by_shuffle()
            return
        self.play_next()

    def irc_update(self, block):
        self.song_irc.setText(QtCore.QString.fromUtf8(block))
        self.desk_irc.setText(QtCore.QString.fromUtf8(block))

    def add(self):
        files = QFileDialog.getOpenFileNames(self, u"请选择歌曲", u"", self.tr(songs.FILTER_FORMAT_STR))
        for file in files:
            result = self.music_mgr.add_song(file)
            if result is True:
                self.list_songs.addItem(songs.get_song_name(songs, file.__str__()))

    def delete(self):
        items = self.list_songs.selectedItems()
        for item in items:
            index = self.list_songs.row(item)
            self.music_mgr.del_song(index)
        self.refresh_list()

    def close(self):
        self.song.clear()
        exit(0)

    def update_time(self, time):
        msz = util.time_2_msz_str(time)
        self.consume_time.setText(util.time_2_ms_str(time))

    def mouseMoveEvent(self, e):
        if e.buttons() & Qt.LeftButton:
            self.move(e.globalPos() - self.drag_pos)
            e.accept()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drag_pos = e.globalPos() - self.frameGeometry().topLeft()
            e.accept()

    def contextMenuEvent(self, e):
        self.pop_menu.exec_(e.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    musicPlayer = Player()
    musicPlayer.show()
    sys.exit(app.exec_())
