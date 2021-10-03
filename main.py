from bs4 import BeautifulSoup

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

import nltk
from collections import Counter


def get_data(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        print('The server could not be found!')
        return None
    bs = BeautifulSoup(html.read(), 'html.parser')
    tokenized = nltk.word_tokenize(bs.text)
    tagged = nltk.pos_tag(tokenized)
    c = Counter()
    for word, tag in tagged:
        c[tag] += 1
    print('Имена собственные: ' + str(c['NN']) + '\n' + 'Предлоги: ' + str(c['IN']) + '\n' + 'Определитель: ' + str(c['DT']) + '\n' + 'Прилагательное: ' + str(c['JJ']))

get_data('https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt')

