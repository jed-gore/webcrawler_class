from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# class to save typing
class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_html_document(self):

        # request for HTML document of given url
        response = requests.get(self.base_url)

        # response will be provided in JSON format
        self.html_document = response.text
        self.soup = BeautifulSoup(self.html_document, "html.parser")

        return

    def get_links(self, print_list=False):
        self.links = []
        for link in self.soup.find_all("a", href=True):
            if print_list == True:
                print(link["href"])
            self.links.append(link)
        return

    def get_tables(self, table_num=""):
        self.tables = pd.read_html(self.base_url)
        if table_num != "":
            return self.tables[table_num]
        return


if __name__ == "__main__":
    #    url = "https://practice.geeksforgeeks.org/courses/"
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    w = WebCrawler(url)
    #    w.get_html_document()
    #    w.get_links(print_list=True)
    print(w.get_tables(1))
