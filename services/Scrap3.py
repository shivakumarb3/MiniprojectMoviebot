import requests
from bs4 import BeautifulSoup

class Scrap3:
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
         #print(soup)
         li = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
         #li=soup.find_all('div', {'class': 'BNeawe iBp4i AP7Wnd'})
         #li=soup.select('div.BNeawe s3v9rd AP7Wnd')
         #li=None
         #print(li)
         s=""
         #print(soup)
         #print(li)
         #for element in li:
           #print(element)
           #s=s+element.get_text()+"\n"
         ans=set({})
         pl=[]
         if li!=None:
            for el in li:
                t=el.get_text()
                #print(t)
                if( (("₹" in t or "$" in t or "USD" in t) and ":" in t) and(t not in ans)):
                    ans.add(t)
                    s=s+t+"\n"
                    
         return s
v=Scrap3("avengers end game","movie collections")
print(v.getAnswer())
#r=Review("rangasthalam")
#print(v.getAnswer())
      

