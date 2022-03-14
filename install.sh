#! /bin/bash

sudo apt-get install xclip -y
sudo apt-get install libnotify-bin -y
NOTIFY=$(which notify-send)
if [ -z $NOTIFY ]
then
    sudo apt-get install notify-send -y
fi

sudo cp -f ./ydt.py /usr/local/bin/ydt
sudo chmod 775 /usr/local/bin/ydt
sudo cp -f ./fanyi.sh /usr/bin/fanyi
sudo chmod 775 /usr/bin/fanyi