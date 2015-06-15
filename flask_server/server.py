from flask import Flask
from flask import request
from flask import render_template
from jr import *
app = Flask(__name__)


@app.route('/companies/', methods=['GET', 'POST'])
def show_user_profile():
	skill_set = request.args.get('skills')
	return(get_rec(skill_set,"companies"))