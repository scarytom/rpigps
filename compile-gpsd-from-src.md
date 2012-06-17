Compliling GPSD from source on Raspberry Pi
===========================================
The packaged version of GPSD on the Raspberry Pi is 2.95, which is rather old.  I could dig around and find a later deb, but I thought I'd try building from sources on the Pi.

__Install required packages__
```bash
sudo apt-get install chrpath
sudo apt-get install libncurses-dev
sudo apt-get install python-dev
sudo apt-get install libcap-dev
```

__Header for timepps__
```bash
cd /usr/include
sudo wget https://github.com/ago/pps-tools/raw/master/timepps.h
```

__Install scons from source (as packaged version < 2.0.1)__
```bash
wget http://prdownloads.sourceforge.net/scons/scons-2.1.0.tar.gz
tar -xf scons-2.1.0.tar.gz
cd scons-2.1.0
sudo python setup.py install
```
__Grab the gpsd source and build/install__
```bash
git clone git://git.savannah.nongnu.org/gpsd.git
cd gpsd/
git checkout release-3.6
scons && scons testregress && sudo scons udev-install
```
