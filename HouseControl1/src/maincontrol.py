'''
Created on Oct 18, 2018

@author: klein
'''

import wx
import os


class MainControl(wx.App):

    def __init__ (self,redirect=False, filename = None):
        """
        Not much doing here
        """
    
    # next statement intializes and is needed for wx to provide the OnInit
        wx.App.__init__(self,redirect)

    def OnInit(self): 
        # where on the screen we have the frame

        
        self.frame = wx.Frame(parent=None,id=-1,title= "House control")
        print " id of frame",self.frame.GetId()

        
        
 
        # make this the topwindow
        self.SetTopWindow(self.frame)
        print "I am in OnInit"
        # temporarya dialog
        return True

    def CalculatePosition(self):
        """calculates the position of the window
        Currently I want to have it in the lower left corner
        """
        # first we get the screen size
        width, height = wx.GetDisplaySize()
        
        # since wx python uses y direction as measured from the top we need to calculate
        # the positions such that the lower edge of the frame is still on the screen
        ypos = height-self.winsize[1]
        self.winpos =(self.xpos,ypos)
        return
 
    def SizeFrame(self,x,y):
        """ sets the window size
        """
        
        
        self.winsize = (x,y) #size of the window
        

        

        self.frame.SetSize(self.winsize) # here we set the frame sizer
        self.CalculatePosition() #calulate the possible position
        self.frame.SetPosition(self.winpos) #set the position

        self.frame.Show()
        return

    def SetPosition(self,left_bottom):
        """
        serts the position of the lower left corner
        """
        
        self.xpos = left_bottom
        return
        
if __name__ == '__main__':
    MC= MainControl(redirect=False) # this redirects out put into a wx python window.
    MC.SetPosition(20)  # sets the left corner in x
    MC.SizeFrame(x=900,y=700) #sizes the frame
    MC.MainLoop()
    pass