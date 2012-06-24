#! /bin/bash
set -e

if (( EUID != 0 )); then
   echo "You must be root to do this." 1>&2
   exit 100
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

adduser --system rpigps

cp $DIR/content/usr/bin/* /usr/bin/
cp $DIR/content/etc/udev/rules.d/* /etc/udev/rules.d/
cp $DIR/content/etc/init.d/rpigps /etc/init.d/rpigps

update-rc.d rpigps defaults
