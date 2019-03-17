import pandas as pd

class Review:
    def __init__(self, intent):
        self.i = intent
        
    def getAnswer(self):
        pd.set_option('max_colwidth',300)
        df = pd.read_csv('movie.csv',index_col=0)
        s=str(df.loc[self.i,["review"]])
        t=str(df.loc[self.i,["comments"]])
        s=s.replace("Name: "+self.i+", dtype: object","")
        t=t.replace("Name: "+self.i+", dtype: object","")
        s=s.replace("\n",'')
        t=t.replace("\n",'')
        s=s.replace("   ",":")
        t=t.replace("   ",":")
        return s+"\n"+t

#r=Review("rangasthalam")
#print(r.getAnswer())
      

