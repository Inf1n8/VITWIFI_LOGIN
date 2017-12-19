import requests
key=['userId','password','serviceName','Submit22']
values=['YOUR_USERID','YOUR_PASSWORD','ProntoAuthentication','Login']
data=dict(zip(key,values))
url_link='http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://captive.apple.com/hotspot-detect.html'
requests.post(url=url_link,data=data)
r=requests.get(url_link)
if(r.status_code==200):
    print("Logged in!")
else:
    print("Sorry couldn't connect successfully")