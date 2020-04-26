#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 17:04
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : thread_async_2.py
# @notice ：


import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():
    class DownloadTaskHandler(Thread):
        def run(self):
            time.sleep(2)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            button1.config(state=tkinter.NORMAL)

    def download():
        button1.config(state=tkinter.DISABLED)
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

    top = tkinter.Tk()
    top.title('Single thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()