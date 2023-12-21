import bs4
import requests

res = requests.get("https://www.amazon.in/s?k=automate+the+boring+stuff&ref=nb_sb_noss")
# res.raise_for_status()
soup = bs4.BeautifulSoup(res.text) # the second argument passed to delte the ugly code
price_div = soup.select('')
print(price_div)
 
