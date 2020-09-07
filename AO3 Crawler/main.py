from PyQt5 import QtCore
from PyQt5.Qt import *
from API_Tool import Article
from cont_info_pane import ContInfoPane
from progress_pane import ProgressPane
from info_pane import InfoPane
from mainGUI_pane import MainPane
import os

if __name__ == '__main__':
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    myGUI_pane = MainPane()
    progress_pane = ProgressPane()
    info_pane = InfoPane(myGUI_pane)
    cont_info_pane = ContInfoPane(myGUI_pane)

    def handle_cont():
        myGUI_pane.hide()
        progress_pane.pb_loading()
        progress_pane.show()
        progress_pane.call_continue_thread()

    if os.path.exists(os.path.join(os.path.dirname(__file__), "scraping_file.dictionary")):
        cont_info_pane.open()
        cont_info_pane.cont_signal.connect(handle_cont)

    def open_info_pane():
        info_pane.show()

    myGUI_pane.info_pane_btn_c_sgn.connect(open_info_pane)

    def handle_data(search_key, search_input, save_dir):
        myGUI_pane.hide()
        progress_pane.pb_loading()
        progress_pane.show()
        progress_pane.call_crawl_thread(search_key, search_input, save_dir)

    myGUI_pane.ok_btn_c_sgn.connect(handle_data)
    myGUI_pane.show()
    sys.exit(app.exec_())
