#encoding=utf-8
__author__ = 'g7842'

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import Qt


class Desk_Irc_UI(QtGui.QLabel):

    def __init__(self, parent=None):
        super(Desk_Irc_UI, self).__init__(parent)
        self.setWindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.resize(1024, 60)
        self.setText(self.tr('irc...'))
        #背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.OpenHandCursor)

        exit_ac = QtGui.QAction(u'隐藏', self)
        self.connect(exit_ac, QtCore.SIGNAL('triggered()'), self.close)

        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL('timeout()'), self.timeout)

        self.pop_menu = QtGui.QMenu(self)
        self.pop_menu.addAction(exit_ac)

        self.move(400, 700)
        self.lrc_width = 0
        self.length = 0
        self.drag_pos = 0

    def contextMenuEvent(self, e):
        self.pop_menu.exec_(e.globalPos())

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drag_pos = e.globalPos() - self.frameGeometry().topLeft()
            e.accept()
        elif e.button() == Qt.MidButton:
            self.close()

    def mouseMoveEvent(self, e):
        if e.buttons() & Qt.LeftButton:
            self.move(e.globalPos() - self.drag_pos)
            e.accept()

    def paintEvent(self, e):
        qp = QtGui.QPainter(self)
        # 反锯齿
        qp.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        font = QtGui.QFont(self.tr("Times New Roman"), 30, QtGui.QFont.Bold)
        qp.setFont(font)

        lg = QtGui.QLinearGradient(0, 20, 0, 50)
        lg.setColorAt(0, QtGui.QColor(0, 170, 255, 255))
        lg.setColorAt(0, QtGui.QColor(61, 214, 191, 250))
        lg.setColorAt(0, QtGui.QColor(85, 255, 255, 255))
        lg.setColorAt(0, QtGui.QColor(0, 170, 255, 255))
        qp.setBrush(lg)
        qp.setPen(QtCore.Qt.NoPen)

        txt_path = QtGui.QPainterPath()
        txt_path.addText(0, 50, font, self.text())
        qp.drawPath(txt_path)

        self.length = txt_path.currentPosition().x()

        qp.setPen(QtCore.Qt.yellow)
        qp.drawText(0, 14, self.lrc_width, 50, QtCore.Qt.AlignLeft, self.text())

    def timeout(self):
        self.lrc_width += self.length
        self.update()

		
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Desk_Irc_UI()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()