
import requests
from bs4 import BeautifulSoup
url = 'https://csia.in/flightinformation/passenger-flight.aspx?flight=arr'

respons = requests.get(url)

content = respons.text

soup = BeautifulSoup(content,'lxml')

view = soup.find('input', {'id': '__VIEWSTATE'}).get('value')


headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

frmdata = {'__LASTFOCUS':'','__EVENTTARGET': 'lnkInternational','__EVENTARGUMENT':'','__VIEWSTATE': view,
           '__VIEWSTATEGENERATOR': 'F2883082',
           'txtSearch': '','TextBoxWatermarkExtender1_ClientState': '',
           'ddlCity': '0','ddlAirline': '0','ddlDate': '',
           'txtSearchFlight': '','hiddenLastSrNo': '','hiddenInputToUpdateATBuffer_CommonToolkitScripts': '1'}

r = requests.post(url, data = frmdata)

s = BeautifulSoup(r.text,'lxml')

file = open('xyz.txt','w')
file.write(s.prettify())
file.close()
"""
import scrapy
class scapper(scrapy.Spider):

    def parse(self,response):
        yield scrapy.FormRequest(
            url,
            formdata=frmdata,
            callback=self.parse_results
        )


    def parse_results(self, response):
        print(response.body)
"""
