#! /bin/bash

xclip=$(which xclip)
if [ -z $xclip ]
then
    sudo apt-get install xclip -y
fi

sudo cp -f ./ydt.py /usr/local/bin/ydt
sudo chmod 775 /usr/local/bin/ydt
sudo cp -f ./fanyi.sh /usr/bin/fanyi
sudo chmod 775 /usr/bin/fanyi

echo "安装完成!!"