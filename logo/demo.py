from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(1,100):
  move(10)
  turn(90)
  color(colors[i%3])