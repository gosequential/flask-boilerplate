from datetime import datetime
from flask import render_template
from . import main
#from .forms import NameForm
#from .. import db
#from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html', current_time=datetime.utcnow())
    