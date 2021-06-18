import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")
import django
django.setup()
from quiz.models import Player_info
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import pandas as pd
def crawler():
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
    url=f"https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?ajax=yw1&page=1"
    response=requests.get(url,headers=headers)
    player_list=[]
    number=[]
    name=[]
    position=[]
    age=[]
    nation=[]
    team=[]
    value=[]
    if response.status_code==200:
        soup=BeautifulSoup(response.content,'html.parser')
        string=soup.find_all('tr',{'class':['odd','even']})
    for info in string:
        information=info.find_all('td')
        #number=information[0].get_text()
        #name=information[3].get_text()
        #position=information[4].get_text()
        #age=information[5].get_text()
        #nation=information[6].img['alt']
        #team=information[7].img['alt']
        #value=information[8].span['title']
        #player={'number':number,'name':name,'position':position,'age':age,'nation':nation,'team':team,'value':value}
        number.append(information[0].get_text())
        name.append(information[3].get_text())
        position.append(information[4].get_text())
        age.append(information[5].get_text())
        nation.append(information[6].img['alt'])
        team.append(information[7].img['alt'])
        value.append(information[8].span['title'])
        #player_list.append(player)
    df=pd.DataFrame({'number':number,'name':name,'position':position,'age':age,'nation':nation,'team':team,'value':value})
    df.to_csv("transfermarket1~25.csv",index=False)
    #df=pd.DataFrame(player_list,columns=['number','name','position','age','nation','team','value'])
    return player_list
if __name__=="__main__":
    data = crawler()
    data.to_csv("transfermarket1~25.csv",index=False)
    for item in data:
        Player_info(number = item['number'], name = item['name'], position = item['position'],age=item['age'],nation=item['nation'],team=item['team'],value=item['value']).save()