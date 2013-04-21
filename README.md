rpigps
======

__Prerequisites on the Raspberry PI__

    sudo apt-get install gpsd
    sudo apt-get install gpsd-clients
    sudo dpkg-reconfigure gpsd

The device will likely appear at `/dev/gps0`

    stty -F /dev/ttyUSB0 ispeed 4800 && cat </dev/ttyUSB0
    gpsd /dev/gps0 -b -n

To pipe GPS JSON data out:

    gpspipe -w > gpsdata.json

A CUI view can be obtained using:

    cgps

__References__

http://www.catb.org/gpsd/installation.html

https://github.com/mapnik/mapnik

https://github.com/openstreetmap/osmosis

https://github.com/CloudMade/Leaflet

http://staticmaps.cloudmade.com/8ee2a50541944fb9bcedded5165f09d9/staticmap?styleid=1&size=700x700&path=color:blue|weight:5|opacity:1.0|44.7947,10.3437|44.7958,10.3444|44.7969,10.3439|44.7977,10.3424|44.7982,10.3406|44.7985,10.3391|44.7991,10.3379|44.7995,10.3364|44.8002,10.3351|44.8006,10.3328|44.8008,10.3308|44.8013,10.3290|44.8014,10.3276|44.8022,10.3250|44.8025,10.3232|44.8028,10.3212|44.8032,10.3194|44.8036,10.3175|44.8040,10.3158|44.8037,10.3141|44.8026,10.3138|44.8013,10.3136|44.7999,10.3147|44.7988,10.3157|44.7976,10.3169|44.7963,10.3179|44.7954,10.3192|44.7948,10.3210|44.7942,10.3219|44.7929,10.3215|44.7920,10.3204|44.7909,10.3190|44.7897,10.3192|44.7886,10.3206|44.7876,10.3220|44.7866,10.3235|44.7855,10.3249|44.7847,10.3261|44.7854,10.3279|44.7860,10.3297|44.7872,10.3304|44.7878,10.3320|44.7887,10.3330|44.7888,10.3349|44.7890,10.3368|44.7890,10.3388|44.7891,10.3398|44.7894,10.3414|44.7905,10.3419|44.7916,10.3424|44.7924,10.3429&marker=size:mid|label:A|44.794797,10.343765&marker=size:mid|label:B|44.792408,10.342905
