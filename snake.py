import turtle as t
import random as rd
import time as ti

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed()
leaf.hideturtle()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',font=('Arial',34,'bold'))
text_turtle.hideturtle()

scre_turtle = t.Turtle()
scre_turtle.hideturtle()
scre_turtle.speed(0)

ti.sleep(3)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()
    outside = x<left_wall or x>right_wall or y>top_wall or y < bottom_wall
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.hideturtle()
    t.write('GAME OVER',align='center',font=('Arial',30,'bold'))
def display_score(current_score):        
    scre_turtle.clear()
    scre_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50
    scre_turtle.write(str(current_score),align='right',font=('Arial',40,'bold'))

def start_game():
    global game_started
    
    if game_started:
        return
    game_started = True 
    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()


t.onkey(start_game,'space')        
t.listen()
t.mainloop()