#! /bin/sh

set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

adduser --system rpigps

cp $DIR/content/etc/init.d/rpigps /etc/init.d/rpigps
update-rc.d rpigps defaults

