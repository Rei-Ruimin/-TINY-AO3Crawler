from PyQt5.Qt import *
from cont_info import Ui_Dialog
from PyQt5 import QtCore


class ContInfoPane(QDialog, Ui_Dialog):
    cont_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def cont_info_ok_btn_c(self):
        self.cont_signal.emit()
        self.close()


if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    window = ContInfoPane()
    window.show()

    sys.exit(app.exec_())
