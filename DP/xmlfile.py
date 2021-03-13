import urllib.request as ur
import xml.etree.ElementTree as ET
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url="http://py4e-data.dr-chuck.net/comments_759541.xml"
xml = ur.urlopen(url).read().decode()
    #print('Retrieved', len(data), 'characters')
    #print(data.decode())
tree = ET.fromstring(xml)

results = tree.findall('comments/comment')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text
sm=0
for number in results:
    sm += int(number.find('count').text)
    #print('lat', lat, 'lng', lng)
print(sm)


    