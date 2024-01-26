import os
from Movement import Movement

def countLines( file ):
    
    count = 0 
    next( file )
    
    
    for line in file:
        
        count = count  + 1  

    return count 
    

if __name__ == '__main__':
    
    file_location = os.path.abspath( "C:/Users/F01321D/Desktop/Script&Programs/Python/AnalizzatoreMovimentiBancari/ListaMovimenti_csv.csv" )
    file = open( file_location , "r" )
    
    listaMovimenti = [] 
        
    for line in file: 
        
        line = file.readline() 
        splittedLine = line.split( ";" )    
        movimento =  Movement( splittedLine )
        listaMovimenti.append( movimento )
        
        
        
    file.close()