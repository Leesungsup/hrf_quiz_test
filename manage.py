#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#import os
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
        number1=information[0].get_text()
        name1=information[3].get_text()
        position1=information[4].get_text()
        age1=information[5].get_text()
        nation1=information[6].img['alt']
        team1=information[7].img['alt']
        value1=information[8].span['title']
        player={'number':number1,'name':name1,'position':position1,'age':age1,'nation':nation1,'team':team1,'value':value1}
        number.append(information[0].get_text())
        name.append(information[3].get_text())
        position.append(information[4].get_text())
        age.append(information[5].get_text())
        nation.append(information[6].img['alt'])
        team.append(information[7].img['alt'])
        value.append(information[8].span['title'])
        player_list.append(player)
    df=pd.DataFrame({'number':number,'name':name,'position':position,'age':age,'nation':nation,'team':team,'value':value})
    df.to_csv("transfermarket1~25.csv",index=False)
    #df=pd.DataFrame(player_list,columns=['number','name','position','age','nation','team','value'])
    return player_list
if __name__=='__main__':
    main()
    data = crawler()
    for item in data:
        Player_info(number = item['number'], name = item['name'], position = item['position'],age=item['age'],nation=item['nation'],team=item['team'],value=item['value']).save()

