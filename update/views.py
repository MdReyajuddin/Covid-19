from django.shortcuts import render
from plyer import notification
from bs4 import BeautifulSoup
from .models import Covid
import time
import requests

# Create your tests here.
def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:\simple\corona\static\img\icon.ico",
        timeout=5
    )
def getdata(url):
    r = requests.get(url)
    return r.text

# Create your views here.
def index(request):
    htmldata = getdata('https://www.mohfw.gov.in/')
    # print(htmldata)
    soup = BeautifulSoup(htmldata, 'html.parser')
    soup.prettify()
    # print(soup)
    tr_data = ""
    for body in soup.find_all('tbody'):
        for tr in body.find_all('tr'):
            tr_data += tr.get_text()
    tr_data = tr_data[1:]
    itemlist = tr_data.split("\n\n")



    states = ['Odisha', 'Karnataka', 'Uttar Pradesh', 'West Bengal']

    result = []
    for item in itemlist[0:30]:
        data_list = item.split('\n')

        if data_list[1] in states:
            state = data_list[1]
            affected = data_list[2]
            cured = data_list[3]
            deaths = data_list[4]


            data ={
                'state': state,
                'affected': affected,
                'cured': cured,
                'deaths': deaths,

            }
            result.append(data)

            ntext = "Cases Of Covid-19 "
            ndata = f"state:{data_list[1]}\naffected:{data_list[2]}\ncured:{data_list[3]}\ndeaths:{data_list[4]}"
            
            notifyMe(ntext, ndata)
            time.sleep(10)
    # time.sleep(3600)
    return render(request, 'index.html', {'list': result})




