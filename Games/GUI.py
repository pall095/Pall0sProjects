from tkinter import *
from Game import Game
import pygame



GAME_TIME = 0.05
SIZE = ( 700 , 700 )


root = Tk()  # create a root widget
root.title("Main Window")
root.configure(background="white")

game = Game( GAME_TIME ,
             SIZE )


start_game = Button( root , text = "Start" , command = game.start)
start_game.pack( )

spawn = Button( root , text = "Spawn")
spawn.pack( )

kill_game = Button( root , text = "Kill!" , command = game.stop )
kill_game.pack( )

root.mainloop()