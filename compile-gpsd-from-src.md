Compliling GPSD from source on Raspberry Pi
===========================================

```bash
sudo apt-get install chrpath
sudo apt-get install libncurses-dev
```


```bash
wget http://prdownloads.sourceforge.net/scons/scons-2.1.0.tar.gz
tar -xf scons-2.1.0.tar.gz
cd scons-2.1.0
sudo python setup.py install
```

'''bash
git clone git://git.savannah.nongnu.org/gpsd.git
cd gpsd/
git checkout release-3.6
scons
'''
