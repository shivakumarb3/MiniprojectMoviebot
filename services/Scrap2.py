import requests
from bs4 import BeautifulSoup

class Scrap2:
    def __init__(self, entity,intent):
        self.e = entity
        self.i=intent
        
    def getAnswer(self):
         p={
    
          'q':self.e+" "+self.i
         }

         r1=requests.get("https://www.google.com/search",params=p)
         #print(r1)
         #print(r1.text)
         #print(self.i)
         soup = BeautifulSoup(r1.text,"html.parser")
         li = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
         #li=soup.select('div.BNeawe s3v9rd AP7Wnd')
         s=""
         #print(soup)
         #print(li)
         #for element in li:
           #print(element)
           #s=s+element.get_text()+"\n"
         for el in li:
               s=s+(el.get_text())+"\n"
         return s
#v=Scrap2("maharshi","crew")
#print(v.getAnswer())
#r=Review("rangasthalam")
#print(v.getAnswer())
      

