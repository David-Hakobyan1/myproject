from flask import render_template,redirect,url_for,Blueprint
from project.games.chingachung.forms import PLAY_Form
import random

ching = Blueprint('ching',__name__)

my_list = ["rock","paper","scissors"]
number1 = 0
number2 = 0

@ching.route('/chingachung',methods=["GET","POST"])
def chingachung():
    global my_list
    global number1
    global number2
    form = PLAY_Form()
    fnum = form.fnum.data
    return render_template("chgame.html",form=form,my_list=my_list,number1=number1,number2=number2,info="start")

@ching.route("/chingachungs",methods=["GET","POST"])
def chingachung_check():
    global number1
    global number2
    global my_list
    rands = random.randrange(len(my_list))
    player2 = my_list[rands]
    form = PLAY_Form()
    fnum = form.fnum.data
    if player2 == fnum:
        pass
    if player2 == "paper" and fnum == "rock":
        number2 += 1
    if player2 == "paper" and fnum == "scissors":
        number1 += 1
    if player2 == "scissors" and fnum == "paper":
        number2 += 1
    if player2 == "scissors" and fnum == "rock":
        number1 += 1
    if player2 == "rock" and fnum == "scissors":
        number2 += 1
    if player2 == "rock" and fnum == "paper":
        number1 += 1
    return render_template("chgame.html",form=form,fnum=fnum,number1=number1,number2=number2,player2=player2,my_list=my_list)
