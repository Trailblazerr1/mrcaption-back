import requests
import gensim
import os
import wikiquotes
from watson_developer_cloud import ToneAnalyzerV3
import json
from aylienapiclient import textapi


def imgscore(words,genres):
    l = 0.0
    summ = []
    for genre in genres:
        for word in words:
            try:
                simScore = model.wv.similarity(genre,word)
                l += simScore
            except:
                pass
        summ.append(l)
        l = 0
    return(genres[summ.index(max(summ))])


data = {
   'tags':[
      {
         "name":"grass",
         "confidence":0.999999761581421
      },
      {
         "name":"outdoor",
         "confidence":0.999970674514771
      },
      {
         "name":"sky",
         "confidence":999289751052856
      },
      {
         "name":"building",
         "confidence":0.996463239192963
      },
      {
         "name":"house",
         "confidence":0.992798030376434
      },
      {
         "name":"lawn",
         "confidence":0.822680294513702
      },
      {
         "name":"green",
         "confidence":0.641222536563873
      },
      {
         "name":"residential",
         "confidence":0.314032256603241
      },
   ],
}

li = []




for d in data['tags']:
    li.append(d['name'])
    
print(li)
cap = []
count=0
for i in li:
    count+=1
    if(count<2):
        dd = wikiquotes.get_quotes(i, "english")
        cap.append(dd[0])
print(cap)

tone_analyzer = ToneAnalyzerV3(
    username='09ad450e-eb00-4ef4-a6ab-e51093e505c4',
    password='kGnXm8HrMFWw',
version='2017-09-26')

for c in cap:
    utterances = [{'text': c, 'user': 'trailblazerr'}]    
    rtone=  tone_analyzer.tone_chat(utterances)
    #print(type(rtone))
    print(rtone["utterances_tone"][0]["tones"][0]["tone_name"])
    if(srtone["utterances_tone"][0]["tones"])
    
    
client = textapi.Client(" 016eb657", " 590dff367360e75235f3753b78ef1488")
sentiment = client.Hashtags({'text': cap[0]})
print(sentiment['hashtags'])