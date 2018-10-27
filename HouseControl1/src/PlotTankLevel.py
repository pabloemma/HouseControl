'''
Created on Oct 27, 2018

@author: klein
'''

import matplotlib.pyplot as plt
import matplotlib.dates as md
import csv
import time
import sys
import datetime as dt
import numpy as np
#from scipy.special._mptestutils import Arg


class PlotTankLevel(object):
    '''
    Modified original plot_level to be a class
    '''


    def __init__(self, mydate='today'):
        '''
        Constructor
        '''
        if (mydate == 'today'):
            self.date_string=dt.datetime.today().strftime('%Y-%m-%d')
        elif("-" in mydate): date_string = mydate
        
        else:
            self.date_string = dt.datetime.today().strftime('%Y-%m-%d')
            
        #initialize the array
        self.x1 = [] 
        self.y1 = []
        self.x2 = []
        self.y2 = []
    
    def FillData(self):
        n=20  
        duration =1000
        filename = '/home/klein/tankfiles/'+self.date_string+'tank.csv'
        with open(filename,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                if(int(row[1]) == 61):
                    self.x1.append(int(row[0]))
                    self.y1.append(int(row[2]))
                elif(int(row[1]) == 60):
                    self.x2.append(int(row[0]))
                    self.y2.append(int(row[2]))
                else:
                    print "Invalid control, wrong IP \n" 
        return
    
    def PlotData(self):
        plt.figure(2)

        time_date1 = [dt.datetime.fromtimestamp(ts) for ts in self.x1]
        time_date2 = [dt.datetime.fromtimestamp(ts) for ts in self.x2]

        time_convert1 = md.date2num(time_date1)
        time_convert2 = md.date2num(time_date2)
#print time_date


        plt.subplot(211)
        plt.xticks(rotation = 25)
        ax=plt.gca()
        #xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
        xfmt = md.DateFormatter('%Y-%m-%d')
        ax.xaxis.set_major_formatter(xfmt)
        ax.xaxis_date()
        #plt.gcf().autofmt_xdate()

        #plt.locator_params(axis='x',nbins =5)
        plt.grid(True)

        plt.plot(time_date1,self.y1, 'g^',label='Workshop Tank')
        plt.legend(loc='upper left')
        plt.subplot(212)

# note these adjustments have to happen within the respective figure part
        plt.subplots_adjust(bottom = .1)
        plt.xticks(rotation = 25)
        ax=plt.gca()
#xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
        xfmt = md.DateFormatter('%H:%M:%S')
        ax.xaxis.set_major_formatter(xfmt)
        ax.xaxis_date()
        #plt.gcf().autofmt_xdate()

        #plt.locator_params(axis='x',nbins =5)
        plt.plot(time_date2,self.y2,"r.",label='Underground tank') # plot with red points
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.subplots_adjust(hspace=.3)
        plt.show()
        
        return


if __name__ == '__main__':
    plotme = PlotTankLevel(mydate = 'today')
    plotme.FillData()
    plotme.PlotData()
    

   