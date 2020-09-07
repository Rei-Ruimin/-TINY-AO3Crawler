from PyQt5.Qt import *
from mainGUI import Ui_Form
from PyQt5 import QtCore


class MainPane(QWidget, Ui_Form):
    info_pane_btn_c_sgn = pyqtSignal()
    ok_btn_c_sgn = pyqtSignal(bool, str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def info_btn_c(self):
        self.info_pane_btn_c_sgn.emit()

    def save_dir_btn_c(self):
        filedir_s = QFileDialog.getExistingDirectory(self, "Choose the save directory", "")
        self.save_dir_le.setText(filedir_s)

    def blank_dir_error_msg(self):
        bf_msg = QMessageBox(QMessageBox.Warning, "RPlot",
                             "Please select the save directory.",
                             QMessageBox.Ok, self)
        bf_msg.open()

    def blank_line_error_msg(self):
        bl_msg = QMessageBox(QMessageBox.Warning, "RPlot",
                             "Please fill the line",
                             QMessageBox.Ok, self)
        bl_msg.open()

    def ok_btn_c(self):
        if self.search_key_le.text() == "" and self.search_p_url_le.text() == "":
            self.blank_line_error_msg()
            return
        elif self.save_dir_le.text() == "" or self.save_dir_le.text() == "the chosen directory will be here":
            self.blank_dir_error_msg()
            return

        if self.search_p_url_le.text() != "":
            search_key = False
            search_input = self.search_p_url_le.text()
        else:
            search_key = True
            search_input = self.search_key_le.text()

        save_dir = self.save_dir_le.text()

        self.ok_btn_c_sgn.emit(search_key, search_input, save_dir)

    def search_key_le_changed(self):
        if self.search_key_le.text() != "":
            self.search_p_url_le.setEnabled(False)
        else:
            self.search_p_url_le.setEnabled(True)

    def search_p_url_le_changed(self):
        if self.search_p_url_le.text() != "":
            self.search_key_le.setEnabled(False)
        else:
            self.search_key_le.setEnabled(True)


if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    window = MainPane()
    window.show()
    sys.exit(app.exec_())
