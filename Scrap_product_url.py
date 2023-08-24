import requests
from lxml import html
import SaveToDatabase as db

def scrapProductURL(catURL):
    base_url = "https://www.flipkart.com"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    payload = {}
    s = requests.Session()

    response = s.request("GET", base_url, headers=headers, data=payload) # For creating the session

    response2 = s.request("GET", catURL, headers=headers, data=payload)
    tree = html.fromstring(response2.content)
    prod_url=tree.xpath('//a[@class="_1fQZEK"]/@href')
    if len(prod_url)==0:
        prod_url=tree.xpath('//div[@class="_13oc-S"]/div/div/a[@class="_2UzuFa"]/@href')
    # print(prod_url)
    for url in prod_url:
        # print(url)
        completeUrl=base_url+url
        db.Save([completeUrl], 'SaveProductURL')








