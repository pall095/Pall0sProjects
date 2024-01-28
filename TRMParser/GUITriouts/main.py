import tkinter as tk
from utils import parseFile, parseFunctionList, populateRequirements, printFunctionBreakedown, populateOutputFile, removeExcessLines, parseParterList


# Gui Parameters
window = tk.Tk()


def readInput( ):

    global filepath
    global entries
    global functionList
    global functionListPath
    global partnerList

    filepath = input_text.get( "1.0","end-1c" )
    functionListPath = "functionList.txt"
    parterListPath = "parterList.txt"
    entries = removeExcessLines( parseFile( filepath ) ) # Entries Structure: 0 = level | 1 = title | 2 = type | 3 = content | 4 = state
    functionList = populateRequirements( entries, parseFunctionList( functionListPath ) )
    partnerList = parseParterList( parterListPath )


def printFunctionBreakDownToWindow( ):

    for i in range( len( functionList ) ):

        tmp = ""
        tmp = "Physical Element: " + functionList[ i ].getPhys( ) + "\n"
        tmp = tmp + "Sys Element: " + functionList[ i ].getSyselement( ) + "\n"
        tmp = tmp + "PID: " + functionList[ i ].getPid() + "\n"
        tmp = tmp + "Function Name: " + functionList[ i ].getName( ) + "\n"
        tmp = tmp + "N° in Work: " +  str( functionList[ i ].getNumInWork( ) )  + "\n"
        tmp = tmp + "N° in Frozen: " + str(functionList[i].getNumInFrozen()) + "\n"
        tmp = tmp + "N° in Released: " + str(functionList[i].getNumReleased()) + "\n"
        tmp = tmp +  "------------------------------------------------------------- \n"

        output_window.insert( tk.END ,  tmp )

def printBreakDownByParter( ):

    for i in range( len( partnerList ) ):

        numFrozen = 0
        numReleased = 0
        numWork = 0

        for j in range( len( functionList ) ):

            if( functionList[ j ].getPhys( ) == partnerList[ i ] ):

                numWork = numWork + functionList[ j ].getNumInWork( )
                numReleased = numReleased+ functionList[j].getNumReleased( )
                numFrozen= numFrozen + functionList[j].getNumInFrozen()

        string = ( "Parter: " + partnerList[ i ] + "\n" )
        string = string + "Num in work: " + str( numWork ) + "\n"
        string = string + "Num in released: " + str( numReleased ) + "\n"
        string = string + "Num in frozen: " + str(numFrozen) + "\n"
        string = string + "------------------------------------------------------------- \n"

        output_window.insert(tk.END, string )

def clearOutput( ):
    output_window.delete("1.0", "end")


input_text = tk.Text( window , height = 1 , width = 100 )
input_text.insert( tk.END , "ALCSys3Export_25Jan2024.csv")
parse_button = tk.Button( text = "Parse file..." , command=lambda : readInput() )
output_window = tk.Text( window , height = 50 , width = 100 )
functionbreakdown_button = tk.Button( text = "Breakdown by function" , command = lambda : printFunctionBreakDownToWindow( ) )
partnerbreakdown_button = tk.Button( text = "Breakdown by partner" , command = lambda  : printBreakDownByParter( ) )
clearbutton = tk.Button( text = "Clear output" , command =  lambda : clearOutput() )
createoutput_checkbox = tk.Checkbutton( text = "Check to create output file")


# Item grid
input_text.grid( row = 1 , column = 0  )
parse_button.grid( row = 1 , column = 1 )
functionbreakdown_button.grid( row = 2 , column = 0 )
partnerbreakdown_button.grid( row = 3 , column = 0 )
clearbutton.grid( row = 4 , column = 0 )
createoutput_checkbox.grid( row = 6 , column = 0 )
output_window.grid( row = 7 , column = 0 )




if __name__ == '__main__':


    tk.mainloop()

