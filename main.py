from time import sleep

import Scrap_product_url
import Scrap_product_info
import SaveToDatabase as db
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def main():
    CategoryUrl=db.GetData('getCategoryUrl')
    for cURL in CategoryUrl:
        catURL=cURL[1]
        Id=cURL[0]
    # catURL = "https://www.flipkart.com/6bo/b5g/~cs-hbtuge4qub/pr?sid=6bo%2Cb5g&collection-tab-name=Gaming&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkdhbWluZyBMYXB0b3BzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=25.productCard.PMU_V2_5"
        Scrap_product_url.scrapProductURL(catURL)
        db.Save([Id], 'updateCategoryCrawlStatus')

    productUrls=db.GetData('getProductUrl')
    for pUrl in productUrls:
        prodUrl=pUrl[0]
        Id=pUrl[1]
        print(prodUrl)
    # prodUrl = 'https://www.flipkart.com/dell-g15-core-i5-12th-gen-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-120-hz-gaming-laptop/p/itm4f9464f994e0f?pid=COMGDJJYAJYPTS4Y&lid=LSTCOMGDJJYAJYPTS4YDCSWYX&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_10&otracker=browse&fm=organic&iid=faf03caa-c1a5-43c0-812f-e657919c165f.COMGDJJYAJYPTS4Y.SEARCH&ppt=None&ppn=None&ssid=gf94iidh6o0000001691572915766'
        Scrap_product_info.scrapProduct(prodUrl)
        db.Save([Id],'updateProductCrawlStatus')
        sleep(5)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
