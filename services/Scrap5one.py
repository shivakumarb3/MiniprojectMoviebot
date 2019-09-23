import requests
from bs4 import BeautifulSoup

class Scrap5one:
    def __init__(self, entity,intent):
        self.e = entity
        self.i=intent
        
    def getAnswer(self):
         p={
    
          'q':self.e+" "+self.i
         }

         r1=requests.get("https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/top-20-best-bollywood-movies-of-2019")
         #print(r1)
         #print(r1.text)
         #print(self.i)
         soup = BeautifulSoup(r1.text,"html.parser")
         li = soup.find_all("div", class_="topten_movies_content")
         #li=soup.select('div.BNeawe s3v9rd AP7Wnd')
         s=""
         #print(soup)
         #print(li)
         for element in li:
           s=s+list(element.get_text().split('\n'))[1]+"\n"
           #print(li)
           #s=s+element.get_text()+"\n"
         
         
         
         return s
v=Scrap5one("bollywood","trending movies")
print(v.getAnswer())
#r=Review("rangasthalam")
#print(v.getAnswer())
      

