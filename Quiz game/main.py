import os

x = 50
y = 50

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{x},{y}"

import pgzrun
WIDTH = 870
HEIGHT = 650

#creating rectangular boxes
marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,350)

#Shifting boxes to their respective position 
marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

#creating variables
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
score = 0
time_left = 10
game_over = False
marquee_message = ""
question_count = 0
question_index = 0
question_sets = []






def draw():
    global marquee_message,question_count
    screen.fill("black")

    #Displaying the rectangles
    screen.draw.filled_rect(marquee_box,"orange")
    screen.draw.filled_rect(question_box,"red")
    screen.draw.filled_rect(timer_box,"purple")
    screen.draw.filled_rect(answer_box1,"yellow")
    screen.draw.filled_rect(answer_box2,"yellow")
    screen.draw.filled_rect(answer_box3,"yellow")
    screen.draw.filled_rect(answer_box4,"yellow")
    screen.draw.filled_rect(skip_box,"pink")
    
    #Displaying text inside the reactnagular boxes
    marquee_message = f"Welcome to QuizMaster!You are at Q:{question_index} out of {question_count}"
    screen.draw.textbox(marquee_message,marquee_box,color = "white")
    screen.draw.textbox(str(time_left),timer_box,color = "white",scolor = "dim grey",shadow = (0.5,0.5))
    screen.draw.textbox("Skip",skip_box,color = "white",angle = -90)

def read_question_file():
    global question_sets,question_count
    #opening the file to be read
    q_file = open("questions.txt",mode="r")
    for each_line in q_file:
        question_sets.append(each_line)
        question_count = question_count + 1
    
    q_file.close()

def read_next_question():
    global question_index
    question_index = question_index + 1
    return question_sets.pop(0).split(",")

def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def update():
    move_marquee()

read_question_file()

one_question_set = read_next_question()
print (one_question_set)

    
    




















pgzrun.go()
