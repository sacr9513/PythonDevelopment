import turtle
import random
import time

 # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

'''@author: Sammie Crowder'''
'''This code creates a resizable tic tac toe board, then adds a human player and computer player. The human can play against the computer and then the console will print a win/loss or encourage the player to play again'''

'''I had a person play this, they said they would rather have the game say "start over" than saying it's a tie, because that made them more likely to play again, I added this because I thought it was a good suggestion'''
# create game manager
class GameManager:
    def __init__(self):
        #set up variables for overall game running
        turtle.tracer(0)
        self.w=600
        self.h=600
        turtle.setup(self.w,self.h)
        self.panel=turtle.Screen()
        self.panel.bgcolor("black")
        self.TurtlesRows=3 # rows
        self.TurtleColums=3 #Colums 
        self.Turts=self.TurtlesRows*self.TurtleColums #how many turtles on the board
        self.size=self.w/80 #how big
        self.spacingwidth= (self.w/self.TurtlesRows) #spacing
        self.spacingheight=(self.h/self.TurtleColums) 
        self.outsideTurtle = turtle.Turtle() #turtle to draw border
        self.running = True #is the game running? 
        
        
       

    def tiles(self):
        '''creates the tiles that are clickable, allowing the human and computer to interact with the game'''
        clicks = []
        for i in range(self.Turts):
            clicks.append(turtle.Turtle(shape="square"))
        for i in range(len(clicks)):          
            clicks[i].shapesize(self.size)
            clicks[i].color("light blue")
            clicks[i].up()
            clicks[i].goto(-self.w/2+(self.w/6), self.h/self.TurtlesRows)
                    
                    
        for i in range(0,3):
            clicks[i].forward(self.spacingwidth*i)
                     
            #second row of turtles
        for i in range(3,6):
            clicks[i].goto(-self.w-self.spacingwidth, self.h/self.TurtlesRows-self.spacingwidth)
            clicks[i].forward(self.spacingwidth*i)        
                       
            #third row of turtles
        for i in range(6,9):
            clicks[i].goto(-self.w-(self.spacingwidth*4), self.h/self.TurtlesRows-(2*self.spacingwidth))
            clicks[i].forward(self.spacingwidth*i)   
        
        return clicks
    

         
    
    
    def draw(self):
            '''
            Creates the outside border that encloses the tiles into a recognizable tic tac toe board. 
            '''
            self.outsideTurtle.color('light green') #color
            self.outsideTurtle.width(50) #size
            self.outsideTurtle.up() # start at the top right corner
            self.outsideTurtle.goto(self.w/2,self.h/2)
            self.outsideTurtle.right(90)
            for i in range (4): #draw a square around the board
                self.outsideTurtle.down()
                self.outsideTurtle.forward(self.w)
                self.outsideTurtle.right(90)
                
    
    
               
    def checkWin(self):  
            '''
            Checks who wins the game, or in case of no winner, encourages another game.

        

            '''
            
            if game.open0 == 1 and game.open1 == 1 and game.open2 == 1: #row checks for player 1
                print('You win!') 
                self.running = False
            if game.open3 == 1 and game.open4 ==1 and game.open5 ==1:
                print('You win!')
                self.running = False
            if game.open6 == 1 and game.open7 ==1 and game.open8 ==1:
                print('You win!')
                self.running = False
                
            if game.open0 ==1 and game.open4 == 1 and game.open8 ==1: # diagonal checks for player one
                print('You win!')
                self.running = False
                
            if game.open2 == 1 and game.open4 ==1 and game.open6 ==1:
                print('You win!')
                self.running = False
            
            
            if game.open0 == 1 and game.open3 ==1 and game.open6 ==1: #column checks for player one
                print('You win!')
                self.running = False
                
            if game.open1 == 1 and game.open4 ==1 and game.open7 ==1:
                print('You win!')
                self.running = False
                
            if game.open2 == 1 and game.open5 ==1 and game.open8 ==1:
                print('You win!')
                self.running = False
            gamemanagement.panel.update()
            
            
            
            
            
            if game.open0 ==2 and game.open1==2 and game.open2 == 2 and self.running==True: #row checks for player 2
                print('Computer Wins :(') 
                self.running = False
                    
            if game.open3 == 2 and game.open4 ==2 and game.open5 ==2 and self.running==True:
                print('Computer Wins :(')
                self.running = False
            
            if game.open6 == 2 and game.open7 ==2 and game.open8 ==2 and self.running==True:
                print('Computer Wins :(')
                self.running = False
                
            if game.open0 ==2 and game.open4 == 2 and game.open8 ==2 and self.running==True: #diagonal checks for player 2
                print('Computer Wins :(')
                self.running = False
        
            if game.open2 == 2 and game.open4 ==2 and game.open6 ==2 and self.running==True:
                print('Computer Wins :(')
                self.running = False
            
            if game.open0 == 2 and game.open3 ==2 and game.open6 ==2 and self.running==True: #column check for player 2
                print('Computer Wins :(')
                self.running = False
                
            if game.open1 == 2 and game.open4 ==2 and game.open7 ==2 and self.running==True:
                print('Computer Wins :(')
                self.running = False
                
            if game.open2 == 2 and game.open5 ==2 and game.open8 ==2 and self.running==True:
                print('Computer Wins :(')
                self.running = False
                
                
            elif game.boardfull == 9:   #end check
               print('No more moves- Start again?')
               self.running = False
            gamemanagement.panel.update()
            
            

            


            

