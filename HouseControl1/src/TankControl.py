'''
Created on Oct 23, 2018

@author: klein
'''

import wx
import MainFrame 
from pkg_resources._vendor.pyparsing import White


class TankControl(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        MC=MainFrame.MainFrame(None,title = "test") # this redirects out put into a wx python window.
        MC.SetPosition(50)  # sets the left corner in x
        MC.SizeFrame(x=600,y=600) #sizes the frame
        button=wx.Button(MC.panel,-1,"Close me",pos=(15,15))


  
 
if __name__ == '__main__':
    
    app= wx.App(redirect=False)

    TC=TankControl()
    app.MainLoop()
    pass
       