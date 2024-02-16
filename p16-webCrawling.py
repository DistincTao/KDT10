import requests
from bs4 import BeautifulSoup
import pymysql
import urllib.request
import time

pageno = 1
targetUrl = "https://lemite.com/product/list.html?cate_no=43&page=" + str(pageno)
baseUrl = 'https://lemite.com/'

headers = {'User-Agent' : 'Mozilla/5.0'}
resp = requests.get(targetUrl, headers=headers)
resp.encoding = 'utf-8'
html = resp.text
# print (html)

if html is not None :
    html = BeautifulSoup(html, 'html.parser')
# print (html)

    try : # 아래의 코드를 수행 
        products = html.find('ul', class_='prdList column4')
        # print(products)
    except : # 예외가 발생하면
        print('Parsing할 상품이 없습니다')
    else :
        products = products.find_all('li', class_= 'item xans-record-')
        for item in products :
            # print(item)
            print("-------------------")
            item.find('p', class_ = 'name').find('a').attrs['href']
            # print(item.find('p', class_ = 'name').find('a').attrs['href'])
            # 상세 페이지 주소
            detailPage = baseUrl + item.find('p', class_ = 'name').find('a').attrs['href']
            # print(detailPage)

            productName = item.find('p', class_= 'name').text.split(":")[1].strip()
            # print(productName)

            thumbNameImg = 'http:' + item.find('div', class_= 'prdimg').find('img').attrs['src']
            # print(thumbNameImg)
            
            # 상품 번호
            startPos = detailPage.find('product_no=') + len('product_no=')
            endPos = detailPage.find('&')
            productNo = detailPage[startPos : endPos]
            # print(productNo)

            productDescription = item.find('li', class_ = "xans-record-").text.split(":")[1].strip()
            # print(productDescription)

            # 판매가
            price = item.find('li', class_ = "xans-record-").find_next('li').text.split(":")[1].strip().replace(",","").replace('원', "")
            # print(price)

            # 할인 판매가
            discountPrice = item.find('li', attrs={'name' : '할인판매가'}).text.split(":")[1].split('원')[0].replace(",","")
            discountRate = item.find('li', attrs={'name' : '할인판매가'}).text.split(":")[1].split('원')[1].replace("%", "")
            # print(discountPrice)
            # print(discountRate)

            print(productName, thumbNameImg, productNo, productDescription, price, discountPrice, discountRate)

            # ----- 이미지 저장 -----
            imagePath = "D:\Lectures\Python\\testthumb\\"
            urllib.request.urlretrieve(thumbNameImg, imagePath + "thumbNail_" + productNo + thumbNameImg[-4:])
