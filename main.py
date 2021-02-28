from requests_oauthlib import OAuth1Session
import json
import re
import twitter_key#キー読み込み

ACCESS_TOKEN=twitter_key.access_token
ACCESS_TOKEN_SECRET=twitter_key.access_token_secret

CONSUMER_KEY=twitter_key.consumer_key
CONSUMER_SECRET=twitter_key.consumer_secret


def get_between(a:str,b:str,text)->str:#aとbに挟まれた文字列を返す
    return re.match(r'.*'+a+'(.*)'+b+'.*',text).group(1)



def search_tweets(text):
    url='https://api.twitter.com/2/tweets/search/recent?'

    params={'query':text,'max_results':10,'tweet.fields':'created_at'}

    oath=OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    response=oath.get(url,params=params)

    return json.loads(response.text)

def main(user_id):
    tweets=search_tweets('from:'+user_id+' #寿司打')

    results=[]

    for i in tweets['data']:
        id:str=i['id']
        text:str=i['text'].split('で、\n')
        date:str=i['created_at'].split('T')[0]

        course=re.search(r'\d+',text[0]).group()+',000' #本文からコースの値段を抽出

        mode=get_between('【','】',text[0]) #本文からモード？を抽出

        otoku=text[1].split('円分')[0] #何円お得(損)だったか

        is_otoku=False #お得かどうか
        if '★' in otoku:
            is_otoku=True
            otoku=otoku.replace('★','')#お得だった場合 ★ を消す

        otoku=int(otoku.replace(',',''))#整数に変換

        result=get_between('（','）',text[1]) #かっこの中(速度とミス数)を抽出

        speed=float(get_between('速度：','key/秒、',result))#速度を抽出して実数に変換

        miss=int(get_between('ミス：','key',result))#ミス数を抽出して整数に変換

        results.append({'date':date,'course':course,'mode':mode,'result':[otoku,is_otoku,speed,miss],'id':id})

    return results

print(main('Roro3828_'))