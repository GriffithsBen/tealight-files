from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while True:
  move()
  if(smell == "fruit"):
    for i in range (0,4):
      turn(i)
      while(look == "fruit"):
        move()  
        
  #if(left_side() == "fruit"):
  #  turn(-1)
  #elif(right_side() == "fruit"):
  #  turn(1)
  #elif (look() == "fruit"):
  #  while (look() == "fruit"):
   #   move()
  #if(left_side() == None):
  #  turn(-1)
  #  move() 44
   
  if(touch() == "wall"):
    if(left_side() != "wall"):
      turn(-1)
      move()
    elif(right_side() != "wall"):
      turn(1)      
    else:
      turn(2)
  