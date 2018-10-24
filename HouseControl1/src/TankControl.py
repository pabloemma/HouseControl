#!/usr/bin/env python

'''
Created on Oct 23, 2018

@author: klein
'''

import wx
import MainFrame 
import socket, errno
import subprocess
import threading




import imp

DE = imp.load_source('ThreadedServer', '/home/klein/git/tank/tank/src/data_exchange_threaded.py')



class TankControl(object):
    '''
    classdocs
    '''


    def __init__(self,port=5478,IP1='192.168.10.60',IP2='192.168.10.61'):
        '''
        Constructor
        '''
        self.port = port # currently we are always using 5478

        self.IP1 = IP1 # the ip addresses of the wto level parsperry pis
        
        self.IP2 = IP2
        
        
        
        
        self.MC=MC=MainFrame.MainFrame(None,title = "test") # this redirects out put into a wx python window.
        MC.SetPosition(50)  # sets the left corner in x
        MC.SizeFrame(x=600,y=600) #sizes the frame
        self.CreateButton()
 
        #Now we start beautify the frame.
 
        self.CreateMenu()
        
        
        

        #serv.CloseAll()

        
    def CreateMenu(self):
        """ this creates the menu for the tankcontrol
        """
        self.menubar = wx.MenuBar()
        # first menu
        menu1 = wx.Menu()
        Quit = menu1.Append(wx.NewId(),"&Quit") # this creates the menu items
        self.menubar.Append(menu1, "&File") # this creates the menu title
        
        
        menu2 = wx.Menu()
        Run = menu2.Append(wx.NewId(),"&Run")
        Control = self.menubar.Append(menu2, "&Control") # this creates the menu title
        
 
        self.MC.SetMenuBar(self.menubar)
        
        
        # Here we bind the different events
        # from File menu
        self.MC.Bind(wx.EVT_MENU,self.OnQuit,Quit)
        
        
        # from Control menue
        self.MC.Bind(wx.EVT_MENU,self.OnRun,Run)
        
        
        
    def CreateButton(self): 
        
           
        button=wx.Button(self.MC.panel,-1,"Close me",pos=(15,15))



    def PortInUse(self):
        """
        checks if the port is already i n use
        """
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind(("127.0.0.1", self.port))
            return False
        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                print("Port is already in use")
                
            else:
            # something else raised the socket.error exception
                print(e)
            return True

        s.close()
        
    def KillPortProcess(self):

        command = 'fuser -k ' +str(self.port)+'/tcp'
        print command
        subprocess.call(command, shell=True)
        pass

    
    
    
    #here come all the event handling routines
    
    def OnQuit(self,event):
        """
        closes all the communications and exits
        """
        print "I am in Quit"
        self.MC.CloseFrame()
        return
    
    def OnRun(self,event):
        """
        this starts the different processes
        """
        print "starting the tank program"
        
        #currently the port being used is 5478
        # we need to test if port 5478 is in use.
        
        if not self.PortInUse():
            print " we are good to go"
        else:
            print "the port is alserv.listen()ready in use"
            print " I will try to kill the process"
            self.KillPortProcess()
            
            # now we can start the program
            #This needs to go into a thread
        
        self.serv = serv = DE.ThreadedServer('',5478)
        serv.OpenFile()
        #here we do a thread

        t1 = threading.Thread(target=serv.listen, args=[])
        t1.start()
        # now we need to start the rocesses on the tank machines
        # make sure we have a key generated and pushed to the machines
        # see for example http://www.linuxproblem.org/art_9.html
        # we have two machines
        
        print "now starting first machine @",self.IP1
        
        t2 = threading.Thread(target=self.ConnectLevelRaspi(self.IP1), args=[])
        t2.start()

        print "now starting next machine @",self.IP2

        t3 = threading.Thread(target=self.ConnectLevelRaspi(self.IP2), args=[])
        t3.start()
        
        
        return

        
    def ConnectLevelRaspi(self,IP): 
        
        
        #command_IP1 = 'ssh pi@'+ IP +' -t -t \'screen -D -RR -S this python /home/pi/tank/tank/src/tanklevel.py \' '  
        command_IP1 = 'ssh pi@'+ IP +' \'nohup python /home/pi/tank/tank/src/tanklevel.py  >/dev/null 2>/dev/null </dev/null & \' '            
        subprocess.call(command_IP1, shell=True)
        return

 
if __name__ == '__main__':
    
    app= wx.App(redirect=True)

    TC=TankControl(port=5478,IP1='192.168.10.60',IP2='192.168.10.61')
    app.MainLoop()
    pass
       