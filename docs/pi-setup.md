```bash
vi /etc/rc/local
sudo mv /boot/boot_enable_ssh.rc /boot/boot.rc
sudo vi /etc/dhcp/dhclient.conf
```

```bash
sudo apt-get install gpsd
sudo apt-get install gpsd-clients
sudo apt-get install git
sudo apt-get install telnet
sudo apt-get install vim
```

```bash
gpspipe -w
gpsd /dev/ttyUSB0 -b -n
gpscat /dev/ttyUSB0
stty -F /dev/ttyUSB0 ispeed 4800 && cat </dev/ttyUSB0
stty -F /dev/gps0 ispeed 4800 && cat </dev/gps0
gpsd -D 5 -N -n /dev/ttyUSB0
sudo gpsd -D 5 -N -n /dev/ttyUSB0
cgps
sudo service gpsd restart
gpsd -D 5 -N -n /dev/gps0
sudo dpkg-reconfigure gpsd
gpxlogger
```
