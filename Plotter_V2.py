# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:37:06 2020

@author: matte
"""


import matplotlib.pyplot as plt
import matplotlib.dates as dates
import os

def isTime( line ):
    
    if( line == "Time" ):
        return True
    else:
        return False
    
    
def isTemperature( line ):
    
    if( line == "Temperature" ):
        return True
    else:
        return False
    
    
def isHumidity( line ):
    
    if( line == "Humidity" ):
        return True
    else:
        return False
    
    


def isSeparator( line ):
    
    if ( line == '=\n' ):
        return True     
    else:
        return False
    
    
def cleanTime( time_array ):
    
    for i in range( len( time_array ) ):
        
        time_array[i].replace( ' ' , '' )
        time_array[i].replace( '\n' , '')
        print( time_array[i] )
        
    return time_array
        


if __name__ == "__main__":
    
    path = os.path.join( r"C:\Users\F01321D\Desktop\Script&Programs\Python\TemperaturePlotter\TemperatureFile2.txt" )
    file = open( path , 'r')
    Lines = file.readlines()
    

    
    temp_arr = []
    hum_arr =  [] 
    time_arr_initial =  []
    
    
    
    for line in Lines:
        
        splitted = line.split( ":" , 1)
        

        if( isTemperature( splitted[0] ) ):
            temp_arr.append( int( splitted[1] ) ) 
            
        if( isTime( splitted[0] ) ):
            time_arr_initial.append( splitted[ 1 ] )
        
        if( isHumidity( splitted[0] ) ):
            hum_arr.append( int( splitted[1 ] ) )
            
            
    time_arr_cleaned = [None]*len( time_arr_initial )
    time_arr_tmp = [None]*len( time_arr_initial )
        
            
    
     
    for i in range( len( time_arr_initial ) ):
        time_arr_tmp[i] = time_arr_initial[i].replace( '\n' ,  '' )
        time_arr_cleaned[i] = time_arr_tmp[i].replace( ' ' ,  '' )
        
    plt.figure( 0 )     
    x = dates.datestr2num( time_arr_cleaned )
    plt.plot_date( x , temp_arr )
    
    plt.figure(1)
    plt.plot_date ( x , hum_arr )
    
    file.close()