# News peak in English by software and take new by UPIKey and url and than speak news
from pstats import Stats
from flask import request
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.Spvoice")
    speak.speak(str)
if __name__=='__main__':
    speak("News for today")
    str1="With reference to the above, this is to inform you that we are carried out Civil construction & Installation  work required for weighbridge building, foundation ramps at KKC link siding under Barora  Area, We are installed  load cell and Structure but after installation of structure and load cell structure and load cell Damaged  on 14.02.2020 "
    speak(str1)
    #url="https://newsapi.org/v2/everything?q=tesla&from=2022-06-14&sortBy=publishedAt&apiKey=94077374cbfd4ee7a8bf311b6376ad68"
    #url="https://newsapi.org/v2/everything?q=tesla&from=2022-06-14&sortBy=publishedAt&apiKey=94077374cbfd4ee7a8bf311b6376ad68"
    #url="https://newsdata.io/api/1/news?apikey=pub_9211e0c7520d0e6d3e13eebb89a70490cb74&q=finance"
    #url="https://newsdata.io/api/1/news?country=in&apikey=pub_9211e0c7520d0e6d3e13eebb89a70490cb74&q=pegasus&language=en"
    #url="https://newsapi.org/v2/everything?q=apple&from=2022-07-13&to=2022-07-13&sortBy=popularity&apiKey=94077374cbfd4ee7a8bf311b6376ad68"
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=94077374cbfd4ee7a8bf311b6376ad68"
    news=requests.get(url).text
    print(news)
    news_dict=json.loads(news)
    print(news_dict["status"])
    arts=news_dict["articles"]
    for articles in arts:
        speak(articles["title"])
        print(articles["title"])
        speak("Moving on the next news")