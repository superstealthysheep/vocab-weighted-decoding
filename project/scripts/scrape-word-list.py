from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = "https://www.talkenglish.com/vocabulary/top-2000-vocabulary.aspx"

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

def clean_text(input):
    return re.sub("\s+", " ", input).strip()

words,freqs,poses = [],[],[]
table = soup.findChildren('table')[1]
for row in table.findChildren('tr')[3:]:
    children = row.findChildren("td")
    # print(len(children))
    # pr
    # word,freq,pos = map(str.strip(children[i].), )
    # print(row.text)
    word = clean_text(children[1].text)
    freq = clean_text(children[2].text)
    pos = clean_text(children[4].text)
    words.append(word)
    freqs.append(freq)
    poses.append(pos)
    # print(word, freq, pos)
    # print(row.text.split())
    # word,freq,pos = row.text.split()

df = pd.DataFrame(data={'word': words, 'freq': freqs, 'pos': poses})
df.to_csv("../data/vocab_2000.csv")

# soup.findChildren('table')[1].findChildren("tr")[5].find_all('td')[1].text.strip() 