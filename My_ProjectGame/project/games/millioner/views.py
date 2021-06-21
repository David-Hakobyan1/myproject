from flask import render_template,Blueprint
from flask_login import current_user,login_required
from project.games.millioner.forms import PLAY_Form
from project.models import BlogPost,User
from project import db

import random

mill = Blueprint('mill',__name__)

with open("file1.txt") as f:
    fc = f.read().strip().split("\n")

lis=[]
for i in fc:
    lis.append(i.split(":"))
rands = random.randrange(len(lis))
num = lis[rands]
numbers = 0

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
    global numbers
    form = PLAY_Form()
    fnum = form.fnum.data
    for i in lis:
        if i == num:
            lis.remove(i)
    if len(lis) != 0:
        if fnum == num[2]:
            info = "Right"
            numbers+=1
            rands = random.randrange(len(lis))
            num = lis[rands]
            return render_template("game.html",form=form,fnum=fnum,mylis=num,info=info)
        else:
            rands = random.randrange(len(lis))
            num = lis[rands]
            info = "Wrong"
            return render_template("game.html",form=form,fnum=fnum,mylis=num,info=info)
    else:
        usernames  = current_user
        usernames = str(usernames)
        user = db.session.query(BlogPost).filter(BlogPost.username == '{}'.format(usernames)).all()
        if not user:
            us = BlogPost(user_id=current_user.id,number=numbers,username=usernames)
            db.session.add(us)
            db.session.commit()
        else:
            us = BlogPost.query.filter_by(username=usernames).update(dict(number=numbers))
            db.session.commit()
        return render_template("endgame.html",info="END",number=numbers)
