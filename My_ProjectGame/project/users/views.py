#users/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from project import db
from project.models import User,BlogPost
from project.users.forms import RegistrationForm,LoginForm
from project import app
from flask_mail import Mail, Message
from random import randrange

users = Blueprint('users',__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hakobyand584@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        value = randrange(100000, 999999, 1)
        code = value
        subject = 'Verification code number'
        msg = 'Your verification code number is` {}'.format(value)
        message = Message(subject, sender="hakobyand584@gmail.com", recipients=[email])
        message.body = msg
        #mail.send(message)
        return render_template('verification.html')
    return render_template("register.html",form=form)

# Verification
@users.route('/verification', methods=['GET', 'POST'])
def verif():
    if int(request.form['number']) == int(code):
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Account registered successfully!")
        return redirect(url_for("users.login"))
    else:
        return redirect(url_for("users.verif"))

# Login
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html',form=form)

@users.route("/all")
def dashboard():
    users = BlogPost.query.all()
    users = sorted(users, key=lambda x: int(x.number), reverse=True)
    return render_template('dashboard.html',users=users)

# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))
