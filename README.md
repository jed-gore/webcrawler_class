# webcrawler_class

Something to save searches because I always forget the syntax for Beautiful Soup.

Remember: always scrape responsibly according to Terms of Service.

Includes a class WebCrawler with methods:
get_html_document()
get_links()
and 
get_tables()

Usage: 
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    w = WebCrawler(url)
    print(w.get_tables(1))
    
![image](https://user-images.githubusercontent.com/39496491/222904327-07476c12-332b-4c94-837e-46a0cae682b8.png)

Also includes a c.py file to handle certification updates for Mac's with fresh python installs so pandas' read_html works on a Mac.
