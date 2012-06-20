import json
import fileinput
import datetime

filename = "C:\\Users\\tom\\Downloads\\track0_godstone.json"

print ("""<?xml version="1.0" encoding="utf-8"?>
<gpx version="1.1" creator="GPSD 3.6 - http://catb.org/gpsd"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns="http://www.topografix.com/GPX/1/1"
        xsi:schemaLocation="http://www.topografix.com/GPX/1/1
        http://www.topografix.com/GPX/1/1/gpx.xsd">
 <metadata>
  <time>2012-06-20T20:41:51.000Z</time>
 </metadata>
 <trk>
  <src>GPSD 3.6</src>
  <trkseg>""")


for line in fileinput.input (filename):
    j = json.loads(line)
    if j['class'] == 'TPV':
        print('   <trkpt lat="' + str(j['lat']) +'" lon="' + str(j['lon']) + '">')
        print('    <ele>' + str(j['alt']) + '</ele>')
        print('    <time>' + datetime.datetime.fromtimestamp(j['time']).strftime('%Y-%m-%dT%H:%M:%S.000Z') + '</time>')
        print('    <src>GPSD tag="' + j['tag'] + '"</src>');
        print('    <fix>3d</fix>')
        print('   </trkpt>')
        
print ("""  </trkseg>
 </trk>
</gpx>""")
