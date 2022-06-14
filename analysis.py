import requests,json,time

googleApikey = '' #generate-api-kry-from-google-cloud-platform

thingspeakWriteKey = '' #write-api-key-of-thingspeak-channel

thingspeakReadKey = '' #read-api-key-of-thingspeak-channel

ytVideoid = ''  #id-of-youtube-video

yturl = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id='+ytVideoid+'&t&key='+googleApikey

channelId = ''#id-of-thingspeak-channel

getUrl = 'https://api.thingspeak.com/channels/'+channelId+'/feeds.json?api_key='+thingspeakReadKey+'&results=1'

updateTime = 60 #Seconds

while True:   
    
    result = requests.get(yturl)

    result = json.loads(result.text)

    result = result['items'][0]['statistics']

    preResult = requests.get(getUrl)

    preResult = json.loads(preResult.text)

    try:
        viewIncrement = int(result['viewCount'])-int(preResult['feeds'][0]['field1'])
    except IndexError as e:
        viewIncrement = 0

    postUrl = "https://api.thingspeak.com/update?ap_key="+thingspeakWriteKey+"&field1="+result['viewCount']+"&field2="+result['likeCount']+"&field3="+result['commentCount']
    
    print("Views Increment:",viewIncrement)


    if(viewIncrement>0):
        result['viewsIncrement'] = str(viewIncrement)
        postUrl = postUrl + "&field4="+result['viewsIncrement']

    print(result)

    z=requests.get(postUrl)

    print(z.status_code)

    print(time.strftime("%H:%M",time.localtime()))

    time.sleep(updateTime)
