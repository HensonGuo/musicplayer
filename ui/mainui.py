#encoding=utf-8
__author__ = 'g7842'

from PyQt4.QtGui import *
from PyQt4 import QtCore
from utils.css_applier import *
from PyQt4 import phonon
from PyQt4 import Qt


CSS_FILE_URL = 'assets\CSS.css'


class MainUI(QtCore.QObject):

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.__css = load_css(CSS_FILE_URL)


    def add_elements(self, main_widget):
        main_widget.setObjectName("MainWidget")
        main_widget.setWindowModality(QtCore.Qt.NonModal)
        main_widget.resize(534, 327.9)
        main_widget.setWindowTitle("")
        main_widget.setAutoFillBackground(True)

        self.header = QtGui.QWidget(main_widget)
        self.header.setGeometry(QtCore.QRect(0, 0, 534, 119.5))
        apply_css(self.header, 'header', self.__css)
        self.header.setObjectName("header")

        self.pop_menu = QtGui.QMenuBar(self.header)
        apply_css_2_button(self.pop_menu, 'btn', self.__css)

        self.btnclose = QtGui.QPushButton(self.header)
        self.btnclose.setGeometry(QtCore.QRect(506, 4, 28, 28))
        self.btnclose.setText("")
        apply_css_2_button(self.btnclose, 'btnclose', self.__css)
        self.btnclose.setObjectName("btnclose")
        self.btnclose.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.title = QtGui.QWidget(self.header)
        self.title.setGeometry(QtCore.QRect(10, 29, 518, 31))
        apply_css(self.title, 'title', self.__css)
        self.title.setObjectName("title")

        self.progress_slider = phonon.Phonon.SeekSlider(self.header)
        self.progress_slider.setGeometry(QtCore.QRect(10, 68, 518, 10))
        self.progress_slider.setObjectName("progress_slider")

        self.song_name = QtGui.QLabel(self.header)
        self.song_name.setGeometry(QtCore.QRect(30, 38, 150, 16))
        self.song_name.setObjectName("song_name")
        self.song_name.setText('')
        apply_css(self.song_name, 'label', self.__css)

        self.song_irc = QtGui.QLabel(self.header)
        self.song_irc.setGeometry(QtCore.QRect(200, 38, 330, 30))
        self.song_irc.setObjectName("song_irc")
        apply_css(self.song_irc, 'label', self.__css)

        self.consume_time = QtGui.QLabel(self.header)
        self.consume_time.setGeometry(QtCore.QRect(475, 38, 50, 16))
        self.consume_time.setObjectName("consume_time")
        self.consume_time.setText('00:00')
        apply_css(self.consume_time, 'label', self.__css)

        self.btnprev = QtGui.QPushButton(self.header)
        self.btnprev.setGeometry(QtCore.QRect(10, 85, 28, 28))
        self.btnprev.setText("")
        apply_css_2_button(self.btnprev, 'btnprev', self.__css)
        self.btnprev.setObjectName("btnprev")
        self.btnprev.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btnplay = QtGui.QPushButton(self.header)
        self.btnplay.setGeometry(QtCore.QRect(35, 85, 28, 28))
        self.btnplay.setText("")
        apply_css_2_button(self.btnplay, 'btnpause', self.__css)
        self.btnplay.setObjectName("btnplay")
        self.btnplay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btnstop = QtGui.QPushButton(self.header)
        self.btnstop.setGeometry(QtCore.QRect(60, 85, 28, 28))
        self.btnstop.setText("")
        apply_css_2_button(self.btnstop, 'btnstop', self.__css)
        self.btnstop.setObjectName("btnstop")
        self.btnstop.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btnnext = QtGui.QPushButton(self.header)
        self.btnnext.setGeometry(QtCore.QRect(85, 85, 28, 28))
        self.btnnext.setText("")
        apply_css_2_button(self.btnnext, 'btnnext', self.__css)
        self.btnnext.setObjectName("btnnext")
        self.btnnext.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btnshuffle = QtGui.QPushButton(self.header)
        self.btnshuffle.setGeometry(QtCore.QRect(110, 85, 28, 28))
        self.btnshuffle.setText("")
        apply_css_2_button(self.btnshuffle, 'btnshuffle', self.__css)
        self.btnshuffle.setObjectName("btnshuffle")
        self.btnshuffle.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btnloop = QtGui.QPushButton(self.header)
        self.btnloop.setGeometry(QtCore.QRect(135, 85, 28, 28))
        self.btnloop.setText("")
        apply_css_2_button(self.btnloop, 'btnloop', self.__css)
        self.btnloop.setObjectName("btnloop")
        self.btnloop.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        # self.btnmute = QtGui.QPushButton(self.header)
        # self.btnmute.setGeometry(QtCore.QRect(385, 85, 28, 28))
        # self.btnmute.setText("")
        # apply_css_2_button(self.btnmute, 'btnmute', self.__css)
        # self.btnmute.setObjectName("btnmute")
        # self.btnmute.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.volume_slider = phonon.Phonon.VolumeSlider(self.header)
        self.volume_slider.setGeometry(QtCore.QRect(415, 90, 110, 22))
        self.volume_slider.setObjectName("volume_slider")
        apply_css(self.volume_slider, 'volumeslider', self.__css)

        self.list_songs = QtGui.QListWidget(main_widget)
        self.list_songs.setGeometry(QtCore.QRect(0, 119.8, 534, 180))
        self.list_songs.setObjectName("listSongs")
        apply_css_2_scrollbar(self.list_songs, 'scrollbar', self.__css, QtCore.Qt.Vertical)

        list_item_bg = get_style('listitembg', self.__css)
        list_select_bg = Qt.QPixmap(list_item_bg)
        palette = Qt.QPalette()
        palette.setBrush(Qt.QPalette.Base, QBrush(list_select_bg))

        self.list_songs.setPalette(palette)
        self.list_songs.setGridSize(Qt.QSize(500, 30))
        self.list_songs.setSpacing(6)

        self.footer = QtGui.QWidget(main_widget)
        self.footer.setGeometry(QtCore.QRect(0, 299.8, 534, 28))
        apply_css(self.footer, 'footer', self.__css)
        self.footer.setObjectName("footer")

        self.btnadd = QtGui.QPushButton(self.footer)
        self.btnadd.setGeometry(QtCore.QRect(475, 3.5, 25, 25))
        self.btnadd.setText("")
        apply_css_2_button(self.btnadd, 'btnadd', self.__css)
        self.btnadd.setObjectName("btnadd")
        self.btnadd.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btndel = QtGui.QPushButton(self.footer)
        self.btndel.setGeometry(QtCore.QRect(509, 3.5, 25, 26))
        self.btndel.setText("")
        apply_css_2_button(self.btndel, 'btndel', self.__css)
        self.btndel.setObjectName("btndel")
        self.btndel.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def set_elements_style(self, target, style, is_button=False):
        if is_button:
            apply_css_2_button(target, style, self.__css)
        else:
            apply_css(target, style, self.__css)


