import json
import urllib.request

i = open("C:\\Users\\tom\\Desktop\\gpsdata.json");

for line in i:
    j = json.loads(line);
    if j['class'] ==  'TPV':
        r.append(str(j['lat']) + ',' + str(j['lon']));


data = '|'.join(r)[:1500];
data = data[:data.rindex('|');

url = 'http://staticmaps.cloudmade.com/8ee2a50541944fb9bcedded5165f09d9/staticmap?styleid=1&size=700x700&path=color:blue|weight:5|opacity:1.0|' + data;
f = urllib.request.urlopen(url);
