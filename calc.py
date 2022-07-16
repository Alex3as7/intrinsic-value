import requests,json
from bs4 import BeautifulSoup

corp_bond = 3.94

def get_g(ticker):

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
    url = f'https://finance.yahoo.com/quote/{ticker}/analysis'

    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    g = soup.find('section',{'class':'smartphone_Px(20px) smartphone_Pt(10px)'}).find_all('table')[5].find_all('tr')[5].find_all('td')[1].text

    g = g.replace('%','')
    
    if g == 'N/A':
        return 1
    else:
        return float(g)

def get_aaa():

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
    url = 'https://ycharts.com/indicators/moodys_seasoned_aaa_corporate_bond_yield'

    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    aaa = soup.find('td',{'class':'text-right'}).text

    aaa = aaa.replace('%','')
    
    return float(aaa)


def calc_value(current_price,eps,g,aaa):

    val = (eps*(8.5+(2*g))*corp_bond)/aaa
    upside = (val/current_price-1)*100

    if val > current_price:
        return {'int_val':val,'upside':upside,'buy':'BUY'}
    else:
        return {'int_val':val,'upside':upside,'buy':'SELL'}


def request_data(ticker):


    url = "https://yfapi.net/v6/finance/quote"

    querystring = {"symbols":ticker,"region":"GB"}

    with open('json/api_key.json', 'r') as j:
        key = json.loads(j.read())["key"]

    headers = {
        'x-api-key': key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    return data['quoteResponse']['result']

