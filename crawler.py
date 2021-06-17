import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")
import django
django.setup()
from quiz.models import Player_info
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
#import pandas as pd
def crawler():
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
    url="https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
    response=requests.get(url,headers=headers)
    player_list=[]
    if response.status_code==200:
        soup=BeautifulSoup(response.content,'html.parser')
        string=soup.find_all('tr',{'class':['odd','even']})
    for info in string:
        information=info.find_all('td')
        player={'number':number,
        'name':name,'position':position,
        'age':age,'nation':nation,'team':team,'value':value}
        number=information[0].get_text()
        name=information[3].get_text()
        position=information[4].get_text()
        age=information[5].get_text()
        nation=information[6].img['alt']
        team=information[7].img['alt']
        value=information[8].span['title']
        player={'number':number,
        'name':name,'position':position,
        'age':age,'nation':nation,'team':team,'value':value}
        player_list.append(player)
    #df=pd.DataFrame(player_list,columns=['number','name','position','age','nation','team','value'])
    return player_list
if __name__=='__main__':
    data = crawler()
    for item in data:
        Player_info(number = item[0], name = item[1], position = item[2],age=item[3],nation=item[4],team=item[5],value=item[6]).save()