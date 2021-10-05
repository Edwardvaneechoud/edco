

from newspaper import Article
from googlesearch import search
from usp.tree import sitemap_tree_for_homepage as stfp
from urllib.parse import urlparse
import re


def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

class website:
    def __init__(self,url):
        self.url = formaturl(url)
        self.parsed_url= urlparse(url)
        self.base_url = self.parsed_url.netloc
        self.base_url_main_url = self.parsed_url.path==''

class search_scraper:
    def __init__(self, query):
        first_10 = search(query,num=10,stop=10)
        self.urls = [u for u in first_10]


class pagescraper(Article):
    def __init__(self, url):
        super().__init__(formaturl(url))

    def scrape_news(self):
        self.download()
        self.parse()



ps = website('https://tiekinetix.com')



def article_info(results=["link1", "link2"], save_text=False):
    full_output = []
    for idx, val in enumerate(results):
        output = {}
        print(val)
        output['id'] = query_input.id
        output['rank'] = idx
        output['url'] = val
        article = Article(output['url'])
        try:
            article.download()
            article.parse()

            print(len(article.text))
            if len(article.text) != 0:
                article.nlp()
                output['title'] = article.title
                output['content'] = article.text
                output['keywords'] = article.keywords
                output['summary'] = article.summary
                output["key_sentences"] = []
                output["language_of_content"] = detect(output['content'])
                for ranking, ks in enumerate(keysentence(output['content'], query_input.language)):
                    ks['rank'] = ranking
                    output["key_sentences"].append(ks)
                if not save_text:
                    del output['content']
                if output["language_of_content"] == query_input.language:
                    full_output.append(output)
        except:
            print("no info")
    return full_output
