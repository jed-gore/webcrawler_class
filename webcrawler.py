from bs4 import BeautifulSoup
import requests
import re


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

    def get_links(self):
        self.links = []
        for link in self.soup.find_all("a", href=True):
            print(link["href"])
            self.links.append(link)


if __name__ == "__main__":
    url = "https://practice.geeksforgeeks.org/courses/"
    w = WebCrawler(url)
    w.get_html_document()
    w.get_links()
