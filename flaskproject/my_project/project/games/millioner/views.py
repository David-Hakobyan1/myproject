from flask import render_template,Blueprint
from project.games.millioner.forms import PLAY_Form
import random

mill = Blueprint('mill',__name__)

with open("file1.txt") as f:
    fc = f.read().strip().split("\n")

lis=[]
for i in fc:
    lis.append(i.split(":"))
rands = random.randrange(len(lis))
num = lis[rands]
number = 0

@mill.route("/millioner",methods=["GET","POST"])
def millioner():
    global num
    form = PLAY_Form()
    fnum = form.fnum.data
    info = ""
    return render_template("game.html",form=form,fnum=fnum,mylis=num,info=info)

@mill.route("/millioners",methods=["GET","POST"])
def millioner_check():
    global num
    global number
    form = PLAY_Form()
    fnum = form.fnum.data
    for i in lis:
        if i == num:
            lis.remove(i)
    if len(lis) != 0:
        if fnum == num[2]:
            info = "Right"
            number+=1
            rands = random.randrange(len(lis))
            num = lis[rands]
            return render_template("game.html",form=form,fnum=fnum,mylis=num,info=info)
        else:
            rands = random.randrange(len(lis))
            num = lis[rands]
            info = "Wrong"
            return render_template("game.html",form=form,fnum=fnum,mylis=num,info=info)
    else:
        return render_template("endgame.html",info="END",number=number)
