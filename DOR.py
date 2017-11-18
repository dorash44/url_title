import requests
from bs4 import BeautifulSoup

def article_titles():# function that print all titles in new your times
    url = "https://www.nytimes.com/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('h2', {'class': 'story-heading'}):  # takes all the links of titles
        title = link.string  # save the title
        print(title)


article_titles()