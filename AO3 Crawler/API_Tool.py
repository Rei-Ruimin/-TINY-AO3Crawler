import requests
import os
from bs4 import BeautifulSoup
import pickle
from PyQt5.Qt import *
import datetime


def generate_proxy_list():
    res = requests.get('https://free-proxy-list.net/', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, "lxml")
    proxy_list = []
    for items in soup.select("#proxylisttable tbody tr"):
        proxy = ':'.join([item.text for item in items.select("td")[:2]])
        proxy_list.append(proxy)
    return proxy_list


class Article:
    author = None
    title = None
    pdf_url = None

    def __init__(self, title=None, author=None, pdf_url=None, url=None):
        self.author = author
        self.title = title
        self.pdf_url = pdf_url
        self.url = url

    def print_all(self):
        print("AUTHOR: {}".format(self.author))
        print("TITLE: {}".format(self.title))
        print("PDF URL: {}".format(self.pdf_url))

    def print(self):
        print("scraping {} by {}".format(self.title, self.author))

    def get_info(self):
        return "scraping {} by {}".format(self.title, self.author)


# store anything about URL
class URL:
    basic_url = "https://archiveofourown.org"

    # search url: sort by default (best match)
    @staticmethod
    def get_search_url(topic):
        return "https://archiveofourown.org/works/search?utf8=%E2%9C%93&work_search%5Bquery%5D={}".format(topic)

    # get the url of next page, return None if there's no url
    @classmethod
    def get_next_page_url(cls, soup):
        # soup is valid
        # if there's next page
        try:
            return cls.basic_url + soup.find("li", {"title": "next", "class": "next"}).a.attrs['href']
        # last page
        except AttributeError:
            return None


