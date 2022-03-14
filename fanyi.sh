#! /bin/bash

word=`xclip -out`
if [[ -z "$word" ]];then
    exit 0
fi
mean=`ydt "${word}"`
