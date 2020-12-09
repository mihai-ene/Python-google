import requests
from bs4 import BeautifulSoup

def getImage(article):
    image = article.find('div',{'class' : 'image_container'})
    location = image.find('a').get('href')
    return location

def getName(article):
    name = article.find('h3').find('a').get('title')
    return name

def getPrice(article):
    price = article.find('div',{'class':'product_price'}).find('p',{'class':'price_color'}).getText()
    return price

def getBooks(object):
    col = ['image', 'name', 'price']
    article = object.find('article', {'class': 'product_pod'})
    image = getImage(article)
    name = getName(article)
    price = getPrice(article)
    data = [image, name, price]

    return dict(zip(col,data))


URL = 'http://books.toscrape.com/catalogue/category/books/science_22/index.html'

if __name__ == '__main__':
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features='html.parser')

    table = soup.find('ol',{'class' : 'row'})
    objects = table.findAll('li',{'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3' })
    books = list(map(getBooks,objects))
    print(books)