class MyCrawler(QObject):
    session = requests.session()
    basic_url = "https://archiveofourown.org"
    proxy_list = generate_proxy_list()
    proxy_idx = 240
    progress_msg_signal = pyqtSignal(str)
    ip_blocked_signal = pyqtSignal()

    def get_random_proxy(self):
        # myproxy = random.choice(proxy_list)
        myproxy = self.proxy_list[self.proxy_idx]
        self.proxy_idx = self.proxy_idx % len(self.proxy_list)
        return myproxy

    def download_pdf(self, file_url, save_dir, file_name):
        proxies = {'http': 'http://' + self.get_random_proxy()}
        r = requests.get(file_url, proxies=proxies, allow_redirects=True)
        with open(os.path.join(save_dir, file_name + '.pdf'), 'wb') as f:
            f.write(r.content)

    # return the beautifulsoup obj of given url
    def getBS(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            cookies = {"view_adult": "true"}
            proxies = {'http': 'http://' + self.get_random_proxy()}
            req = requests.get(url, headers=headers, cookies=cookies, proxies=proxies)

        except requests.exceptions.RequestException:
            msg = "RequestException! error with url"
            print(msg)
            self.progress_msg_signal.emit(msg)
            return None
        return BeautifulSoup(req.text, 'html.parser')

    # return the pdf_url using the bs obj of a single work page
    def parse_single_work_page(self, soup):
        try:
            pdf_url = soup.find("ul", {"class": "work navigation actions", "role": "menu"}). \
                find('ul', {"class": "expandable secondary"}). \
                find(lambda tag: tag.get_text() == 'PDF').a.attrs['href']
        # if the ip is blocked
        except AttributeError:
            print(soup)
            self.progress_msg_signal.emit("Retry later!")
            # save the article set
            return None

        return self.basic_url + pdf_url

    # starts from the given search_url, crawl page by page until there's no next page button
    # return a set of Article obj
    def parse_search_page_by_page(self, search_url, article_set, topic, save_dir, work_url_set):
        bs = self.getBS(search_url)

        work_num_str = bs.find(lambda tag: tag.name == "h3" and "Found" in tag.text).get_text().split()
        work_num = work_num_str[0]
        msg = f'{work_num} works found'
        print(msg)
        self.progress_msg_signal.emit(msg)
        current_search_page_url = search_url
        while True:
            # get the info of works in this page
            works = bs.find("ol", {"class": "work index group"})
            for work in works.findAll('li', {"class": "work blurb group"}):
                title = work.find("h4", {"class": "heading"}).findAll('a')[0].get_text()
                author = work.find("h4", {"class": "heading"}).findAll('a')[1].get_text()
                work_url = work.find("h4", {"class": "heading"}).findAll('a')[0].attrs['href']

                if work_url not in work_url_set:
                    # get the pdf url of that work
                    work_bs = self.getBS(self.basic_url + work_url)
                    pdf_url = self.parse_single_work_page(work_bs)
                    # if IP is not blocked
                    if pdf_url:
                        article = Article(title, author, pdf_url, work_url)
                        article_set.add(article)
                        article.print()
                        work_url_set.add(work_url)
                        self.progress_msg_signal.emit(article.get_info())
                    # if IP is blocked, pdf_url == None
                    else:
                        # save the current search page url and article set
                        save_dict = {"current_search_page_url": current_search_page_url,
                                     "article_set": article_set,
                                     'topic': topic,
                                     'save_dir': save_dir,
                                     'work_url_set': work_url_set}
                        with open(os.path.join(os.path.dirname(__file__), "scraping_file.dictionary"), 'wb') as file:
                            pickle.dump(save_dict, file)

                        return -1
                else:
                    continue

            # IP block when clicked next page
            if URL.get_next_page_url(bs) == -1:
                save_dict = {"current_search_page_url": current_search_page_url,
                             "article_set": article_set,
                             'topic': topic,
                             'save_dir': save_dir,
                             'work_url_set': work_url_set}
                with open(os.path.join(os.path.dirname(__file__), "scraping_file.dictionary"), 'wb') as file:
                    pickle.dump(save_dict, file)
                return -1
            # there's a next page
            elif URL.get_next_page_url(bs):
                print(f'current_search_page_url: {current_search_page_url}')
                current_search_page_url = URL.get_next_page_url(bs)
                bs = self.getBS(current_search_page_url)

                # have to make sure bs is valid
                # check if the page have clickable previous button
                try:
                    previous_page_tag = bs.find("li", {"title": "previous", "class": "previous"}).a.attrs['href']
                # if there's no previous page -- retry page -- ip blocked!
                except AttributeError:
                    save_dict = {"current_search_page_url": current_search_page_url,
                                 "article_set": article_set,
                                 'topic': topic,
                                 'save_dir': save_dir,
                                 'work_url_set': work_url_set}
                    with open(os.path.join(os.path.dirname(__file__), "scraping_file.dictionary"), 'wb') as file:
                        pickle.dump(save_dict, file)

                    return -1

                msg = "-" * 20 + f'{len(article_set)}/{work_num}' + "-" * 20
                print(msg)
                self.progress_msg_signal.emit(msg)
                # time.sleep(random.randint(2, 10))
            # there's no next page
            else:
                msg = "-" * 20 + f"Finished scraping {len(article_set)} works" + "-" * 20 + "\n"
                print(msg)
                self.progress_msg_signal.emit(msg)
                return article_set

    def handle_article_set(self, article_set, save_dir, topic):
        # make sure the directory is valid
        topic = check_forbidden_char(topic)
        parent_dir = os.path.join(save_dir, (topic + '--AO3'))
        os.mkdir(parent_dir)
        os.chdir(parent_dir)

        saved_author_list = []
        saved_work_count = 0
        total_work_num = len(article_set)
        for article in article_set:
            title_checked = check_forbidden_char(article.title)
            author_checked = check_forbidden_char(article.author)
            msg = "saving " + article.title + " by " + article.author

            if title_checked != article.title:
                msg += f" (title adjusted to {title_checked})"
            elif author_checked != article.author:
                msg += f" (author adjusted to {author_checked})"

            print(msg)
            self.progress_msg_signal.emit(msg)
            saved_work_count += 1
            if saved_work_count % 20 == 0:
                msg = "-" * 20 + f'{saved_work_count}/{total_work_num}' + '-' * 20
                print(msg)
                self.progress_msg_signal.emit(msg)

            path = os.path.join(parent_dir, author_checked)
            if author_checked in saved_author_list:
                self.download_pdf(article.pdf_url, path, title_checked)
            # create new folder named with this new author
            else:
                os.mkdir(path)
                self.download_pdf(article.pdf_url, path, title_checked)
                saved_author_list.append(author_checked)

        msg = '-' * 20 + f"Finished saving {saved_work_count} works" + '-' * 20
        print(msg)
        self.progress_msg_signal.emit(msg)
        # txt msg
        with open(os.path.join(parent_dir, 'infomation.txt'), "w") as file:
            file.write(f"The program finished at {datetime.datetime.now()}\n"
                       f"Total number of work: {saved_work_count}\n"
                       f"Total number of author: {len(saved_author_list)}\n")

    def crawl_and_save_by_key_word(self, topic, save_dir):
        article_set = set()
        work_url_set = set()
        article_set = self.parse_search_page_by_page(URL.get_search_url(topic), article_set, topic, save_dir, work_url_set)

        # if IP is blocked
        if article_set == -1:
            self.progress_msg_signal.emit(f"Oops, the IP is blocked at {datetime.datetime.now()}!\n"
                                          f"Don't worry, the current data is saved. Please reopen "
                                          f"the program and continue the web scraping later (at least 10 minutes)")
            self.ip_blocked_signal.emit()
        else:
            self.handle_article_set(article_set, save_dir, topic)

    def crawl_and_save_by_search_url(self, search_url, save_dir):
        article_set = set()
        work_url_set = set()
        article_set = self.parse_search_page_by_page(search_url, article_set, "your_result", save_dir, work_url_set)

        # if IP is blocked
        if article_set == -1:
            self.progress_msg_signal.emit(f"Oops, the IP is blocked at {datetime.datetime.now()}!\n"
                                          f"Don't worry, the current data is saved. Please reopen "
                                          f"the program and continue the web scraping later (at least 10 minutes)")
            self.ip_blocked_signal.emit()
        else:
            self.handle_article_set(article_set, save_dir, "your_result")

    def continue_crawling(self):
        with open(os.path.join(os.path.dirname(__file__), "scraping_file.dictionary"), 'rb') as file:
            save_D = pickle.load(file)
            search_url = save_D["current_search_page_url"]
            article_set = save_D["article_set"]
            topic = save_D['topic']
            save_dir = save_D['save_dir']
            work_url_set = save_D['work_url_set']

        article_set = self.parse_search_page_by_page(search_url, article_set, topic, save_dir, work_url_set)
        # if IP is blocked
        if article_set == -1:
            self.progress_msg_signal.emit(f"Oops, the IP is blocked at {datetime.datetime.now()}!\n"
                                          f"Don't worry, the current data is saved. Please reopen "
                                          f"the program and continue the web scraping later (at least 10 minutes)")
            self.ip_blocked_signal.emit()
        else:
            self.handle_article_set(article_set, save_dir, topic)
            os.remove(os.path.join(os.path.dirname(__file__), "scraping_file.dictionary"))


def check_forbidden_char(str):
    forbidden_chars = '\ / : * ? " < > |'.split()
    for char in forbidden_chars:
        if str.find(char) != -1:
            str = str.replace(char, 'x')
    return str


if __name__ == '__main__':
    # ao3crawler = MyCrawler()
    # ao3crawler.continue_crawling()
    # os.remove("scraping_file.dictionary")
    print(os.path.dirname(__file__))
    # ao3crawler.crawl_and_save_by_key_word("白兰/入江正一",'C:/Users/11602/Desktop/WebScraping/MyAO3Crawler')
    # ao3crawler.crawl_and_save_by_search_url(
    #     'https://archiveofourown.org/works/search?utf8=%E2%9C%93&work_search%5Bquery%5D=%22%E9%B8%A3%E4%BD%90%22',
    #     'C:/Users/11602/Desktop/WebScraping/MyAO3Crawler')
    # go_through_all_things_way2("https://archiveofourown.org/works/search?utf8=%E2%9C%93&work_search%5Bquery%5D=%E2%80%9D%E5%8D%9A%E4%BD%90%E2%80%9C",
    #                            'C:/Users/11602/Desktop/WebScraping/MyAO3Crawler')
    # with open("current_search_page_url", 'rb') as file:
    #     bs = pickle.load(file)
    # print(bs)

    # bs = APITool.getBS(URL.get_search_url('"鸣佐"'))
    #
    # work_num_str = bs.find(lambda tag: tag.name == "h3" and "Found" in tag.text).get_text().split()
    # work_num = work_num_str[0]
    # print(f'{work_num} works found')