class Player:
    '''this class creates the player variables. The computer is a child class of this class'''
    def __init__(self):
        self.turn = True
        self.open0=0
        self.open1=0
        self.open2=0
        self.open3 = 0
        self.open4= 0
        self.open5 = 0
        self.open6= 0
        self.open7 = 0
        self.open8 = 0
        self.boardfull=0
                
         
   #first tile      
    def circle0(self,x,y):
        if self.turn:  # is it the human player's turn?    
            clicks[0].shape('circle') # turn tile into circle
            clicks[0].stamp() #stamp circle
            clicks[0].ht() #hide the turtle to stop further click interaction
            self.turn= not self.turn # change to computer's turn
            self.open0 = 1 # change the value to pass to wincheck
            self.boardfull +=1 # count turns for stalemate/play again check
            player2.functions.remove(game.circle0) #remove the ability for computer to access this function
            
        elif not self.turn: # is it the computer player's turn?    
            clicks[0].shape('triangle') #turn tile into triangle 
            clicks[0].stamp() #stamp triangle
            clicks[0].ht() #hide the turtle to stop further click interaction 
            self.open =2 # change value to pass to wincheck
            self.turn= True # change to players turn
            self.boardfull +=1 # add to turn count for stalemate/play again check
            player2.functions.remove(game.circle0) #remove the ability for computer to access this function again
        else:
            print('pick another') # add other 
         
        gamemanagement.panel.update()
        
