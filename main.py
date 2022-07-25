from bs4 import BeautifulSoup 
import lxml 
import requests
import time


def get_interns():
    plain_html= requests.get('https://wuzzuf.net/search/jobs/?a=hpb&filters%5Bcountry%5D%5B0%5D=Egypt&q=internship%20data%20analysis').text
    soup = BeautifulSoup(plain_html, "lxml")
    jobs= soup.find_all('div',class_="css-pkv5jc")

    for  job in jobs:
        name=job.find('a',class_="css-o171kl").text
        loc=job.find('span',class_="css-5wys0k").text
        try:
            since=job.find('div' , class_="css-do6t5g").text
        except Exception:
            pass

        try:
            more_info=job.div.h2.a['href']
        except Exception :
            pass
        
        with open('interns.txt' , 'a') as f :
            f.write(f''' {name} , in {loc} , since {since} , for more inforamtion visit https://wuzzuf.net/{more_info} \n''')
    print('file saved ')

if __name__ == '__main__' :
    while True :
        get_interns()
        print('the next update within 6 hours')
        time.sleep(21600)
        





    



