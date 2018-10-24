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
        self.MC=MC=MainFrame.MainFrame(None,title = "test") # this redirects out put into a wx python window.
        MC.SetPosition(50)  # sets the left corner in x
        MC.SizeFrame(x=600,y=600) #sizes the frame
        self.CreateButton()
 
        #Now we start beautify the frame.
 
        self.CreateMenu()
        
    def CreateMenu(self):
        """ this creates the menu for the tankcontrol
        """
        self.menubar = wx.MenuBar()
        # first menu
        menu1 = wx.Menu()
        menu1.Append(wx.NewId(),"&Quit") # this creates the menu items
        self.menubar.Append(menu1, "&File") # this creates the menu title
        
        
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(),"&Run")
        self.menubar.Append(menu2, "&Control") # this creates the menu title
        
 
        self.MC.SetMenuBar(self.menubar)
        
        
    def CreateButton(self): 
        
           
        button=wx.Button(self.MC.panel,-1,"Close me",pos=(15,15))


  
 
if __name__ == '__main__':
    
    app= wx.App(redirect=False)

    TC=TankControl()
    app.MainLoop()
    pass
       