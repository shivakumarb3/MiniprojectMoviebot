import requests
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self, intent):
        self.i = intent
        
    def getAnswer(self):
         p={
    
          'q':self.i+" review"
         }

         r1=requests.get("https://www.google.com/search",params=p)
         #print(r1)
         #print(self.i)
         soup = BeautifulSoup(r1.text,"html.parser")
         li=   soup.select('div.XAiqpc')
         s=""

#print(li)
         for element in li:
            print(element.text)
            s=s+element.text+"\n"
         return s
#v=Scrap("aquaman")
#print(v.getAnswer())
#r=Review("rangasthalam")
#print(r.getAnswer())
      

