import pgzrun


HEIGHT=500
WIDTH=800

marque_rect=Rect(0,0,800,80)



def marque_move():
    marque_rect.x=marque_rect.x-5
    if marque_rect.right<0:
        marque_rect.left=800

def draw():
    screen.fill("white")
    screen.draw.filled_rect(marque_rect,"white")
    screen.draw.textbox("Welcome to the pop quizz! ", marque_rect,color="blue")



def update():
     marque_move()






























pgzrun.go()