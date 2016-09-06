import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)


def close_event(event):
    reply = QMessageBox.question(Qw, 'Message',
                                 "Are you sure to quit?", QMessageBox.Yes |
                                 QMessageBox.No, QMessageBox.No)

    if reply == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Qw = QWidget()
    QToolTip.setFont(QFont('SansSerif', 10))
    Qw.setToolTip('This is a <b>QWidget</b> widget')

    btn = QPushButton('Button', Qw)
    btn.setToolTip('This is a <p>QPushButton</p> widget')
    btn.resize(btn.sizeHint())
    btn.move(50, 50)

    qbtn = QPushButton('Quit', Qw)
    qbtn.clicked.connect(QCoreApplication.instance().quit)
    qbtn.resize(qbtn.sizeHint())
    qbtn.move(100, 100)

    Qw.closeEvent = close_event
    qr = Qw.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    Qw.move(qr.topLeft())

    Qw.setGeometry(300, 300, 300, 200)
    Qw.setWindowTitle('Tooltips')
    Qw.show()
    sys.exit(app.exec_())