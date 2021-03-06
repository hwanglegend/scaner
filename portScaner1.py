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
        self.txt_output = ScrolledText(self, width = 60)
        self.txt_output.grid(row = 4, column = 1)
        
    def scan(self,host, port = '1:1024'):
        if re.match('^\d+\.\d+\.\d+.\d+\:\d+\.\d+\.\d+.\d+$',host):
            starthost = re.split(':', host)[0]
            endhost = re.split(':', host)[1]
            hostlist = self.__hostlist__(starthost, endhost)

        elif re.match('^\d+\.\d+\.\d+.\d+\\(^[0-9]$|^[1-2]\d$|^3[0-2]$)$',host):
            bits = int(re.split('\\', host)[1])

        elif re.match('\d+\.\d+\.\d+.\d+$',host):
            hostlist = [host]

        if re.match('\d+\:\d+', port):
           start= int(re.split('\:', port)[0])
           end = int(re.split('\:',port)[1])
           portlist = range(start, end+1)            

        elif re.match('\d+\,',port):
           portlist = re.split(',', port)
          
        elif re.match('^\d+$', port):
           addr = (host, int(port))
           self.scaning = str(port)
           portlist = [port]
        for hostx in hostlist:
            for portx in portlist:
                self.__checkPort(hostx, portx)
    def __checkPort(self, host, port):
        addr = (host, int(port))
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        except IOError as e:
            print(e)
        try:
            res = s.connect(addr)
            print(port, res)
            if res == 0 :
                self.txt_output.insert(INSERT,'HOST: %s ,PORT: %s : OPEN\n' % (host,port))
        except IOError as e:
            print(str(e))
        time.sleep(delay)
        s.close()


    def __hostlist__(starthost, endhost)
        intstarthost = struct.unpack('!I', socket.inet_aton(starthost))
        intendhost = struct.unpack('!I', socket.inet_aton(endhost))
        if intstarthost > intendhost:
            ex = intstarthost
            intstarthost = intendhost
            intendhost = ex
        inthost = intstarthost
        while inthost <=intendhost:
            strhost = socket.inet_ntoa(struct.pack('!I', inthost)
            yield strhost
            inthost = inthost + 1

        
        


main = MainWindow()
main.mainloop()
