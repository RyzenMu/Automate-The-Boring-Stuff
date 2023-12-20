import bs4
import requests

res = requests.get("https://www.amazon.in/s?k=automate+boring+stuff+with+python&adgrpid=1327112144093773&hvadid=82944779187287&hvbmt=bp&hvdev=c&hvlocphy=149260&hvnetw=o&hvqmt=p&hvtargid=kwd-82945388991580%3Aloc-90&hydadcr=25339_2784053&tag=msndeskstdin-21&ref=pd_sl_kxeqs8yz8_p")
# res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser') # the second argument passed to delte the ugly code
price_div = soup.select('#search > div.s-desktop-width-max.s-desktop-content.s-wide-grid-style-t1.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(7) > div > div > span > div > div > div > div.puisg-col.puisg-col-4-of-12.puisg-col-8-of-16.puisg-col-12-of-20.puisg-col-12-of-24.puis-list-col-right > div > div > div.puisg-row > div.puisg-col.puisg-col-4-of-12.puisg-col-4-of-16.puisg-col-4-of-20.puisg-col-4-of-24 > div > div.a-section.a-spacing-none.a-spacing-top-micro.puis-price-instructions-style > div:nth-child(2) > div:nth-child(1) > a > span > span:nth-child(2) > span.a-price-whole')
print(price_div)
 
