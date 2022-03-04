import requests
from html.parser import HTMLParser
import html5lib
from bs4 import BeautifulSoup
import pprint

def scrapeShops():
    shopMasterDict = {} 

    j = 1
    while j <= 50:
        url = "https://www.yelp.com/search?find_desc=coffee+shop&find_loc=Chicago%2C+IL+60608&ns=1&start=" + str(j * 10)
        data = requests.get(url)
        scraper = BeautifulSoup(data.text, 'html5lib')
        #list of allshops 
        timeline = scraper.find_all('li', {'class':"border-color--default__09f24__NPAKY"}, recursive=True)
        i = 0
        while i < 20:
            try:
                shopDict = {}
                childContainer = timeline[i].find_all('div', {'class':"container__09f24__mpR8_ hoverable__09f24__wQ_on margin-t3__09f24__riq4X margin-b3__09f24__l9v5d padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border--top__09f24__exYYb border--right__09f24__X7Tln border--bottom__09f24___mg5X border--left__09f24__DMOkM border-color--default__09f24__NPAKY"})
                #pulling shop name and image link from left sib container
                childImageContainer = childContainer[0].find_all('div' , {'class' : "arrange-unit__09f24__rqHTg border-color--default__09f24__NPAKY"}, recursive=True )
                shopImage = childImageContainer[0].find('img', {'class' : "css-xlzvdl"}, recursive = True).get('src')
                shopName = childImageContainer[0].find('img', {'class' : "css-xlzvdl"}, recursive = True).get('alt')
                #pulling shop data from right sub container
                childDataContainer = childContainer[0].find_all('div' , {'class' : "arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG border-color--default__09f24__NPAKY"}, recursive=True )
                #pulling various items from data container
                shopLocation = childDataContainer[0].find_all('span', {'class': "css-1e4fdj9"})[1].contents
                shopNumReviews = childDataContainer[0].find_all('span', {'class': "css-1e4fdj9"})[0].contents
                shopTag = childDataContainer[0].find_all('p', {'class': "css-1p8aobs"})[0].contents
                shopRating = childDataContainer[0].find_all('div', {'class' : "i-stars__09f24__foihJ i-stars--regular-4-half__09f24__hBtsc border-color--default__09f24__NPAKY overflow--hidden__09f24___ayzG"}, recursive=True)[0].get('aria-label')
                #adding data to master dictionary, key is shop name
                shopDict[shopName] = (shopImage, shopLocation, shopRating, shopNumReviews, shopTag)
                shopMasterDict.update(shopDict)
            except IndexError:
                IndexError
            i += 1
        j += 1  

    return shopMasterDict