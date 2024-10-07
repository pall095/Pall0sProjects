# -*- coding: utf-8 -*-
from collatz_fun import collatz
import matplotlib.pyplot as plt
import numpy as np
import math 
from utils import normalizeSeries


if __name__ == "__main__" :
    
    N_start =  10000
    reduction_step = 1
    angle_step = math.radians( 0.5 )
    angle_offset = 0 
    series = [ ]
    
    
    while N_start > 0 :
        
        N = N_start
        series = [ ]
        
        print( "Current N_start: " + str( N_start ) )
    
        while N != 1 :
            
            #print( "Current Collatz calculation: " + str( N ) )
            N = collatz( N )
            series.append( N )
            
        series.append( 1 )
        cosines = np.cos( np.arange( 0 - angle_offset , math.pi - angle_offset , math.pi / len( series ) ) ) 
        sines = np.sin( np.arange( 0 - angle_offset , math.pi - angle_offset , math.pi / len( series ) ) )
            
        try: 
            X =  cosines * np.array( series )
            Y =  sines * np.array( series )
            
        except :
            print( "Catched an error")
            
        N_start = N_start - reduction_step 
        angle_offset = angle_offset + angle_step
        plt.plot( X , Y , '-ob')
        print( "---" )
        

    plt.show( )
    
    