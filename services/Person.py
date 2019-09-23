import requests
import json

class Person:
  def __init__(self, msg):
    self.msg = msg
    self.r = ""
    self.headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '5eba7db59e9e47a484d8597b3d9cd884 ',
        }
    self.params ={
    # Query parameter
    'q':msg,
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
    }
    self. r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/4ba351d2-bb3d-4005-aee3-8aa2c3c255bf',headers=self.headers, params=self.params).json()
  def getIntent(self):
    return  self.r['topScoringIntent']['intent']
  def getEntity(self):
    #print(self.r)
    return  self.r['entities'][0]['entity']
p=Person("tollywood  trending")
#print(p.getIntent())
#print(p.getEntity())

