'''
from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "hola"

if __name__ == '__main__':
    app.run()



'''




import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import pathlib
import argparse
import math

parser=argparse.ArgumentParser(description='Prueba TrueHome')
parser.add_argument('-n','--numero',type=int, help='Total to customize the number of houses',default=150)
args = parser.parse_args()

dato=math.ceil(args.numero/48)


async def fetch(url, session, pag):
    async with session.get(url) as response:
        html_body = await response.read()
        return {"body": html_body, "pag": pag}  

async def page(start_pag=1, pags_ago=dato):
    html_body = ""
    tasks = []
    pag = start_pag

    async with ClientSession() as session: 
        for i in range(0, pags_ago):
            url = f'https://inmuebles.metroscubicos.com/distrito-federal/_Desde_{pag}'
            print("pag", pag, url)
            tasks.append(
                asyncio.create_task(
                    fetch(url, session, pag)
                )
            )
            pag = ((i+1) * 48)+1

        pages_content = await asyncio.gather(*tasks) 
        return pages_content

results = asyncio.run(page())


async def house(start_pag=0, pags_ago=args.numero):
    html_body = ""
    tasks = []

    async with ClientSession() as session: 
        for i in range(0, pags_ago):
            pag=i+1
            url = link_house[i]
            #print("pag", pag, url)
            tasks.append(
                asyncio.create_task(
                    fetch(url, session, pag)
                )
            )
        pages_content = await asyncio.gather(*tasks) 
        return pages_content




link_house=[]

for result in results:
    html_data = result.get('body')
    soup = BeautifulSoup(html_data , 'lxml')
    for a in soup.find_all('a', class_="item__info-link"):
         link_house.append(a['href'])

results = asyncio.run(house())


names=[]
prices=[]
descriptions=[]
amenities=[]
sizes=[]
images=[]
adress=[]

for result in results:
    html_data = result.get('body')
    soup = BeautifulSoup(html_data , 'lxml')

    name = soup.find_all(class_="vip-product-info__development__name")
    for i in name:
        names.append(i.text)

    price= soup.find_all('strong', limit=1)
    for i in price:
        prices.append(i.text)
    
    description= soup.find_all(class_="preformated-text",limit=1)
    for i in description:
        descriptions.append((i.text).strip())
    
    amenitie = soup.find_all(class_="boolean-attribute-list",limit=1)
    for i in amenitie:
       amenities.append((i.text).strip())

    size = soup.find_all(class_="vip-product-info__attribute-value",limit=1)
    for i in size:
       sizes.append(i.text)
    
    image = soup.findAll('img',limit=1)
    for i in image:
        images.append(i['src'])
 
   
    adres = soup.find_all(class_="map-location")
    for i in adres:
       adress.append(i.text)


