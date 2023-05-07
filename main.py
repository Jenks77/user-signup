from flask import Flask, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    template = jinja_env.get_template('signup_form.html')
    return template.render(user="",email="",error="")
@app.route('/', methods=['POST'])
def submit():
    template = jinja_env.get_template('signup_form.html')
    user = request.form['uname']
    email = request.form['email']

    if request.form['pass1'] == request.form['pass2']:
        template = jinja_env.get_template('welcome.html')
        return template.render(user=user)
    else:
        return template.render(error="Passwords do not match",user=user,email=email)

app.run()