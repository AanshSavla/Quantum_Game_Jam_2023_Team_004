#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:51:30 2023

@author: aanshsavla
"""

import pygame,sys

# The below GameObject class define all the movable things in the game like
# boat and all the characters.
class GameObject:
    def __init__(self,image,width,height,x,y):
        self.image = pygame.transform.scale(image,(width,height)) # Decreases size of the image to fit.
        self.x = x #Give x-coordinate
        self.y = y #Give y_coordinate
        self.right = True #Checks whether boat is in right or left. Based on this it will decide whether to move right or left
    
    # Get function returns x,y coordinates of the object
    def get_x(self):
        return self.x 
    def get_y(self):
        return self.y
    
    #Set function sets x and y coordinates of the object.
    def set_x(self,new_x):
        self.x = new_x
    def set_y(self,new_y):
        self.y = new_y
    
    # If the boat is in right then we have to move to the left. This function sets and
    # tells some other function that now the boat will be to the left.
    def set_left(self):
        self.right = False
        
    # If the boat is in left then we have to move to the right. This function sets and
    # tells some other function that now the boat will be to the right.
    def set_right(self):
        self.right = True
        
    # To get the value of the right variable to make a decision whether to move left or right.
    def get_right(self):
        return self.right
        
        
 # This class inherits the GameObject class and just introduces two new variables
# pr(Person on right) and pl(Person on left). Other variables in the init function
# are just repeated from the GameObject class. This class gets and sets
# the object on the pr and pl.       
class Boat(GameObject):
    def __init__(self,image,width,height,x,y):
        self.pl = None
        self.pr = None
        self.image = image
        self.image = pygame.transform.scale(image,(width,height))
        self.x = x
        self.y = y
        self.right = True
    def set_pl(self,pleft):
        self.pl = pleft
    def set_pr(self,pright):
        self.pr = pright
    def get_pr(self):
        return self.pr
    def get_pl(self):
        return self.pl
    
    
    
# This class also inherits GameObject and adds 4 new variables.
# Just assume right as initial land and left as final land
# Initial-X of person on right side land
# Initial-Y of person on right side land
# Final-X of person on left side land
# Final-X of person on left side land

class Person(GameObject):
    def __init__(self,image,width,height,x,y,fin_x,fin_y):
        self.image = pygame.transform.scale(image,(width,height))
        self.x = x
        self.y = y
        self.right = True
        self.init_x = x
        self.init_y = y
        self.fin_x = fin_x
        self.fin_y = fin_y



pygame.init()

win = pygame.display.set_mode((1500, 800)) # Display initial screen

pygame.display.set_caption("Entangled Love") # Title
boat_image = pygame.image.load('boat.png') #Boat image import
boat = Boat(boat_image,200,160,1000,490) # Created boat object with size and position
run = True # In any game we must run an infinite loop to display the background and object. This is the run variable
sp_image = pygame.image.load('SM.png') # Import Man image
sp1 = Person(sp_image,75,100,1450,400,250,400) #Created first man object defining image size, initial x and y, Final x and y, So they land only on their position and dont overlap with other person everytime they move
sp2 = Person(sp_image,75,100,1400,400,200,400) # Create second man object
sw_image = pygame.image.load('SW.png') # Import Woman Image
sw1 = Person(sw_image,75,100,1350,400,150,400) #Create first woman object
sw2 = Person(sw_image,75,100,1300,400,100,400) #Create seond woman object
m_image = pygame.image.load('monster.png') # Import Monster Image
m1 = Person(m_image,75,100,1250,400,50,400) # Create first monster object
m2 = Person(m_image,75,100,1200,400,0,400) # Create second monster object

# Displaying all the four things on the screen
def display_boat(boat):
    win.blit(boat.image, (boat.get_x(),boat.get_y()))
    
def display_sp(sp):
    win.blit(sp.image, (sp.get_x(),sp.get_y()))
    
def display_sw(sw):
    win.blit(sw.image, (sw.get_x(),sw.get_y()))
    
def display_monsters(m):
    win.blit(m.image, (m.get_x(),m.get_y()))
    

    
# Set position of the characters while running.
def set_pos(s,x,y):
    
    s.set_x(x)
    s.set_y(y)
    
# To place a particular character on right side of the boat or left side of the boat when they are on right land
#Written to avoid overlapping of characters on places.  
def place_pos_right(p,boat):
    if boat.pr == None:
        set_pos(p,1100,450)
        boat.set_pr(p)
    else:
        set_pos(p,1050,450)
        boat.set_pl(p)
        
    
# To place a particular character on right side of the boat or left side of the boat when they are on left land
def place_pos_left(p,boat):
    if boat.pr == None:
        set_pos(p,400,450)
        boat.set_pr(p)
    else:
        set_pos(p,350,450)
        boat.set_pl(p)
        
        
# When both persons are on the boat then we have to move everything together to opposite end.
   
    
def move_boat_person(boat):  
    # Boat can move if there is person sitting on the right but no one on the left
    if(boat.pl == None and boat.pr != None):
        update_boat_x = boat.get_x() # Get the current value of the boat
        if(boat.get_right()):
            update_boat_x -= 700 # River width is 700. So subtract to move left. Y coordinate wont change.
            boat.pr.set_x(boat.pr.get_x()-700) # Subtract 700 from the x coordinate of the person sitting on right, so boat and person both move simultaneously
            boat.set_left() # Set the right variable accordingly
        else:
            update_boat_x += 700 # If boat on left then add 700.
            boat.pr.set_x(boat.pr.get_x()+700)
            boat.set_right()
        boat.set_x(update_boat_x)
        
    # Similar explaination for the next 2.    
    
    # Boat can move if there is person sitting on the left but no one on the right
    elif(boat.pr == None and boat.pl != None):
        update_boat_x = boat.get_x()
        if(boat.get_right()):
            update_boat_x -= 700
            boat.pl.set_x(boat.pl.get_x()-700)
            boat.set_left()
        else:
            update_boat_x += 700
            boat.pl.set_x(boat.pl.get_x()+700)
            boat.set_right()
        boat.set_x(update_boat_x)
        
    # Boat can move if there is person sitting on both sides
    elif(boat.pl != None and boat.pr != None):
        update_boat_x = boat.get_x()
        if(boat.get_right()):
            update_boat_x -= 700
            boat.pl.set_x(boat.pl.get_x()-700)
            boat.pr.set_x(boat.pr.get_x()-700)
            boat.set_left()
        else:
            update_boat_x += 700
            boat.pr.set_x(boat.pr.get_x()+700)
            boat.pl.set_x(boat.pl.get_x()+700)
            boat.set_right()
        boat.set_x(update_boat_x)
        
    
    
# The main game loop starts
while run:
    # Event handler: Detecting Mouse click. 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:   #Quitting game 
            run = False
            sys.exit()
    
    win.fill((69, 255, 202)) #Give background color
    pygame.draw.rect(win, (255,0,0), (10, 10, 40, 40)) #Given a red rectangle which act as a button to move the boat.
    pygame.draw.rect(win, (39, 158, 255), (300, 600, 900, 200)) # Draw water
    pygame.draw.rect(win, (110, 203, 99), (0, 500, 300, 300)) # Draw left land
    pygame.draw.rect(win, (110, 203, 99), (1200, 500, 300, 300)) # Draw right land
    display_boat(boat) # Display boat
    
    #Display all characters
    display_sp(sp1)
    display_sp(sp2)
    display_sw(sw1)
    display_sw(sw2)
    display_monsters(m1)
    display_monsters(m2)
    
    ev = pygame.event.get() # Catching the mouse click event
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            # Based on the position of mouse click appropriate action will be taken.
            # Below is position of red button. It will move boat.
            if(pos[0]>10 and pos[0]<50 and pos[1]>10 and pos[1]<50):
                move_boat_person(boat)
                
            # Moving any object from land to boat. There are 4 else if condition
            # Since there are 4 positions on the boat. 2(pr,pl) when boat is on right
            # and 2 when boat is on the left. When you click any person on the boat
            # that person will move to its appropriate position on the land.
            elif(pos[0]>1100 and pos[0]<1175 and pos[1]>450 and pos[1]<650):
                set_pos(boat.get_pr(),boat.get_pr().init_x,boat.get_pr().init_y)
                boat.set_pr(None)
            elif(pos[0]>1050 and pos[0]<1125 and pos[1]>450 and pos[1]<650):
                set_pos(boat.get_pl(),boat.get_pl().init_x,boat.get_pl().init_y)
                boat.set_pl(None)
            elif(pos[0]>400 and pos[0]<475 and pos[1]>450 and pos[1]<650):
                set_pos(boat.get_pr(),boat.get_pr().fin_x,boat.get_pr().fin_y)
                boat.set_pr(None)
            elif(pos[0]>350 and pos[0]<425 and pos[1]>450 and pos[1]<650):
                set_pos(boat.get_pl(),boat.get_pl().fin_x,boat.get_pl().fin_y)
                boat.set_pl(None)
                
            # Moving Men from land to boat. 4 conditions. 2 seperate conditions for 
            #  each men objects on right land. 2 seperate conditions for each men object
            # on left land. They will jump to boat.
                
            elif(pos[0]>1450 and pos[0]<1500 and pos[1]>400 and pos[1]<600):
                place_pos_right(sp1,boat)
            elif(pos[0]>1400 and pos[0]<1475 and pos[1]>400 and pos[1]<600):
                place_pos_right(sp2,boat)
            elif(pos[0]>250 and pos[0]<325 and pos[1]>400 and pos[1]<600):
                place_pos_left(sp1,boat)
            elif(pos[0]>200 and pos[0]<275 and pos[1]>400 and pos[1]<600):
                place_pos_left(sp2,boat)
           
            # Similarly moving Women from land to boat
                
            elif(pos[0]>1350 and pos[0]<1425 and pos[1]>400 and pos[1]<600):
                place_pos_right(sw1,boat)
            elif(pos[0]>1300 and pos[0]<1375 and pos[1]>400 and pos[1]<600):
                place_pos_right(sw2,boat) 
            elif(pos[0]>150 and pos[0]<225 and pos[1]>400 and pos[1]<600):
                place_pos_left(sw1,boat)
            elif(pos[0]>100 and pos[0]<175 and pos[1]>400 and pos[1]<600):
                place_pos_left(sw2,boat)
                
            # Similarly moving monster from land to boat.
                
            elif(pos[0]>1250 and pos[0]<1325 and pos[1]>400 and pos[1]<600):
                place_pos_right(m1,boat)
            elif(pos[0]>1200 and pos[0]<1275 and pos[1]>400 and pos[1]<600):
                place_pos_right(m2,boat) 
            elif(pos[0]>50 and pos[0]<125 and pos[1]>400 and pos[1]<600):
                place_pos_left(m1,boat)
            elif(pos[0]>0 and pos[0]<75 and pos[1]>400 and pos[1]<600):
                place_pos_left(m2,boat)
            
                
                
    pygame.display.update() # Updating the screen everytime. 

pygame.quit()
sys.exit()

# Boat image from : <a href="https://www.freepik.com/free-vector/wooden-boat-with-paddle-white-background_18552769.htm#query=boat%20game&position=34&from_view=keyword&track=ais">Image by brgfx</a> on Freepik
