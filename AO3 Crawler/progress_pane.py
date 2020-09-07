from PyQt5.Qt import *
from progress_bar import Ui_Form
from PyQt5 import QtCore
from API_Tool import MyCrawler
import os
import time
import pickle


class CrawlThread(QThread):
    progress_msg_sgn = pyqtSignal(str)
    all_msg = ""

    def __init__(self, search_key_used, topic, save_dir):
        super(CrawlThread, self).__init__()
        self.search_key_used = search_key_used
        self.topic = topic
        self.save_dir = save_dir

    def run(self):
        ao3crawler = MyCrawler()
        ao3crawler.progress_msg_signal.connect(self.handle_progress_msg)
        if self.search_key_used:
            ao3crawler.crawl_and_save_by_key_word(self.topic, self.save_dir)
        else:
            ao3crawler.crawl_and_save_by_search_url(self.topic, self.save_dir)

    def handle_progress_msg(self, progress_msg):
        self.all_msg += (progress_msg+'\n')
        self.progress_msg_sgn.emit(self.all_msg)


class ContinueCrawlThread(QThread):
    progress_msg_sgn = pyqtSignal(str)
    all_msg = ""

    def __init__(self):
        super(ContinueCrawlThread, self).__init__()

    def run(self):
        ao3crawler = MyCrawler()
        ao3crawler.progress_msg_signal.connect(self.handle_progress_msg)
        ao3crawler.continue_crawling()

    def handle_progress_msg(self, progress_msg):
        self.all_msg += (progress_msg+'\n')
        self.progress_msg_sgn.emit(self.all_msg)


class TimerThread(QThread):
    update = pyqtSignal()

    def run(self):
        while True:
            self.update.emit()
            time.sleep(0.5)

    def stop(self):
        self.terminate()


class ProgressPane(QWidget, Ui_Form):
    dot_num = 0

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        # self.textBrowser.setText("aaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\naaaaa\n")

    def scroll_bar_to_bottom(self):
        # make sure the scroll bar is at the bottom of textbroswer
        cursor = self.textBrowser.textCursor()
        pos = len(self.textBrowser.toPlainText())
        cursor.setPosition(pos)
        self.textBrowser.ensureCursorVisible()
        self.textBrowser.setTextCursor(cursor)

    def pb_finished(self):
        self.timer_thread.stop()
        self.open_folder_btn.setEnabled(True)
        self.msg_l.setText("Finished!")

    def pb_loading(self):
        self.open_folder_btn.setEnabled(False)
        self.msg_l.setText("Loading")

        self.timer_thread = TimerThread()
        self.timer_thread.update.connect(self.pb_loading_update)
        self.timer_thread.start()

    def pb_loading_update(self):
        self.dot_num = (self.dot_num+1)%4
        self.msg_l.setText("Loading" + '.' * self.dot_num)

    def open_folder(self):
        # make sure the folder is created (in case the thread end due to IP blocked)
        if os.path.isdir(os.path.join(self.save_dir, self.folder_name)):
            os.startfile(os.path.join(self.save_dir, self.folder_name))
            self.close()
        else:
            self.open_invalid_folder_msg()
            self.open_folder_btn.setEnabled(False)

    def open_invalid_folder_msg(self):
        bf_msg = QMessageBox(QMessageBox.Warning, "The folder is invalid",
                             "Please retry later!",
                             QMessageBox.Ok, self)
        bf_msg.open()

    def update_progress_msg(self, msg):
        self.textBrowser.setText(msg)
        self.scroll_bar_to_bottom()

    def call_crawl_thread(self, search_key_used, topic, save_dir):
        self.save_dir = save_dir
        if search_key_used:
            self.folder_name = check_forbidden_char(topic) + '--AO3'
        else:
            self.folder_name = 'your_result--AO3'

        self.thread = CrawlThread(search_key_used, topic, save_dir)
        self.thread.progress_msg_sgn.connect(self.update_progress_msg)
        self.thread.start()
        self.thread.finished.connect(self.pb_finished)

    def call_continue_thread(self):
        self.thread2 = ContinueCrawlThread()
        self.thread2.progress_msg_sgn.connect(self.update_progress_msg)
        self.thread2.start()
        self.thread2.finished.connect(self.pb_finished)
        with open("scraping_file.dictionary", 'rb') as file:
            save_D = pickle.load(file)
            self.folder_name = save_D['topic'] + "--AO3"
            self.save_dir = save_D['save_dir']


def check_forbidden_char(str):
    forbidden_chars = '\ / : * ? " < > |'.split()
    for char in forbidden_chars:
        if str.find(char) != -1:
            str = str.replace(char, 'x')
    return str


if __name__ == '__main__':
    # import sys
    #
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # app = QApplication(sys.argv)
    #
    # window = ProgressPane()
    # window.show()
    #
    # sys.exit(app.exec_())
    print(os.path.isdir('C:/Users/11602/Desktop/WebScraping/MyAO3Crawler/x鸣佐x--AO3'))
    print(os.path.isdir(os.path.join('C:/Users/11602/Desktop/WebScraping/MyAO3Crawler', 'x鸣佐x--AO3')))
