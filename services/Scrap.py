import requests
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self, entity,intent):
        self.e = entity
        self.i=intent
        
    def getAnswer(self):
         p={
    
          'q':self.e+" "+self.i
         }

         r1=requests.get("https://www.google.com/search",params=p)
         #print(r1)
         #print(self.i)
         soup = BeautifulSoup(r1.text,"html.parser")
         li = soup.find('span', {'class': 'oqSTJd'})
         li2=soup.find('div', {'class': 'BNeawe vvjwJb AP7Wnd'})
         #li2=soup.findAll("div", class_="BNeawe vvjwJb AP7Wnd")
         #li=soup.select('div.BNeawe s3v9rd AP7Wnd')
         s=""
         #print(soup)
         #print(li2)
         #print(li)
         r=""
         ans=set({})
         #print("starts now")
         if li2!=None:
            for element  in li2:
                if element not in ans:
                    ans.add(element)
                    r=r+element+"\n"
                
         #print(ans1)
         if li!=None:
            for element in li:
                if element not in ans:
                    ans.add(element)
                    r=r+element+"\n"
                #print(element)
            
         #print(ans2)
         
         return r
#v=Scrap("evaru ","review")
#print(v.getAnswer())
#r=Review("rangasthalam")
#print(v.getAnswer())
      

