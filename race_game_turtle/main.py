import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(height=900, width=1000)

user_bet = screen.textinput(title="place your bets", prompt="which turtle will win the race enter a color:  ")

colors = ["red", "blue", "orange", "green", "yellow", "purple"]
y_positions= [-120, -80, -20, 40, 100, 160]
turtles = []
race_on = True

for index in range(0, 6):
    new_turle = Turtle(shape="turtle")
    new_turle.penup()
    new_turle.goto(x=-430, y=y_positions[index])
    new_turle.color(colors[index])
    turtles.append(new_turle)


if user_bet:
    race_on =True
    
while race_on:
  
    for turtle in turtles:
      if turtle.xcor()>430:
        
        race_on = False
        winning_color= turtle.pencolor()
        if winning_color == user_bet:
            print(f"you have won the winning turtle is {winning_color}")
        else:
            print(f"you  have lost the winning turtle is {winning_color} ")
            
      random_distance =random.randint(0,10)
      turtle.forward(random_distance)






screen.exitonclick()
