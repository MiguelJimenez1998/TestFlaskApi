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

async def main(start_pag=1, pags_ago=dato):
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
            pag = (i+1) * 48

        pages_content = await asyncio.gather(*tasks) 
        return pages_content


results = asyncio.run(main())

#output_dir = pathlib.Path().resolve() / "snapshots"
#output_dir.mkdir(parents=True, exist_ok=True)



from bs4 import BeautifulSoup
link_house=[]

for result in results:
    print(len(results))
    #current_pag = result.get("pag")
    '''
    html_data = result.get('body')
    soup = BeautifulSoup(html_data , 'lxml')
    for a in soup.find_all('a', class_="item__info-link"):
         link_house.append(a['href'])
    '''
    #output_file = output_dir / f"{current_pag}.html"
    #output_file.write_text(html_data.decode())

#print(len(link_house))

#import requests
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_data , 'lxml')


#for a in soup.find_all('a', class_="item__info-link"):
 #   print("Found the URL:", a['href']) 




#class="item__info-link"