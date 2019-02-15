import requests
from bs4 import BeautifulSoup
import lxml
from urllib.parse import urlparse, parse_qs

url = 'https://www.rightmove.co.uk/property-to-rent/property-79047791.html'

def main(url):
    if which_site(url) == 'rightmove':
        soup = soup_creator(url)
        right_move_dict = {}
        price, latitude, longitude, furnish_type = right_move_parser(soup)
        for i in ('price', 'latitude', 'longitude', 'furnish_type'):
            # the locals()[i] specifies the scope to i otherwise soup will also be outputed since it is in local scope
            right_move_dict[i] = locals()[i]
        return right_move_dict
    else:
        pass

def which_site(url):
    if 'rightmove' in url:
        return 'rightmove'
    else:
        pass

def soup_creator(url):
    try:
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data, 'lxml')
        return soup
    except Exception as e:
        print(e)
        return False

# Calls sub-functions that parse individual variables
def right_move_parser(soup):
    try:
        price = price_strip(soup)
        latitude, longitude = long_lat_strip(soup)
        furnish_type = furnish_strip(soup)
        return price, latitude, longitude, furnish_type
    except TypeError:('type error')
    except Exception as e:
        print(e)
        return False, False, False, False

def price_strip(soup):
    price_tag = soup.select('p#propertyHeaderPrice > strong')
    price = price_tag[0].text.strip()
    return price

def long_lat_strip(soup):
    location = soup.findAll("a", {"href":"#location"})
    for item in location:
        data = item.find("img", {"alt":"Get map and local information"})
        if data:
            url_content = urlparse(data['src'])
            query_string = parse_qs(url_content.query)
            latitude = float(query_string['latitude'][0])
            longitude = float(query_string['longitude'][0])
    return latitude, longitude

def furnish_strip(soup):
    info = soup.select('div#lettingInformation')
    furnish_type = info[0].find("td", {"id":"furnishedType"}).text
    return furnish_type
       

print(main(url))
