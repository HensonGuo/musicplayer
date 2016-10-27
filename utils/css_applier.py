#encoding=utf-8
__author__ = 'g7842'

import string
from PyQt4 import QtGui
from PyQt4 import QtCore


#存储一个样式的map
#时间比较赶，暂不支持样式继承


def load_css(url):
    with open(url, "r") as f:
        data = f.read()
    data_len = len(data)
    last_start_mark = 0  #上一次'{'的索引位置
    last_end_mark = 0   #上一次'}'的索引位置
    i = 0
    cssmap = {}
    while i < data_len:
        if data[i] == '{':
            last_start_mark = i
            if last_end_mark == 0:
                css_name = string.strip(data[0:i])
            else:
                css_name = string.strip(data[last_end_mark + 1:i])
        elif data[i] == '}':
            last_end_mark = i
            style_name = string.strip(data[last_start_mark + 1:i])
            cssmap[css_name] = style_name
        else:
            pass
        i += 1

    return cssmap


def apply_css(target, style, cssmap):
    key = '.' + style
    check_valid(target, key, cssmap)
    css = cssmap[key]
    target.setStyleSheet(QtCore.QString.fromUtf8(css))


def apply_css_2_button(target, style, cssmap):
    upname = '.' + style
    check_valid(target, upname, cssmap)
    hovername = '.' + style + ':hover'

    upcss = cssmap[upname]
    if hovername in cssmap:
        hovercss = cssmap[hovername]
        target.setStyleSheet(QtCore.QString.fromUtf8('QPushButton{' + upcss + '} QPushButton:hover{' + hovercss + '}'))
    else:
        target.setStyleSheet(QtCore.QString.fromUtf8(upcss))


def apply_css_2_scrollbar(target, style, cssmap, direction):
    dname = ''
    if direction == QtCore.Qt.Horizontal:
        dname = 'horizontal'
    else:
        dname = 'vertical'
    style = '.' + style
    key = style + '::' + dname
    value = 'QScrollBar::' + dname + '{' + cssmap[key] + '}'

    handle_key = style + '::' + 'handle:' + dname
    if handle_key in cssmap:
        value = value + 'QScrollBar::' + 'handle:' + dname + '{' + cssmap[handle_key] + '}'

    add_line_key = style + '::' + 'add-line:' + dname
    if add_line_key in cssmap:
        value = value + 'QScrollBar::' + 'add-line:' + dname + '{' + cssmap[add_line_key] + '}'

    sub_line_key = style + '::' + 'sub-line:' + dname
    if sub_line_key in cssmap:
        value = value + 'QScrollBar::' + 'sub-line:' + dname + '{' + cssmap[sub_line_key] + '}'

    target.setStyleSheet(QtCore.QString.fromUtf8(value))


def get_style(style, cssmap):
    key = '.' + style
    return cssmap[key]


def check_valid(target, key, cssmap):
    if not isinstance(target, QtGui.QWidget):
        raise TypeError('target is not Qwidget')
    if key not in cssmap:
        raise KeyError('not exist this style')
