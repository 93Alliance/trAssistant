#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import argparse
import random
import hashlib
import json
import tkinter as tk  # 使用Tkinter前需要先导入

APPID = '026650580f5ed88e'
APPKey = 'Wf4UyZjTKCwvyrAuNajG3Zze3NIE7EBT'

windowWidth = 320
windowHeight = 140

def fanyi(word, goNext):
    baseUrl = 'https://openapi.youdao.com/api'
    salt = str(random.randint(1000000, 9999999))
    sign = APPID + word + salt + APPKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    md5Sign = m1.hexdigest()
    queryFrom = {
            'appKey': APPID,
            'q': word,
            'from': 'auto',
            'to': 'auto',
            'salt': salt,
            'sign': md5Sign,
        }
    r = requests.post(baseUrl, data=queryFrom)
    if r.status_code == 200:
        res = json.loads(r.text)
        if res['errorCode'] == '0':
            showRes(word, res)
            if goNext:
                print('\n')
                inputWord(False)
        else:
            print(res['errorCode'])
            exit()
    else:
        print(r.status_code)
        exit()

def showRes(word, res):
    trs = []
    for i in res['translation']:
        trs.append(i)

    p = []
    if 'basic' in res:
       phoneticBasic = res['basic']
       if 'us-phonetic' in phoneticBasic:
          p.append('美式: ' + phoneticBasic['us-phonetic'])
       if 'uk-phonetic' in phoneticBasic:
          p.append('英式: ' + phoneticBasic['uk-phonetic'])   
    showFloatCard("".join(trs), "  ".join(p))
    
def inputWord (isFirst):
    if isFirst:
        print('\n\033[1;36m英汉互译词典\033[0m by FungLeo')
        print('\033[35mTip：退出程序请输入 \033[1;31mexit\033[4;0m\n')
    word = input('请输入要翻译的内容：')
    if word == 'exit':
        print('\033[0m很高兴为您服务')
        exit()
    else:
        fanyi(word, True)

def showFloatCard(result, phonetic):
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    sh = window.winfo_screenheight()
    scale = round(sh / 1080.0)
    global windowWidth
    global windowHeight
    windowWidth = windowWidth * scale
    windowHeight = windowHeight * scale

    # 第2步，给窗口的可视化起名字
    window.title('有道')
    window.configure(bg='white')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry(str(windowWidth)+"x"+str(windowHeight))

    if phonetic != "":
        phoneticL = tk.Label(window, text=phonetic, bg="white", justify=tk.LEFT)
        phoneticL.pack()

    # 第4步，在图形界面上设定标签
    resultL = tk.Label(window, text=result, bg="white", wraplength=windowWidth-4, justify=tk.LEFT)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    # 第5步，放置标签
    resultL.pack(fill=tk.BOTH, expand=tk.YES)
    # 放置lable的方法有：1）l.pack(); 2)l.place();

    def onWindowResize(event=None):
        global windowWidth
        global windowHeight
        # <Configure event x=967 y=871 width=320 height=140>
        # 目前会不停的进入if分支调整大小
        if event is not None:
            if windowWidth != window.winfo_width() or windowHeight != window.winfo_height():
                windowWidth = window.winfo_width()
                windowHeight = window.winfo_height()
                w = windowWidth - 4
                resultL.config(wraplength=w)
        return

    window.bind('<Configure>', onWindowResize)

    # 第6步，主窗口循环显示
    window.mainloop()
    # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
    # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'YouDao Fanyi Cli'
    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s V0.0.1')
    parser.add_argument('word', type = str, help = '需要翻译的单词', nargs = '?')

    args = parser.parse_args()

    if args.word == None:
        inputWord(True)
    else:
        fanyi(args.word, False)

