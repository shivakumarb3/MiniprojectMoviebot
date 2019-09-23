import requests
from bs4 import BeautifulSoup

class Scrap5:
    def __init__(self, entity,intent):
        self.e = entity
        self.i=intent
        
    def getAnswer(self):
         p={
    
          'q':self.e+" "+self.i
         }
         r1=""
         if(self.e=='tollywood' or self.e=='Tollywood' or self.e=='TOLLYWOOD' or self.e=='telugu'):
             r1=requests.get("https://timesofindia.indiatimes.com/entertainment/telugu/tollywood/top-20-best-telugu-movies-of-2019")
         elif (self.e=='hollywood' or self.e=='Hollywood' or self.e=="HOLLYWOOD" or self.e=='english'):
             r1=requests.get("https://timesofindia.indiatimes.com/entertainment/english/hollywood/top-20-best-hollywood-movies-of-2019")
         elif(self.e=='bollywood' or self.e=="Bollywood" or self.e=="BOLLYWOOD" or self.e=='hindi'):
             r1=requests.get("https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/top-20-best-bollywood-movies-of-2019")
         #print(r1)
         #print(r1.text)
         #print(self.i)
         soup = BeautifulSoup(r1.text,"html.parser")
         li = soup.find_all("div", class_="topten_movies_content")
         #li=soup.select('div.BNeawe s3v9rd AP7Wnd')
         s=""
         #print(li)
         #print(li)
         for element in li:
           s=s+list(element.get_text().split('\n'))[1]+"\n"
         
         
         
         return s
v=Scrap5("telugu","trending movies")
print(v.getAnswer())
#r=Review("rangasthalam")
#print(v.getAnswer())
      

