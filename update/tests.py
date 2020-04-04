from django.test import TestCase
from plyer import notification
from bs4 import BeautifulSoup
import time
import requests

# Create your tests here.
def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:\simple\corona\static\img\icon.ico",
        timeout=2
    )
def getdata(url):
    r = requests.get(url)
    return r.text

if __name__=="__main__":
    while True:
    #     notifyMe("Reyaj", "lets together come together to fight virus")
        htmldata= getdata('https://www.mohfw.gov.in/')
        # print(htmldata)
        soup = BeautifulSoup(htmldata, 'html.parser')
        # print(soup)
        tr_data =""
        for body in soup.find_all('tbody'):
            for tr in body.find_all('tr'):
                tr_data += tr.get_text()
        tr_data=tr_data[1:]
        itemlist=tr_data.split("\n\n")

        states = ['Odisha', 'Karnataka', 'Uttar Pradesh', 'West Bengal']

        for item in itemlist[0:31]:
            datalist = item.split('\n')
            print(datalist)
            if datalist[1] in states:
                ntext= "Cases Of Covid-19 "
                ndata = f"state : {datalist[1]}\n affected : {datalist[2]}\n cured : {datalist[3]}\n deaths : {datalist[4]}"
                notifyMe(ntext, ndata)
                time.sleep(5)


        time.sleep(60)