#each time is basically the same as the first one and functions the same.         
            
        #second tile    
    def circle1(self,x,y):
        if self.turn:   
            clicks[1].shape('circle')
            clicks[1].stamp()
            clicks[1].ht()
            self.turn= not self.turn
            self.open1 = 1
            self.boardfull +=1
            player2.functions.remove(game.circle1)
        elif not self.turn:
            clicks[1].shape('triangle')
            clicks[1].stamp()
            clicks[1].ht()
            self.turn= True
            self.open1 = 2
            self.boardfull +=1
            player2.functions.remove(game.circle1)
        else:
            print('pick another')
        gamemanagement.panel.update()   
        
        
       #third tile 
    def circle2(self,x,y):
        if self.turn:     
            clicks[2].shape('circle')
            clicks[2].stamp()
            clicks[2].ht()
            self.turn= not self.turn 
            self.open2 = 1
            self.boardfull +=1
            player2.functions.remove(game.circle2)
        elif not self.turn:
            clicks[2].shape('triangle')
            clicks[2].stamp()
            clicks[2].ht()
            self.turn= True
            self.open2 =2
            self.boardfull +=1
            player2.functions.remove(game.circle2)
        else:
            print('pick another') 
        gamemanagement.panel.update()
            
         #fourth tile   
    def circle3(self,x,y):
        if self.turn:     
            clicks[3].shape('circle')
            clicks[3].stamp()
            clicks[3].ht()
            self.turn= not self.turn 
            self.open3 = 1
            self.boardfull +=1
            player2.functions.remove(game.circle3)
        elif not self.turn:
            clicks[3].shape('triangle')
            clicks[3].stamp()
            clicks[3].ht()
            self.turn= True
            self.open3 =2
            self.boardfull +=1
            player2.functions.remove(game.circle3)
        else:
            print('pick another') 
        gamemanagement.panel.update()
            
          #fifth tile  
    def circle4(self,x,y):
        if self.turn:     
            clicks[4].shape('circle')
            clicks[4].stamp()
            clicks[4].ht()
            self.turn= not self.turn 
            self.open4 = 1
            self.boardfull +=1
            player2.functions.remove(game.circle4)
        elif not self.turn:
            clicks[4].shape('triangle')
            clicks[4].stamp()
            clicks[4].ht()
            self.turn= True
            self.open4 =2
            self.boardfull +=1
            player2.functions.remove(game.circle4)
        else:
            print('pick another')
        gamemanagement.panel.update()
            
         #sixths tile  
    def circle5(self,x,y):
        if self.turn:     
            clicks[5].shape('circle')
            clicks[5].stamp()
            clicks[5].ht()
            self.turn= not self.turn 
            self.open5 = 1
            self.boardfull +=1
            player2.functions.remove(game.circle5)
        elif not self.turn:
            clicks[5].shape('triangle')
            clicks[5].stamp()
            clicks[5].ht()
            self.turn= True
            self.open5 =2
            self.boardfull +=1
            player2.functions.remove(game.circle5)
        else:
            print('pick another') 
        gamemanagement.panel.update()
            
            #seventh tile
    def circle6(self,x,y):
        if self.turn:     
            clicks[6].shape('circle')
            clicks[6].stamp()
            clicks[6].ht()
            self.turn= not self.turn 
            self.open6 = 1
            self.boardfull +=1
            player2.functions.remove(game.circle6)
        elif not self.turn:
            clicks[6].shape('triangle')
            clicks[6].stamp()
            clicks[6].ht()
            self.turn= True
            self.open6 =2
            self.boardfull +=1
            player2.functions.remove(game.circle6)
        else:
            print('pick another')
        gamemanagement.panel.update()
            
            
            #eight tile
    def circle7(self,x,y): 
        if self.turn:     
            clicks[7].shape('circle')
            clicks[7].stamp()
            clicks[7].ht()
            self.turn= not self.turn 
            self.open7 = 1
            self.boardfull +=1
            player2.functions.remove(game.circle7)
        elif not self.turn:
            clicks[7].shape('triangle')
            clicks[7].stamp()
            clicks[7].ht()
            self.turn= True
            self.open7 =2
            self.boardfull +=1
            player2.functions.remove(game.circle7)
        else:
            print('pick another')
        gamemanagement.panel.update()
            
            #ninth tile
    def circle8(self,x,y):
        if self.turn:     
            clicks[8].shape('circle')
            clicks[8].stamp()
            clicks[8].ht()
            self.turn= not self.turn 
            self.open8 = 1
            self.boardfull +=1
            player2.functions.remove(game.circle8)
        elif not self.turn:
            clicks[8].shape('triangle')
            clicks[8].stamp()
            clicks[8].ht()
            self.turn= True
            self.open8 =2
            self.boardfull +=1
            player2.functions.remove(game.circle8)
        else:
            print('pick another') 
        gamemanagement.panel.update()
        
        
    

            
            
 

class Computer(Player): 
    '''This class creates a subclass from the Player class that extends the Player class to instantiate the computer player'''
    def __init__(self):
        self.functions = [game.circle0, game.circle1, game.circle2, game.circle3, game.circle4, game.circle5, game.circle6, game.circle7, game.circle8]
        Player.__init__(self)
    def computerTurn(self,x,y):
            if not game.turn:
                    time.sleep(1)
                    random.choice(self.functions)(x,y)  
                    game.turn = True
            gamemanagement.panel.update()   
        
        
            
            

    

        
game = Player() # create player       
gamemanagement = GameManager() #create the gamemanager
clicks = gamemanagement.tiles()    #instantiate the tiles
gamemanagement.draw() #instantiate the border
player2 = Computer() #create the computer player



# each click results in click tile being transformed to a circle or a square
clicks[0].onclick(game.circle0)
clicks[1].onclick(game.circle1)
clicks[2].onclick(game.circle2)
clicks[3].onclick(game.circle3)
clicks[4].onclick(game.circle4)
clicks[5].onclick(game.circle5)
clicks[6].onclick(game.circle6)
clicks[7].onclick(game.circle7)
clicks[8].onclick(game.circle8)    
#this click is envoked on panel click, so that every time a human player clicks on a tile, the computer is prompted to play. 

    






turtle.update() 
    
                
                         

            
          
# continuously check for a win condition      
while gamemanagement.running:
    gamemanagement.checkWin()
    gamemanagement.panel.onclick(player2.computerTurn)

# =========LISTENERS & CLEANUP =========
gamemanagement.panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.