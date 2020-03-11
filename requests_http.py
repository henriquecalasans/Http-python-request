import requests
import json

#Get
r = requests.get('https://github.com/timeline.json',stream=True)
payload_get = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get',params=payload_get)




#Post example 1 
url = 'https://api.github.com/some/endpoint'
payload_post_1 = {'key1':'value1','key2':'value2'}
r1 = requests.post(url,data=json.dumps(payload_post_1))
print (r)


#Post example 2 
url_post = "http://httpbin.org/post"
payload_post_2 = {'team':'Corinthians','Car':'Lambo'}
r2 = requests.post(url_post,data=payload_post_2)
print (r2.text)