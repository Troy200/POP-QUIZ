import pgzrun


HEIGHT=500
WIDTH=800

time_left=10
marque_rect=Rect( 0,0,800,80)
timer_rect=Rect(680,150,100,100)
skip_rect=Rect(680,260,100,200)
question_rect=Rect(10,150,600,100)
questions_file="POP_QUIZ/questions.txt"
questions=[]
answer_rect1=Rect(10,270,290,110)
answer_rect2=Rect(310,270,290,110)
answer_rect3=Rect(10,390,290,110)
answer_rect4=Rect(310,390,290,110)
answerboxes=[answer_rect1,answer_rect2,answer_rect3,answer_rect4]
def marque_move():
    marque_rect.x=marque_rect.x-5
    if marque_rect.right<0:
        marque_rect.left=800

def draw():
    screen.fill("white")
    screen.draw.filled_rect(marque_rect,"white")
    screen.draw.textbox("Welcome to the pop quizz! ", marque_rect,color="blue")
    screen.draw.filled_rect(timer_rect,"blue")
    screen.draw.textbox(str(time_left),timer_rect,color="white")
    screen.draw.filled_rect(skip_rect,"blue")
    screen.draw.textbox("SKIP ", skip_rect,color="white")
    screen.draw.filled_rect(question_rect,"blue")
    screen.draw.textbox(question[0].strip(),question_rect ,color="white")
    index=1
    for answerbox in answerboxes:
        screen.draw.filled_rect(answerbox,"blue")
        screen.draw.textbox(question[index].strip() , answerbox,color="white")
        index=index+1



def timeupdate():
    global time_left
    if time_left:
        time_left=time_left-1

def questionsreader():
    q_file=open(questions_file,"r")
    for question in q_file:
        questions.append(question)

    q_file.close()

def q_only_reader():
    return questions.pop(0).split(",")


def update():
     marque_move()


questionsreader()
question=q_only_reader()

clock.schedule_interval(timeupdate,1.0)











pgzrun.go()