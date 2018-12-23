#Hard-coded session id. Got it from IE
#9th line from import requests has auto generates session id for asp.net by hitting the actual page. 
#Currently generated session id not working. Working around this using wireshark and analyse the response packet.
#If code doesnt work, get  new session id from IE dev tools and paste it here(17th line from import requests).


import requests
from bs4 import BeautifulSoup
flight_list = []
srno=0
while True:
    session = requests.Session()
    sresp = session.get('https://csia.in/flightinformation/FetchRecordsHandler.ashx?lastSrNo=0&Page=P')
    #print(session.cookies.get_dict())
    cookie_dict = session.cookies.get_dict()
    session_id = cookie_dict['ASP.NET_SessionId']
    
    header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    ,'Accept-Encoding': 'gzip, deflate, br'
    ,'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'
    #,'Cache-Control': 'max-age=0'
    ,'Connection': 'keep-alive'
    ,'Cookie': 'ASP.NET_SessionId=ly2hlibddk5bd015aiszeafg; __utma=148441253.132324892.1545552262.1545552262.1545552262.1; __utmb=148441253.2.10.1545552262; __utmc=148441253; __utmz=148441253.1545552262.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1'
    ,'Host': 'csia.in'
    #,'Upgrade-Insecure-Requests': '1'
    ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
        
    r = requests.get(url='https://csia.in/flightinformation/FetchRecordsHandler.ashx?lastSrNo='+str(srno)+'&Page=P',headers = header)
    if r.status_code==200:
        tbl = r.content
        print(len(tbl))
        if len(tbl)==0:
            break
        soup = BeautifulSoup(tbl,'lxml')
        row = soup.find_all('tr')
        for x in row:
            flight_list.append(x.text)
            print(x.text)
            print()
            print()
    srno = srno+10
