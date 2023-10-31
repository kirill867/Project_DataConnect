from flask import Blueprint, render_template, request
from sql_provider import SQLProvider
from database import work_with_db
from blueprints.authorization.access import login_required
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '7210109',
    'db': 'ships_in_ports'
}
profile_app = Blueprint('profile', __name__, template_folder='templates')
provider = SQLProvider('blueprints/profile/sql/')

@profile_app.route('/')
@login_required
def index():
    return render_template('profile-index.html')

@profile_app.route('/prov1', methods = ['GET', 'POST'])
@login_required
def get_sql1():
    if request.method == 'GET':
        return render_template('prov1.html')
    else:
        vol = request.form.get('Volume', None)
        if vol is not None:
            sql = provider.get('task1.sql', i=vol)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output.html', str=result)

@profile_app.route('/prov2', methods = ['GET', 'POST'])
@login_required
def get_sql2():
    if request.method == 'GET':
        return render_template('prov2.html')
    else:
        date1 = request.form.get('date1', None)
        date2 = request.form.get('date2', None)
        if date1 is not None and date2 is not None:
            sql = provider.get('task2.sql', date1=date1, date2=date2)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output.html', str=result)