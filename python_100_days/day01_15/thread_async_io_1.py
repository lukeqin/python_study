#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 16:56
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : thread_async_io_1.py
# @notice ：


import time
import tkinter
import tkinter.messagebox


def download():
    time.sleep(3)
    tkinter.messagebox.showinfo('Info', 'Download done')

def show_about():
    tkinter.messagebox.showinfo('About', 'AAAAA')

def main():
    top = tkinter.Tk()
    top.title('single thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='about', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()