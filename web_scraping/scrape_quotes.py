import requests
import bs4 

results = requests.get("http://quotes.toscrape.com")

soup = bs4.BeautifulSoup(results.text,"lxml")

quotes = soup.select(".quote")

for quote in quotes :

    author = quote.select(".author")
    text = quote.select(".text")

    print(text[0].get_text()+ " by "+author[0].get_text())

