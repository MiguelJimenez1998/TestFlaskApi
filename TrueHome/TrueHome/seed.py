import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import pathlib
import argparse
import math

#parser=argparse.ArgumentParser(description='Prueba TrueHome')
#parser.add_argument('-n','--numero',type=int, help='Total to customize the number of houses',default=150)
#rgs = parser.parse_args()

def scrapy (num_cantidad):
    dato=math.ceil(num_cantidad/48)


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


    async def house(start_pag=0, pags_ago=num_cantidad):
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


    campos=[]

    for result in results:
        
        html_data = result.get('body')
        soup = BeautifulSoup(html_data , 'lxml')

        name = soup.find_all(class_="vip-product-info__development__name")
        name=name[0].text if len(name) > 0 else None

        price= soup.find_all('strong', limit=1)
        price= price[0].text if len(price) > 0 else None
    
        description= soup.find_all(class_="preformated-text",limit=1)
        description=(description[0].text).strip() if len(description) > 0 else None

        amenitie = soup.find_all(class_="boolean-attribute-list",limit=1)
        amenitie = (amenitie[0].text).strip() if len(amenitie) > 0 else None

        size = soup.find_all(class_="vip-product-info__attribute-value",limit=1)
        size = size[0].text if len(size) > 0 else None
        
        image = soup.findAll('img',limit=1)
        image = image[0]['src'] if len(image) > 0 else None
    
        adress = soup.find_all(class_="map-location")
        adress = adress[0].text if len(adress) > 0 else None
        adress = adress.split(",")
        if adress[0].split(" ")[-1].isdigit():
            num=adress[0].split(" ")[-1]
            calle=" ".join(adress[0].split(" ")[:-1])
        else:
            num=None
            calle=adress[0]

        sett=adress[1] if len(adress) >= 2 else None
        town=adress[2] if len(adress) >= 3 else None
        state=" ".join(adress[3:]) if len(adress) >= 4 else None
        country="Mexico"

        campos.append([name,price,description,amenitie,size,image,[calle,num,sett,town,state,country]])
    return(campos)






