'''
Created on Oct 23, 2018

@author: klein
'''

import wx
import os

class MainFrame(wx.Frame):

    def __init__ (self,*args, **kwargs):
        """
        Not much doing here
        """
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self,-1)
        
        self.Show()
        
        
    def CalculatePosition(self):
        """calculates the position of the window
        Currently I want to have it in the lower left corner
        """
        # first we get the screen size
        width, height = wx.GetDisplaySize()
        
        # since wx python uses y direction as measured from the top we need to calculate
        # the positions such that the lower edge of the frame is still on the screen
        self.ypos = height-self.winsize[1]
        print self.xpos
        self.winpos =(self.xpos,self.ypos)
        return
 
    def SizeFrame(self,x,y):
        """ sets the window size
        """
        
        
        self.winsize = (x,y) #size of the window
        

        

        self.SetSize(self.winsize) # here we set the frame sizer
        self.CalculatePosition() #calulate the possible position
        self.winpos=(self.xpos,self.ypos)
        self.SetPosition(self.winpos) #set the position
        self.Show()
        return

    def SetPosition(self,left_bottom):
        """
        serts the position of the lower left corner
        """
        
        self.xpos = left_bottom
        return
    
    def CloseFrame(self):
        self.Close()

if __name__ == '__main__':
    
    app= wx.App(redirect=False)
    MC= MainFrame(None,title='my test') # this redirects out put into a wx python window.
    MC.SetPosition(500)  # sets the left corner in x
    MC.SizeFrame(x=600,y=600) #sizes the frame
    app.MainLoop()
    pass
