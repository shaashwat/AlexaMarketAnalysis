import quandl
import urllib
import json

def getInvestorSentiment():
    quandl.ApiConfig.api_key = "63csnyxcdys7ovvev6ub"
    url = "https://www.quandl.com/api/v3/datasets/AAII/AAII_SENTIMENT.json?api_key="+quandl.ApiConfig.api_key
    response = urllib.urlopen(url)
    database = json.loads((response.read()))
    dataset = database['dataset']
    data = dataset['data']
    mostrecent = data[0]
    date = mostrecent[0]
    bullish = mostrecent[1]
    neutral = mostrecent[2]
    bearish = mostrecent[3]
    percents = [str(int(round(bullish*100)))+"% bullish, ", str(int(round(neutral*100)))+"% neutral, and ", str(int(round(bearish*100)))+"% bearish."]
    #format of percents is [bullish, neutral, bearish]
    onestringpercents = ''.join(percents)
    return onestringpercents
