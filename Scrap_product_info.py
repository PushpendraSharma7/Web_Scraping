import requests
from lxml import html
import SaveToDatabase as db
def scrapProduct(productURL):
    base_url = "https://www.flipkart.com"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    payload = {}
    s = requests.Session()

    response = s.request("GET", base_url, headers=headers, data=payload)  # For creating the session

    webUrl = s.request("GET", productURL, headers=headers, data=payload)
    tree = html.fromstring(webUrl.content)

    Name = tree.xpath('//div//span[@class="B_NuCI"]/text()')
    ProductName=ProductName=str(Name).split('-')[0].split('[')[1]
    Original_Price = tree.xpath('//div[@class="_3I9_wc _2p6lqe"]/text()[1] | //div[@class="_3I9_wc _2p6lqe"]/text()[2]')
    Product_Original_Price=str(Original_Price[0])+str(Original_Price[1])
    Product_Discounted_Price = tree.xpath('//div[@class="aMaAEs"]/div[4]/div/div/div[1]/text() | //div[@class="aMaAEs"]/div[3]/div/div/div[1]/text()')[0]
    ModelNumber = tree.xpath('//div[@class="_3k-BhJ"][1]/table/tbody/tr[2]/td[2]/ul/li/text()')[0]
    ProcessorDetails=tree.xpath('//div[@class="_3k-BhJ"][2]/table/tbody/tr[3]/td[2]/ul/li/text() | //div[@class="_3k-BhJ"][2]/table/tbody/tr[4]/td[2]/ul/li/text() |/'
                                ' //div[@class="_3k-BhJ"][2]/table/tbody/tr[5]/td[2]/ul/li/text()')
    Processor= str(ProcessorDetails[0])+ ' ' +str(ProcessorDetails[1])
    RAM = tree.xpath('//div[@class="_3k-BhJ"][2]/table/tbody/tr[8]/td[2]/ul/li/text()')[0]
    OperatingSysytem=tree.xpath('//div[@class="_3k-BhJ"][3]/table/tbody/tr[2]/td[2]/ul/li/text() | //div[@class="_3k-BhJ"][3]/table/tbody/tr[1]/td[2]/ul/li/text()')[0]


    db.Save([ProductName, Product_Original_Price, str(Product_Discounted_Price), str(ModelNumber), Processor, str(RAM), str(OperatingSysytem)], 'SaveProduct')


