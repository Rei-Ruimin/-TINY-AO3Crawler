from PyQt5.Qt import *
from info import Ui_Dialog
from PyQt5 import QtCore


class InfoPane(QDialog, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("About your keyword")

    def close_btn_c(self):
        self.close()


if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    window = InfoPane()
    window.show()

    sys.exit(app.exec_())
