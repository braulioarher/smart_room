from flask import render_template, Blueprint

blp = Blueprint("Index", __name__)

@blp.route('/')
def index():
    context = {
        'title' : 'Home'
    }
    return render_template('/index.html', **context)