import requests
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self, entity,intent):
        self.e = entity
        self.i=intent
        
    def getAnswer(self):
         r1=requests.get("https://www.imdb.com/title/tt7465992/")
         #print(r1)
         #print(self.i)
         #print(r1.text)
         soup = BeautifulSoup(r1.text,"html.parser")
         #li = soup.find('span', {'class': 'oqSTJd'})
         print(soup)
         li2=soup.find('div', {'class': 'inline canwrap'})
         #li=soup.select('div.BNeawe s3v9rd AP7Wnd')
         s=""
         #print(li2.find('span').text)
         #r=li2.find('span').text
         r=""
         #print(li2)
        
         #print(li2)
         #li2.find('p').text
         #if li2!=None:
            #for element  in li2:
                #for e in element:
                    #print(e)
                
         #if li!=None:
            #for element in li:
           #print(element)
                #s=s+element+"\n"
         #return s+"\n"+r
         return r
v=Scrap("maharshi","review")
print(v.getAnswer())
#r=Review("rangasthalam")
#print(v.getAnswer())
      

