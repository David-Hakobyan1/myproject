from flask import Flask,render_template,request,Blueprint
from project.games.pole_chudes.forms import PLAY_Form1
import random

pole = Blueprint('pole',__name__)

with open("file2.txt") as f:
    fc = f.read().strip().split("\n")

my_list=[]
for el in fc:
    my_list.append(el.split(":"))

num = random.randrange(0,len(my_list))
question  = my_list[num]
my_quest = question[0]
answer = question[1]
lattice = question[2]
lattice = list(lattice)

@pole.route("/pole_chudes",methods=["GET","POST"])
def pole_chudes():
    global my_quest,answer,lattice,my_list,question
    form1 = PLAY_Form1()
    fnum = form1.fnum.data
    quest = "Question"
    lis=[]
    if question in my_list:
        my_list.remove(question)
    if form1.validate_on_submit():
        c=-1
        for i in answer:
            c+=1
            if fnum==i:
                lattice[c]=i
                if "#" not in lattice and len(my_list) != 0:
                    num = random.randrange(0,len(my_list))
                    question  = my_list[num]
                    my_quest = question[0]
                    answer = question[1]
                    lattice = question[2]
                    lattice = list(lattice)
                if "#" not in lattice and len(my_list) == 0:
                    return render_template("endpgame.html",info="You won!")
            else:
                continue
    return render_template("file1.html",form1=form1,fnum=fnum,my_quest=my_quest,lattice=lattice,quest=quest)

