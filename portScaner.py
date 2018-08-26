# coding: utf-8


import socket
import sys,re
from tkinter import *
from datetime import datetime

socket.setdefaulttimeout(0.5)

class MainWindow(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.host = StringVar()
        self.port = StringVar()
        self.host.set('127.0.0.1')
        self.port.set(r'1:1024')
        self.master.title('PortScaner')
        self.lbl_host = Label(self, text = 'host:')
        self.lbl_host.pack(side = LEFT)
        self.entry_host = Entry(self, textvariable = self.host)
        self.entry_host.pack(side = LEFT)
        self.lbl_port = Label(self, text = 'port:')
        self.lbl_port.pack(side = LEFT)
        self.entry_port = Entry(self, textvariable = self.port)
        self.entry_port.pack(side = LEFT)
        self.btn_scan = Button(self, text = 'SCAN', command = lambda:self.scan(self.host.get(),self.port.get()))
        self.btn_scan.pack(side = LEFT)
        self.txt_output = Text(self, width = 60, height = 10)
        self.txt_output.pack()
    def scan(self,host, port = '1:1024'):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except IOError as e:
            print(e)
        if re.match('\d+\:\d+', port):
            start= int(re.split(':', port)[0])
            end = int(re.split(':',port)[1])
            for portx in range(start, end + 1):
                addr = (host,portx)
                try:
                    res = s.connect_ex(addr)
                    if res == 0 :
                        self.txt_output.insert(INSERT,'PORT %s : OPEN\n' % portx)
                except IOError as e:
                    self.txt_output.insert(INSERT,str(e))





main = MainWindow()
main.mainloop()
