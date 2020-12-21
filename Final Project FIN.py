
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:13:59 2020

@author: Sammie Crowder
"""
import turtle
import random
import time
running = True #controls while loop for events
turtle.tracer(0)

class Manager: #set up variables
    def __init__(self, buffer=30): #buffer is the min space between objects until they react to each other
        turtle.tracer(0)
        self.w=400
        self.h=400
        turtle.setup(self.w,self.h)
        self.panel=turtle.Screen()
        self.panel.bgcolor("black")
        self.PredatorList = [] #empty list for Prey
        self.PreyList = [] #empty list for Predators
        self.PlantList = [] #empty list for Plants
        self.buffer = buffer
        
     #adapted from Dr. Z's input to use the turtle.distance and buffer to check for collision.    
    def Collision(self, pullList, turt, someTurt):
        '''This method takes a List value, a turtle value from the list and then another turtle to compare against. Distance between the two collision turtles is tested, 
        if it's less than the buffer distance, something will happen'''
        for i in range(len(pullList)):
              return  turt.distance(someTurt) < self.buffer
          
    
          
    def Counter(self): 
        '''I had a hard time getting the inbuilt ontimer event to work with the events in my methods, so I created my own counter. self.Sec starts at
        0, and counts upwards until it reaches a value which triggers a Predator Death (turns into a Plant)'''
        self.Sec = 0


            
        
 #this Class sets up the Predator Turtle and List       
class Predator:         
    def __init__(self):
        #creates a turtle predator and appends to a list
      pass
    def predatorCreate(self):
        '''this method creates a turtle and appends to a list of turtles for later manipulation. each turtle is spawned at a random location on the left
        side of the screen'''
        
        for i in range(3):
            self.Pred = turtle.Turtle(shape="square") #main predator turtle
            self.Pred.shapesize(1) 
            self.Pred.up()
            self.Pred.color("red")
            Ecosystem.PredatorList.append(self.Pred)
            Ecosystem.PredatorList[i].goto(random.randint(-Ecosystem.w/2, 0),random.randint(-Ecosystem.w/2, Ecosystem.w/2))
            Ecosystem.panel.update() 
            turtle.update()
            

            
    def predatorDie(self):
            '''this method turns a predator into a plant when the timer hits a certain value'''
            for Predators.Pred in Ecosystem.PredatorList:
                Plants.plantRespawn()
                Ecosystem.PredatorList[-1].color("black") #make Predator invisible by turning it the same color as the background. 
                Ecosystem.PredatorList.pop(-1) #take predator off list
                
                break #only one predator dies at a time. 

                     
             
        #the movement method
    def movement(self, theList, speed, right, left):
        '''
        method creates the movement for the predator. 

        Speed- the jump increment of the predator, right- ability to turn right at random, left- ability to turn left at random. 

        '''
        self.speed = speed
        self.right = right
        self.left = left
        self.theList = theList
        
        time.sleep(0.1)
        #Turtles don't leave the screen- when they hit the edge of the screen, they turn around and head back into the center of the screen. 
        for i in range(len(self.theList)): 
            self.theList[i].forward(self.speed)
            self.theList[i].left(random.randint(self.right,self.left))
            xbounds = self.theList[i].xcor()<-Ecosystem.w/2 or self.theList[i].xcor()>Ecosystem.w/2
            ybounds = self.theList[i].ycor()<-Ecosystem.h/2 or self.theList[i].ycor()>Ecosystem.h/2
            if xbounds or ybounds: 
                self.theList[i].left(180)    
            Ecosystem.panel.update() 
            
            
            
#this Class sets up the Prey Turtle and List
class Prey:        
    def __init__(self):
        pass
    #creates a turtle prey and appends to list
    def preyCreate(self): 
        '''creates prey and appends to list, then scatters them around the right part of the screen'''
        for i in range(15):
            self.Pre = turtle.Turtle(shape="triangle")
            Ecosystem.PreyList.append(self.Pre)    
            for i in range(len(Ecosystem.PreyList)):          
                Ecosystem.PreyList[i].shapesize(2)
                Ecosystem.PreyList[i].color("yellow")
                Ecosystem.PreyList[i].up()
                Ecosystem.PreyList[i].goto(random.randint(0, Ecosystem.w/2),random.randint(0, Ecosystem.w/2))
      
        
        
            
    
 #plant class to create the plant turtles. 

class Plant:
    def __init__(self):
         self.sizing = 1.5 #size of plant
    def plantCreate(self):
        '''creates the plant turtles and sets the visual appearance '''
        for i in range(5): 
            self.Plant = turtle.Turtle(shape = "circle")
            Ecosystem.PlantList.append(self.Plant)    
            for i in range(len(Ecosystem.PlantList)):          
                Ecosystem.PlantList[i].shapesize(self.sizing)
                Ecosystem.PlantList[i].color("dark green")
                Ecosystem.PlantList[i].up()
                Ecosystem.PlantList[i].goto(random.randint(-Ecosystem.w/2, 0),random.randint(-Ecosystem.w/2, Ecosystem.w/2))
        
    
    def plantRespawn(self):
        ''''creates a new plant to replace a predator when it 'dies'''
        for i in range(1): 
            self.Plant = turtle.Turtle(shape = "circle")
            Ecosystem.PlantList.append(self.Plant)
            Ecosystem.PlantList[-1].goto(Ecosystem.PredatorList[-1].pos()) #creates the plant at the position where the last Predator died. 
            
            for i in range(len(Ecosystem.PlantList)):          
                Ecosystem.PlantList[i].shapesize(self.sizing)
                Ecosystem.PlantList[i].color("dark green")
                Ecosystem.PlantList[i].up()
                
                
       

#instantiate classes
Ecosystem = Manager()
Preys = Prey()
Plants = Plant()
Predators = Predator()
   
#create list of each type of organism      
Predators.predatorCreate()  
Plants.plantCreate()
Preys.preyCreate()  




  
#create counter to track time events. 
Ecosystem.Counter()



#runs all the events in the system
while running:  
    Predators.movement(Ecosystem.PredatorList,5,-30,30) #predator moves
    Predators.movement(Ecosystem.PreyList, 7, -35, 25) #prey moves
    for k in range(len(Ecosystem.PredatorList)): #step through the collision distance tests. 
        for i in range(len(Ecosystem.PreyList)): 
            if Ecosystem.Collision(Ecosystem.PredatorList, Ecosystem.PreyList[i], Ecosystem.PredatorList[k]): #if the distance is smaller than buffer- 
                Ecosystem.PreyList[i].hideturtle() #hide the turtle that is collided with in the PreyList
                Ecosystem.PreyList[i].goto(1000,1000) #Was having trouble 'pop'ing the collided turtle, would end up with an index out of range error,
                #so I just get the turtle to go way off the screen when it's collided with, effectively destroying it (not allowing it at a distance to collide anymore)
                
                
    for m in range(len(Ecosystem.PreyList)): #step through the collision distance tests. 
        for n in range(len(Ecosystem.PlantList)):
            if Ecosystem.Collision(Ecosystem.PreyList, Ecosystem.PlantList[n], Ecosystem.PreyList[m]): #if the distance is smaller than buffer- 
                Ecosystem.PlantList[n].hideturtle() #hide the turtle that is collided with in the PlantList
                Ecosystem.PlantList[n].goto(1000,1000)
                
                
    Ecosystem.Sec += 1 #Add one to timer value
    time.sleep(0.5) #time break
    if Ecosystem.Sec == 30: #when the timer = a certain value
        Predators.predatorDie() #a predator dies
        Ecosystem.Sec = 0 #timer is reset 
    
    Ecosystem.panel.update()
    turtle.update()
    
    
      
                
    
# =========LISTENERS & CLEANUP =========
Ecosystem.panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.    
   
