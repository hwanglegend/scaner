# coding: utf-8


import socket
import sys,re,threading, time
from tkinter import *
from datetime import datetime

socket.setdefaulttimeout(0.5)
delay = 0
class MainWindow(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.host = StringVar()
        self.port = StringVar()
        self.scaning = StringVar()
        self.host.set('127.0.0.1')
        self.port.set(r'1:1024')
        self.master.title('PortScaner')
        self.lbl_host = Label(self, text = 'host:')
        self.lbl_host.grid(row =0,column =0)
        self.entry_host = Entry(self, textvariable = self.host)
        self.entry_host.grid(row = 0, column = 1)
        self.lbl_port = Label(self, text = 'port:')
        self.lbl_port.grid(row = 1, column = 0)
        self.entry_port = Entry(self, textvariable = self.port)
        self.entry_port.grid(row = 1, column = 1)
        self.btn_scan = Button(self, text = 'SCAN', command = lambda:self.scan(self.host.get(),self.port.get()))
        self.btn_scan.grid(row = 2, column = 1)
        self.lbl_scaning = Label(self, text = 'scaning:')
        self.lbl_scaning.grid(row=3,column = 0)
        self.entry_scanning = Entry(self, textvariable = self.scaning)
        self.entry_scanning.grid(row= 3, column = 1)
        self.txt_output = Text(self, width = 60, height = 10)
        self.txt_output.grid(row = 4, column = 1)
        
    def scan(self,host, port = '1:1024'):
        
        if re.match('\d+\:\d+', port):
            start= int(re.split(':', port)[0])
            end = int(re.split(':',port)[1])
            for portx in range(start, end + 1):
                
                self.scaning = str(portx)
                self.__checkPort(host, portx)
         
        elif re.match('\d+\,',port):
            portlist = re.split(',', port)
            for portx in portlist:
                #self.scaning = str(portx)
                self.__checkPort(host, int(portx))
        elif re.match('\d+$', port):
            addr = (host, int(port))
            self.scaning = str(port)
            self.__checkPort(host, port)

    def __checkPort(self,host, port):
        addr = (host, int(port))
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        except IOError as e:
            print(e)
        try:
            res = s.connect_ex(addr)
            print(port, res)
            if res == 0 :
                self.txt_output.insert(INSERT,'HOST: %s ,PORT: %s : OPEN\n' % (host,port))
        except IOError as e:
            self.txt_output.insert(INSERT,str(e))
        time.sleep(delay)
        s.close()





main = MainWindow()
main.mainloop()
